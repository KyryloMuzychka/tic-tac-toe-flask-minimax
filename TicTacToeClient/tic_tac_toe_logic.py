from PySide6.QtCore import QTimer
from tic_tac_toe_form_design import TicTacToeFormDesign
from game.board import Board
from game.bot_factory import BotFactory
from view.rating_view import RatingView
from view.player_view import PlayerView
from view.game_view import GameView
from config import SIZE

class TicTacToeLogic:
    def __init__(self, auth_form, req):
        self.auth_form = auth_form
        self.request = req
        self.tic_tac_toe_form = TicTacToeFormDesign()
        self.tic_tac_toe_form.show()
        self.current_player = 'X'
        self.board = Board()
        self.tic_tac_toe_form.currentLabel.setText(f'Current: {self.current_player}')
        self.set_data()
        self.winner = None
        self.player_view = PlayerView(self.tic_tac_toe_form, self.auth_form, self.request)
        self.get_bot()
        self.game_view = GameView(self.tic_tac_toe_form, self.board)
        self.set_events()

    def set_events(self):
        self.tic_tac_toe_form.tabMenu.currentChanged.connect(self.tab_changed)
        self.tic_tac_toe_form.newGameButton.clicked.connect(self.reset_game)
        
        # Connect each cell button click to handle_button_click with correct row and col values
        for i in range(SIZE):
            for j in range(SIZE):
                self.tic_tac_toe_form.cellButtons[i][j].clicked.connect(lambda _, row=i, col=j: self.handle_button_click(row, col))
        
        self.tic_tac_toe_form.buttonSetNewData.clicked.connect(self.player_view.update_login_password)
        self.tic_tac_toe_form.buttonDeleteAccount.clicked.connect(self.player_view.soft_delete)

    def tab_changed(self, index):
        if index == 1:
            RatingView(self.tic_tac_toe_form, self.request)

    def get_bot(self):
        self.difficulty = self.tic_tac_toe_form.select_mode.currentText()
        self.bot = BotFactory.get_bot(self.difficulty)

    def change_current_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.tic_tac_toe_form.currentLabel.setText(f'Current: {self.current_player}')

    def set_data(self):
        response = self.request.get_player_info()
        self.tic_tac_toe_form.labelLoginName.setText(f"Login: {response['player_info']['login']}")
        self.tic_tac_toe_form.labelDraws.setText(f"Draws: {response['player_info']['draws']}")
        self.tic_tac_toe_form.labelLosses.setText(f"Losses: {response['player_info']['losses']}")
        self.tic_tac_toe_form.labelWins.setText(f"Wins: {response['player_info']['wins']}")

    def end_game(self, current_player):
        if self.board.check_winner(current_player):
            self.game_view.show_winner(self.current_player)
            response = self.request.get_player_info()
            if self.current_player == 'X':
                current_wins = response['player_info']['wins']
                self.request.update_wins(current_wins + 1)
                self.tic_tac_toe_form.labelWins.setText(f'Wins: {current_wins + 1}')
            else:
                current_losses = response['player_info']['losses']
                self.request.update_losses(current_losses + 1)
                self.tic_tac_toe_form.labelLosses.setText(f'Losses: {current_losses + 1}')
            self.game_view.disable_cell_buttons()
            self.winner = self.current_player
            return True
        if self.check_draw():
            self.game_view.show_draw()
            self.game_view.disable_cell_buttons()
            return True
        return False

    def handle_button_click(self, row, col):
        if self.board.get_cell(row, col) == '' and self.current_player == 'X':
            self.board.set_cell(row, col, self.current_player)
            button = self.tic_tac_toe_form.cellButtons[row][col]
            button.setText(self.current_player)
            self.game_view.refresh_board()
            if self.end_game(self.current_player):
                return
            self.change_current_player()
            QTimer.singleShot(500, self.make_bot_move)

    def make_bot_move(self):
        self.bot.make_move(self.board, self.current_player)
        self.game_view.refresh_board()
        if self.end_game(self.current_player):
            return
        self.change_current_player()

    def reset_game(self):       
        self.board.reset_board()
        for row in self.tic_tac_toe_form.cellButtons:
            for cell in row:
                cell.setText('')
                cell.setStyleSheet('')
                cell.setEnabled(True)
        self.tic_tac_toe_form.gameResult.setText('')
        self.game_view.enable_cell_buttons()
        self.get_bot()        
        if self.winner == 'O':
            self.current_player = 'O'
            self.make_bot_move()
        else:
            self.current_player = 'X'


    def check_draw(self):
        if self.board.is_full():
            response = self.request.get_player_info()
            current_draws = response['player_info']['draws']
            self.request.update_draws(current_draws + 1)
            self.tic_tac_toe_form.labelDraws.setText(f'Draws: {current_draws + 1}')
            return True
        return False
