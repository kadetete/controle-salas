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


def pegarInfo(self):
    usuario = self.ui.lineEditUsuario.text()
    senha = self.ui.lineEditSenha.text()
    login1 = Login(usuario, senha)
    autenticado = login1.authenticate()
    if autenticado:
        mainwindow.show()
        login.close

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    login = LoginJanela()
    login.show()
    login.ui.butaoEntrar.clicked.connect(pegarInfo())
    sys.exit(app.exec())
