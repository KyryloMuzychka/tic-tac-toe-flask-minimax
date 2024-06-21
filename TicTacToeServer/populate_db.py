import pyodbc
from config import CONNECTION_STRING
from password_manager import PasswordManager

players = [
    ("1", 10, 5, 2),
    ("gamerAce123", 15, 3, 4),
    ("playerNinja", 7, 8, 5),
    ("tigerWarrior", 12, 6, 3),
    ("dragonSlayer", 20, 2, 1),
    ("mysticMage", 11, 4, 6),
    ("shadowHunter", 8, 9, 3),
    ("lightBringer", 14, 5, 2),
    ("stormRider", 9, 7, 6),
    ("fireFury", 18, 4, 2),
    ("iceQueen", 13, 6, 3),
    ("windWalker", 6, 10, 5),
    ("earthGuardian", 10, 8, 3),
    ("waterWraith", 17, 3, 4),
    ("thunderGod", 15, 5, 1),
    ("ironGiant", 12, 7, 3),
    ("silverSurfer", 11, 6, 4),
    ("goldenKnight", 16, 3, 2),
    ("crimsonRogue", 9, 8, 4),
    ("emeraldArcher", 14, 5, 3)
]

def populate_database():
    try:
        conn = pyodbc.connect(CONNECTION_STRING)
        cursor = conn.cursor()

        for player in players:
            login, wins, losses, draws = player
            hashed_password = PasswordManager.hash_password("pass")
            query = """
                    INSERT INTO players (login, password, wins, losses, draws)
                    VALUES (?, ?, ?, ?, ?)
                    """
            cursor.execute(query, login, hashed_password, wins, losses, draws)

        conn.commit()
        cursor.close()
        conn.close()
        print("Players inserted successfully.")
    except pyodbc.Error as e:
        print(f"Error inserting players: {e}")

if __name__ == "__main__":
    populate_database()
