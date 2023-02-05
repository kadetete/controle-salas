# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTimeEdit,
    QWidget)

class WidgetCalendario(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        font = QFont()
        font.setFamilies([u"Versa"])
        Widget.setFont(font)
        icon = QIcon(QIcon.fromTheme(u"dialog-question"))
        Widget.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelTitulo = QLabel(Widget)
        self.labelTitulo.setObjectName(u"labelTitulo")
        font1 = QFont()
        font1.setFamilies([u"Versa"])
        font1.setPointSize(24)
        font1.setBold(False)
        font1.setItalic(False)
        self.labelTitulo.setFont(font1)
        self.labelTitulo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelTitulo, 0, 0, 1, 4)

        self.calendarWidget = QCalendarWidget(Widget)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.gridLayout.addWidget(self.calendarWidget, 1, 0, 1, 4)

        self.labelHoraEntrada = QLabel(Widget)
        self.labelHoraEntrada.setObjectName(u"labelHoraEntrada")

        self.gridLayout.addWidget(self.labelHoraEntrada, 2, 1, 1, 1)

        self.timeEditHoraEntrada = QTimeEdit(Widget)
        self.timeEditHoraEntrada.setObjectName(u"timeEditHoraEntrada")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEditHoraEntrada.sizePolicy().hasHeightForWidth())
        self.timeEditHoraEntrada.setSizePolicy(sizePolicy)
        self.timeEditHoraEntrada.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.timeEditHoraEntrada, 2, 2, 1, 1)

        self.labelHoraSaida = QLabel(Widget)
        self.labelHoraSaida.setObjectName(u"labelHoraSaida")

        self.gridLayout.addWidget(self.labelHoraSaida, 3, 1, 1, 1)

        self.timeEditHoraSaida = QTimeEdit(Widget)
        self.timeEditHoraSaida.setObjectName(u"timeEditHoraSaida")
        self.timeEditHoraSaida.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.timeEditHoraSaida, 3, 2, 1, 1)

        self.pushButtonConfirmar = QPushButton(Widget)
        self.pushButtonConfirmar.setObjectName(u"pushButtonConfirmar")

        self.gridLayout.addWidget(self.pushButtonConfirmar, 4, 1, 1, 1)

        self.pushButtonSair = QPushButton(Widget)
        self.pushButtonSair.setObjectName(u"pushButtonSair")

        self.gridLayout.addWidget(self.pushButtonSair, 4, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(188, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 3, 2, 1)

        self.horizontalSpacer = QSpacerItem(188, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 2, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Calend\u00e1rio", None))
        self.labelTitulo.setText(QCoreApplication.translate("Widget", u"Insira data e hora:", None))
        self.labelHoraEntrada.setText(QCoreApplication.translate("Widget", u"Hora de entrada:", None))
        self.labelHoraSaida.setText(QCoreApplication.translate("Widget", u"Hora de sa\u00edda:", None))
        self.pushButtonConfirmar.setText(QCoreApplication.translate("Widget", u"Confirmar", None))
        self.pushButtonSair.setText(QCoreApplication.translate("Widget", u"Sair", None))
    # retranslateUi

