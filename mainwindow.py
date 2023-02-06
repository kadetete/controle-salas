# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_menu import MenuMainWindow
from login.ui_login import LoginWidget
from calendario.ui_calendario import WidgetCalendario
from cliente.ui_cliente import ClienteWidget
from banco_de_dados.banco_de_dados import *


class MainWindow(QMainWindow, MenuMainWindow):
    def __init__(self) ->None:
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.pushButton_voltar_menu.clicked.connect(self.closedMenu)

    def closedMenu(self):
        calendario.show()
        self.close()

class LoginWidget(QWidget, LoginWidget):
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

class CalendarioWidget(QWidget, WidgetCalendario):
    def __init__(self) ->None:
        super(CalendarioWidget,self).__init__()
        self.setupUi(self)
        self.pushButtonConfirmar.clicked.connect(self.checkCalendario)
        self.pushButtonSair.clicked.connect(self.closedCalendario)

    def checkCalendario(self):
        mainwindow.show()
        self.close()

    def closedCalendario(self):
        login.show()
        self.close()

class ClienteWidget(QWidget, WidgetCalendario):
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
    
