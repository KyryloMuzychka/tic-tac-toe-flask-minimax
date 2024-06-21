import pyodbc
from config import CONNECTION_STRING
from password_manager import PasswordManager
from datetime import datetime

class DB:
    def __init__(self):
        self.connection_string = CONNECTION_STRING

    def _execute_query(self, query, params=()):
        try:
            print("Connecting to database...")
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            print("Executing query...")
            cursor.execute(query, params)
            print("Query executed successfully.")
            return cursor
        except pyodbc.Error as e:
            print(f"Database error: {e}")
            return None

    def _execute_update(self, query, params=()):
        connection = None
        cursor = None
        try:
            print("Connecting to database...")
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            print("Executing update...")
            cursor.execute(query, params)
            connection.commit()
            print("Update committed successfully.")
            return True
        except pyodbc.Error as e:
            print(f"Database error: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def register_player(self, login, password):
        try:
            hashed_password = PasswordManager.hash_password(password)
            query = """
                    INSERT INTO players (login, password, registration_date, deletion_date, wins, losses, draws)
                    VALUES (?, ?, GETDATE(), NULL, 0, 0, 0)
                    """
            return self._execute_update(query, (login, hashed_password))
        except pyodbc.Error:
            return False

    def login(self, login, password):
        try:
            query = 'SELECT password FROM players WHERE login = ? AND deletion_date IS NULL'
            cursor = self._execute_query(query, (login,))
            if cursor:
                result = cursor.fetchone()
                print(f"Query result: {result}")
                if result and PasswordManager.check_password(password, result[0].encode('utf-8')):
                    print("Password match successful")
                    return True
                else:
                    print("Password match failed or user not found")
            else:
                print("Cursor is None")
            return False
        except pyodbc.Error as e:
            print(f"Database error: {e}")
            return False

    def get_player_info(self, login):
        try:
            query = 'SELECT login, wins, losses, draws FROM players WHERE login = ?'
            cursor = self._execute_query(query, (login,))
            row = cursor.fetchone()
            if row:
                return {
                    "login": row[0],
                    "wins": row[1],
                    "losses": row[2],
                    "draws": row[3]
                }
            return None
        except pyodbc.Error:
            return None

    def update_login(self, current_login, new_login):
        query = 'UPDATE players SET login = ? WHERE login = ?'
        return self._execute_update(query, (new_login, current_login))

    def update_password(self, login, new_password):
        try:
            hashed_password = PasswordManager.hash_password(new_password)
            query = 'UPDATE players SET password = ? WHERE login = ?'
            return self._execute_update(query, (hashed_password, login))
        except pyodbc.Error:
            return False

    def update_wins(self, login, wins):
        query = 'UPDATE players SET wins = ? WHERE login = ?'
        return self._execute_update(query, (wins, login))

    def update_losses(self, login, losses):
        query = 'UPDATE players SET losses = ? WHERE login = ?'
        return self._execute_update(query, (losses, login))

    def update_draws(self, login, draws):
        query = 'UPDATE players SET draws = ? WHERE login = ?'
        return self._execute_update(query, (draws, login))

    def soft_delete_player(self, login):
        deletion_date = datetime.now()
        query = 'UPDATE players SET deletion_date = ? WHERE login = ?'
        return self._execute_update(query, (deletion_date, login))

    def get_top_players(self):
        try:
            query = """
                    SELECT 
                        TOP 5
                        players.login AS 'Login',
                        players.wins AS 'Wins',
                        players.losses AS 'Losses',
                        players.draws AS 'Draws',
                        (players.wins + players.losses + players.draws) AS 'Games',
                        (players.wins * 2 + players.draws) AS 'Points',
                        RANK() OVER (ORDER BY (players.wins * 2 + players.draws) DESC, players.wins DESC, (players.wins + players.losses + players.draws) ASC) AS 'Rank'
                    FROM players
                    WHERE players.deletion_date IS NULL
                    ORDER BY Points DESC, Wins DESC, Games ASC
                    """
            cursor = self._execute_query(query)
            result = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in result]
        except pyodbc.Error:
            return None

    def get_player_rank(self, login):
        try:
            query = """
                    WITH RankedPlayers AS (
                        SELECT 
                            players.login AS 'Login',
                            players.wins AS 'Wins',
                            players.losses AS 'Losses',
                            players.draws AS 'Draws',
                            (players.wins + players.losses + players.draws) AS 'Games',
                            (players.wins * 2 + players.draws) AS 'Points',
                            RANK() OVER (ORDER BY (players.wins * 2 + players.draws) DESC, players.wins DESC, (players.wins + players.losses + players.draws) ASC) AS 'Rank'
                        FROM players
                        WHERE players.deletion_date IS NULL
                    )
                    SELECT * FROM RankedPlayers WHERE login = ?
                    """
            cursor = self._execute_query(query, (login,))
            result = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in result]
        except pyodbc.Error:
            return None
