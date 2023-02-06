# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

from banco_de_dados.banco_de_dados import *
from arquivos_py.ui_mainwindow import Ui_MainWindow
from arquivos_py.ui_login import Ui_LoginWidget
from arquivos_py.ui_calendario import Ui_CalendarioWidget
from arquivos_py.ui_cliente import Ui_ClienteWidget


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) ->None:
        super(MainWindow,self).__init__()
        self.setupUi(self)

class LoginWidget(QWidget, Ui_LoginWidget):
    def __init__(self) ->None:
        super(LoginWidget,self).__init__()
        self.setupUi(self)
        self.butaoEntrar.clicked.connect(self.checkLogin)
        self.botaoSair.clicked.connect(self.closedLogin)

    def checkLogin(self):
        usuario = self.lineEditUsuario.text()
        senha = self.lineEditSenha.text()
        login1 = Login(usuario, senha)
        autenticado = login1.authenticate()
        if autenticado == True:
            calendario.show()
            self.close()
            
    def closedLogin(self):
        self.close()

class CalendarioWidget(QWidget, Ui_CalendarioWidget):
    def __init__(self) ->None:
        super(CalendarioWidget,self).__init__()
        self.setupUi(self)

class ClienteWidget(QWidget, Ui_ClienteWidget):
    def __init__(self) ->None:
        super(ClienteWidget,self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    login = LoginWidget()
    calendario = CalendarioWidget()
    cliente = ClienteWidget()
    login.show()
    sys.exit(app.exec())
    
