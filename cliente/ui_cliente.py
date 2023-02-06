# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cliente.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class ClienteWidget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(564, 455)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QSize(564, 455))
        Widget.setMaximumSize(QSize(564, 455))
        font = QFont()
        font.setFamilies([u"Versa Versa"])
        font.setPointSize(11)
        Widget.setFont(font)
        Widget.setStyleSheet(u"background-color:rgb(44, 44, 44);\n"
"color:rgb(241, 241, 241);")
        self.vertical_layout_customer_cadastre = QVBoxLayout(Widget)
        self.vertical_layout_customer_cadastre.setObjectName(u"vertical_layout_customer_cadastre")
        self.verticalSpacer_1 = QSpacerItem(70, 60, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vertical_layout_customer_cadastre.addItem(self.verticalSpacer_1)

        self.horizontal_layout_sicoges = QHBoxLayout()
        self.horizontal_layout_sicoges.setObjectName(u"horizontal_layout_sicoges")
        self.horizontal_layout_sicoges.setContentsMargins(-1, 0, -1, -1)
        self.horizontal_spacer_sicoges_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontal_layout_sicoges.addItem(self.horizontal_spacer_sicoges_1)

        self.label_sicoges = QLabel(Widget)
        self.label_sicoges.setObjectName(u"label_sicoges")

        self.horizontal_layout_sicoges.addWidget(self.label_sicoges)

        self.horizontal_spacer_sicoges_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontal_layout_sicoges.addItem(self.horizontal_spacer_sicoges_2)


        self.vertical_layout_customer_cadastre.addLayout(self.horizontal_layout_sicoges)

        self.verticalSpacer_2 = QSpacerItem(30, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vertical_layout_customer_cadastre.addItem(self.verticalSpacer_2)

        self.horizontal_llayout_customer_cadastre = QHBoxLayout()
        self.horizontal_llayout_customer_cadastre.setObjectName(u"horizontal_llayout_customer_cadastre")
        self.horizontal_spacer_customer_cadastre_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontal_llayout_customer_cadastre.addItem(self.horizontal_spacer_customer_cadastre_1)

        self.label_customer_cadastre = QLabel(Widget)
        self.label_customer_cadastre.setObjectName(u"label_customer_cadastre")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_customer_cadastre.sizePolicy().hasHeightForWidth())
        self.label_customer_cadastre.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Versa Versa"])
        font1.setPointSize(24)
        self.label_customer_cadastre.setFont(font1)
        self.label_customer_cadastre.setAlignment(Qt.AlignCenter)

        self.horizontal_llayout_customer_cadastre.addWidget(self.label_customer_cadastre)

        self.horizontal_spacer_customer_cadastre_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontal_llayout_customer_cadastre.addItem(self.horizontal_spacer_customer_cadastre_2)


        self.vertical_layout_customer_cadastre.addLayout(self.horizontal_llayout_customer_cadastre)

        self.verticalSpacer_3 = QSpacerItem(13, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vertical_layout_customer_cadastre.addItem(self.verticalSpacer_3)

        self.horizontal_layout_nome_cliente = QHBoxLayout()
        self.horizontal_layout_nome_cliente.setObjectName(u"horizontal_layout_nome_cliente")
        self.horizontal_spacer_nome_cliente_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontal_layout_nome_cliente.addItem(self.horizontal_spacer_nome_cliente_1)

        self.line_edit_nome_cliente = QLineEdit(Widget)
        self.line_edit_nome_cliente.setObjectName(u"line_edit_nome_cliente")
        self.line_edit_nome_cliente.setFont(font)
        self.line_edit_nome_cliente.setInputMethodHints(Qt.ImhNoEditMenu)
        self.line_edit_nome_cliente.setFrame(True)
        self.line_edit_nome_cliente.setAlignment(Qt.AlignCenter)
        self.line_edit_nome_cliente.setDragEnabled(False)
        self.line_edit_nome_cliente.setReadOnly(False)
        self.line_edit_nome_cliente.setClearButtonEnabled(False)

        self.horizontal_layout_nome_cliente.addWidget(self.line_edit_nome_cliente)

        self.horizontal_spacer_nome_cliente_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontal_layout_nome_cliente.addItem(self.horizontal_spacer_nome_cliente_2)


        self.vertical_layout_customer_cadastre.addLayout(self.horizontal_layout_nome_cliente)

        self.verticalSpacer_4 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vertical_layout_customer_cadastre.addItem(self.verticalSpacer_4)

        self.horizontal_layout_sobrenome_cliente = QHBoxLayout()
        self.horizontal_layout_sobrenome_cliente.setObjectName(u"horizontal_layout_sobrenome_cliente")
        self.horizontal_spacer_sobrenome_cliente_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontal_layout_sobrenome_cliente.addItem(self.horizontal_spacer_sobrenome_cliente_1)

        self.line_edit_sobrenome_cliente = QLineEdit(Widget)
        self.line_edit_sobrenome_cliente.setObjectName(u"line_edit_sobrenome_cliente")
        self.line_edit_sobrenome_cliente.setFont(font)
        self.line_edit_sobrenome_cliente.setEchoMode(QLineEdit.Normal)
        self.line_edit_sobrenome_cliente.setAlignment(Qt.AlignCenter)

        self.horizontal_layout_sobrenome_cliente.addWidget(self.line_edit_sobrenome_cliente)

        self.horizontal_spacer_sobrenome_cliente_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontal_layout_sobrenome_cliente.addItem(self.horizontal_spacer_sobrenome_cliente_2)


        self.vertical_layout_customer_cadastre.addLayout(self.horizontal_layout_sobrenome_cliente)

        self.verticalSpacer_5 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vertical_layout_customer_cadastre.addItem(self.verticalSpacer_5)

        self.horizontal_layout_matricula = QHBoxLayout()
        self.horizontal_layout_matricula.setObjectName(u"horizontal_layout_matricula")
        self.horizontal_spacer_matricula_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontal_layout_matricula.addItem(self.horizontal_spacer_matricula_1)

        self.line_edit_matricula = QLineEdit(Widget)
        self.line_edit_matricula.setObjectName(u"line_edit_matricula")
        self.line_edit_matricula.setFont(font)
        self.line_edit_matricula.setInputMethodHints(Qt.ImhNone)
        self.line_edit_matricula.setAlignment(Qt.AlignCenter)

        self.horizontal_layout_matricula.addWidget(self.line_edit_matricula)

        self.horizontal_spacer_matricula_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontal_layout_matricula.addItem(self.horizontal_spacer_matricula_2)


        self.vertical_layout_customer_cadastre.addLayout(self.horizontal_layout_matricula)

        self.verticalSpacer_6 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vertical_layout_customer_cadastre.addItem(self.verticalSpacer_6)

        self.horizontal_layout_register = QHBoxLayout()
        self.horizontal_layout_register.setObjectName(u"horizontal_layout_register")
        self.horizontal_spacer_register_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontal_layout_register.addItem(self.horizontal_spacer_register_1)

        self.push_button_register = QPushButton(Widget)
        self.push_button_register.setObjectName(u"push_button_register")
        sizePolicy.setHeightForWidth(self.push_button_register.sizePolicy().hasHeightForWidth())
        self.push_button_register.setSizePolicy(sizePolicy)
        self.push_button_register.setFont(font)

        self.horizontal_layout_register.addWidget(self.push_button_register)

        self.horizontal_spacer_register_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontal_layout_register.addItem(self.horizontal_spacer_register_2)


        self.vertical_layout_customer_cadastre.addLayout(self.horizontal_layout_register)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.vertical_layout_customer_cadastre.addItem(self.verticalSpacer_7)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Cadastro de clientes", None))
        self.label_sicoges.setText(QCoreApplication.translate("Widget", u"SICOGES", None))
        self.label_customer_cadastre.setText(QCoreApplication.translate("Widget", u"CADASTRO DE CLIENTES", None))
        self.line_edit_nome_cliente.setInputMask("")
        self.line_edit_nome_cliente.setText("")
        self.line_edit_nome_cliente.setPlaceholderText(QCoreApplication.translate("Widget", u"Nome", None))
        self.line_edit_sobrenome_cliente.setText("")
        self.line_edit_sobrenome_cliente.setPlaceholderText(QCoreApplication.translate("Widget", u"Sobrenome", None))
        self.line_edit_matricula.setText("")
        self.line_edit_matricula.setPlaceholderText(QCoreApplication.translate("Widget", u"Matr\u00edcula", None))
        self.push_button_register.setText(QCoreApplication.translate("Widget", u"Registrar", None))
    # retranslateUi

