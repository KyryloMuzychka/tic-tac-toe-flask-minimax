from PySide6.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QLabel, QTabWidget,
    QHBoxLayout, QSizePolicy, QSpacerItem, QGridLayout,
    QLineEdit, QTableWidget, QComboBox
)
from PySide6.QtCore import QSize, Qt, QCoreApplication
from style import (
    getSaveNewDataButtonStyle, getDeleteAccountButtonStyle, getLabelStyle,
    getLabelErrorStyle, getLabelSuccessStyle, getEditStyle,
    getLabelDrawsStyle, getNewGameButtonStyle, getTabWidgetStyle,
    getLabelWinsStyle, getLabelLossesStyle
)

class TicTacToeFormDesign(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_interface(self)

    def set_interface(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(750, 400)
        Widget.setMinimumSize(QSize(750, 400))
        Widget.setSizeIncrement(QSize(750, 400))        

        self.tabMenu = QTabWidget(Widget)
        self.tabMenu.setGeometry(10, 10, 750, 370)
        self.tabMenu.setObjectName("tabMenu")        
        self.tabMenu.setStyleSheet(getTabWidgetStyle())        
        
        self.init_game_tab()
        self.init_rating_tab()
        self.init_player_tab()
        self.set_styles()        

    def init_game_tab(self):
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Main vertical layout
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setAlignment(Qt.AlignLeft)  # Align all elements to the left
        
        self.labelLoginName = QLabel("Login:")
        self.verticalLayout.addWidget(self.labelLoginName)
        
        self.labelWins = QLabel("Wins:")
        self.verticalLayout.addWidget(self.labelWins)
        
        self.labelLosses = QLabel("Losses:")
        self.verticalLayout.addWidget(self.labelLosses)
        
        self.labelDraws = QLabel("Draws:")
        self.verticalLayout.addWidget(self.labelDraws)            
        
        self.currentLabel = QLabel("Current:")
        self.verticalLayout.addWidget(self.currentLabel)
        
        self.select_mode = QComboBox()
        self.select_mode.addItems(["Novice", "Defense", "Attack", "Guru", "AI"])
        self.verticalLayout.addWidget(self.select_mode)
        
        self.gameResult = QLabel()
        self.verticalLayout.addWidget(self.gameResult)
        
        self.newGameButton = QPushButton("New Game")
        self.verticalLayout.addWidget(self.newGameButton)
        
        self.horizontalLayout.addLayout(self.verticalLayout)
        
        self.gridLayout = QGridLayout()
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        
        self.cellButtons = []
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = QPushButton()
                sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                button.setSizePolicy(sizePolicy)
                button.setMinimumSize(QSize(100, 100))
                button.setMaximumSize(QSize(100, 100))
                button.setObjectName(f"cellButton_{i * 3 + j + 1}")
                self.gridLayout.addWidget(button, i, j, 1, 1)             
                row_buttons.append(button)
            self.cellButtons.append(row_buttons)
        
        self.horizontalLayout.addLayout(self.gridLayout)
        self.tabMenu.addTab(self.tab, "Game")

    def init_rating_tab(self):
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.tableWidget = QTableWidget()
        self.tableWidget.setMaximumHeight(210) 
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget)                
        self.tabMenu.addTab(self.tab_2, "Rating")

    def init_player_tab(self):
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")

        # Main vertical layout
        self.verticalLayout_3 = QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setAlignment(Qt.AlignCenter)

        # Container for centering
        self.centerContainer = QWidget()
        self.centerLayout = QVBoxLayout(self.centerContainer)
        self.centerLayout.setAlignment(Qt.AlignCenter)

        # Horizontal layout for login label and result label
        self.horizontalLayout_1 = QHBoxLayout()
        self.labelNewLogin = QLabel("New Login:")
        self.labelResultUpdateLogin = QLabel()
        
        self.labelNewLogin.setAlignment(Qt.AlignLeft)  # Align text to the left
        self.labelResultUpdateLogin.setAlignment(Qt.AlignRight)
        
        self.horizontalLayout_1.addWidget(self.labelNewLogin)
        self.horizontalLayout_1.addWidget(self.labelResultUpdateLogin)
        self.centerLayout.addLayout(self.horizontalLayout_1)
        
        self.editNewLogin = QLineEdit()
        self.centerLayout.addWidget(self.editNewLogin)
        
        # Horizontal layout for password label and result label
        self.horizontalLayout_2 = QHBoxLayout()
        self.labelNewPassword = QLabel("New Password:")
        self.labelResultUpdatePassword = QLabel()
        
        self.labelNewPassword.setAlignment(Qt.AlignLeft)  # Align text to the left
        self.labelResultUpdatePassword.setAlignment(Qt.AlignRight)
        
        self.horizontalLayout_2.addWidget(self.labelNewPassword)
        self.horizontalLayout_2.addWidget(self.labelResultUpdatePassword)
        self.centerLayout.addLayout(self.horizontalLayout_2)
        
        self.editNewPassword = QLineEdit()
        self.centerLayout.addWidget(self.editNewPassword)
        
        verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.centerLayout.addItem(verticalSpacer)
        
        self.buttonSetNewData = QPushButton("Save New Data")
        self.centerLayout.addWidget(self.buttonSetNewData)
        
        self.buttonDeleteAccount = QPushButton("Delete Account")
        self.centerLayout.addWidget(self.buttonDeleteAccount)
        
        # Add center container to main layout
        self.verticalLayout_3.addWidget(self.centerContainer)
        
        self.tabMenu.addTab(self.tab_3, "Player")
        
    def set_styles(self):
        self.labelLoginName.setStyleSheet(getLabelStyle())
        self.labelDraws.setStyleSheet(getLabelDrawsStyle())        
        self.labelWins.setStyleSheet(getLabelWinsStyle())
        self.labelLosses.setStyleSheet(getLabelLossesStyle())
        self.currentLabel.setStyleSheet(getLabelStyle())        
        self.newGameButton.setStyleSheet(getNewGameButtonStyle())        
        self.editNewLogin.setStyleSheet(getEditStyle())
        self.editNewPassword.setStyleSheet(getEditStyle())
        self.labelResultUpdateLogin.setStyleSheet(getLabelErrorStyle())
        self.labelResultUpdatePassword.setStyleSheet(getLabelSuccessStyle())
        self.labelNewLogin.setStyleSheet(getLabelStyle())
        self.labelNewPassword.setStyleSheet(getLabelStyle())
        self.buttonSetNewData.setStyleSheet(getSaveNewDataButtonStyle())
        self.buttonDeleteAccount.setStyleSheet(getDeleteAccountButtonStyle())

    def retranslateUi(self, Widget):
        _translate = QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Tic Tac Toe"))
