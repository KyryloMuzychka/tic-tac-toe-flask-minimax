from style import getLabelDrawsStyle, getLabelWinsStyle, getLabelLossesStyle
from config import SIZE

class GameView():
    def __init__(self, tic_tac_toe_form, board):
        self.tic_tac_toe_form = tic_tac_toe_form  
        self.board = board        
        
    def show_winner(self, player):
        self.tic_tac_toe_form.gameResult.setText(f"{player} Wins!")
        if player == 'X':
            self.tic_tac_toe_form.gameResult.setStyleSheet(getLabelWinsStyle())
        else:
            self.tic_tac_toe_form.gameResult.setStyleSheet(getLabelLossesStyle())

    def show_draw(self):
        self.tic_tac_toe_form.gameResult.setText("It's a Draw!")
        self.tic_tac_toe_form.gameResult.setStyleSheet(getLabelDrawsStyle())

    def refresh_board(self):
        for row in range(SIZE):
            for col in range(SIZE):
                cell_value = self.board.get_cell(row, col)
                button = self.tic_tac_toe_form.cellButtons[row][col]
                button.setText(cell_value)
                if cell_value == "X":
                    button.setStyleSheet("color: blue; font-size: 24pt;")
                else:
                    button.setStyleSheet("color: red; font-size: 24pt;")
                    
    def disable_cell_buttons(self):
        for row in self.tic_tac_toe_form.cellButtons:
            for cell in row:
                cell.setDisabled(True)    
                
    def enable_cell_buttons(self):
        for row in self.tic_tac_toe_form.cellButtons:
            for cell in row:
                cell.setDisabled(False)                                