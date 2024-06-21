import random
import math
from game.board import SIZE, Board

class BotStrategy:
    def make_move(self, board, current_player):
        pass

class NoviceBot(BotStrategy):
    def make_move(self, board, current_player):
        empty_cells = [(i, j) for i in range(SIZE) for j in range(SIZE) if board.get_cell(i, j) == '']
        if empty_cells:
            row, col = random.choice(empty_cells)
            board.set_cell(row, col, current_player)

class DefenseBot(BotStrategy):
    def make_move(self, board, current_player):
        if not self.block_player_win(board, current_player):
            NoviceBot().make_move(board, current_player)

    def block_player_win(self, board, current_player):
        for i in range(SIZE):
            for j in range(SIZE):
                if board.get_cell(i, j) == '':
                    board.set_cell(i, j, 'X')
                    if board.check_winner('X'):
                        board.set_cell(i, j, current_player)
                        return True
                    board.set_cell(i, j, '')
        return False

class AttackBot(BotStrategy):
    def make_move(self, board, current_player):
        if not self.complete_bot_win(board, current_player):
            NoviceBot().make_move(board, current_player)

    def complete_bot_win(self, board, current_player):
        for i in range(SIZE):
            for j in range(SIZE):
                if board.get_cell(i, j) == '':
                    board.set_cell(i, j, current_player)
                    if board.check_winner(current_player):
                        return True
                    board.set_cell(i, j, '')
        return False

class GuruBot(BotStrategy):    
    def make_move(self, board, current_player):
        if not AttackBot().complete_bot_win(board, current_player) and not DefenseBot().block_player_win(board, current_player):
            NoviceBot().make_move(board, current_player)

class AIBot(BotStrategy):
    def make_move(self, board, current_player):
        move = self.minimax(board, sum(row.count('') for row in board.board), current_player)
        row, col = move[0], move[1]
        if row != -1 and col != -1:
            board.set_cell(row, col, current_player)

    def minimax(self, state, empty_cells_amount, player):
        if player == 'O':
            best = [-1, -1, -math.inf]
        else:
            best = [-1, -1, math.inf]

        if empty_cells_amount == 0 or state.check_winner('O') or state.check_winner('X'):
            score = self.evaluate(state)
            return [-1, -1, score]

        empty_cells = [(i, j) for i in range(SIZE) for j in range(SIZE) if state.get_cell(i, j) == '']

        for cell in empty_cells:
            x, y = cell
            state.set_cell(x, y, player)
            next_player = 'O' if player == 'X' else 'X'
            score = self.minimax(state, empty_cells_amount - 1, next_player)
            state.set_cell(x, y, '')
            score[0], score[1] = x, y

            if player == 'O':
                if score[2] > best[2]:
                    best = score
            else:
                if score[2] < best[2]:
                    best = score

        return best

    def evaluate(self, state):
        if state.check_winner('O'):
            return 1
        elif state.check_winner('X'):
            return -1
        else:
            return 0
