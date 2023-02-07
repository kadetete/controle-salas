# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_ambientes.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class WidgetAmbientes(object):
    def setupUi(self, main_widget):
        if not main_widget.objectName():
            main_widget.setObjectName(u"main_widget")
        main_widget.resize(599, 584)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_widget.sizePolicy().hasHeightForWidth())
        main_widget.setSizePolicy(sizePolicy)
        main_widget.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"color: rgb(241, 241, 241);")
        self.verticalLayout = QVBoxLayout(main_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header_container_auditorium = QFrame(main_widget)
        self.header_container_auditorium.setObjectName(u"header_container_auditorium")
        self.header_container_auditorium.setFrameShape(QFrame.StyledPanel)
        self.header_container_auditorium.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.header_container_auditorium)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title_sicoges_auditorium = QLabel(self.header_container_auditorium)
        self.title_sicoges_auditorium.setObjectName(u"title_sicoges_auditorium")
        self.title_sicoges_auditorium.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies([u"Versa Versa"])
        font.setPointSize(24)
        self.title_sicoges_auditorium.setFont(font)

        self.verticalLayout_2.addWidget(self.title_sicoges_auditorium)


        self.verticalLayout.addWidget(self.header_container_auditorium)

        self.main_container_auditorium = QWidget(main_widget)
        self.main_container_auditorium.setObjectName(u"main_container_auditorium")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_container_auditorium.sizePolicy().hasHeightForWidth())
        self.main_container_auditorium.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.main_container_auditorium)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.main_container_auditorium)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.page_lab = QWidget()
        self.page_lab.setObjectName(u"page_lab")
        self.gridLayout_8 = QGridLayout(self.page_lab)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.widget_lab_03 = QWidget(self.page_lab)
        self.widget_lab_03.setObjectName(u"widget_lab_03")
        self.gridLayout_14 = QGridLayout(self.widget_lab_03)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.subtitle_lab_03 = QLabel(self.widget_lab_03)
        self.subtitle_lab_03.setObjectName(u"subtitle_lab_03")
        font1 = QFont()
        font1.setFamilies([u"Versa Versa"])
        font1.setPointSize(11)
        self.subtitle_lab_03.setFont(font1)

        self.gridLayout_14.addWidget(self.subtitle_lab_03, 0, 0, 1, 2)

        self.label_description_lab_03 = QLabel(self.widget_lab_03)
        self.label_description_lab_03.setObjectName(u"label_description_lab_03")
        font2 = QFont()
        font2.setFamilies([u"Versa Versa"])
        font2.setPointSize(12)
        self.label_description_lab_03.setFont(font2)
        self.label_description_lab_03.setStyleSheet(u"")
        self.label_description_lab_03.setScaledContents(False)
        self.label_description_lab_03.setAlignment(Qt.AlignCenter)
        self.label_description_lab_03.setWordWrap(True)

        self.gridLayout_14.addWidget(self.label_description_lab_03, 1, 0, 1, 3)

        self.pushButton_reserve_lab_03 = QPushButton(self.widget_lab_03)
        self.pushButton_reserve_lab_03.setObjectName(u"pushButton_reserve_lab_03")

        self.gridLayout_14.addWidget(self.pushButton_reserve_lab_03, 2, 0, 1, 1)

        self.pushButton_delete_lab_03 = QPushButton(self.widget_lab_03)
        self.pushButton_delete_lab_03.setObjectName(u"pushButton_delete_lab_03")

        self.gridLayout_14.addWidget(self.pushButton_delete_lab_03, 2, 1, 1, 1)

        self.pushButton_edit_lab_03 = QPushButton(self.widget_lab_03)
        self.pushButton_edit_lab_03.setObjectName(u"pushButton_edit_lab_03")

        self.gridLayout_14.addWidget(self.pushButton_edit_lab_03, 2, 2, 1, 1)


        self.gridLayout_8.addWidget(self.widget_lab_03, 2, 0, 1, 1)

        self.widget_meeting_class_01 = QWidget(self.page_lab)
        self.widget_meeting_class_01.setObjectName(u"widget_meeting_class_01")
        self.gridLayout_15 = QGridLayout(self.widget_meeting_class_01)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.subtitle_lab_01 = QLabel(self.widget_meeting_class_01)
        self.subtitle_lab_01.setObjectName(u"subtitle_lab_01")
        self.subtitle_lab_01.setFont(font1)

        self.gridLayout_15.addWidget(self.subtitle_lab_01, 0, 0, 1, 2)

        self.label_description_lab_01 = QLabel(self.widget_meeting_class_01)
        self.label_description_lab_01.setObjectName(u"label_description_lab_01")
        self.label_description_lab_01.setFont(font2)
        self.label_description_lab_01.setStyleSheet(u"")
        self.label_description_lab_01.setScaledContents(False)
        self.label_description_lab_01.setAlignment(Qt.AlignCenter)
        self.label_description_lab_01.setWordWrap(True)

        self.gridLayout_15.addWidget(self.label_description_lab_01, 1, 0, 1, 3)

        self.pushButton_reserve_lab_01 = QPushButton(self.widget_meeting_class_01)
        self.pushButton_reserve_lab_01.setObjectName(u"pushButton_reserve_lab_01")

        self.gridLayout_15.addWidget(self.pushButton_reserve_lab_01, 2, 0, 1, 1)

        self.pushButton_delete_lab_01 = QPushButton(self.widget_meeting_class_01)
        self.pushButton_delete_lab_01.setObjectName(u"pushButton_delete_lab_01")

        self.gridLayout_15.addWidget(self.pushButton_delete_lab_01, 2, 1, 1, 1)

        self.pushButton_edit_lab_01 = QPushButton(self.widget_meeting_class_01)
        self.pushButton_edit_lab_01.setObjectName(u"pushButton_edit_lab_01")

        self.gridLayout_15.addWidget(self.pushButton_edit_lab_01, 2, 2, 1, 1)


        self.gridLayout_8.addWidget(self.widget_meeting_class_01, 1, 0, 1, 1)

        self.widget_lab_02 = QWidget(self.page_lab)
        self.widget_lab_02.setObjectName(u"widget_lab_02")
        self.gridLayout_13 = QGridLayout(self.widget_lab_02)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.subtitle_lab_02 = QLabel(self.widget_lab_02)
        self.subtitle_lab_02.setObjectName(u"subtitle_lab_02")
        self.subtitle_lab_02.setFont(font1)

        self.gridLayout_13.addWidget(self.subtitle_lab_02, 0, 0, 1, 2)

        self.label_description_lab_02 = QLabel(self.widget_lab_02)
        self.label_description_lab_02.setObjectName(u"label_description_lab_02")
        self.label_description_lab_02.setFont(font2)
        self.label_description_lab_02.setStyleSheet(u"")
        self.label_description_lab_02.setScaledContents(False)
        self.label_description_lab_02.setAlignment(Qt.AlignCenter)
        self.label_description_lab_02.setWordWrap(True)

        self.gridLayout_13.addWidget(self.label_description_lab_02, 1, 0, 1, 3)

        self.pushButton_reserve_lab_02 = QPushButton(self.widget_lab_02)
        self.pushButton_reserve_lab_02.setObjectName(u"pushButton_reserve_lab_02")

        self.gridLayout_13.addWidget(self.pushButton_reserve_lab_02, 2, 0, 1, 1)

        self.pushButton_delete_lab_02 = QPushButton(self.widget_lab_02)
        self.pushButton_delete_lab_02.setObjectName(u"pushButton_delete_lab_02")

        self.gridLayout_13.addWidget(self.pushButton_delete_lab_02, 2, 1, 1, 1)

        self.pushButton_edit_lab_02 = QPushButton(self.widget_lab_02)
        self.pushButton_edit_lab_02.setObjectName(u"pushButton_edit_lab_02")

        self.gridLayout_13.addWidget(self.pushButton_edit_lab_02, 2, 2, 1, 1)


        self.gridLayout_8.addWidget(self.widget_lab_02, 1, 1, 1, 1)

        self.subtitle_lab = QLabel(self.page_lab)
        self.subtitle_lab.setObjectName(u"subtitle_lab")
        self.subtitle_lab.setMinimumSize(QSize(0, 25))
        self.subtitle_lab.setMaximumSize(QSize(16777215, 25))
        self.subtitle_lab.setSizeIncrement(QSize(0, 0))
        font3 = QFont()
        font3.setFamilies([u"Versa Versa"])
        font3.setPointSize(18)
        self.subtitle_lab.setFont(font3)

        self.gridLayout_8.addWidget(self.subtitle_lab, 0, 0, 1, 2)

        self.stackedWidget.addWidget(self.page_lab)
        self.page_auditorium = QWidget()
        self.page_auditorium.setObjectName(u"page_auditorium")
        sizePolicy1.setHeightForWidth(self.page_auditorium.sizePolicy().hasHeightForWidth())
        self.page_auditorium.setSizePolicy(sizePolicy1)
        self.gridLayout_3 = QGridLayout(self.page_auditorium)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget_auditorium_01 = QWidget(self.page_auditorium)
        self.widget_auditorium_01.setObjectName(u"widget_auditorium_01")
        self.gridLayout_4 = QGridLayout(self.widget_auditorium_01)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.subtitle_auditorium_01 = QLabel(self.widget_auditorium_01)
        self.subtitle_auditorium_01.setObjectName(u"subtitle_auditorium_01")
        self.subtitle_auditorium_01.setFont(font1)
        self.subtitle_auditorium_01.setScaledContents(False)
        self.subtitle_auditorium_01.setWordWrap(True)

        self.gridLayout_4.addWidget(self.subtitle_auditorium_01, 0, 0, 1, 3)

        self.label_description_auditorium_01 = QLabel(self.widget_auditorium_01)
        self.label_description_auditorium_01.setObjectName(u"label_description_auditorium_01")
        self.label_description_auditorium_01.setFont(font1)
        self.label_description_auditorium_01.setStyleSheet(u"")
        self.label_description_auditorium_01.setScaledContents(False)
        self.label_description_auditorium_01.setAlignment(Qt.AlignCenter)
        self.label_description_auditorium_01.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label_description_auditorium_01, 1, 0, 1, 3)

        self.pushButton_reserve_auditorium_01 = QPushButton(self.widget_auditorium_01)
        self.pushButton_reserve_auditorium_01.setObjectName(u"pushButton_reserve_auditorium_01")

        self.gridLayout_4.addWidget(self.pushButton_reserve_auditorium_01, 2, 0, 1, 1)

        self.pushButton_delete_auditorium_01 = QPushButton(self.widget_auditorium_01)
        self.pushButton_delete_auditorium_01.setObjectName(u"pushButton_delete_auditorium_01")

        self.gridLayout_4.addWidget(self.pushButton_delete_auditorium_01, 2, 1, 1, 1)

        self.pushButton_edit_auditorium_01 = QPushButton(self.widget_auditorium_01)
        self.pushButton_edit_auditorium_01.setObjectName(u"pushButton_edit_auditorium_01")

        self.gridLayout_4.addWidget(self.pushButton_edit_auditorium_01, 2, 2, 1, 1)


        self.gridLayout_3.addWidget(self.widget_auditorium_01, 1, 0, 1, 1)

        self.widget_auditorium_03 = QWidget(self.page_auditorium)
        self.widget_auditorium_03.setObjectName(u"widget_auditorium_03")
        self.gridLayout_6 = QGridLayout(self.widget_auditorium_03)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.subtitle_auditorium_03 = QLabel(self.widget_auditorium_03)
        self.subtitle_auditorium_03.setObjectName(u"subtitle_auditorium_03")
        self.subtitle_auditorium_03.setFont(font1)
        self.subtitle_auditorium_03.setWordWrap(True)

        self.gridLayout_6.addWidget(self.subtitle_auditorium_03, 0, 0, 1, 3)

        self.label_description_auditorium_03 = QLabel(self.widget_auditorium_03)
        self.label_description_auditorium_03.setObjectName(u"label_description_auditorium_03")
        self.label_description_auditorium_03.setFont(font1)
        self.label_description_auditorium_03.setStyleSheet(u"")
        self.label_description_auditorium_03.setScaledContents(True)
        self.label_description_auditorium_03.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_description_auditorium_03.setWordWrap(True)

        self.gridLayout_6.addWidget(self.label_description_auditorium_03, 1, 0, 1, 3)

        self.pushButton_reserve_auditorium_03 = QPushButton(self.widget_auditorium_03)
        self.pushButton_reserve_auditorium_03.setObjectName(u"pushButton_reserve_auditorium_03")

        self.gridLayout_6.addWidget(self.pushButton_reserve_auditorium_03, 2, 0, 1, 1)

        self.pushButton_delete_auditorium_03 = QPushButton(self.widget_auditorium_03)
        self.pushButton_delete_auditorium_03.setObjectName(u"pushButton_delete_auditorium_03")

        self.gridLayout_6.addWidget(self.pushButton_delete_auditorium_03, 2, 1, 1, 1)

        self.pushButton_edit_auditorium_03 = QPushButton(self.widget_auditorium_03)
        self.pushButton_edit_auditorium_03.setObjectName(u"pushButton_edit_auditorium_03")

        self.gridLayout_6.addWidget(self.pushButton_edit_auditorium_03, 2, 2, 1, 1)


        self.gridLayout_3.addWidget(self.widget_auditorium_03, 2, 0, 1, 1)

        self.subtitle_environments_auditorium = QLabel(self.page_auditorium)
        self.subtitle_environments_auditorium.setObjectName(u"subtitle_environments_auditorium")
        self.subtitle_environments_auditorium.setMaximumSize(QSize(16777215, 25))
        self.subtitle_environments_auditorium.setFont(font3)
        self.subtitle_environments_auditorium.setWordWrap(False)

        self.gridLayout_3.addWidget(self.subtitle_environments_auditorium, 0, 0, 1, 2)

        self.widget_auditorium_02 = QWidget(self.page_auditorium)
        self.widget_auditorium_02.setObjectName(u"widget_auditorium_02")
        self.gridLayout_5 = QGridLayout(self.widget_auditorium_02)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.subtitle_auditorium_02 = QLabel(self.widget_auditorium_02)
        self.subtitle_auditorium_02.setObjectName(u"subtitle_auditorium_02")
        self.subtitle_auditorium_02.setFont(font1)
        self.subtitle_auditorium_02.setWordWrap(True)

        self.gridLayout_5.addWidget(self.subtitle_auditorium_02, 0, 0, 1, 3)

        self.label_description_auditorium_02 = QLabel(self.widget_auditorium_02)
        self.label_description_auditorium_02.setObjectName(u"label_description_auditorium_02")
        self.label_description_auditorium_02.setFont(font1)
        self.label_description_auditorium_02.setStyleSheet(u"")
        self.label_description_auditorium_02.setScaledContents(True)
        self.label_description_auditorium_02.setAlignment(Qt.AlignCenter)
        self.label_description_auditorium_02.setWordWrap(True)

        self.gridLayout_5.addWidget(self.label_description_auditorium_02, 1, 0, 1, 3)

        self.pushButton_reserve_auditorium_02 = QPushButton(self.widget_auditorium_02)
        self.pushButton_reserve_auditorium_02.setObjectName(u"pushButton_reserve_auditorium_02")

        self.gridLayout_5.addWidget(self.pushButton_reserve_auditorium_02, 2, 0, 1, 1)

        self.pushButton_delete_auditorium_2 = QPushButton(self.widget_auditorium_02)
        self.pushButton_delete_auditorium_2.setObjectName(u"pushButton_delete_auditorium_2")

        self.gridLayout_5.addWidget(self.pushButton_delete_auditorium_2, 2, 1, 1, 1)

        self.pushButton_edit_auditorium_02 = QPushButton(self.widget_auditorium_02)
        self.pushButton_edit_auditorium_02.setObjectName(u"pushButton_edit_auditorium_02")

        self.gridLayout_5.addWidget(self.pushButton_edit_auditorium_02, 2, 2, 1, 1)


        self.gridLayout_3.addWidget(self.widget_auditorium_02, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_auditorium)
        self.page_class_meeting = QWidget()
        self.page_class_meeting.setObjectName(u"page_class_meeting")
        self.gridLayout_2 = QGridLayout(self.page_class_meeting)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_class_meeting_01 = QWidget(self.page_class_meeting)
        self.widget_class_meeting_01.setObjectName(u"widget_class_meeting_01")
        self.gridLayout_7 = QGridLayout(self.widget_class_meeting_01)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.subtitle_class_meeting_01 = QLabel(self.widget_class_meeting_01)
        self.subtitle_class_meeting_01.setObjectName(u"subtitle_class_meeting_01")
        self.subtitle_class_meeting_01.setFont(font1)

        self.gridLayout_7.addWidget(self.subtitle_class_meeting_01, 0, 0, 1, 1)

        self.label_description_class_meeting_01 = QLabel(self.widget_class_meeting_01)
        self.label_description_class_meeting_01.setObjectName(u"label_description_class_meeting_01")
        self.label_description_class_meeting_01.setFont(font2)
        self.label_description_class_meeting_01.setStyleSheet(u"")
        self.label_description_class_meeting_01.setScaledContents(False)
        self.label_description_class_meeting_01.setAlignment(Qt.AlignCenter)
        self.label_description_class_meeting_01.setWordWrap(True)

        self.gridLayout_7.addWidget(self.label_description_class_meeting_01, 1, 0, 1, 3)

        self.pushButton_reserve_class_meeting_01 = QPushButton(self.widget_class_meeting_01)
        self.pushButton_reserve_class_meeting_01.setObjectName(u"pushButton_reserve_class_meeting_01")

        self.gridLayout_7.addWidget(self.pushButton_reserve_class_meeting_01, 2, 0, 1, 1)

        self.pushButton_delete_class_meeting_01 = QPushButton(self.widget_class_meeting_01)
        self.pushButton_delete_class_meeting_01.setObjectName(u"pushButton_delete_class_meeting_01")

        self.gridLayout_7.addWidget(self.pushButton_delete_class_meeting_01, 2, 1, 1, 1)

        self.pushButton_edit_class_meeting_01 = QPushButton(self.widget_class_meeting_01)
        self.pushButton_edit_class_meeting_01.setObjectName(u"pushButton_edit_class_meeting_01")

        self.gridLayout_7.addWidget(self.pushButton_edit_class_meeting_01, 2, 2, 1, 1)


        self.gridLayout_2.addWidget(self.widget_class_meeting_01, 1, 0, 1, 1)

        self.widget_class_meeting_02 = QWidget(self.page_class_meeting)
        self.widget_class_meeting_02.setObjectName(u"widget_class_meeting_02")
        self.gridLayout_10 = QGridLayout(self.widget_class_meeting_02)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.subtitle_class_meeting_02 = QLabel(self.widget_class_meeting_02)
        self.subtitle_class_meeting_02.setObjectName(u"subtitle_class_meeting_02")
        self.subtitle_class_meeting_02.setFont(font1)

        self.gridLayout_10.addWidget(self.subtitle_class_meeting_02, 0, 0, 1, 1)

        self.label_description_class_meeting_02 = QLabel(self.widget_class_meeting_02)
        self.label_description_class_meeting_02.setObjectName(u"label_description_class_meeting_02")
        self.label_description_class_meeting_02.setFont(font2)
        self.label_description_class_meeting_02.setStyleSheet(u"")
        self.label_description_class_meeting_02.setScaledContents(False)
        self.label_description_class_meeting_02.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.label_description_class_meeting_02.setWordWrap(True)

        self.gridLayout_10.addWidget(self.label_description_class_meeting_02, 1, 0, 1, 3)

        self.pushButton_reserve_class_meeting_02 = QPushButton(self.widget_class_meeting_02)
        self.pushButton_reserve_class_meeting_02.setObjectName(u"pushButton_reserve_class_meeting_02")

        self.gridLayout_10.addWidget(self.pushButton_reserve_class_meeting_02, 2, 0, 1, 1)

        self.pushButton_delete_class_meeting_02 = QPushButton(self.widget_class_meeting_02)
        self.pushButton_delete_class_meeting_02.setObjectName(u"pushButton_delete_class_meeting_02")

        self.gridLayout_10.addWidget(self.pushButton_delete_class_meeting_02, 2, 1, 1, 1)

        self.pushButton_edit_class_meeting_02 = QPushButton(self.widget_class_meeting_02)
        self.pushButton_edit_class_meeting_02.setObjectName(u"pushButton_edit_class_meeting_02")

        self.gridLayout_10.addWidget(self.pushButton_edit_class_meeting_02, 2, 2, 1, 1)


        self.gridLayout_2.addWidget(self.widget_class_meeting_02, 1, 1, 1, 1)

        self.subtitle_environments_meeting = QLabel(self.page_class_meeting)
        self.subtitle_environments_meeting.setObjectName(u"subtitle_environments_meeting")
        self.subtitle_environments_meeting.setMaximumSize(QSize(16777215, 25))
        self.subtitle_environments_meeting.setFont(font3)

        self.gridLayout_2.addWidget(self.subtitle_environments_meeting, 0, 0, 1, 2)

        self.widget_class_meeting_03 = QWidget(self.page_class_meeting)
        self.widget_class_meeting_03.setObjectName(u"widget_class_meeting_03")
        self.gridLayout_11 = QGridLayout(self.widget_class_meeting_03)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.subtitle_sl_pipa = QLabel(self.widget_class_meeting_03)
        self.subtitle_sl_pipa.setObjectName(u"subtitle_sl_pipa")
        self.subtitle_sl_pipa.setFont(font1)

        self.gridLayout_11.addWidget(self.subtitle_sl_pipa, 0, 0, 1, 1)

        self.label_7 = QLabel(self.widget_class_meeting_03)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"")
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(True)

        self.gridLayout_11.addWidget(self.label_7, 1, 0, 1, 3)

        self.pushButton_reserve_meeting_03 = QPushButton(self.widget_class_meeting_03)
        self.pushButton_reserve_meeting_03.setObjectName(u"pushButton_reserve_meeting_03")

        self.gridLayout_11.addWidget(self.pushButton_reserve_meeting_03, 2, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.widget_class_meeting_03)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout_11.addWidget(self.pushButton_13, 2, 1, 1, 1)

        self.pushButton_14 = QPushButton(self.widget_class_meeting_03)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.gridLayout_11.addWidget(self.pushButton_14, 2, 2, 1, 1)


        self.gridLayout_2.addWidget(self.widget_class_meeting_03, 2, 0, 1, 1)

        self.widget_class_meeting_04 = QWidget(self.page_class_meeting)
        self.widget_class_meeting_04.setObjectName(u"widget_class_meeting_04")
        self.gridLayout_12 = QGridLayout(self.widget_class_meeting_04)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.subtitle_class_meeting_04 = QLabel(self.widget_class_meeting_04)
        self.subtitle_class_meeting_04.setObjectName(u"subtitle_class_meeting_04")
        self.subtitle_class_meeting_04.setFont(font1)

        self.gridLayout_12.addWidget(self.subtitle_class_meeting_04, 0, 0, 1, 2)

        self.label_description_class_meeting_04 = QLabel(self.widget_class_meeting_04)
        self.label_description_class_meeting_04.setObjectName(u"label_description_class_meeting_04")
        self.label_description_class_meeting_04.setFont(font2)
        self.label_description_class_meeting_04.setStyleSheet(u"")
        self.label_description_class_meeting_04.setScaledContents(False)
        self.label_description_class_meeting_04.setAlignment(Qt.AlignCenter)
        self.label_description_class_meeting_04.setWordWrap(True)

        self.gridLayout_12.addWidget(self.label_description_class_meeting_04, 1, 0, 1, 3)

        self.pushButton_reserve_class_meeting_04 = QPushButton(self.widget_class_meeting_04)
        self.pushButton_reserve_class_meeting_04.setObjectName(u"pushButton_reserve_class_meeting_04")

        self.gridLayout_12.addWidget(self.pushButton_reserve_class_meeting_04, 2, 0, 1, 1)

        self.pushButton_delete_class_meeting_04 = QPushButton(self.widget_class_meeting_04)
        self.pushButton_delete_class_meeting_04.setObjectName(u"pushButton_delete_class_meeting_04")

        self.gridLayout_12.addWidget(self.pushButton_delete_class_meeting_04, 2, 1, 1, 1)

        self.pushButton_edit_class_meeting_04 = QPushButton(self.widget_class_meeting_04)
        self.pushButton_edit_class_meeting_04.setObjectName(u"pushButton_edit_class_meeting_04")

        self.gridLayout_12.addWidget(self.pushButton_edit_class_meeting_04, 2, 2, 1, 1)


        self.gridLayout_2.addWidget(self.widget_class_meeting_04, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_class_meeting)
        self.page_sl_study = QWidget()
        self.page_sl_study.setObjectName(u"page_sl_study")
        self.gridLayout_9 = QGridLayout(self.page_sl_study)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.widget_class_study_04 = QWidget(self.page_sl_study)
        self.widget_class_study_04.setObjectName(u"widget_class_study_04")
        self.gridLayout_19 = QGridLayout(self.widget_class_study_04)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.subtitle_class_meeting_4 = QLabel(self.widget_class_study_04)
        self.subtitle_class_meeting_4.setObjectName(u"subtitle_class_meeting_4")
        self.subtitle_class_meeting_4.setFont(font1)

        self.gridLayout_19.addWidget(self.subtitle_class_meeting_4, 0, 0, 1, 1)

        self.label_description_class_study_04 = QLabel(self.widget_class_study_04)
        self.label_description_class_study_04.setObjectName(u"label_description_class_study_04")
        self.label_description_class_study_04.setFont(font2)
        self.label_description_class_study_04.setStyleSheet(u"")
        self.label_description_class_study_04.setScaledContents(False)
        self.label_description_class_study_04.setAlignment(Qt.AlignCenter)
        self.label_description_class_study_04.setWordWrap(True)

        self.gridLayout_19.addWidget(self.label_description_class_study_04, 1, 0, 1, 3)

        self.pushButton_reserve_class_study_04 = QPushButton(self.widget_class_study_04)
        self.pushButton_reserve_class_study_04.setObjectName(u"pushButton_reserve_class_study_04")

        self.gridLayout_19.addWidget(self.pushButton_reserve_class_study_04, 2, 0, 1, 1)

        self.pushButton_delete_class_study_4 = QPushButton(self.widget_class_study_04)
        self.pushButton_delete_class_study_4.setObjectName(u"pushButton_delete_class_study_4")

        self.gridLayout_19.addWidget(self.pushButton_delete_class_study_4, 2, 1, 1, 1)

        self.pushButton_edit_class_study_04 = QPushButton(self.widget_class_study_04)
        self.pushButton_edit_class_study_04.setObjectName(u"pushButton_edit_class_study_04")

        self.gridLayout_19.addWidget(self.pushButton_edit_class_study_04, 2, 2, 1, 1)


        self.gridLayout_9.addWidget(self.widget_class_study_04, 2, 1, 1, 1)

        self.widget_class_study_01 = QWidget(self.page_sl_study)
        self.widget_class_study_01.setObjectName(u"widget_class_study_01")
        self.gridLayout_16 = QGridLayout(self.widget_class_study_01)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.subtitle_class_study_01 = QLabel(self.widget_class_study_01)
        self.subtitle_class_study_01.setObjectName(u"subtitle_class_study_01")
        self.subtitle_class_study_01.setFont(font1)

        self.gridLayout_16.addWidget(self.subtitle_class_study_01, 0, 0, 1, 1)

        self.label_description_class_study_01 = QLabel(self.widget_class_study_01)
        self.label_description_class_study_01.setObjectName(u"label_description_class_study_01")
        self.label_description_class_study_01.setFont(font2)
        self.label_description_class_study_01.setStyleSheet(u"")
        self.label_description_class_study_01.setScaledContents(False)
        self.label_description_class_study_01.setAlignment(Qt.AlignCenter)
        self.label_description_class_study_01.setWordWrap(True)

        self.gridLayout_16.addWidget(self.label_description_class_study_01, 1, 0, 1, 3)

        self.pushButton_reserve_class_study_01 = QPushButton(self.widget_class_study_01)
        self.pushButton_reserve_class_study_01.setObjectName(u"pushButton_reserve_class_study_01")

        self.gridLayout_16.addWidget(self.pushButton_reserve_class_study_01, 2, 0, 1, 1)

        self.pushButton_delete_class_study_01 = QPushButton(self.widget_class_study_01)
        self.pushButton_delete_class_study_01.setObjectName(u"pushButton_delete_class_study_01")

        self.gridLayout_16.addWidget(self.pushButton_delete_class_study_01, 2, 1, 1, 1)

        self.pushButton_edit_class_study_01 = QPushButton(self.widget_class_study_01)
        self.pushButton_edit_class_study_01.setObjectName(u"pushButton_edit_class_study_01")

        self.gridLayout_16.addWidget(self.pushButton_edit_class_study_01, 2, 2, 1, 1)


        self.gridLayout_9.addWidget(self.widget_class_study_01, 1, 0, 1, 1)

        self.widget_class_study_03 = QWidget(self.page_sl_study)
        self.widget_class_study_03.setObjectName(u"widget_class_study_03")
        self.gridLayout_18 = QGridLayout(self.widget_class_study_03)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.subtitle_class_meeting_03 = QLabel(self.widget_class_study_03)
        self.subtitle_class_meeting_03.setObjectName(u"subtitle_class_meeting_03")
        self.subtitle_class_meeting_03.setFont(font1)

        self.gridLayout_18.addWidget(self.subtitle_class_meeting_03, 0, 0, 1, 1)

        self.label_description_class_study_03 = QLabel(self.widget_class_study_03)
        self.label_description_class_study_03.setObjectName(u"label_description_class_study_03")
        self.label_description_class_study_03.setFont(font2)
        self.label_description_class_study_03.setStyleSheet(u"")
        self.label_description_class_study_03.setScaledContents(False)
        self.label_description_class_study_03.setAlignment(Qt.AlignCenter)
        self.label_description_class_study_03.setWordWrap(True)

        self.gridLayout_18.addWidget(self.label_description_class_study_03, 1, 0, 1, 3)

        self.pushButton_reserve_class_study_03 = QPushButton(self.widget_class_study_03)
        self.pushButton_reserve_class_study_03.setObjectName(u"pushButton_reserve_class_study_03")

        self.gridLayout_18.addWidget(self.pushButton_reserve_class_study_03, 2, 0, 1, 1)

        self.pushButton_delete_class_study_03 = QPushButton(self.widget_class_study_03)
        self.pushButton_delete_class_study_03.setObjectName(u"pushButton_delete_class_study_03")

        self.gridLayout_18.addWidget(self.pushButton_delete_class_study_03, 2, 1, 1, 1)

        self.pushButton_edit_class_study_03 = QPushButton(self.widget_class_study_03)
        self.pushButton_edit_class_study_03.setObjectName(u"pushButton_edit_class_study_03")

        self.gridLayout_18.addWidget(self.pushButton_edit_class_study_03, 2, 2, 1, 1)


        self.gridLayout_9.addWidget(self.widget_class_study_03, 2, 0, 1, 1)

        self.widget_class_study_02 = QWidget(self.page_sl_study)
        self.widget_class_study_02.setObjectName(u"widget_class_study_02")
        self.gridLayout_17 = QGridLayout(self.widget_class_study_02)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.subtitle_class_study_02 = QLabel(self.widget_class_study_02)
        self.subtitle_class_study_02.setObjectName(u"subtitle_class_study_02")
        self.subtitle_class_study_02.setFont(font1)

        self.gridLayout_17.addWidget(self.subtitle_class_study_02, 0, 0, 1, 1)

        self.label_description_class_study_02 = QLabel(self.widget_class_study_02)
        self.label_description_class_study_02.setObjectName(u"label_description_class_study_02")
        self.label_description_class_study_02.setFont(font2)
        self.label_description_class_study_02.setStyleSheet(u"")
        self.label_description_class_study_02.setScaledContents(False)
        self.label_description_class_study_02.setAlignment(Qt.AlignCenter)
        self.label_description_class_study_02.setWordWrap(True)

        self.gridLayout_17.addWidget(self.label_description_class_study_02, 1, 0, 1, 3)

        self.pushButton_reserve_class_study_02 = QPushButton(self.widget_class_study_02)
        self.pushButton_reserve_class_study_02.setObjectName(u"pushButton_reserve_class_study_02")

        self.gridLayout_17.addWidget(self.pushButton_reserve_class_study_02, 2, 0, 1, 1)

        self.pushButton_delete_class_study_02 = QPushButton(self.widget_class_study_02)
        self.pushButton_delete_class_study_02.setObjectName(u"pushButton_delete_class_study_02")

        self.gridLayout_17.addWidget(self.pushButton_delete_class_study_02, 2, 1, 1, 1)

        self.pushButton_edit_class_study_02 = QPushButton(self.widget_class_study_02)
        self.pushButton_edit_class_study_02.setObjectName(u"pushButton_edit_class_study_02")

        self.gridLayout_17.addWidget(self.pushButton_edit_class_study_02, 2, 2, 1, 1)


        self.gridLayout_9.addWidget(self.widget_class_study_02, 1, 1, 1, 1)

        self.subtitle_class_study = QLabel(self.page_sl_study)
        self.subtitle_class_study.setObjectName(u"subtitle_class_study")
        self.subtitle_class_study.setMaximumSize(QSize(16777215, 25))
        self.subtitle_class_study.setFont(font3)

        self.gridLayout_9.addWidget(self.subtitle_class_study, 0, 0, 1, 2)

        self.stackedWidget.addWidget(self.page_sl_study)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.main_container_auditorium)

        self.footer_container = QFrame(main_widget)
        self.footer_container.setObjectName(u"footer_container")
        self.footer_container.setMaximumSize(QSize(16777215, 40))
        self.footer_container.setFrameShape(QFrame.StyledPanel)
        self.footer_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.footer_container)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 2, 0)
        self.footer_frame_auditorium = QFrame(self.footer_container)
        self.footer_frame_auditorium.setObjectName(u"footer_frame_auditorium")
        self.footer_frame_auditorium.setFrameShape(QFrame.StyledPanel)
        self.footer_frame_auditorium.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.footer_frame_auditorium)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 2, 2, 2)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.footer_icon_facebook = QLabel(self.footer_frame_auditorium)
        self.footer_icon_facebook.setObjectName(u"footer_icon_facebook")
        self.footer_icon_facebook.setMaximumSize(QSize(20, 20))
        self.footer_icon_facebook.setPixmap(QPixmap(u"icons/github.png"))
        self.footer_icon_facebook.setScaledContents(True)
        self.footer_icon_facebook.setWordWrap(False)

        self.horizontalLayout.addWidget(self.footer_icon_facebook)

        self.footer_icon_likedin = QLabel(self.footer_frame_auditorium)
        self.footer_icon_likedin.setObjectName(u"footer_icon_likedin")
        self.footer_icon_likedin.setMaximumSize(QSize(20, 20))
        self.footer_icon_likedin.setPixmap(QPixmap(u"icons/linkedin.png"))
        self.footer_icon_likedin.setScaledContents(True)

        self.horizontalLayout.addWidget(self.footer_icon_likedin)

        self.footer_icon_git = QLabel(self.footer_frame_auditorium)
        self.footer_icon_git.setObjectName(u"footer_icon_git")
        self.footer_icon_git.setMaximumSize(QSize(20, 20))
        self.footer_icon_git.setPixmap(QPixmap(u"icons/facebook-app-symbol.png"))
        self.footer_icon_git.setScaledContents(True)

        self.horizontalLayout.addWidget(self.footer_icon_git)


        self.verticalLayout_5.addWidget(self.footer_frame_auditorium)


        self.verticalLayout.addWidget(self.footer_container)


        self.retranslateUi(main_widget)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(main_widget)
    # setupUi

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QCoreApplication.translate("main_widget", u"Form", None))
        self.title_sicoges_auditorium.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p align=\"center\">SICOGES</p><p align=\"center\"><br/></p></body></html>", None))
        self.subtitle_lab_03.setText(QCoreApplication.translate("main_widget", u"laborat\u00f3rio 03", None))
        self.label_description_lab_03.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">sala 01 - t\u00e9rreo - campacidade para 40 pessoas</span></p><p><span style=\" font-size:11pt;\"><br/></span></p></body></html>", None))
        self.pushButton_reserve_lab_03.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_delete_lab_03.setText(QCoreApplication.translate("main_widget", u"excluir", None))
        self.pushButton_edit_lab_03.setText(QCoreApplication.translate("main_widget", u"editar", None))
        self.subtitle_lab_01.setText(QCoreApplication.translate("main_widget", u"Laborat\u00f3rio 01", None))
        self.label_description_lab_01.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">sala 01 - t\u00e9rreo - campacidade para 21 pessoas</span></p><p><span style=\" font-size:11pt;\"><br/></span></p></body></html>", None))
        self.pushButton_reserve_lab_01.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_delete_lab_01.setText(QCoreApplication.translate("main_widget", u"excluir", None))
        self.pushButton_edit_lab_01.setText(QCoreApplication.translate("main_widget", u"editar", None))
        self.subtitle_lab_02.setText(QCoreApplication.translate("main_widget", u"laborat\u00f3rio 02", None))
        self.label_description_lab_02.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">sala 02 - t\u00e9rreo - campacidade para 36 pessoas</span></p><p><span style=\" font-size:11pt;\"><br/></span></p></body></html>", None))
        self.pushButton_reserve_lab_02.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_delete_lab_02.setText(QCoreApplication.translate("main_widget", u"excluir", None))
        self.pushButton_edit_lab_02.setText(QCoreApplication.translate("main_widget", u"editar", None))
        self.subtitle_lab.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p align=\"center\">Laborat\u00f3rios</p></body></html>", None))
        self.subtitle_auditorium_01.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p align=\"center\">audit\u00f3rio 01</p><p align=\"center\"><br/></p></body></html>", None))
        self.label_description_auditorium_01.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p>169 m\u00b2 com p\u00e9 direito de 2,90 metros e capacidade para 120 lugares (cadeiras fixas)</p><p align=\"center\"><br/></p></body></html>", None))
        self.pushButton_reserve_auditorium_01.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_delete_auditorium_01.setText(QCoreApplication.translate("main_widget", u"excluir", None))
        self.pushButton_edit_auditorium_01.setText(QCoreApplication.translate("main_widget", u"editar", None))
        self.subtitle_auditorium_03.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p align=\"center\">Audit\u00f3rio 03</p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>", None))
        self.label_description_auditorium_03.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p>Descri\u00e7\u00e3o</p><p><br/></p><p><br/></p><p><br/></p><p><br/></p></body></html>", None))
        self.pushButton_reserve_auditorium_03.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_delete_auditorium_03.setText(QCoreApplication.translate("main_widget", u"excluir", None))
        self.pushButton_edit_auditorium_03.setText(QCoreApplication.translate("main_widget", u"editar", None))
        self.subtitle_environments_auditorium.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p align=\"center\">audit\u00f3rios</p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>", None))
        self.subtitle_auditorium_02.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p align=\"center\">audit\u00f3rio 02</p><p align=\"center\"><br/></p></body></html>", None))
        self.label_description_auditorium_02.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p>\u00c1rea total de 481m\u00b2 com capacidaed para 400 pessoas em audit\u00f3rio</p><p><br/></p><p><br/></p><p><br/></p><p align=\"center\"><br/></p></body></html>", None))
        self.pushButton_reserve_auditorium_02.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_delete_auditorium_2.setText(QCoreApplication.translate("main_widget", u"excluir", None))
        self.pushButton_edit_auditorium_02.setText(QCoreApplication.translate("main_widget", u"editar", None))
        self.subtitle_class_meeting_01.setText(QCoreApplication.translate("main_widget", u"Sala 01", None))
        self.label_description_class_meeting_01.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">54m\u00b2 com campacidade para 45 pessoas</span></p><p><span style=\" font-size:11pt;\"><br/></span></p></body></html>", None))
        self.pushButton_reserve_class_meeting_01.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_delete_class_meeting_01.setText(QCoreApplication.translate("main_widget", u"excluir", None))
        self.pushButton_edit_class_meeting_01.setText(QCoreApplication.translate("main_widget", u"editar", None))
        self.subtitle_class_meeting_02.setText(QCoreApplication.translate("main_widget", u"Sala 02", None))
        self.label_description_class_meeting_02.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">37m\u00b2 com capacidade para 25 pessoas</span></p><p><span style=\" font-size:11pt;\"><br/></span></p><p><span style=\" font-size:11pt;\"><br/></span></p><p><span style=\" font-size:11pt;\"><br/></span></p></body></html>", None))
        self.pushButton_reserve_class_meeting_02.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_delete_class_meeting_02.setText(QCoreApplication.translate("main_widget", u"exluir", None))
        self.pushButton_edit_class_meeting_02.setText(QCoreApplication.translate("main_widget", u"editar ", None))
        self.subtitle_environments_meeting.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p align=\"center\">salas de reuni\u00e3o</p><p align=\"center\"><br/></p></body></html>", None))
        self.subtitle_sl_pipa.setText(QCoreApplication.translate("main_widget", u"sala 03", None))
        self.label_7.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">43m\u00b2 com capacidade para 30 pessoas</span></p><p><span style=\" font-size:11pt;\"><br/></span></p><p><span style=\" font-size:11pt;\"><br/></span></p></body></html>", None))
        self.pushButton_reserve_meeting_03.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_13.setText(QCoreApplication.translate("main_widget", u"excluir", None))
        self.pushButton_14.setText(QCoreApplication.translate("main_widget", u"editar", None))
        self.subtitle_class_meeting_04.setText(QCoreApplication.translate("main_widget", u"sala 04", None))
        self.label_description_class_meeting_04.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">34m\u00b2 com capacidade para 20 pessoas</span></p><p><span style=\" font-size:11pt;\"><br/></span></p><p><span style=\" font-size:11pt;\"><br/></span></p></body></html>", None))
        self.pushButton_reserve_class_meeting_04.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_delete_class_meeting_04.setText(QCoreApplication.translate("main_widget", u"excluir", None))
        self.pushButton_edit_class_meeting_04.setText(QCoreApplication.translate("main_widget", u"editar", None))
        self.subtitle_class_meeting_4.setText(QCoreApplication.translate("main_widget", u"sala 04", None))
        self.label_description_class_study_04.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p>descri\u00e7\u00e3o</p><p><br/></p></body></html>", None))
        self.pushButton_reserve_class_study_04.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_delete_class_study_4.setText(QCoreApplication.translate("main_widget", u"excluir", None))
        self.pushButton_edit_class_study_04.setText(QCoreApplication.translate("main_widget", u"editar", None))
        self.subtitle_class_study_01.setText(QCoreApplication.translate("main_widget", u"sala 01", None))
        self.label_description_class_study_01.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p>descri\u00e7\u00e3o</p><p><br/></p></body></html>", None))
        self.pushButton_reserve_class_study_01.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_delete_class_study_01.setText(QCoreApplication.translate("main_widget", u"excluir", None))
        self.pushButton_edit_class_study_01.setText(QCoreApplication.translate("main_widget", u"editar", None))
        self.subtitle_class_meeting_03.setText(QCoreApplication.translate("main_widget", u"sala 03", None))
        self.label_description_class_study_03.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p>descri\u00e7\u00e3o</p><p><br/></p></body></html>", None))
        self.pushButton_reserve_class_study_03.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_delete_class_study_03.setText(QCoreApplication.translate("main_widget", u"excluir", None))
        self.pushButton_edit_class_study_03.setText(QCoreApplication.translate("main_widget", u"editar", None))
        self.subtitle_class_study_02.setText(QCoreApplication.translate("main_widget", u"sala 02", None))
        self.label_description_class_study_02.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p>descri\u00e7\u00e3o</p><p><br/></p></body></html>", None))
        self.pushButton_reserve_class_study_02.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_delete_class_study_02.setText(QCoreApplication.translate("main_widget", u"excluir", None))
        self.pushButton_edit_class_study_02.setText(QCoreApplication.translate("main_widget", u"editar", None))
        self.subtitle_class_study.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p align=\"center\">salas de estudo</p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>", None))
        self.footer_icon_facebook.setText("")
        self.footer_icon_likedin.setText("")
        self.footer_icon_git.setText("")
    # retranslateUi

