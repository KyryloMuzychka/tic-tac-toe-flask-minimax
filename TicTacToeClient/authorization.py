from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QFormLayout, QLineEdit, QLabel
from PySide6.QtCore import Qt
from tic_tac_toe_logic import TicTacToeLogic
from style import (getLabelStyle, getLabelErrorStyle, getLabelSuccessStyle, 
                   getEditStyle, getRegisterAccountButtonStyle, getLoginAccountButtonStyle)

class Authorization(QWidget):
    def __init__(self, facade, parent=None):
        super().__init__(parent)
        self.facade = facade
        self.set_interface()

    def set_interface(self):
        self.setWindowTitle("Authorization")
        self.setFixedSize(300, 300)
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)

        self.registerLayout = QFormLayout()
        self.loginEdit = QLineEdit()
        self.passwordEdit = QLineEdit()
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        self.headerLabel = QLabel("Authorization")
        self.headerLabel.setAlignment(Qt.AlignCenter)

        self.registerButton = QPushButton("Register")
        self.statusLabel = QLabel()

        self.loginButton = QPushButton("Login")

        self.layout.addWidget(self.headerLabel, alignment=Qt.AlignCenter)
        self.registerLayout.addRow("Login:", self.loginEdit)
        self.registerLayout.addRow("Password:", self.passwordEdit)
        self.layout.addLayout(self.registerLayout)
        self.layout.addWidget(self.loginButton)
        self.layout.addWidget(self.registerButton)
        self.layout.addWidget(self.statusLabel)

        self.setLayout(self.layout)

        self.registerButton.clicked.connect(self.register)
        self.loginButton.clicked.connect(self.login)
        
        self.setStyle()
    
    def setStyle(self):
        self.headerLabel.setStyleSheet(getLabelStyle())
        self.loginEdit.setStyleSheet(getEditStyle())
        self.passwordEdit.setStyleSheet(getEditStyle())
        self.loginButton.setStyleSheet(getLoginAccountButtonStyle())
        self.registerButton.setStyleSheet(getRegisterAccountButtonStyle())
    
    def handle_request_authorization(self, authorization_function):
        login = self.loginEdit.text()
        password = self.passwordEdit.text()
        result = authorization_function(login, password)
        self.statusLabel.setText(result['info'])        
        if result['valid']:
            self.statusLabel.setStyleSheet(getLabelSuccessStyle())
            self.show_tic_tac_toe()            
        else:
            self.statusLabel.setStyleSheet(getLabelErrorStyle())            
        
    def register(self):
        self.handle_request_authorization(self.facade.register_user)

    def login(self):
        self.handle_request_authorization(self.facade.login_user)
        
    def show_tic_tac_toe(self):
        self.tic_tac_toe_form = TicTacToeLogic(self, self.facade)
        self.close()
