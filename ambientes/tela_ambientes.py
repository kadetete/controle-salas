# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_04_v5.ui'
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
    QLabel, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_main_widget(object):
    def setupUi(self, main_widget):
        if not main_widget.objectName():
            main_widget.setObjectName(u"main_widget")
        main_widget.resize(599, 571)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_widget.sizePolicy().hasHeightForWidth())
        main_widget.setSizePolicy(sizePolicy)
        main_widget.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"color: rgb(241, 241, 241);")
        self.verticalLayout = QVBoxLayout(main_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header_container = QFrame(main_widget)
        self.header_container.setObjectName(u"header_container")
        self.header_container.setFrameShape(QFrame.StyledPanel)
        self.header_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.header_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title_sicoges = QLabel(self.header_container)
        self.title_sicoges.setObjectName(u"title_sicoges")
        self.title_sicoges.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies([u"Versa Versa"])
        font.setPointSize(24)
        self.title_sicoges.setFont(font)

        self.verticalLayout_2.addWidget(self.title_sicoges)


        self.verticalLayout.addWidget(self.header_container)

        self.main_container = QWidget(main_widget)
        self.main_container.setObjectName(u"main_container")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_container.sizePolicy().hasHeightForWidth())
        self.main_container.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.main_container)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.main_container)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.page_lab = QWidget()
        self.page_lab.setObjectName(u"page_lab")
        self.gridLayout_8 = QGridLayout(self.page_lab)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.widget_lab_03 = QWidget(self.page_lab)
        self.widget_lab_03.setObjectName(u"widget_lab_03")
        self.subtitle_lab_03 = QLabel(self.widget_lab_03)
        self.subtitle_lab_03.setObjectName(u"subtitle_lab_03")
        self.subtitle_lab_03.setGeometry(QRect(0, 0, 86, 18))
        font1 = QFont()
        font1.setFamilies([u"Versa Versa"])
        font1.setPointSize(11)
        self.subtitle_lab_03.setFont(font1)
        self.pushButton_40 = QPushButton(self.widget_lab_03)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setGeometry(QRect(10, 140, 75, 24))
        self.pushButton_41 = QPushButton(self.widget_lab_03)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setGeometry(QRect(180, 140, 75, 24))
        self.pushButton_42 = QPushButton(self.widget_lab_03)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setGeometry(QRect(95, 140, 75, 24))
        self.label_11 = QLabel(self.widget_lab_03)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 40, 241, 91))
        font2 = QFont()
        font2.setFamilies([u"Versa Versa"])
        font2.setPointSize(12)
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"")
        self.label_11.setScaledContents(False)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setWordWrap(True)

        self.gridLayout_8.addWidget(self.widget_lab_03, 2, 0, 1, 1)

        self.widget_lab_01 = QWidget(self.page_lab)
        self.widget_lab_01.setObjectName(u"widget_lab_01")
        self.subtitle_lab_01 = QLabel(self.widget_lab_01)
        self.subtitle_lab_01.setObjectName(u"subtitle_lab_01")
        self.subtitle_lab_01.setGeometry(QRect(0, 0, 86, 18))
        self.subtitle_lab_01.setFont(font1)
        self.pushButton_34 = QPushButton(self.widget_lab_01)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setGeometry(QRect(10, 140, 75, 24))
        self.pushButton_35 = QPushButton(self.widget_lab_01)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setGeometry(QRect(95, 140, 75, 24))
        self.pushButton_36 = QPushButton(self.widget_lab_01)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setGeometry(QRect(180, 140, 75, 24))
        self.label_9 = QLabel(self.widget_lab_01)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 40, 241, 91))
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"")
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setWordWrap(True)

        self.gridLayout_8.addWidget(self.widget_lab_01, 1, 0, 1, 1)

        self.widget_lab_02 = QWidget(self.page_lab)
        self.widget_lab_02.setObjectName(u"widget_lab_02")
        self.subtitle_lab_2 = QLabel(self.widget_lab_02)
        self.subtitle_lab_2.setObjectName(u"subtitle_lab_2")
        self.subtitle_lab_2.setGeometry(QRect(0, 0, 86, 18))
        self.subtitle_lab_2.setFont(font1)
        self.pushButton_37 = QPushButton(self.widget_lab_02)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setGeometry(QRect(10, 140, 75, 24))
        self.pushButton_38 = QPushButton(self.widget_lab_02)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setGeometry(QRect(95, 140, 75, 24))
        self.pushButton_39 = QPushButton(self.widget_lab_02)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setGeometry(QRect(180, 140, 75, 24))
        self.label_10 = QLabel(self.widget_lab_02)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 40, 241, 91))
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"")
        self.label_10.setScaledContents(False)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setWordWrap(True)

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
        self.widget_aud_gurgel = QWidget(self.page_auditorium)
        self.widget_aud_gurgel.setObjectName(u"widget_aud_gurgel")
        self.subtitle_aud_gurgel = QLabel(self.widget_aud_gurgel)
        self.subtitle_aud_gurgel.setObjectName(u"subtitle_aud_gurgel")
        self.subtitle_aud_gurgel.setGeometry(QRect(0, 0, 271, 36))
        self.subtitle_aud_gurgel.setFont(font1)
        self.subtitle_aud_gurgel.setScaledContents(False)
        self.subtitle_aud_gurgel.setWordWrap(True)
        self.pushButton = QPushButton(self.widget_aud_gurgel)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 140, 75, 24))
        self.pushButton_2 = QPushButton(self.widget_aud_gurgel)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(95, 140, 75, 24))
        self.pushButton_3 = QPushButton(self.widget_aud_gurgel)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(180, 140, 75, 24))
        self.label_2 = QLabel(self.widget_aud_gurgel)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 40, 241, 91))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)

        self.gridLayout_3.addWidget(self.widget_aud_gurgel, 1, 0, 1, 1)

        self.widget_aud_faria = QWidget(self.page_auditorium)
        self.widget_aud_faria.setObjectName(u"widget_aud_faria")
        self.subtitle_aud_faria = QLabel(self.widget_aud_faria)
        self.subtitle_aud_faria.setObjectName(u"subtitle_aud_faria")
        self.subtitle_aud_faria.setGeometry(QRect(0, 0, 251, 36))
        self.subtitle_aud_faria.setFont(font1)
        self.subtitle_aud_faria.setWordWrap(True)
        self.pushButton_4 = QPushButton(self.widget_aud_faria)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 140, 75, 24))
        self.pushButton_5 = QPushButton(self.widget_aud_faria)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(95, 140, 75, 24))
        self.pushButton_6 = QPushButton(self.widget_aud_faria)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(180, 140, 75, 24))
        self.label_4 = QLabel(self.widget_aud_faria)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 40, 241, 91))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"")
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_4.setWordWrap(True)

        self.gridLayout_3.addWidget(self.widget_aud_faria, 2, 0, 1, 1)

        self.subtitle_environments_auditorium = QLabel(self.page_auditorium)
        self.subtitle_environments_auditorium.setObjectName(u"subtitle_environments_auditorium")
        self.subtitle_environments_auditorium.setMaximumSize(QSize(16777215, 25))
        self.subtitle_environments_auditorium.setFont(font3)
        self.subtitle_environments_auditorium.setWordWrap(False)

        self.gridLayout_3.addWidget(self.subtitle_environments_auditorium, 0, 0, 1, 2)

        self.widget_aud_fonseca = QWidget(self.page_auditorium)
        self.widget_aud_fonseca.setObjectName(u"widget_aud_fonseca")
        self.subtitle_aud_fonseca = QLabel(self.widget_aud_fonseca)
        self.subtitle_aud_fonseca.setObjectName(u"subtitle_aud_fonseca")
        self.subtitle_aud_fonseca.setGeometry(QRect(0, 0, 261, 36))
        self.subtitle_aud_fonseca.setFont(font1)
        self.subtitle_aud_fonseca.setWordWrap(True)
        self.pushButton_7 = QPushButton(self.widget_aud_fonseca)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(10, 140, 75, 24))
        self.pushButton_8 = QPushButton(self.widget_aud_fonseca)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(95, 140, 75, 24))
        self.pushButton_9 = QPushButton(self.widget_aud_fonseca)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(180, 140, 75, 24))
        self.label_3 = QLabel(self.widget_aud_fonseca)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 40, 241, 91))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"")
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.gridLayout_3.addWidget(self.widget_aud_fonseca, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_auditorium)
        self.page_class_meeting = QWidget()
        self.page_class_meeting.setObjectName(u"page_class_meeting")
        self.gridLayout_2 = QGridLayout(self.page_class_meeting)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_meet_zumbi = QWidget(self.page_class_meeting)
        self.widget_meet_zumbi.setObjectName(u"widget_meet_zumbi")
        self.subtitle_sl_zumbi = QLabel(self.widget_meet_zumbi)
        self.subtitle_sl_zumbi.setObjectName(u"subtitle_sl_zumbi")
        self.subtitle_sl_zumbi.setGeometry(QRect(0, 0, 86, 18))
        self.subtitle_sl_zumbi.setFont(font1)
        self.pushButton_10 = QPushButton(self.widget_meet_zumbi)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(10, 140, 75, 24))
        self.pushButton_11 = QPushButton(self.widget_meet_zumbi)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(95, 140, 75, 24))
        self.pushButton_15 = QPushButton(self.widget_meet_zumbi)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(180, 140, 75, 24))
        self.label_5 = QLabel(self.widget_meet_zumbi)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 40, 241, 91))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"")
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(True)

        self.gridLayout_2.addWidget(self.widget_meet_zumbi, 1, 0, 1, 1)

        self.widget_meet_muriu = QWidget(self.page_class_meeting)
        self.widget_meet_muriu.setObjectName(u"widget_meet_muriu")
        self.subtitle_sl_muriu = QLabel(self.widget_meet_muriu)
        self.subtitle_sl_muriu.setObjectName(u"subtitle_sl_muriu")
        self.subtitle_sl_muriu.setGeometry(QRect(0, 0, 87, 18))
        self.subtitle_sl_muriu.setFont(font1)
        self.pushButton_16 = QPushButton(self.widget_meet_muriu)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(10, 140, 75, 24))
        self.pushButton_17 = QPushButton(self.widget_meet_muriu)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(95, 140, 75, 24))
        self.pushButton_18 = QPushButton(self.widget_meet_muriu)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(180, 140, 75, 24))
        self.label_6 = QLabel(self.widget_meet_muriu)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 40, 241, 91))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"")
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)

        self.gridLayout_2.addWidget(self.widget_meet_muriu, 1, 1, 1, 1)

        self.label = QLabel(self.page_class_meeting)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 25))
        self.label.setFont(font3)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)

        self.widget_meet_pipa = QWidget(self.page_class_meeting)
        self.widget_meet_pipa.setObjectName(u"widget_meet_pipa")
        self.subtitle_sl_pipa = QLabel(self.widget_meet_pipa)
        self.subtitle_sl_pipa.setObjectName(u"subtitle_sl_pipa")
        self.subtitle_sl_pipa.setGeometry(QRect(0, 0, 75, 18))
        self.subtitle_sl_pipa.setFont(font1)
        self.pushButton_12 = QPushButton(self.widget_meet_pipa)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(10, 140, 75, 24))
        self.pushButton_13 = QPushButton(self.widget_meet_pipa)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(95, 140, 75, 24))
        self.pushButton_14 = QPushButton(self.widget_meet_pipa)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(180, 140, 75, 24))
        self.label_7 = QLabel(self.widget_meet_pipa)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 40, 241, 91))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"")
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(True)

        self.gridLayout_2.addWidget(self.widget_meet_pipa, 2, 0, 1, 1)

        self.widget_meet_pitangui = QWidget(self.page_class_meeting)
        self.widget_meet_pitangui.setObjectName(u"widget_meet_pitangui")
        self.subtitle_sl_pitangui = QLabel(self.widget_meet_pitangui)
        self.subtitle_sl_pitangui.setObjectName(u"subtitle_sl_pitangui")
        self.subtitle_sl_pitangui.setGeometry(QRect(0, 0, 106, 18))
        self.subtitle_sl_pitangui.setFont(font1)
        self.pushButton_19 = QPushButton(self.widget_meet_pitangui)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(10, 140, 75, 24))
        self.pushButton_20 = QPushButton(self.widget_meet_pitangui)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(95, 140, 75, 24))
        self.pushButton_21 = QPushButton(self.widget_meet_pitangui)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(180, 140, 75, 24))
        self.label_8 = QLabel(self.widget_meet_pitangui)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 40, 241, 91))
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"")
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setWordWrap(True)

        self.gridLayout_2.addWidget(self.widget_meet_pitangui, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_class_meeting)
        self.page_sl_study = QWidget()
        self.page_sl_study.setObjectName(u"page_sl_study")
        self.gridLayout_9 = QGridLayout(self.page_sl_study)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.widget_28 = QWidget(self.page_sl_study)
        self.widget_28.setObjectName(u"widget_28")
        self.subtitle_sl_04 = QLabel(self.widget_28)
        self.subtitle_sl_04.setObjectName(u"subtitle_sl_04")
        self.subtitle_sl_04.setGeometry(QRect(0, 0, 86, 18))
        self.subtitle_sl_04.setFont(font1)
        self.pushButton_31 = QPushButton(self.widget_28)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setGeometry(QRect(10, 140, 75, 24))
        self.pushButton_32 = QPushButton(self.widget_28)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setGeometry(QRect(95, 140, 75, 24))
        self.pushButton_33 = QPushButton(self.widget_28)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setGeometry(QRect(180, 140, 75, 24))

        self.gridLayout_9.addWidget(self.widget_28, 2, 1, 1, 1)

        self.widget_25 = QWidget(self.page_sl_study)
        self.widget_25.setObjectName(u"widget_25")
        self.subtitle_sl_01 = QLabel(self.widget_25)
        self.subtitle_sl_01.setObjectName(u"subtitle_sl_01")
        self.subtitle_sl_01.setGeometry(QRect(0, 0, 86, 18))
        self.subtitle_sl_01.setFont(font1)
        self.pushButton_22 = QPushButton(self.widget_25)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setGeometry(QRect(95, 140, 75, 24))
        self.pushButton_23 = QPushButton(self.widget_25)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setGeometry(QRect(10, 140, 75, 24))
        self.pushButton_24 = QPushButton(self.widget_25)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setGeometry(QRect(180, 140, 75, 24))

        self.gridLayout_9.addWidget(self.widget_25, 1, 0, 1, 1)

        self.widget_27 = QWidget(self.page_sl_study)
        self.widget_27.setObjectName(u"widget_27")
        self.subtitle_sl_03 = QLabel(self.widget_27)
        self.subtitle_sl_03.setObjectName(u"subtitle_sl_03")
        self.subtitle_sl_03.setGeometry(QRect(0, 0, 86, 18))
        self.subtitle_sl_03.setFont(font1)
        self.pushButton_28 = QPushButton(self.widget_27)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setGeometry(QRect(10, 140, 75, 24))
        self.pushButton_29 = QPushButton(self.widget_27)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setGeometry(QRect(95, 140, 75, 24))
        self.pushButton_30 = QPushButton(self.widget_27)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setGeometry(QRect(180, 140, 75, 24))

        self.gridLayout_9.addWidget(self.widget_27, 2, 0, 1, 1)

        self.widget_26 = QWidget(self.page_sl_study)
        self.widget_26.setObjectName(u"widget_26")
        self.subtitle_sl_02 = QLabel(self.widget_26)
        self.subtitle_sl_02.setObjectName(u"subtitle_sl_02")
        self.subtitle_sl_02.setGeometry(QRect(0, 0, 86, 18))
        self.subtitle_sl_02.setFont(font1)
        self.pushButton_25 = QPushButton(self.widget_26)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setGeometry(QRect(10, 140, 75, 24))
        self.pushButton_26 = QPushButton(self.widget_26)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setGeometry(QRect(95, 140, 75, 24))
        self.pushButton_27 = QPushButton(self.widget_26)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setGeometry(QRect(180, 140, 75, 24))

        self.gridLayout_9.addWidget(self.widget_26, 1, 1, 1, 1)

        self.subtitle_sl_study = QLabel(self.page_sl_study)
        self.subtitle_sl_study.setObjectName(u"subtitle_sl_study")
        self.subtitle_sl_study.setMaximumSize(QSize(16777215, 25))
        self.subtitle_sl_study.setFont(font3)

        self.gridLayout_9.addWidget(self.subtitle_sl_study, 0, 0, 1, 2)

        self.stackedWidget.addWidget(self.page_sl_study)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.main_container)

        self.footer_conteiner = QFrame(main_widget)
        self.footer_conteiner.setObjectName(u"footer_conteiner")
        self.footer_conteiner.setMaximumSize(QSize(16777215, 40))
        self.footer_conteiner.setFrameShape(QFrame.StyledPanel)
        self.footer_conteiner.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.footer_conteiner)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 2, 0)
        self.frame_4 = QFrame(self.footer_conteiner)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 2, 2, 2)
        self.icon_container = QFrame(self.frame_4)
        self.icon_container.setObjectName(u"icon_container")
        self.icon_container.setLayoutDirection(Qt.LeftToRight)
        self.icon_container.setFrameShape(QFrame.StyledPanel)
        self.icon_container.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.icon_container)

        self.icon_facebook = QLabel(self.frame_4)
        self.icon_facebook.setObjectName(u"icon_facebook")
        self.icon_facebook.setMaximumSize(QSize(20, 20))
        self.icon_facebook.setPixmap(QPixmap(u"../icons/github.png"))
        self.icon_facebook.setScaledContents(True)
        self.icon_facebook.setWordWrap(False)

        self.horizontalLayout.addWidget(self.icon_facebook)

        self.icon_likedin = QLabel(self.frame_4)
        self.icon_likedin.setObjectName(u"icon_likedin")
        self.icon_likedin.setMaximumSize(QSize(20, 20))
        self.icon_likedin.setPixmap(QPixmap(u"../icons/linkedin.png"))
        self.icon_likedin.setScaledContents(True)

        self.horizontalLayout.addWidget(self.icon_likedin)

        self.icon_git = QLabel(self.frame_4)
        self.icon_git.setObjectName(u"icon_git")
        self.icon_git.setMaximumSize(QSize(20, 20))
        self.icon_git.setPixmap(QPixmap(u"../icons/facebook-app-symbol.png"))
        self.icon_git.setScaledContents(True)

        self.horizontalLayout.addWidget(self.icon_git)


        self.verticalLayout_5.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.footer_conteiner)


        self.retranslateUi(main_widget)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main_widget)
    # setupUi

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QCoreApplication.translate("main_widget", u"Form", None))
        self.title_sicoges.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p align=\"center\">SICOGES</p><p align=\"center\"><br/></p></body></html>", None))
        self.subtitle_lab_03.setText(QCoreApplication.translate("main_widget", u"sala 03", None))
        self.pushButton_40.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_41.setText(QCoreApplication.translate("main_widget", u"editar", None))
        self.pushButton_42.setText(QCoreApplication.translate("main_widget", u"excluir", None))
        self.label_11.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">sala 01 - t\u00e9rreo - campacidade para 40 pessoas</span></p><p><span style=\" font-size:11pt;\"><br/></span></p></body></html>", None))
        self.subtitle_lab_01.setText(QCoreApplication.translate("main_widget", u"sala 01", None))
        self.pushButton_34.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_35.setText(QCoreApplication.translate("main_widget", u"excluir", None))
        self.pushButton_36.setText(QCoreApplication.translate("main_widget", u"editar", None))
        self.label_9.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">sala 01 - t\u00e9rreo - campacidade para 21 pessoas</span></p><p><span style=\" font-size:11pt;\"><br/></span></p></body></html>", None))
        self.subtitle_lab_2.setText(QCoreApplication.translate("main_widget", u"sala 02", None))
        self.pushButton_37.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_38.setText(QCoreApplication.translate("main_widget", u"excluir", None))
        self.pushButton_39.setText(QCoreApplication.translate("main_widget", u"editar", None))
        self.label_10.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">sala 02 - t\u00e9rreo - campacidade para 36 pessoas</span></p><p><span style=\" font-size:11pt;\"><br/></span></p></body></html>", None))
        self.subtitle_lab.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p align=\"center\">Laborat\u00f3rios</p></body></html>", None))
        self.subtitle_aud_gurgel.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p align=\"center\">bloco c : audit\u00f3rio de\u00edfilo gurgel</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_2.setText(QCoreApplication.translate("main_widget", u"excluir", None))
        self.pushButton_3.setText(QCoreApplication.translate("main_widget", u"editar", None))
        self.label_2.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p>169 m\u00b2 com p\u00e9 direito de 2,90 metros e capacidade para 120 lugares (cadeiras fixas)</p><p align=\"center\"><br/></p></body></html>", None))
        self.subtitle_aud_faria.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p align=\"center\">bloco c : wilma de faria</p></body></html>", None))
        self.pushButton_4.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_5.setText(QCoreApplication.translate("main_widget", u"excluir", None))
        self.pushButton_6.setText(QCoreApplication.translate("main_widget", u"editar", None))
        self.label_4.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p>896 m\u00b2 com p\u00e9 direito entre 4,30m e 8,90m, e capacidade para 676 lugares (cadeiras fixas) com placo e tela de proje\u00e7\u00e3o.</p><p><br/></p><p><br/></p><p><br/></p></body></html>", None))
        self.subtitle_environments_auditorium.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p align=\"center\">audit\u00f3rios</p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>", None))
        self.subtitle_aud_fonseca.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p align=\"center\">audit\u00f3rio ademilde fonseca</p></body></html>", None))
        self.pushButton_7.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_8.setText(QCoreApplication.translate("main_widget", u"excluir", None))
        self.pushButton_9.setText(QCoreApplication.translate("main_widget", u"editar", None))
        self.label_3.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p>\u00c1rea total de 481m\u00b2 com capacidaed para 400 pessoas em audit\u00f3rio</p><p><br/></p><p><br/></p><p><br/></p><p align=\"center\"><br/></p></body></html>", None))
        self.subtitle_sl_zumbi.setText(QCoreApplication.translate("main_widget", u"sala zumbi", None))
        self.pushButton_10.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_11.setText(QCoreApplication.translate("main_widget", u"excluir", None))
        self.pushButton_15.setText(QCoreApplication.translate("main_widget", u"editar", None))
        self.label_5.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">54m\u00b2 com campacidade para 45 pessoas</span></p><p><span style=\" font-size:11pt;\"><br/></span></p></body></html>", None))
        self.subtitle_sl_muriu.setText(QCoreApplication.translate("main_widget", u"sala muri\u00fa", None))
        self.pushButton_16.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_17.setText(QCoreApplication.translate("main_widget", u"exluir", None))
        self.pushButton_18.setText(QCoreApplication.translate("main_widget", u"editar ", None))
        self.label_6.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">37m\u00b2 com capacidade para 25 pessoas</span></p><p><span style=\" font-size:11pt;\"><br/></span></p><p><span style=\" font-size:11pt;\"><br/></span></p><p><span style=\" font-size:11pt;\"><br/></span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p align=\"center\">salas de reuni\u00e3o</p><p align=\"center\"><br/></p></body></html>", None))
        self.subtitle_sl_pipa.setText(QCoreApplication.translate("main_widget", u"sala pipa", None))
        self.pushButton_12.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_13.setText(QCoreApplication.translate("main_widget", u"excluir", None))
        self.pushButton_14.setText(QCoreApplication.translate("main_widget", u"editar", None))
        self.label_7.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">43m\u00b2 com capacidade para 30 pessoas</span></p><p><span style=\" font-size:11pt;\"><br/></span></p><p><span style=\" font-size:11pt;\"><br/></span></p></body></html>", None))
        self.subtitle_sl_pitangui.setText(QCoreApplication.translate("main_widget", u"sala pitangui", None))
        self.pushButton_19.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_20.setText(QCoreApplication.translate("main_widget", u"excluir", None))
        self.pushButton_21.setText(QCoreApplication.translate("main_widget", u"editar", None))
        self.label_8.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p><span style=\" font-size:11pt;\">34m\u00b2 com capacidade para 20 pessoas</span></p><p><span style=\" font-size:11pt;\"><br/></span></p><p><span style=\" font-size:11pt;\"><br/></span></p></body></html>", None))
        self.subtitle_sl_04.setText(QCoreApplication.translate("main_widget", u"sala 04", None))
        self.pushButton_31.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_32.setText(QCoreApplication.translate("main_widget", u"excluir", None))
        self.pushButton_33.setText(QCoreApplication.translate("main_widget", u"editar", None))
        self.subtitle_sl_01.setText(QCoreApplication.translate("main_widget", u"sala 01", None))
        self.pushButton_22.setText(QCoreApplication.translate("main_widget", u"excluir", None))
        self.pushButton_23.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_24.setText(QCoreApplication.translate("main_widget", u"editar", None))
        self.subtitle_sl_03.setText(QCoreApplication.translate("main_widget", u"sala 03", None))
        self.pushButton_28.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_29.setText(QCoreApplication.translate("main_widget", u"excluir", None))
        self.pushButton_30.setText(QCoreApplication.translate("main_widget", u"editar", None))
        self.subtitle_sl_02.setText(QCoreApplication.translate("main_widget", u"sala 02", None))
        self.pushButton_25.setText(QCoreApplication.translate("main_widget", u"reservar", None))
        self.pushButton_26.setText(QCoreApplication.translate("main_widget", u"excluir", None))
        self.pushButton_27.setText(QCoreApplication.translate("main_widget", u"editar", None))
        self.subtitle_sl_study.setText(QCoreApplication.translate("main_widget", u"<html><head/><body><p align=\"center\">salas de estudo</p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>", None))
        self.icon_facebook.setText("")
        self.icon_likedin.setText("")
        self.icon_git.setText("")
    # retranslateUi

