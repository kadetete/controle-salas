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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
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

        self.verticalSpacer_2 = QSpacerItem(30, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vertical_layout_customer_cadastre.addItem(self.verticalSpacer_2)

        self.horizontal_layout_user_name = QHBoxLayout()
        self.horizontal_layout_user_name.setObjectName(u"horizontal_layout_user_name")
        self.horizontal_spacer_user_name_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontal_layout_user_name.addItem(self.horizontal_spacer_user_name_1)

        self.line_edit_user_name = QLineEdit(Widget)
        self.line_edit_user_name.setObjectName(u"line_edit_user_name")
        self.line_edit_user_name.setFont(font)
        self.line_edit_user_name.setInputMethodHints(Qt.ImhNoEditMenu)
        self.line_edit_user_name.setFrame(True)
        self.line_edit_user_name.setAlignment(Qt.AlignCenter)
        self.line_edit_user_name.setDragEnabled(False)
        self.line_edit_user_name.setReadOnly(False)
        self.line_edit_user_name.setClearButtonEnabled(False)

        self.horizontal_layout_user_name.addWidget(self.line_edit_user_name)

        self.horizontal_spacer_user_name_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontal_layout_user_name.addItem(self.horizontal_spacer_user_name_2)


        self.vertical_layout_customer_cadastre.addLayout(self.horizontal_layout_user_name)

        self.verticalSpacer_3 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vertical_layout_customer_cadastre.addItem(self.verticalSpacer_3)

        self.horizontal_layout_matriculation = QHBoxLayout()
        self.horizontal_layout_matriculation.setObjectName(u"horizontal_layout_matriculation")
        self.horizontal_spacer_matriculation_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontal_layout_matriculation.addItem(self.horizontal_spacer_matriculation_1)

        self.line_edit_matriculation = QLineEdit(Widget)
        self.line_edit_matriculation.setObjectName(u"line_edit_matriculation")
        self.line_edit_matriculation.setFont(font)
        self.line_edit_matriculation.setInputMethodHints(Qt.ImhNone)
        self.line_edit_matriculation.setAlignment(Qt.AlignCenter)

        self.horizontal_layout_matriculation.addWidget(self.line_edit_matriculation)

        self.horizontal_spacer_matriculation_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontal_layout_matriculation.addItem(self.horizontal_spacer_matriculation_2)


        self.vertical_layout_customer_cadastre.addLayout(self.horizontal_layout_matriculation)

        self.verticalSpacer_4 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vertical_layout_customer_cadastre.addItem(self.verticalSpacer_4)

        self.horizontal_layout_user_password = QHBoxLayout()
        self.horizontal_layout_user_password.setObjectName(u"horizontal_layout_user_password")
        self.horizontal_spacer_user_password_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontal_layout_user_password.addItem(self.horizontal_spacer_user_password_1)

        self.line_edit_user_password = QLineEdit(Widget)
        self.line_edit_user_password.setObjectName(u"line_edit_user_password")
        self.line_edit_user_password.setFont(font)
        self.line_edit_user_password.setEchoMode(QLineEdit.Password)
        self.line_edit_user_password.setAlignment(Qt.AlignCenter)

        self.horizontal_layout_user_password.addWidget(self.line_edit_user_password)

        self.horizontal_spacer_user_password_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontal_layout_user_password.addItem(self.horizontal_spacer_user_password_2)


        self.vertical_layout_customer_cadastre.addLayout(self.horizontal_layout_user_password)

        self.verticalSpacer_5 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vertical_layout_customer_cadastre.addItem(self.verticalSpacer_5)

        self.horizontal_layoutt_user_password_confirmation = QHBoxLayout()
        self.horizontal_layoutt_user_password_confirmation.setObjectName(u"horizontal_layoutt_user_password_confirmation")
        self.horizontal_spacer_user_password_confirmation_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontal_layoutt_user_password_confirmation.addItem(self.horizontal_spacer_user_password_confirmation_1)

        self.line_edit_user_password_confirmation = QLineEdit(Widget)
        self.line_edit_user_password_confirmation.setObjectName(u"line_edit_user_password_confirmation")
        self.line_edit_user_password_confirmation.setFont(font)
        self.line_edit_user_password_confirmation.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.line_edit_user_password_confirmation.setMaxLength(16)
        self.line_edit_user_password_confirmation.setFrame(True)
        self.line_edit_user_password_confirmation.setEchoMode(QLineEdit.Password)
        self.line_edit_user_password_confirmation.setAlignment(Qt.AlignCenter)

        self.horizontal_layoutt_user_password_confirmation.addWidget(self.line_edit_user_password_confirmation)

        self.horizontal_spacer_user_password_confirmation_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontal_layoutt_user_password_confirmation.addItem(self.horizontal_spacer_user_password_confirmation_2)


        self.vertical_layout_customer_cadastre.addLayout(self.horizontal_layoutt_user_password_confirmation)

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
        self.label_customer_cadastre.setText(QCoreApplication.translate("Widget", u"CADASTRO DE CLIENTES", None))
        self.line_edit_user_name.setInputMask("")
        self.line_edit_user_name.setText("")
        self.line_edit_user_name.setPlaceholderText(QCoreApplication.translate("Widget", u"Nome do usu\u00e1rio", None))
        self.line_edit_matriculation.setText("")
        self.line_edit_matriculation.setPlaceholderText(QCoreApplication.translate("Widget", u"Matr\u00edcula", None))
        self.line_edit_user_password.setText("")
        self.line_edit_user_password.setPlaceholderText(QCoreApplication.translate("Widget", u"Senha", None))
        self.line_edit_user_password_confirmation.setText("")
        self.line_edit_user_password_confirmation.setPlaceholderText(QCoreApplication.translate("Widget", u"Confirma\u00e7\u00e3o de Senha", None))
        self.push_button_register.setText(QCoreApplication.translate("Widget", u"Registrar", None))
    # retranslateUi

