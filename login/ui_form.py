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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
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
        self.lbSicoges.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_4.addWidget(self.lbSicoges)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.lbLogin = QLabel(Widget)
        self.lbLogin.setObjectName(u"lbLogin")
        font1 = QFont()
        font1.setFamilies([u"Versa Versa"])
        font1.setPointSize(18)
        self.lbLogin.setFont(font1)
        self.lbLogin.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbLogin.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout.addWidget(self.lbLogin)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.lbUsuario = QLabel(Widget)
        self.lbUsuario.setObjectName(u"lbUsuario")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbUsuario.sizePolicy().hasHeightForWidth())
        self.lbUsuario.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Versa Versa"])
        font2.setPointSize(12)
        self.lbUsuario.setFont(font2)
        self.lbUsuario.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbUsuario)

        self.lineEditUsuario = QLineEdit(Widget)
        self.lineEditUsuario.setObjectName(u"lineEditUsuario")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEditUsuario.sizePolicy().hasHeightForWidth())
        self.lineEditUsuario.setSizePolicy(sizePolicy1)
        self.lineEditUsuario.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditUsuario)

        self.lbSenha = QLabel(Widget)
        self.lbSenha.setObjectName(u"lbSenha")
        sizePolicy.setHeightForWidth(self.lbSenha.sizePolicy().hasHeightForWidth())
        self.lbSenha.setSizePolicy(sizePolicy)
        self.lbSenha.setFont(font2)
        self.lbSenha.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbSenha)

        self.lineEditSenha = QLineEdit(Widget)
        self.lineEditSenha.setObjectName(u"lineEditSenha")
        sizePolicy1.setHeightForWidth(self.lineEditSenha.sizePolicy().hasHeightForWidth())
        self.lineEditSenha.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditSenha)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.butaoEntrar = QPushButton(Widget)
        self.butaoEntrar.setObjectName(u"butaoEntrar")
        sizePolicy1.setHeightForWidth(self.butaoEntrar.sizePolicy().hasHeightForWidth())
        self.butaoEntrar.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamilies([u"Versa Versa"])
        font3.setPointSize(10)
        self.butaoEntrar.setFont(font3)
        self.butaoEntrar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(76, 76, 76);")

        self.horizontalLayout_2.addWidget(self.butaoEntrar)

        self.botaoSair = QPushButton(Widget)
        self.botaoSair.setObjectName(u"botaoSair")
        sizePolicy1.setHeightForWidth(self.botaoSair.sizePolicy().hasHeightForWidth())
        self.botaoSair.setSizePolicy(sizePolicy1)
        self.botaoSair.setFont(font3)
        self.botaoSair.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(76, 76, 76);")
        self.botaoSair.setFlat(False)

        self.horizontalLayout_2.addWidget(self.botaoSair)


        self.formLayout.setLayout(2, QFormLayout.SpanningRole, self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Login", None))
        self.lbSicoges.setText(QCoreApplication.translate("Widget", u"SICOGES", None))
        self.lbLogin.setText(QCoreApplication.translate("Widget", u"Login", None))
        self.lbUsuario.setText(QCoreApplication.translate("Widget", u"Usu\u00e1rio:", None))
        self.lbSenha.setText(QCoreApplication.translate("Widget", u"Senha:", None))
        self.butaoEntrar.setText(QCoreApplication.translate("Widget", u"Entrar", None))
        self.botaoSair.setText(QCoreApplication.translate("Widget", u"Sair", None))
    # retranslateUi

