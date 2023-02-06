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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QPushButton,
    QScrollBar, QSizePolicy, QTableView, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(769, 505)
        self.gridFrame = QFrame(Widget)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setGeometry(QRect(10, 13, 746, 61))
        self.gridFrame.setFrameShape(QFrame.Box)
        self.gridFrame.setFrameShadow(QFrame.Raised)
        self.gridFrame.setLineWidth(1)
        self.horizontalLayout_3 = QHBoxLayout(self.gridFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_relatorio_volar = QPushButton(self.gridFrame)
        self.pushButton_relatorio_volar.setObjectName(u"pushButton_relatorio_volar")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_relatorio_volar.sizePolicy().hasHeightForWidth())
        self.pushButton_relatorio_volar.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Versa"])
        font.setPointSize(10)
        self.pushButton_relatorio_volar.setFont(font)
        self.pushButton_relatorio_volar.setLayoutDirection(Qt.RightToLeft)
        icon = QIcon()
        iconThemeName = u"go-previous"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"../../controle-salas", QSize(), QIcon.Normal, QIcon.Off)

        self.pushButton_relatorio_volar.setIcon(icon)
        self.pushButton_relatorio_volar.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_relatorio_volar)

        self.label_33 = QLabel(self.gridFrame)
        self.label_33.setObjectName(u"label_33")
        font1 = QFont()
        font1.setFamilies([u"Versa"])
        font1.setPointSize(24)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_33.setFont(font1)
        self.label_33.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_33)

        self.gridFrame_8 = QFrame(Widget)
        self.gridFrame_8.setObjectName(u"gridFrame_8")
        self.gridFrame_8.setGeometry(QRect(20, 144, 731, 341))
        font2 = QFont()
        font2.setFamilies([u"Versa"])
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        self.gridFrame_8.setFont(font2)
        self.gridFrame_8.setFrameShape(QFrame.Box)
        self.gridFrame_8.setFrameShadow(QFrame.Sunken)
        self.gridLayout_7 = QGridLayout(self.gridFrame_8)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.tableView_relatorio = QTableView(self.gridFrame_8)
        self.tableView_relatorio.setObjectName(u"tableView_relatorio")

        self.horizontalLayout_29.addWidget(self.tableView_relatorio)


        self.gridLayout_7.addLayout(self.horizontalLayout_29, 0, 0, 1, 1)

        self.verticalScrollBar_relatorio = QScrollBar(self.gridFrame_8)
        self.verticalScrollBar_relatorio.setObjectName(u"verticalScrollBar_relatorio")
        self.verticalScrollBar_relatorio.setOrientation(Qt.Vertical)

        self.gridLayout_7.addWidget(self.verticalScrollBar_relatorio, 0, 1, 1, 1)

        self.horizontalFrame_7 = QFrame(Widget)
        self.horizontalFrame_7.setObjectName(u"horizontalFrame_7")
        self.horizontalFrame_7.setGeometry(QRect(20, 90, 731, 41))
        self.horizontalFrame_7.setFrameShape(QFrame.Box)
        self.horizontalFrame_7.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_30 = QHBoxLayout(self.horizontalFrame_7)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_35 = QLabel(self.horizontalFrame_7)
        self.label_35.setObjectName(u"label_35")
        font3 = QFont()
        font3.setFamilies([u"Versa"])
        font3.setStrikeOut(False)
        font3.setKerning(True)
        self.label_35.setFont(font3)
        self.label_35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.label_35)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.pushButton_relatorio_volar.setText("")
        self.label_33.setText(QCoreApplication.translate("Widget", u"                           SICOGES", None))
        self.label_35.setText(QCoreApplication.translate("Widget", u"Relatorio de Salas Reservadas", None))
    # retranslateUi

