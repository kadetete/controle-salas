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
from sala_de_reuniao.ui_sala_de_reuniao import Sala_de_reuniao
from sala_de_estudo.ui_sala_de_estudo import Sala_de_estudo
from tela_auditorios.ui_auditorios import Auditorios
from laboratorio.ui_laboratorio import Laboratorio
from edicao_de_ambientes.ui_edicao_de_ambientes import Ambientes
from relacaoreservas.ui_relacaoreservas import RelacaoReservas
import datetime

class LoginWidget(QWidget, LoginWidget):
    def __init__(self) ->None:
        super(LoginWidget,self).__init__()
        self.setupUi(self)
        self.butaoEntrar.clicked.connect(lambda: self.checkLogin())
        self.botaoSair.clicked.connect(lambda: closed(self))

    def checkLogin(self):
        usuario = self.lineEditUsuario.text()
        senha = self.lineEditSenha.text()
        login1 = Login(usuario, senha)
        autenticado = login1.authenticate()
        if autenticado == True:
            calendario.checkcalendario()
            closed(self, calendario)
  
class CalendarioWidget(QWidget, WidgetCalendario):
    def __init__(self) ->None:
        super(CalendarioWidget,self).__init__()
        data = datetime.date.today()
        hora_atual = datetime.datetime.now()
        self.data_min = QDate(data.year, data.month, data.day)
        self.horario_min = QTime(hora_atual.hour, hora_atual.minute, hora_atual.second)
        self.horario_max = QTime(hora_atual.hour + 1, hora_atual.minute, hora_atual.second)
        self.setupUi(self)
        self.calendarWidget.setMinimumDate(self.data_min)
        self.calendarWidget.clicked.connect(self.checkcalendario)
        self.pushButtonConfirmar.clicked.connect(self.confirmar)
        self.pushButtonSair.clicked.connect(lambda: closed(self, login))
    def checkcalendario(self):
        calendario = self.calendarWidget.selectedDate()
        if self.data_min.getDate() == calendario.getDate():
            self.timeEditHoraEntrada.setMinimumTime(self.horario_min)
            self.timeEditHoraSaida.setMinimumTime(self.horario_max)
        else:
            self.timeEditHoraEntrada.setMinimumTime(QTime(0, 0, 0))
            self.timeEditHoraEntrada.setMinimumTime(QTime(0, 0, 0))

    def confirmar(self):
        calendario = self.calendarWidget.selectedDate()
        data = calendario.getDate()
        horario_inicio = self.timeEditHoraEntrada.time()
        horario_fim = self.timeEditHoraSaida.time()
        hora_inicio, hora_fim = self.formatarData((horario_inicio.hour()), (horario_fim.hour()))
        min_inicio, min_fim  = self.formatarData((horario_inicio.minute()), (horario_fim.minute()))
        self.data_escolida = [data[2], data[1], data[0]]
        self.horario_inicio_escolido = [hora_inicio, min_inicio]
        self.horario_final_escolido = [hora_fim, min_fim]
        self.pushButtonConfirmar.clicked.connect(lambda: self.data_time_escolido())
        mainwindow.label_dias.setText(f'{data[2]}/{data[1]}/{data[0]}')
        mainwindow.label_hora.setText(f'{hora_inicio}:{min_inicio} - {hora_fim}:{min_fim}')
        closed(self, mainwindow)

    def data_time_escolido(self):
        data_time = [self.data_escolida, self.horario_inicio_escolido, self.horario_final_escolido]
        ambiente.dataTime(data_time)


    def formatarData(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        if self.inicio < 10:
            self.inicio = f'0{self.inicio}'
        if self.fim < 10:
            self.fim = f'0{self.fim}'
        return self.inicio, self.fim

class MainWindow(QMainWindow, MenuMainWindow):
    def __init__(self) ->None:
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.pushButton_voltar_menu.clicked.connect(lambda: closed(self, calendario))
        self.pushButton_Auditorios.clicked.connect(lambda: closed(self, auditorio))
        self.pushButton_SalaReuniao.clicked.connect(lambda: closed(self, sala_reuniao))
        self.pushButton_SalasEstudo.clicked.connect(lambda: closed(self, sala_estudo))
        self.pushButton_Labs.clicked.connect(lambda: closed(self, laboratorio))
        self.pushButton_relatorio.clicked.connect(lambda: closed(self, relacao_de_reservas))


class Sala_de_reuniao(QWidget, Sala_de_reuniao):
    def __init__(self) ->None:
        super(Sala_de_reuniao, self).__init__()
        self.setupUi(self)
        self.pushButton_reserve_reuniao01.clicked.connect(lambda: ambiente.reservar('101'))
        self.pushButton_reserve_reuniao01.clicked.connect(lambda: closed(self))
        self.pushButton_edit_reuniao01.clicked.connect(lambda: ambiente.editar('101'))
        self.pushButton_edit_reuniao01.clicked.connect(lambda: self.label_description_reuniao01.setText(self.visual('101')))     

        self.pushButton_reserve_reuniao02.clicked.connect(lambda: ambiente.reservar('102'))
        self.pushButton_reserve_reuniao02.clicked.connect(lambda: closed(self))
        self.pushButton_reserve_reuniao02.clicked.connect(lambda: ambiente.editar('102'))
        self.pushButton_reserve_reuniao02.clicked.connect(lambda: self.label_description_reuniao02.setText(self.visual('102')))     

        self.pushButton_reserve_reuniao03.clicked.connect(lambda: ambiente.reservar('103'))
        self.pushButton_reserve_reuniao03.clicked.connect(lambda: closed(self))
        self.pushButton_edit_reuniao03.clicked.connect(lambda: ambiente.editar('103'))
        self.pushButton_edit_reuniao03.clicked.connect(lambda: self.label_description_reuniao03.setText(self.visual('103')))     

        self.pushButton_reserve_reuniao04.clicked.connect(lambda: ambiente.reservar('104'))
        self.pushButton_reserve_reuniao04.clicked.connect(lambda: closed(self))
        self.pushButton_edit_reuniao04.clicked.connect(lambda: ambiente.editar('104'))
        self.pushButton_edit_reuniao04.clicked.connect(lambda: self.label_description_reuniao04.setText(self.visual('104')))     

        self.pushButton_reuniao_voltar.clicked.connect(lambda: closed(self, mainwindow))
    def visual(self, id):
        BD_Ambientes(id).visualizar()


class Auditorios(QWidget, Auditorios):
    def __init__(self) -> None:
        super(Auditorios, self).__init__()
        self.setupUi(self)
        self.pushButton_reserve_class_meeting_2.clicked.connect(lambda: ambiente.reservar('201'))
        self.pushButton_reserve_class_meeting_2.clicked.connect(lambda: closed(self))
        self.pushButton_edit_class_meeting_2.clicked.connect(lambda: ambiente.editar('201'))
        self.pushButton_edit_class_meeting_2.clicked.connect(lambda: self.label_description_class_meeting_2.setText(self.visual('201')))     

        self.pushButton_reserve_class_meeting_3.clicked.connect(lambda: ambiente.reservar('202'))
        self.pushButton_reserve_class_meeting_3.clicked.connect(lambda: closed(self))
        self.pushButton_edit_class_meeting_3.clicked.connect(lambda: ambiente.editar('202'))
        self.pushButton_edit_class_meeting_3.clicked.connect(lambda: self.label_description_class_meeting_3.setText(self.visual('202')))     

        self.pushButton_reserve_class_meeting_4.clicked.connect(lambda: ambiente.reservar('203'))
        self.pushButton_reserve_class_meeting_4.clicked.connect(lambda: closed(self))
        self.pushButton_edit_class_meeting_4.clicked.connect(lambda: ambiente.editar('203'))
        self.pushButton_edit_class_meeting_4.clicked.connect(lambda: self.label_description_class_meeting_4.setText(self.visual('203')))     

        self.pushButton_reserve_class_meeting_5.clicked.connect(lambda: ambiente.reservar('204'))
        self.pushButton_reserve_class_meeting_5.clicked.connect(lambda: closed(self))
        self.pushButton_edit_class_meeting_5.clicked.connect(lambda: ambiente.editar('204'))
        self.pushButton_edit_class_meeting_5.clicked.connect(lambda: self.label_description_class_meeting_5.setText(self.visual('204')))     

        self.pushButton_auditorio_voltar.clicked.connect(lambda: closed(self, mainwindow))
    def visual(self, id):
        BD_Ambientes(id).visualizar()

class Laboratorio(QWidget, Laboratorio):
    def __init__(self) -> None:
        super(Laboratorio, self).__init__()
        self.setupUi(self)
        self.pushButton_reserve_lab01.clicked.connect(lambda: ambiente.reservar('301'))
        self.pushButton_reserve_lab01.clicked.connect(lambda: closed(self))
        self.pushButton_edit_lab01.clicked.connect(lambda: ambiente.editar('301'))
        self.pushButton_edit_lab01.clicked.connect(lambda: self.label_description_lab01.setText(self.visual('301')))     

        self.pushButton_reserve_lab02.clicked.connect(lambda: ambiente.reservar('302'))
        self.pushButton_reserve_lab02.clicked.connect(lambda: closed(self))
        self.pushButton_edit_lab02.clicked.connect(lambda: ambiente.editar('302'))
        self.pushButton_edit_lab02.clicked.connect(lambda: self.label_description_lab02.setText(self.visual('302')))   

        self.pushButton_reserve_lab03.clicked.connect(lambda: ambiente.reservar('303'))
        self.pushButton_reserve_lab03.clicked.connect(lambda: closed(self))
        self.pushButton_edit_lab03.clicked.connect(lambda: ambiente.editar('303'))
        self.pushButton_edit_lab03.clicked.connect(lambda: self.label_description_lab03.setText(self.visual('303')))     

        self.pushButton_reserve_lab04.clicked.connect(lambda: ambiente.reservar('304'))
        self.pushButton_reserve_lab04.clicked.connect(lambda: closed(self))
        self.pushButton_edit_lab04.clicked.connect(lambda: ambiente.editar('304'))
        self.pushButton_edit_lab04.clicked.connect(lambda: self.label_description_lab04.setText(self.visual('304')))     

        self.pushButton_lab_voltar.clicked.connect(lambda: closed(self, mainwindow))
    def visual(self, id):
        BD_Ambientes(id).visualizar()

class Sala_de_estudo(QWidget, Sala_de_estudo):
    def __init__(self) ->None:
        super(Sala_de_estudo, self).__init__()
        self.setupUi(self)
        self.pushButton_reserve_class_meeting_01.clicked.connect(lambda: ambiente.reservar('401'))
        self.pushButton_reserve_class_meeting_01.clicked.connect(lambda: closed(self))
        self.pushButton_edit_class_meeting_01.clicked.connect(lambda: ambiente.editar('401'))
        self.pushButton_edit_class_meeting_01.clicked.connect(lambda: self.label_description_class_meeting_01.setText(self.visual('401')))     

        self.pushButton_reserve_class_meeting_02.clicked.connect(lambda: ambiente.reservar('402'))
        self.pushButton_reserve_class_meeting_02.clicked.connect(lambda: closed(self))
        self.pushButton_edit_class_meeting_02.clicked.connect(lambda: ambiente.editar('402'))
        self.pushButton_edit_class_meeting_02.clicked.connect(lambda: self.label_description_class_meeting_02.setText(self.visual('402')))     

        self.pushButton_reserve_class_meeting_03.clicked.connect(lambda: ambiente.reservar('403'))
        self.pushButton_reserve_class_meeting_03.clicked.connect(lambda: closed(self))
        self.pushButton_edit_class_meeting_03.clicked.connect(lambda: ambiente.editar('403'))
        self.pushButton_edit_class_meeting_03.clicked.connect(lambda: self.label_description_class_meeting_03.setText(self.visual('403')))     

        self.pushButton_reserve_class_meeting_04.clicked.connect(lambda: ambiente.reservar('404'))
        self.pushButton_reserve_class_meeting_04.clicked.connect(lambda: closed(self))
        self.pushButton_edit_class_meeting_04.clicked.connect(lambda: ambiente.editar('404'))
        self.pushButton_edit_class_meeting_04.clicked.connect(lambda: self.label_description_class_meeting_04.setText(self.visual('404')))     

        self.pushButton_salaestudo_voltar.clicked.connect(lambda: closed(self, mainwindow))
    def visual(self, id):
        BD_Ambientes(id).visualizar()

class Ambientes(QWidget, Ambientes):
    def __init__(self) ->None:
        super(Ambientes, self).__init__()
        self.setupUi(self)

    def dataTime(self, data_time):
        self.data_time1 = data_time[1]
        self.data_time2 = data_time[2]
        self.data_time3 = data_time[3]

    def reservar(self, id_ambiente):
        self.id_ambiente = id_ambiente
        BD_Ambientes(id_ambiente).incluir(' ',' ')
        cliente.show()

    def confirmarResevar(self, id_cliente): 
        try:
            Reseva(id_cliente, self.id_ambiente, self.data_time1, self.data_time2, self.data_time3).verificar_resevas()
        except:
            data_time = datetime.datetime.now()
            horario_inicio = [data_time.hour, data_time.minute]
            horario_final = [data_time.hour + 1, data_time.minute]
            Reseva(id_cliente, self.id_ambiente, calendario.data_escolida, horario_inicio, horario_final).verificar_resevas()   
        closed(self, relacao_de_reservas)

    def editar(self, id_ambiente):
        self.id_ambiente = id_ambiente
        tipo = ''
        sala = ''
        a, b = id_ambiente[1:], id_ambiente[:-2]
        if b == '1':
            ambiente = 'Sala de Reunião'
            tipo = 'Sala'
        elif b == '2':
            ambiente = 'Auditório'
            tipo = 'Auditório'
        elif b== '3':
            ambiente = 'Laboratório'
            tipo = 'Lab'
        elif b  == '4':
            ambiente = 'Sala de Estudo'
            tipo = 'Sala'

        sala = f'{tipo} {a}' 
        self.label_ambiente_edit.setText(ambiente) 
        self.label_sala_edit.setText(sala)
        
        self.show()
        self.butaoConfirmar.clicked.connect(lambda: self.confirmarEdicao())
        self.botaoCancelar.clicked.connect(lambda: self.close())

    def confirmarEdicao(self):
        descricao = str(self.textEdit_descricao_ambiente.toPlainText())
        tamanho = str(self.lineEdit__tamanho_ambiente.text())
        if descricao != '' and tamanho != '':
            print(self.id_ambiente, descricao, tamanho)
            BD_Ambientes(self.id_ambiente).incluir(descricao, tamanho)
        closed(self)

        
        
class ClienteWidget(QWidget, ClienteWidget):
    def __init__(self) ->None:
        super(ClienteWidget,self).__init__()
        self.setupUi(self)
        self.push_button_register.clicked.connect(lambda: self.checkCliente())

    def checkCliente(self):
        self.cliente1 = ''
        matricula = self.line_edit_matricula.text()
        nome = self.line_edit_nome_cliente.text()
        sobrenome = self.line_edit_sobrenome_cliente.text()
        if (matricula != '' and nome != ""):
            self.cliente1 = Cliente(matricula, nome, sobrenome)
            self.cliente1.incluir()
            ambiente.confirmarResevar(self.cliente1.id())
            self.close()

class RelacaoReservas(QWidget, RelacaoReservas):
    def __init__(self) ->None:
        super(RelacaoReservas,self).__init__()
        self.setupUi(self)
        self.pushButton_relatorio_volar.clicked.connect(lambda: closed(self, mainwindow))
def dados():
    login1 = Login('Admin', '12345')
    login1.incluir()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginWidget()
    calendario = CalendarioWidget()
    mainwindow = MainWindow()
    sala_reuniao = Sala_de_reuniao()
    sala_estudo = Sala_de_estudo()
    auditorio = Auditorios()
    laboratorio = Laboratorio()
    relacao_de_reservas = RelacaoReservas()
    ambiente = Ambientes()
    cliente = ClienteWidget()
    dados()

    def closed(closedjanela, oponjanela = None):
        closedjanela.close()
        if oponjanela != None:
            oponjanela.show()  
    login.show()
    sys.exit(app.exec())
    
