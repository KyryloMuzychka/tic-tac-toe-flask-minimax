import sys
from PySide6.QtWidgets import QApplication
from authorization import Authorization
from request.request_facade import RequestFacade
from config import URL

if __name__ == "__main__":
    app = QApplication(sys.argv)
    facade = RequestFacade(URL)
    authorization_form = Authorization(facade)
    authorization_form.show()
    sys.exit(app.exec())
