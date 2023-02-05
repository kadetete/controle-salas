# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'form.ui'
##
# Created by: Qt User Interface Compiler version 6.4.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
                               QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)
from banco_de_dados.banco_de_dados import Login


class LoginWidget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(321, 260)
        Widget.setMinimumSize(QSize(321, 260))
        Widget.setMaximumSize(QSize(321, 260))
        Widget.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbSicoges = QLabel(Widget)
        self.lbSicoges.setObjectName(u"lbSicoges")
        font = QFont()
        font.setFamilies([u"Versa Versa"])
        font.setPointSize(24)
        self.lbSicoges.setFont(font)
        self.lbSicoges.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbSicoges.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.verticalLayout_4.addWidget(self.lbSicoges)

        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.lbLogin = QLabel(Widget)
        self.lbLogin.setObjectName(u"lbLogin")
        font1 = QFont()
        font1.setFamilies([u"Versa Versa"])
        font1.setPointSize(18)
        self.lbLogin.setFont(font1)
        self.lbLogin.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbLogin.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        self.verticalLayout.addWidget(self.lbLogin)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(
            20, 24, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEditUsuario = QLineEdit(Widget)
        self.lineEditUsuario.setObjectName(u"lineEditUsuario")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEditUsuario.sizePolicy().hasHeightForWidth())
        self.lineEditUsuario.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Versa"])
        font2.setPointSize(11)
        self.lineEditUsuario.setFont(font2)
        self.lineEditUsuario.setLayoutDirection(Qt.LeftToRight)
        self.lineEditUsuario.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEditUsuario)

        self.formLayout.setLayout(
            0, QFormLayout.FieldRole, self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEditSenha = QLineEdit(Widget)
        self.lineEditSenha.setObjectName(u"lineEditSenha")
        sizePolicy.setHeightForWidth(
            self.lineEditSenha.sizePolicy().hasHeightForWidth())
        self.lineEditSenha.setSizePolicy(sizePolicy)
        self.lineEditSenha.setFont(font2)
        self.lineEditSenha.setEchoMode(QLineEdit.Password)
        self.lineEditSenha.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lineEditSenha)

        self.formLayout.setLayout(
            1, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.verticalLayout_2.addLayout(self.formLayout)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.butaoEntrar = QPushButton(Widget)
        self.butaoEntrar.setObjectName(u"butaoEntrar")
        sizePolicy.setHeightForWidth(
            self.butaoEntrar.sizePolicy().hasHeightForWidth())
        self.butaoEntrar.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Versa Versa"])
        font3.setPointSize(10)
        self.butaoEntrar.setFont(font3)
        self.butaoEntrar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(76, 76, 76);")

        self.horizontalLayout_2.addWidget(self.butaoEntrar)

        self.botaoSair = QPushButton(Widget)
        self.botaoSair.setObjectName(u"botaoSair")
        sizePolicy.setHeightForWidth(
            self.botaoSair.sizePolicy().hasHeightForWidth())
        self.botaoSair.setSizePolicy(sizePolicy)
        self.botaoSair.setFont(font3)
        self.botaoSair.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(76, 76, 76);")
        self.botaoSair.setFlat(False)

        self.horizontalLayout_2.addWidget(self.botaoSair)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.clicadoentrar = self.butaoEntrar.clicked

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(
            QCoreApplication.translate("Widget", u"Login", None))
        self.lbSicoges.setText(
            QCoreApplication.translate("Widget", u"SICOGES", None))
        self.lbLogin.setText(
            QCoreApplication.translate("Widget", u"Login", None))
        self.lineEditUsuario.setPlaceholderText(
            QCoreApplication.translate("Widget", u"Usu\u00e1rio", None))
        self.lineEditSenha.setPlaceholderText(
            QCoreApplication.translate("Widget", u"Senha", None))
        self.butaoEntrar.setText(
            QCoreApplication.translate("Widget", u"Entrar", None))
        self.botaoSair.setText(
            QCoreApplication.translate("Widget", u"Sair", None))
    # retranslateUi

    def pegarInfo(self):
        usuario = self.lineEditUsuario.text()
        senha = self.lineEditSenha.text()
        login1 = Login(usuario, senha)
        autenticado = login1.authenticate()
        return autenticado