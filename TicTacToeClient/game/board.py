from config import SIZE

class Board:
    def __init__(self):
        self.reset_board()

    def reset_board(self):
        self.board = [['' for _ in range(SIZE)] for _ in range(SIZE)]

    def set_cell(self, row, col, player):
        self.board[row][col] = player

    def get_cell(self, row, col):
        return self.board[row][col]

    def is_full(self):
        return all(cell != '' for row in self.board for cell in row)

    def check_winner(self, player):
        return any(
            all(cell == player for cell in row) for row in self.board
        ) or any(
            all(row[i] == player for row in self.board) for i in range(SIZE)
        ) or all(
            self.board[i][i] == player for i in range(SIZE)
        ) or all(
            self.board[i][SIZE - 1 - i] == player for i in range(SIZE)
        )
