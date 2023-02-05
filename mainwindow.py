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

class LoginJanela(QWidget, LoginWidget):
    def __init__(self) ->None:
        super(LoginJanela,self).__init__()
        self.setupUi(self)

        self.butaoEntrar.clicked.connect(self.checkLogin)

    def checkLogin(self):
        usuario = self.lineEditUsuario.text()
        senha = self.lineEditSenha.text()
        login1 = Login(usuario, senha)
        autenticado = login1.authenticate()
        if autenticado == True:
            mainwindow.show()
            self.close
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    login = LoginJanela()
    login.show()
    sys.exit(app.exec())
    
