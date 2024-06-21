from PySide6.QtWidgets import QTableWidgetItem


class RatingView:
    def __init__(self, tic_tac_toe_form, request):
        self.tic_tac_toe_form = tic_tac_toe_form
        self.request = request
        self.setRating()

    def setRating(self):
        response = self.request.top_players()
        rank = self.request.get_player_rank()
        if response['valid'] and rank['valid']:
            top_players = response['info']
            player_rank = rank['info']

            players = top_players + player_rank

            self.tic_tac_toe_form.tableWidget.clearContents()
            self.tic_tac_toe_form.tableWidget.setRowCount(len(players))
            headers = ['Rank', 'Login', 'Wins', 'Losses', 'Draws', 'Games', 'Points']
            self.tic_tac_toe_form.tableWidget.setColumnCount(len(headers))
            self.tic_tac_toe_form.tableWidget.setHorizontalHeaderLabels(headers)

            for idx, player in enumerate(players):
                for col, key in enumerate(headers):
                    item = QTableWidgetItem(str(player.get(key, '')))
                    self.tic_tac_toe_form.tableWidget.setItem(idx, col, item)

            self.tic_tac_toe_form.tableWidget.verticalHeader().setVisible(False)