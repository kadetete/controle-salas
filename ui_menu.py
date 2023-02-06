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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

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
        self.verticalSpacer = QSpacerItem(12, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 2)

        self.gridFrame = QFrame(self.centralwidget)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setFrameShape(QFrame.Box)
        self.gridFrame.setFrameShadow(QFrame.Raised)
        self.gridFrame.setLineWidth(1)
        self.gridLayout_2 = QGridLayout(self.gridFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.gridFrame)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Versa"])
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 1, 2, 1, 1)

        self.label_2 = QLabel(self.gridFrame)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Versa"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.gridFrame)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Versa"])
        font2.setPointSize(24)
        font2.setBold(False)
        font2.setItalic(False)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 3)


        self.gridLayout.addWidget(self.gridFrame, 2, 0, 1, 2)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy1)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setLayoutDirection(Qt.RightToLeft)
        icon = QIcon(QIcon.fromTheme(u"go-previous"))
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_5, 0, 0, 1, 1)

        self.gridFrame1 = QFrame(self.centralwidget)
        self.gridFrame1.setObjectName(u"gridFrame1")
        self.gridFrame1.setFrameShape(QFrame.Box)
        self.gridFrame1.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.gridFrame1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_4 = QPushButton(self.gridFrame1)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setFamilies([u"Versa"])
        font3.setPointSize(12)
        font3.setItalic(True)
        self.pushButton_4.setFont(font3)

        self.gridLayout_4.addWidget(self.pushButton_4, 2, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.gridFrame1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setFont(font3)

        self.gridLayout_4.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.gridFrame1)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)
        self.pushButton_3.setFont(font3)

        self.gridLayout_4.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.gridFrame1)
        self.label_4.setObjectName(u"label_4")
        font4 = QFont()
        font4.setFamilies([u"Versa"])
        font4.setPointSize(18)
        self.label_4.setFont(font4)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 2)

        self.pushButton = QPushButton(self.gridFrame1)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy3)
        self.pushButton.setFont(font3)

        self.gridLayout_4.addWidget(self.pushButton, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.gridFrame1, 4, 0, 4, 2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(18, -1, -1, -1)

        self.gridLayout.addLayout(self.verticalLayout_2, 8, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Hora:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Dias Selecionados:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SICOGES", None))
        self.pushButton_5.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"SALAS DE ESTUDO", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"AUDITORIOS", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"LABORATORIOS", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"LISTA DE AMBIENTES", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"SALA DE REUNI\u00c3O", None))
    # retranslateUi

