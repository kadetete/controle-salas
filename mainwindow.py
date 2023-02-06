# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QDate, QDateTime, QTime

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_menu import MenuMainWindow
from login.ui_login import LoginWidget
from calendario.ui_calendario import WidgetCalendario
from cliente.ui_cliente import ClienteWidget
from banco_de_dados.banco_de_dados import *
import datetime


class MainWindow(QMainWindow, MenuMainWindow):
    def __init__(self) ->None:
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.pushButton_voltar_menu.clicked.connect(self.closedMenu)
        self.pushButton_Auditorios.clicked.connect(self.redirectAuditorio)
        self.pushButton_SalaReuniao.clicked.connect(self.redirectSalaReuniao)
        self.pushButton_SalasEstudo.clicked.connect(self.redirectSalaEstudo)
        self.pushButton_Labs.clicked.connect(self.redirectLaboratorio)


    def closedMenu(self):
        calendario.show()
        self.close()

    def redirectAuditorio(self):
        self.close()

    def redirectSalaReuniao(self):
        self.close()

    def redirectLaboratorio(self):
        self.close()

    def redirectSalaEstudo(self):
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
        data = datetime.date.today()
        ano_min = data.year
        mes_min = data.month
        dia_min = data.day
        hora_atual = datetime.datetime.now()
        hora_min = hora_atual.hour
        min_min = hora_atual.minute
        seg_min = hora_atual.second
        data_min = QDate(ano_min, mes_min, dia_min)
        horario_min = QTime(hora_min, min_min, seg_min)
        horario_max = QTime(hora_min + 1, min_min, seg_min)
        hmin = QDateTime(data_min, horario_min)
        hmax = QDateTime(data_min, horario_max)
        self.setupUi(self)
        self.calendarWidget.setMinimumDate(data_min)
        self.timeEditHoraEntrada.setMinimumDateTime(hmin)
        self.timeEditHoraSaida.setMinimumDateTime(hmax)
        self.pushButtonConfirmar.clicked.connect(self.confirmar)
        self.pushButtonSair.clicked.connect(self.closedCalendario)

    def confirmar(self):
        calendario = self.calendarWidget.selectedDate()
        data = calendario.getDate()
        horario_inicio = self.timeEditHoraEntrada.time()
        horario_fim = self.timeEditHoraSaida.time()
        hora_inicio, hora_fim = self.formatarData((horario_inicio.hour()), (horario_fim.hour()))
        min_inicio, min_fim  = self.formatarData((horario_inicio.minute()), (horario_fim.minute()))
        
        mainwindow.label_dias.setText(f'{data[2]}/{data[1]}/{data[0]}')
        mainwindow.label_hora.setText(f'{hora_inicio}:{min_inicio} - {hora_fim}:{min_fim}')
        mainwindow.show()
        self.close()

    def closedCalendario(self):
        login.show()
        self.close()

    def formatarData(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        if self.inicio < 10:
            self.inicio = f'0{self.inicio}'
        if self.fim < 10:
            self.fim = f'0{self.fim}'
        return self.inicio, self.fim
        
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
    
