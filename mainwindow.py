# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from login.login import LoginWidget
from banco_de_dados.banco_de_dados import Login

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

class LoginJanela(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = LoginWidget()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    login = LoginJanela()
    login.show()
    usuario, senha = login.ui.butaoEntrar.clicked.connect(login.ui.pegarInfo())
    login1 = Login(usuario, senha)
    autenticado = login1.authenticate()
    if autenticado:
        mainwindow.show()
    sys.exit(app.exec())
