# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class MenuMainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(774, 482)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_voltar_menu = QPushButton(self.centralwidget)
        self.pushButton_voltar_menu.setObjectName(u"pushButton_voltar_menu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_voltar_menu.sizePolicy().hasHeightForWidth())
        self.pushButton_voltar_menu.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Versa"])
        font.setPointSize(10)
        self.pushButton_voltar_menu.setFont(font)
        self.pushButton_voltar_menu.setLayoutDirection(Qt.RightToLeft)
        icon = QIcon()
        iconThemeName = u"go-previous"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.pushButton_voltar_menu.setIcon(icon)
        self.pushButton_voltar_menu.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_voltar_menu, 0, 0, 1, 1)

        self.gridFrame = QFrame(self.centralwidget)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setFrameShape(QFrame.Box)
        self.gridFrame.setFrameShadow(QFrame.Raised)
        self.gridFrame.setLineWidth(1)
        self.gridLayout_2 = QGridLayout(self.gridFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_hora = QLabel(self.gridFrame)
        self.label_hora.setObjectName(u"label_hora")

        self.gridLayout_2.addWidget(self.label_hora, 2, 4, 1, 1)

        self.label_2 = QLabel(self.gridFrame)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Versa"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_3 = QLabel(self.gridFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 2, 3, 1, 1)

        self.label_dias = QLabel(self.gridFrame)
        self.label_dias.setObjectName(u"label_dias")

        self.gridLayout_2.addWidget(self.label_dias, 2, 1, 1, 1)

        self.label = QLabel(self.gridFrame)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Versa"])
        font2.setPointSize(24)
        font2.setBold(False)
        font2.setItalic(False)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 5)

        self.pushButton_relatorio = QPushButton(self.gridFrame)
        self.pushButton_relatorio.setObjectName(u"pushButton_relatorio")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_relatorio.sizePolicy().hasHeightForWidth())
        self.pushButton_relatorio.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.pushButton_relatorio, 1, 2, 1, 1)


        self.gridLayout.addWidget(self.gridFrame, 2, 0, 1, 2)

        self.gridFrame1 = QFrame(self.centralwidget)
        self.gridFrame1.setObjectName(u"gridFrame1")
        self.gridFrame1.setFrameShape(QFrame.Box)
        self.gridFrame1.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.gridFrame1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_4 = QLabel(self.gridFrame1)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setFamilies([u"Versa"])
        font3.setPointSize(18)
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 2)

        self.pushButton_Labs = QPushButton(self.gridFrame1)
        self.pushButton_Labs.setObjectName(u"pushButton_Labs")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_Labs.sizePolicy().hasHeightForWidth())
        self.pushButton_Labs.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setFamilies([u"Versa"])
        font4.setPointSize(12)
        font4.setItalic(True)
        self.pushButton_Labs.setFont(font4)

        self.gridLayout_4.addWidget(self.pushButton_Labs, 3, 0, 1, 1)

        self.pushButton_Auditorios = QPushButton(self.gridFrame1)
        self.pushButton_Auditorios.setObjectName(u"pushButton_Auditorios")
        sizePolicy3.setHeightForWidth(self.pushButton_Auditorios.sizePolicy().hasHeightForWidth())
        self.pushButton_Auditorios.setSizePolicy(sizePolicy3)
        self.pushButton_Auditorios.setFont(font4)

        self.gridLayout_4.addWidget(self.pushButton_Auditorios, 1, 1, 1, 1)

        self.pushButton_SalasEstudo = QPushButton(self.gridFrame1)
        self.pushButton_SalasEstudo.setObjectName(u"pushButton_SalasEstudo")
        sizePolicy3.setHeightForWidth(self.pushButton_SalasEstudo.sizePolicy().hasHeightForWidth())
        self.pushButton_SalasEstudo.setSizePolicy(sizePolicy3)
        self.pushButton_SalasEstudo.setFont(font4)

        self.gridLayout_4.addWidget(self.pushButton_SalasEstudo, 3, 1, 1, 1)

        self.pushButton_SalaReuniao = QPushButton(self.gridFrame1)
        self.pushButton_SalaReuniao.setObjectName(u"pushButton_SalaReuniao")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_SalaReuniao.sizePolicy().hasHeightForWidth())
        self.pushButton_SalaReuniao.setSizePolicy(sizePolicy4)
        self.pushButton_SalaReuniao.setFont(font4)

        self.gridLayout_4.addWidget(self.pushButton_SalaReuniao, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.gridFrame1, 4, 0, 4, 2)

        self.verticalSpacer = QSpacerItem(12, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_voltar_menu.setText(QCoreApplication.translate("MainWindow", u"voltar", None))
        self.label_hora.setText(QCoreApplication.translate("MainWindow", u"hhhhhh", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Dias Selecionados:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Hora:", None))
        self.label_dias.setText(QCoreApplication.translate("MainWindow", u"ddddd", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SICOGES", None))
        self.pushButton_relatorio.setText(QCoreApplication.translate("MainWindow", u"Salas reservadas", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"LISTA DE AMBIENTES", None))
        self.pushButton_Labs.setText(QCoreApplication.translate("MainWindow", u"LABORATORIOS", None))
        self.pushButton_Auditorios.setText(QCoreApplication.translate("MainWindow", u"AUDITORIOS", None))
        self.pushButton_SalasEstudo.setText(QCoreApplication.translate("MainWindow", u"SALAS DE ESTUDO", None))
        self.pushButton_SalaReuniao.setText(QCoreApplication.translate("MainWindow", u"SALA DE REUNI\u00c3O", None))
    # retranslateUi

