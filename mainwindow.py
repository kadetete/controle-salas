# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from login.login import LoginWidget

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

class LoginJanela(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = LoginWidget()
        self.ui.setupUi(self)
    
    def fechar(self):
        self.close()
        mainwindow.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    login = LoginJanela()
    login.show()
    login.ui.valorMudado.connect(login.fechar)
    sys.exit(app.exec())
    
