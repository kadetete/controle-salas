# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edicao_de_ambientes.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

<<<<<<< Updated upstream
class Ambientes(object):
=======
class EdicaoAmbientes(object):
>>>>>>> Stashed changes
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(600, 400)
        Widget.setMinimumSize(QSize(600, 400))
        Widget.setMaximumSize(QSize(600, 400))
        Widget.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_ambiente_edit = QVBoxLayout()
        self.verticalLayout_ambiente_edit.setObjectName(u"verticalLayout_ambiente_edit")
        self.label_ambiente_edit = QLabel(Widget)
        self.label_ambiente_edit.setObjectName(u"label_ambiente_edit")
        font = QFont()
        font.setFamilies([u"Versa Versa"])
        font.setPointSize(24)
        self.label_ambiente_edit.setFont(font)
        self.label_ambiente_edit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_ambiente_edit.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_ambiente_edit.addWidget(self.label_ambiente_edit)

        self.verticalSpacer_ambiente_edit = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_ambiente_edit.addItem(self.verticalSpacer_ambiente_edit)


        self.verticalLayout.addLayout(self.verticalLayout_ambiente_edit)

        self.label_sala_edit = QLabel(Widget)
        self.label_sala_edit.setObjectName(u"label_sala_edit")
        font1 = QFont()
        font1.setFamilies([u"Versa Versa"])
        font1.setPointSize(18)
        self.label_sala_edit.setFont(font1)
        self.label_sala_edit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_sala_edit.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout.addWidget(self.label_sala_edit)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 24, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_tamanho_ambiente = QHBoxLayout()
        self.horizontalLayout_tamanho_ambiente.setObjectName(u"horizontalLayout_tamanho_ambiente")
        self.lineEdit__tamanho_ambiente = QLineEdit(Widget)
        self.lineEdit__tamanho_ambiente.setObjectName(u"lineEdit__tamanho_ambiente")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit__tamanho_ambiente.sizePolicy().hasHeightForWidth())
        self.lineEdit__tamanho_ambiente.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Noto Sans CJK JP"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.lineEdit__tamanho_ambiente.setFont(font2)
        self.lineEdit__tamanho_ambiente.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit__tamanho_ambiente.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_tamanho_ambiente.addWidget(self.lineEdit__tamanho_ambiente)


        self.verticalLayout_3.addLayout(self.horizontalLayout_tamanho_ambiente)

        self.horizontalLayout_descricao_ambiente = QHBoxLayout()
        self.horizontalLayout_descricao_ambiente.setObjectName(u"horizontalLayout_descricao_ambiente")
        self.textEdit_descricao_ambiente = QTextEdit(Widget)
        self.textEdit_descricao_ambiente.setObjectName(u"textEdit_descricao_ambiente")

        self.horizontalLayout_descricao_ambiente.addWidget(self.textEdit_descricao_ambiente)


        self.verticalLayout_3.addLayout(self.horizontalLayout_descricao_ambiente)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_botoes = QHBoxLayout()
        self.horizontalLayout_botoes.setObjectName(u"horizontalLayout_botoes")
        self.butaoConfirmar = QPushButton(Widget)
        self.butaoConfirmar.setObjectName(u"butaoConfirmar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.butaoConfirmar.sizePolicy().hasHeightForWidth())
        self.butaoConfirmar.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamilies([u"Versa Versa"])
        font3.setPointSize(10)
        self.butaoConfirmar.setFont(font3)
        self.butaoConfirmar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(76, 76, 76);")

        self.horizontalLayout_botoes.addWidget(self.butaoConfirmar)

        self.botaoCancelar = QPushButton(Widget)
        self.botaoCancelar.setObjectName(u"botaoCancelar")
        sizePolicy1.setHeightForWidth(self.botaoCancelar.sizePolicy().hasHeightForWidth())
        self.botaoCancelar.setSizePolicy(sizePolicy1)
        self.botaoCancelar.setFont(font3)
        self.botaoCancelar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(76, 76, 76);")
        self.botaoCancelar.setFlat(False)

        self.horizontalLayout_botoes.addWidget(self.botaoCancelar)


        self.verticalLayout_2.addLayout(self.horizontalLayout_botoes)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Edição de ambientes", None))
        self.label_ambiente_edit.setText(QCoreApplication.translate("Widget", u"ambiente_edit", None))
        self.label_sala_edit.setText(QCoreApplication.translate("Widget", u"Sala_edit", None))
        self.lineEdit__tamanho_ambiente.setPlaceholderText(QCoreApplication.translate("Widget", u"Digite aqui o novo tamanho da sala", None))
        self.textEdit_descricao_ambiente.setPlaceholderText(QCoreApplication.translate("Widget", u"Digite aqui nova descri\u00e7\u00e3o da sala", None))
        self.butaoConfirmar.setText(QCoreApplication.translate("Widget", u"confirmar", None))
        self.botaoCancelar.setText(QCoreApplication.translate("Widget", u"cancelar", None))
    # retranslateUi

