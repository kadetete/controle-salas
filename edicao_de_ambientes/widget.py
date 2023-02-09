# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
<<<<<<< Updated upstream
from ui_edicao_de_ambientes import Ambientes
=======
from ui_edicao_de_ambientes import EdicaoAmbientes
>>>>>>> Stashed changes

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
<<<<<<< Updated upstream
        self.ui = Ambientes()
=======
        self.ui = EdicaoAmbientes()
>>>>>>> Stashed changes
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
