# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Demo_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGraphicsView, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_DempApp(object):
    def setupUi(self, DempApp):
        if not DempApp.objectName():
            DempApp.setObjectName(u"DempApp")
        DempApp.resize(1269, 862)
        DempApp.setStyleSheet(u"background-color: rgb(245, 250, 254);\n"
"color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(DempApp)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"	border: none;\n"
"	height: 40px;\n"
"	text-align: left;\n"
"	padding-left: 16px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/icon/logo.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 30, -1, -1)
        self.dashboard_btn = QPushButton(self.widget_2)
        self.dashboard_btn.setObjectName(u"dashboard_btn")
        font1 = QFont()
        font1.setBold(True)
        self.dashboard_btn.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/icon/dashboard.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard_btn.setIcon(icon)
        self.dashboard_btn.setIconSize(QSize(26, 26))
        self.dashboard_btn.setCheckable(True)
        self.dashboard_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dashboard_btn)

        self.data_btn = QPushButton(self.widget_2)
        self.data_btn.setObjectName(u"data_btn")
        self.data_btn.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/icon/database.png", QSize(), QIcon.Normal, QIcon.Off)
        self.data_btn.setIcon(icon1)
        self.data_btn.setIconSize(QSize(26, 26))
        self.data_btn.setCheckable(True)
        self.data_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.data_btn)

        self.pre_data_btn = QPushButton(self.widget_2)
        self.pre_data_btn.setObjectName(u"pre_data_btn")
        self.pre_data_btn.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/icon/document.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pre_data_btn.setIcon(icon2)
        self.pre_data_btn.setIconSize(QSize(26, 26))
        self.pre_data_btn.setCheckable(True)
        self.pre_data_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pre_data_btn)

        self.filter_btn = QPushButton(self.widget_2)
        self.filter_btn.setObjectName(u"filter_btn")
        self.filter_btn.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/icon/filter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.filter_btn.setIcon(icon3)
        self.filter_btn.setIconSize(QSize(26, 26))
        self.filter_btn.setCheckable(True)
        self.filter_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.filter_btn)

        self.defi_btn = QPushButton(self.widget_2)
        self.defi_btn.setObjectName(u"defi_btn")
        self.defi_btn.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/icon/title.png", QSize(), QIcon.Normal, QIcon.Off)
        self.defi_btn.setIcon(icon4)
        self.defi_btn.setIconSize(QSize(26, 26))
        self.defi_btn.setCheckable(True)
        self.defi_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.defi_btn)

        self.hot_data = QPushButton(self.widget_2)
        self.hot_data.setObjectName(u"hot_data")
        self.hot_data.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/icon/hot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hot_data.setIcon(icon5)
        self.hot_data.setIconSize(QSize(26, 26))
        self.hot_data.setCheckable(True)
        self.hot_data.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.hot_data)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 395, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.pushButton_12 = QPushButton(self.widget_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u":/icon/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon6)
        self.pushButton_12.setIconSize(QSize(26, 26))
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.pushButton_12)


        self.horizontalLayout_3.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.dashboar_page = QWidget()
        self.dashboar_page.setObjectName(u"dashboar_page")
        self.stackedWidget.addWidget(self.dashboar_page)
        self.pre_data_page = QWidget()
        self.pre_data_page.setObjectName(u"pre_data_page")
        self.gridLayout_3 = QGridLayout(self.pre_data_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget_7 = QWidget(self.pre_data_page)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setStyleSheet(u"QPushButton {\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: #fff3;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.widget_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_3 = QSpacerItem(228, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_3)

        self.label_11 = QLabel(self.widget_7)
        self.label_11.setObjectName(u"label_11")
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.label_11.setFont(font2)

        self.horizontalLayout_21.addWidget(self.label_11)

        self.horizontalSpacer_4 = QSpacerItem(228, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_4)


        self.gridLayout_2.addLayout(self.horizontalLayout_21, 0, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pushButton_3 = QPushButton(self.widget_7)
        self.pushButton_3.setObjectName(u"pushButton_3")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.pushButton_3.setFont(font3)
        self.pushButton_3.setStyleSheet(u"padding: 10px")

        self.horizontalLayout_13.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.widget_7)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font3)
        self.pushButton_4.setStyleSheet(u"padding: 10px")

        self.horizontalLayout_13.addWidget(self.pushButton_4)

        self.lineEdit_5 = QLineEdit(self.widget_7)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"padding: 6px")

        self.horizontalLayout_13.addWidget(self.lineEdit_5)


        self.gridLayout_2.addLayout(self.horizontalLayout_13, 1, 0, 1, 1)

        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.radioButton_4 = QRadioButton(self.widget_8)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout_14.addWidget(self.radioButton_4)

        self.radioButton_5 = QRadioButton(self.widget_8)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.horizontalLayout_14.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.widget_8)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.horizontalLayout_14.addWidget(self.radioButton_6)

        self.radioButton_7 = QRadioButton(self.widget_8)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.horizontalLayout_14.addWidget(self.radioButton_7)

        self.radioButton_8 = QRadioButton(self.widget_8)
        self.radioButton_8.setObjectName(u"radioButton_8")

        self.horizontalLayout_14.addWidget(self.radioButton_8)

        self.radioButton_9 = QRadioButton(self.widget_8)
        self.radioButton_9.setObjectName(u"radioButton_9")

        self.horizontalLayout_14.addWidget(self.radioButton_9)

        self.pushButton_5 = QPushButton(self.widget_8)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font3)

        self.horizontalLayout_14.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.widget_8)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font3)

        self.horizontalLayout_14.addWidget(self.pushButton_6)


        self.gridLayout_2.addWidget(self.widget_8, 2, 0, 1, 1)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.tableWidget_2 = QTableWidget(self.widget_7)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setStyleSheet(u"QTableWidget {\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: black;\n"
"}")

        self.horizontalLayout_20.addWidget(self.tableWidget_2)

        self.widget_21 = QWidget(self.widget_7)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setStyleSheet(u"QLineEdit{\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: black;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.widget_21)
        self.verticalLayout_3.setSpacing(60)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_12 = QLabel(self.widget_21)
        self.label_12.setObjectName(u"label_12")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.label_12.setFont(font4)
        self.label_12.setStyleSheet(u"margin-right: 44px")

        self.horizontalLayout_15.addWidget(self.label_12)

        self.lineEdit_6 = QLineEdit(self.widget_21)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout_15.addWidget(self.lineEdit_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_13 = QLabel(self.widget_21)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font4)
        self.label_13.setStyleSheet(u"margin-right: 0.4px")

        self.horizontalLayout_16.addWidget(self.label_13)

        self.lineEdit_7 = QLineEdit(self.widget_21)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.horizontalLayout_16.addWidget(self.lineEdit_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_14 = QLabel(self.widget_21)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font4)

        self.horizontalLayout_17.addWidget(self.label_14)

        self.lineEdit_8 = QLineEdit(self.widget_21)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.horizontalLayout_17.addWidget(self.lineEdit_8)


        self.verticalLayout_3.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_15 = QLabel(self.widget_21)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font4)
        self.label_15.setStyleSheet(u"margin-right:10px")

        self.horizontalLayout_18.addWidget(self.label_15)

        self.lineEdit_9 = QLineEdit(self.widget_21)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.horizontalLayout_18.addWidget(self.lineEdit_9)


        self.verticalLayout_3.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_16 = QLabel(self.widget_21)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font4)

        self.horizontalLayout_19.addWidget(self.label_16)

        self.textEdit_2 = QTextEdit(self.widget_21)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setStyleSheet(u"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: black;")

        self.horizontalLayout_19.addWidget(self.textEdit_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_19)


        self.horizontalLayout_20.addWidget(self.widget_21)


        self.gridLayout_2.addLayout(self.horizontalLayout_20, 3, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.pre_data_page)
        self.filter_page = QWidget()
        self.filter_page.setObjectName(u"filter_page")
        self.gridLayout_7 = QGridLayout(self.filter_page)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.widget_10 = QWidget(self.filter_page)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setStyleSheet(u"QPushButton {\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: #fff3;\n"
"}")
        self.gridLayout_6 = QGridLayout(self.widget_10)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_5 = QSpacerItem(238, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_5)

        self.label_17 = QLabel(self.widget_10)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)

        self.horizontalLayout_22.addWidget(self.label_17)

        self.horizontalSpacer_6 = QSpacerItem(238, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_6)


        self.gridLayout_6.addLayout(self.horizontalLayout_22, 0, 0, 1, 1)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.pushButton_7 = QPushButton(self.widget_10)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font3)
        self.pushButton_7.setStyleSheet(u"padding: 10px")

        self.horizontalLayout_23.addWidget(self.pushButton_7)

        self.lineEdit_10 = QLineEdit(self.widget_10)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setStyleSheet(u"padding: 6px")

        self.horizontalLayout_23.addWidget(self.lineEdit_10)


        self.gridLayout_6.addLayout(self.horizontalLayout_23, 1, 0, 1, 1)

        self.widget_11 = QWidget(self.widget_10)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.radioButton_10 = QRadioButton(self.widget_11)
        self.radioButton_10.setObjectName(u"radioButton_10")

        self.horizontalLayout_24.addWidget(self.radioButton_10)

        self.radioButton_11 = QRadioButton(self.widget_11)
        self.radioButton_11.setObjectName(u"radioButton_11")

        self.horizontalLayout_24.addWidget(self.radioButton_11)

        self.radioButton_14 = QRadioButton(self.widget_11)
        self.radioButton_14.setObjectName(u"radioButton_14")

        self.horizontalLayout_24.addWidget(self.radioButton_14)

        self.pushButton_9 = QPushButton(self.widget_11)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font3)
        self.pushButton_9.setStyleSheet(u"")

        self.horizontalLayout_24.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.widget_11)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font3)
        self.pushButton_10.setStyleSheet(u"")

        self.horizontalLayout_24.addWidget(self.pushButton_10)


        self.gridLayout_6.addWidget(self.widget_11, 2, 0, 1, 1)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.tableWidget_3 = QTableWidget(self.widget_10)
        if (self.tableWidget_3.columnCount() < 2):
            self.tableWidget_3.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setStyleSheet(u"QTableWidget {\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: black;\n"
"}")

        self.horizontalLayout_29.addWidget(self.tableWidget_3)

        self.widget_12 = QWidget(self.widget_10)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setStyleSheet(u"QLineEdit{\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QWidget{\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QLabel{\n"
"	border: none;\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.widget_12)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(41)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_18 = QLabel(self.widget_12)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)
        self.label_18.setStyleSheet(u"background-color: rgb(0, 170, 0);\n"
"padding: 10px;")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_18)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_19 = QLabel(self.widget_12)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.horizontalLayout_25.addWidget(self.label_19)

        self.lineEdit_11 = QLineEdit(self.widget_12)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.horizontalLayout_25.addWidget(self.lineEdit_11)


        self.verticalLayout_6.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_20 = QLabel(self.widget_12)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)

        self.horizontalLayout_26.addWidget(self.label_20)

        self.lineEdit_12 = QLineEdit(self.widget_12)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.horizontalLayout_26.addWidget(self.lineEdit_12)


        self.verticalLayout_6.addLayout(self.horizontalLayout_26)


        self.verticalLayout_12.addLayout(self.verticalLayout_6)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(35)
        self.label_21 = QLabel(self.widget_12)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)
        self.label_21.setStyleSheet(u"background-color: rgb(0, 170, 0);\n"
"padding: 10px;")
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_21, 0, 0, 1, 1)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_22 = QLabel(self.widget_12)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)

        self.horizontalLayout_27.addWidget(self.label_22)

        self.lineEdit_14 = QLineEdit(self.widget_12)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.horizontalLayout_27.addWidget(self.lineEdit_14)


        self.gridLayout_5.addLayout(self.horizontalLayout_27, 1, 0, 1, 1)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_23 = QLabel(self.widget_12)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)

        self.horizontalLayout_28.addWidget(self.label_23)

        self.lineEdit_13 = QLineEdit(self.widget_12)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.horizontalLayout_28.addWidget(self.lineEdit_13)


        self.gridLayout_5.addLayout(self.horizontalLayout_28, 2, 0, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_24 = QLabel(self.widget_12)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_24)

        self.tableWidget_4 = QTableWidget(self.widget_12)
        if (self.tableWidget_4.columnCount() < 3):
            self.tableWidget_4.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        self.tableWidget_4.setObjectName(u"tableWidget_4")

        self.verticalLayout_7.addWidget(self.tableWidget_4)


        self.gridLayout_5.addLayout(self.verticalLayout_7, 3, 0, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout_5)


        self.horizontalLayout_29.addWidget(self.widget_12)

        self.widget_13 = QWidget(self.widget_10)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setStyleSheet(u"QLineEdit{\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QWidget{\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QLabel{\n"
"	border: none;\n"
"}")
        self.gridLayout_4 = QGridLayout(self.widget_13)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.graphicsView = QGraphicsView(self.widget_13)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_4.addWidget(self.graphicsView, 0, 0, 1, 1)


        self.horizontalLayout_29.addWidget(self.widget_13)


        self.gridLayout_6.addLayout(self.horizontalLayout_29, 3, 0, 1, 1)


        self.gridLayout_7.addWidget(self.widget_10, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.filter_page)
        self.defi_page = QWidget()
        self.defi_page.setObjectName(u"defi_page")
        self.gridLayout_9 = QGridLayout(self.defi_page)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.widget_14 = QWidget(self.defi_page)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setStyleSheet(u"QPushButton {\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: #fff3;\n"
"}")
        self.gridLayout_8 = QGridLayout(self.widget_14)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalSpacer_7 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_7)

        self.label_25 = QLabel(self.widget_14)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font2)

        self.horizontalLayout_30.addWidget(self.label_25)

        self.horizontalSpacer_8 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_8)


        self.gridLayout_8.addLayout(self.horizontalLayout_30, 0, 0, 1, 1)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.pushButton_8 = QPushButton(self.widget_14)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font3)
        self.pushButton_8.setStyleSheet(u"padding: 10px\n"
"")

        self.horizontalLayout_31.addWidget(self.pushButton_8)

        self.lineEdit_15 = QLineEdit(self.widget_14)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setStyleSheet(u"padding: 6px;")

        self.horizontalLayout_31.addWidget(self.lineEdit_15)

        self.lineEdit_20 = QLineEdit(self.widget_14)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setStyleSheet(u"padding:6px")

        self.horizontalLayout_31.addWidget(self.lineEdit_20)


        self.gridLayout_8.addLayout(self.horizontalLayout_31, 1, 0, 1, 1)

        self.widget_15 = QWidget(self.widget_14)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_32 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.radioButton_12 = QRadioButton(self.widget_15)
        self.radioButton_12.setObjectName(u"radioButton_12")

        self.horizontalLayout_32.addWidget(self.radioButton_12)

        self.radioButton_16 = QRadioButton(self.widget_15)
        self.radioButton_16.setObjectName(u"radioButton_16")

        self.horizontalLayout_32.addWidget(self.radioButton_16)

        self.pushButton_13 = QPushButton(self.widget_15)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setFont(font3)
        self.pushButton_13.setStyleSheet(u"padding: 4px")

        self.horizontalLayout_32.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.widget_15)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setFont(font3)
        self.pushButton_14.setStyleSheet(u"padding:4px")

        self.horizontalLayout_32.addWidget(self.pushButton_14)


        self.gridLayout_8.addWidget(self.widget_15, 2, 0, 1, 1)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.widget_16 = QWidget(self.widget_14)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_9 = QVBoxLayout(self.widget_16)
        self.verticalLayout_9.setSpacing(50)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_26 = QLabel(self.widget_16)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(16777215, 40))
        self.label_26.setFont(font4)
        self.label_26.setStyleSheet(u"background-color: rgb(0, 170, 0);")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_26)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_27 = QLabel(self.widget_16)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font3)

        self.horizontalLayout_33.addWidget(self.label_27)

        self.lineEdit_16 = QLineEdit(self.widget_16)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.horizontalLayout_33.addWidget(self.lineEdit_16)


        self.verticalLayout_8.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_28 = QLabel(self.widget_16)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font3)

        self.horizontalLayout_34.addWidget(self.label_28)

        self.lineEdit_17 = QLineEdit(self.widget_16)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.horizontalLayout_34.addWidget(self.lineEdit_17)


        self.verticalLayout_8.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_29 = QLabel(self.widget_16)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font3)

        self.horizontalLayout_35.addWidget(self.label_29)

        self.lineEdit_18 = QLineEdit(self.widget_16)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.horizontalLayout_35.addWidget(self.lineEdit_18)


        self.verticalLayout_8.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_30 = QLabel(self.widget_16)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font3)

        self.horizontalLayout_36.addWidget(self.label_30)

        self.lineEdit_19 = QLineEdit(self.widget_16)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.horizontalLayout_36.addWidget(self.lineEdit_19)


        self.verticalLayout_8.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_31 = QLabel(self.widget_16)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font3)

        self.horizontalLayout_37.addWidget(self.label_31)

        self.lineEdit_21 = QLineEdit(self.widget_16)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.horizontalLayout_37.addWidget(self.lineEdit_21)


        self.verticalLayout_8.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_32 = QLabel(self.widget_16)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font3)

        self.horizontalLayout_38.addWidget(self.label_32)

        self.lineEdit_22 = QLineEdit(self.widget_16)
        self.lineEdit_22.setObjectName(u"lineEdit_22")

        self.horizontalLayout_38.addWidget(self.lineEdit_22)


        self.verticalLayout_8.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_33 = QLabel(self.widget_16)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font3)

        self.horizontalLayout_39.addWidget(self.label_33)

        self.lineEdit_23 = QLineEdit(self.widget_16)
        self.lineEdit_23.setObjectName(u"lineEdit_23")

        self.horizontalLayout_39.addWidget(self.lineEdit_23)


        self.verticalLayout_8.addLayout(self.horizontalLayout_39)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)


        self.horizontalLayout_40.addWidget(self.widget_16)

        self.tableWidget_5 = QTableWidget(self.widget_14)
        if (self.tableWidget_5.columnCount() < 2):
            self.tableWidget_5.setColumnCount(2)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.setStyleSheet(u"QTableWidget {\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: black;\n"
"}")

        self.horizontalLayout_40.addWidget(self.tableWidget_5)


        self.gridLayout_8.addLayout(self.horizontalLayout_40, 3, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget_14, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.defi_page)
        self.hot_page = QWidget()
        self.hot_page.setObjectName(u"hot_page")
        self.gridLayout_12 = QGridLayout(self.hot_page)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.widget_17 = QWidget(self.hot_page)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setStyleSheet(u"QPushButton {\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: #fff3;\n"
"}")
        self.gridLayout_11 = QGridLayout(self.widget_17)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalSpacer_9 = QSpacerItem(188, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_9)

        self.label_34 = QLabel(self.widget_17)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font2)

        self.horizontalLayout_41.addWidget(self.label_34)

        self.horizontalSpacer_10 = QSpacerItem(188, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_10)


        self.gridLayout_11.addLayout(self.horizontalLayout_41, 0, 0, 1, 1)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.pushButton_11 = QPushButton(self.widget_17)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font3)
        self.pushButton_11.setStyleSheet(u"padding:10px;")

        self.horizontalLayout_42.addWidget(self.pushButton_11)

        self.lineEdit_24 = QLineEdit(self.widget_17)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setStyleSheet(u"padding: 6px")

        self.horizontalLayout_42.addWidget(self.lineEdit_24)

        self.lineEdit_25 = QLineEdit(self.widget_17)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setStyleSheet(u"padding: 6px")

        self.horizontalLayout_42.addWidget(self.lineEdit_25)


        self.gridLayout_11.addLayout(self.horizontalLayout_42, 1, 0, 1, 1)

        self.widget_18 = QWidget(self.widget_17)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_43 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.radioButton_13 = QRadioButton(self.widget_18)
        self.radioButton_13.setObjectName(u"radioButton_13")

        self.horizontalLayout_43.addWidget(self.radioButton_13)

        self.radioButton_17 = QRadioButton(self.widget_18)
        self.radioButton_17.setObjectName(u"radioButton_17")

        self.horizontalLayout_43.addWidget(self.radioButton_17)

        self.pushButton_15 = QPushButton(self.widget_18)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setFont(font3)
        self.pushButton_15.setStyleSheet(u"padding: 6px")

        self.horizontalLayout_43.addWidget(self.pushButton_15)


        self.gridLayout_11.addWidget(self.widget_18, 2, 0, 1, 1)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.widget_19 = QWidget(self.widget_17)
        self.widget_19.setObjectName(u"widget_19")
        self.gridLayout_10 = QGridLayout(self.widget_19)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_35 = QLabel(self.widget_19)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(16777215, 44))
        self.label_35.setFont(font4)
        self.label_35.setStyleSheet(u"background-color: rgb(0, 170, 0);")
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_10.addWidget(self.label_35, 0, 0, 1, 1)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_36 = QLabel(self.widget_19)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font3)

        self.horizontalLayout_44.addWidget(self.label_36)

        self.lineEdit_26 = QLineEdit(self.widget_19)
        self.lineEdit_26.setObjectName(u"lineEdit_26")

        self.horizontalLayout_44.addWidget(self.lineEdit_26)


        self.gridLayout_10.addLayout(self.horizontalLayout_44, 1, 0, 1, 1)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_37 = QLabel(self.widget_19)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font3)

        self.horizontalLayout_45.addWidget(self.label_37)

        self.lineEdit_27 = QLineEdit(self.widget_19)
        self.lineEdit_27.setObjectName(u"lineEdit_27")

        self.horizontalLayout_45.addWidget(self.lineEdit_27)


        self.gridLayout_10.addLayout(self.horizontalLayout_45, 2, 0, 1, 1)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_38 = QLabel(self.widget_19)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font3)

        self.horizontalLayout_46.addWidget(self.label_38)

        self.lineEdit_28 = QLineEdit(self.widget_19)
        self.lineEdit_28.setObjectName(u"lineEdit_28")

        self.horizontalLayout_46.addWidget(self.lineEdit_28)


        self.gridLayout_10.addLayout(self.horizontalLayout_46, 3, 0, 1, 1)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_39 = QLabel(self.widget_19)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font3)

        self.horizontalLayout_47.addWidget(self.label_39)

        self.lineEdit_29 = QLineEdit(self.widget_19)
        self.lineEdit_29.setObjectName(u"lineEdit_29")

        self.horizontalLayout_47.addWidget(self.lineEdit_29)


        self.gridLayout_10.addLayout(self.horizontalLayout_47, 4, 0, 1, 1)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_40 = QLabel(self.widget_19)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font3)

        self.horizontalLayout_48.addWidget(self.label_40)

        self.lineEdit_30 = QLineEdit(self.widget_19)
        self.lineEdit_30.setObjectName(u"lineEdit_30")

        self.horizontalLayout_48.addWidget(self.lineEdit_30)


        self.gridLayout_10.addLayout(self.horizontalLayout_48, 5, 0, 1, 1)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_41 = QLabel(self.widget_19)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font3)

        self.horizontalLayout_49.addWidget(self.label_41)

        self.lineEdit_31 = QLineEdit(self.widget_19)
        self.lineEdit_31.setObjectName(u"lineEdit_31")

        self.horizontalLayout_49.addWidget(self.lineEdit_31)


        self.gridLayout_10.addLayout(self.horizontalLayout_49, 6, 0, 1, 1)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_42 = QLabel(self.widget_19)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font3)

        self.horizontalLayout_50.addWidget(self.label_42)

        self.lineEdit_32 = QLineEdit(self.widget_19)
        self.lineEdit_32.setObjectName(u"lineEdit_32")

        self.horizontalLayout_50.addWidget(self.lineEdit_32)


        self.gridLayout_10.addLayout(self.horizontalLayout_50, 7, 0, 1, 1)


        self.horizontalLayout_51.addWidget(self.widget_19)

        self.widget_20 = QWidget(self.widget_17)
        self.widget_20.setObjectName(u"widget_20")
        self.verticalLayout_10 = QVBoxLayout(self.widget_20)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_43 = QLabel(self.widget_20)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font4)
        self.label_43.setStyleSheet(u"background-color: rgb(0, 170, 0);\n"
"padding: 10px;")
        self.label_43.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_43)

        self.tableWidget_6 = QTableWidget(self.widget_20)
        if (self.tableWidget_6.columnCount() < 7):
            self.tableWidget_6.setColumnCount(7)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(6, __qtablewidgetitem15)
        self.tableWidget_6.setObjectName(u"tableWidget_6")
        self.tableWidget_6.setStyleSheet(u"QTableWidget{\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: black;\n"
"}")

        self.verticalLayout_10.addWidget(self.tableWidget_6)


        self.horizontalLayout_51.addWidget(self.widget_20)


        self.gridLayout_11.addLayout(self.horizontalLayout_51, 3, 0, 1, 1)


        self.gridLayout_12.addWidget(self.widget_17, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.hot_page)
        self.data_page = QWidget()
        self.data_page.setObjectName(u"data_page")
        self.gridLayout = QGridLayout(self.data_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.data_page)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(308, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(278, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_4 = QWidget(self.data_page)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font4)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.dateEdit = QDateEdit(self.widget_4)
        self.dateEdit.setObjectName(u"dateEdit")

        self.horizontalLayout_5.addWidget(self.dateEdit)

        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.dateEdit_2 = QDateEdit(self.widget_4)
        self.dateEdit_2.setObjectName(u"dateEdit_2")

        self.horizontalLayout_5.addWidget(self.dateEdit_2)


        self.gridLayout.addWidget(self.widget_4, 1, 0, 1, 1)

        self.widget_5 = QWidget(self.data_page)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"QPushButton {\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: rgb(127, 118, 120);\n"
"}")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.radioButton = QRadioButton(self.widget_5)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_6.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.widget_5)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_6.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.widget_5)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_6.addWidget(self.radioButton_3)

        self.pushButton = QPushButton(self.widget_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)

        self.horizontalLayout_6.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setAutoExclusive(False)

        self.horizontalLayout_6.addWidget(self.pushButton_2)


        self.gridLayout.addWidget(self.widget_5, 2, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.tableWidget = QTableWidget(self.data_page)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: black;")

        self.horizontalLayout_12.addWidget(self.tableWidget)

        self.widget_6 = QWidget(self.data_page)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"QLineEdit{\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: black;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget_6)
        self.verticalLayout.setSpacing(60)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.widget_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"margin-right: 44px")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.lineEdit = QLineEdit(self.widget_6)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_7.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.widget_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"margin-right: 0.4px")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.lineEdit_2 = QLineEdit(self.widget_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_8.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.widget_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font4)

        self.horizontalLayout_9.addWidget(self.label_8)

        self.lineEdit_3 = QLineEdit(self.widget_6)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_9.addWidget(self.lineEdit_3)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.widget_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font4)
        self.label_9.setStyleSheet(u"margin-right:10px")

        self.horizontalLayout_10.addWidget(self.label_9)

        self.lineEdit_4 = QLineEdit(self.widget_6)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_10.addWidget(self.lineEdit_4)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.widget_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font4)

        self.horizontalLayout_11.addWidget(self.label_10)

        self.textEdit = QTextEdit(self.widget_6)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: black;")

        self.horizontalLayout_11.addWidget(self.textEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_12.addWidget(self.widget_6)


        self.gridLayout.addLayout(self.horizontalLayout_12, 3, 0, 1, 1)

        self.stackedWidget.addWidget(self.data_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_3.addWidget(self.widget_3)

        DempApp.setCentralWidget(self.centralwidget)

        self.retranslateUi(DempApp)
        self.pushButton_12.clicked.connect(DempApp.close)

        self.stackedWidget.setCurrentIndex(4)
        self.pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(DempApp)
    # setupUi

    def retranslateUi(self, DempApp):
        DempApp.setWindowTitle(QCoreApplication.translate("DempApp", u"MainWindow", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("DempApp", u"Sidebar", None))
        self.dashboard_btn.setText(QCoreApplication.translate("DempApp", u"Dashboard", None))
        self.data_btn.setText(QCoreApplication.translate("DempApp", u"D\u1eef li\u1ec7u", None))
        self.pre_data_btn.setText(QCoreApplication.translate("DempApp", u"Ti\u1ec1n x\u1eed l\u00fd", None))
        self.filter_btn.setText(QCoreApplication.translate("DempApp", u"Ph\u00e2n c\u1ee5m", None))
        self.defi_btn.setText(QCoreApplication.translate("DempApp", u"X\u0110T\u00eanC\u0110", None))
        self.hot_data.setText(QCoreApplication.translate("DempApp", u"X\u0110\u0110NC\u0110", None))
        self.pushButton_12.setText(QCoreApplication.translate("DempApp", u"Quit", None))
        self.label_11.setText(QCoreApplication.translate("DempApp", u"Ti\u1ec1n x\u1eed l\u00fd d\u1eef li\u1ec7u", None))
        self.pushButton_3.setText(QCoreApplication.translate("DempApp", u"Load d\u1eef li\u1ec7u", None))
        self.pushButton_4.setText(QCoreApplication.translate("DempApp", u"Import t\u1eeb file", None))
        self.radioButton_4.setText(QCoreApplication.translate("DempApp", u"Chu\u1ea9n ho\u00e1 d\u1eef li\u1ec7u", None))
        self.radioButton_5.setText(QCoreApplication.translate("DempApp", u"T\u00e1ch c\u00e2u", None))
        self.radioButton_6.setText(QCoreApplication.translate("DempApp", u"T\u00e1ch t\u1eeb", None))
        self.radioButton_7.setText(QCoreApplication.translate("DempApp", u"G\u00e1n nh\u00e3n t\u1eeb lo\u1ea1i", None))
        self.radioButton_8.setText(QCoreApplication.translate("DempApp", u"Lo\u1ea1i b\u1ecf h\u01b0 t\u1eeb", None))
        self.radioButton_9.setText(QCoreApplication.translate("DempApp", u"L\u01b0u d\u1eef li\u1ec7u hu\u1ea5n luy\u1ec7n", None))
        self.pushButton_5.setText(QCoreApplication.translate("DempApp", u"Th\u1ef1c hi\u1ec7n", None))
        self.pushButton_6.setText(QCoreApplication.translate("DempApp", u"Export", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DempApp", u"Ch\u1ee7 \u0111\u1ec1", None));
        self.label_12.setText(QCoreApplication.translate("DempApp", u"ID:", None))
        self.label_13.setText(QCoreApplication.translate("DempApp", u"Websites:", None))
        self.label_14.setText(QCoreApplication.translate("DempApp", u"Th\u1eddi gi\u1ea1n:", None))
        self.label_15.setText(QCoreApplication.translate("DempApp", u"Ti\u00eau \u0111\u1ec1:", None))
        self.label_16.setText(QCoreApplication.translate("DempApp", u"N\u1ed9i dung:", None))
        self.label_17.setText(QCoreApplication.translate("DempApp", u"Ph\u00e2n c\u1ee5m ch\u1ee7 \u0111\u1ec1", None))
        self.pushButton_7.setText(QCoreApplication.translate("DempApp", u"Load d\u1eef li\u1ec7u", None))
        self.radioButton_10.setText(QCoreApplication.translate("DempApp", u"Ph\u00e2n c\u1ee5m ch\u1ee7 \u0111\u1ec1 b\u1eb1ng DBSCAN", None))
        self.radioButton_11.setText(QCoreApplication.translate("DempApp", u"Ph\u00e2n c\u1ee5m ch\u1ee7 \u0111\u1ec1 b\u1eb1ng DBSCAN c\u1ea3i ti\u1ebfn", None))
        self.radioButton_14.setText(QCoreApplication.translate("DempApp", u"L\u01b0u m\u00f4 h\u00ecnh", None))
        self.pushButton_9.setText(QCoreApplication.translate("DempApp", u"Ph\u00e2n c\u1ee5m ch\u1ee7 \u0111\u1ec1", None))
        self.pushButton_10.setText(QCoreApplication.translate("DempApp", u"Export", None))
        ___qtablewidgetitem1 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DempApp", u"Ch\u1ee7 \u0111\u1ec1", None));
        self.label_18.setText(QCoreApplication.translate("DempApp", u"K\u1ebeT QU\u1ea2 T\u00cdNH TO\u00c1N THAM S\u1ed0 EPS V\u00c0 MINPTS", None))
        self.label_19.setText(QCoreApplication.translate("DempApp", u"Tham s\u1ed1 eps: ", None))
        self.label_20.setText(QCoreApplication.translate("DempApp", u"Tham s\u1ed1 MinPts: ", None))
        self.label_21.setText(QCoreApplication.translate("DempApp", u"K\u1ebeT QU\u1ea2 T\u00cdNH TO\u00c1N THAM S\u1ed0 EPS V\u00c0 MINPTS", None))
        self.label_22.setText(QCoreApplication.translate("DempApp", u"S\u1ed1 c\u1ee5m ch\u1ee7 \u0111\u1ec1 t\u00ecm \u0111\u01b0\u1ee3c:", None))
        self.label_23.setText(QCoreApplication.translate("DempApp", u"S\u1ed1 \u0111i\u1ec3m nhi\u1ec5u:", None))
        self.label_24.setText(QCoreApplication.translate("DempApp", u"Nh\u00e3n c\u1ee5m ch\u1ee7 \u0111\u1ec1:", None))
        ___qtablewidgetitem2 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DempApp", u"Label", None));
        ___qtablewidgetitem3 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DempApp", u"x", None));
        ___qtablewidgetitem4 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("DempApp", u"y", None));
        self.label_25.setText(QCoreApplication.translate("DempApp", u"X\u00e1c \u0111\u1ecbnh t\u00ean ch\u1ee7 \u0111\u1ec1", None))
        self.pushButton_8.setText(QCoreApplication.translate("DempApp", u"Nh\u1eadp d\u1eef li\u1ec7u", None))
        self.radioButton_12.setText(QCoreApplication.translate("DempApp", u"Ph\u00e2n c\u1ee5m ch\u1ee7 \u0111\u1ec1 b\u1eb1ng DBSCAN c\u1ea3i ti\u1ebfn", None))
        self.radioButton_16.setText(QCoreApplication.translate("DempApp", u"L\u01b0u k\u1ebft qu\u1ea3", None))
        self.pushButton_13.setText(QCoreApplication.translate("DempApp", u"X\u00e1c \u0111\u1ecbnh t\u00ean ch\u1ee7 \u0111\u1ec1", None))
        self.pushButton_14.setText(QCoreApplication.translate("DempApp", u"Export", None))
        self.label_26.setText(QCoreApplication.translate("DempApp", u"K\u1ebft qu\u1ea3 ph\u00e2n c\u1ee5m ch\u1ee7 \u0111\u1ec1", None))
        self.label_27.setText(QCoreApplication.translate("DempApp", u"S\u1ed1 trang tin:", None))
        self.label_28.setText(QCoreApplication.translate("DempApp", u"S\u1ed1 l\u01b0\u1ee3ng b\u00e0i vi\u1ebft:", None))
        self.label_29.setText(QCoreApplication.translate("DempApp", u"Tham s\u1ed1 eps:", None))
        self.label_30.setText(QCoreApplication.translate("DempApp", u"Tham s\u1ed1 Minpts:", None))
        self.label_31.setText(QCoreApplication.translate("DempApp", u"B\u00e0i vi\u1ebft \u0111\u01b0\u1ee3c ph\u00e2n c\u1ee5m:", None))
        self.label_32.setText(QCoreApplication.translate("DempApp", u"S\u1ed1 c\u1ee5m ch\u1ee7 \u0111\u1ec1 t\u00ecm \u0111\u01b0\u1ee3c:", None))
        self.label_33.setText(QCoreApplication.translate("DempApp", u"S\u1ed1 l\u01b0\u1ee3ng nhi\u1ec5u:", None))
        ___qtablewidgetitem5 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("DempApp", u"Ch\u1ee7 \u0111\u1ec1", None));
        self.label_34.setText(QCoreApplication.translate("DempApp", u"X\u00e1c \u0111\u1ecbnh \u0111\u1ed9 n\u00f3ng ch\u1ee7 \u0111\u1ec1", None))
        self.pushButton_11.setText(QCoreApplication.translate("DempApp", u"Load d\u1eef li\u1ec7u", None))
        self.radioButton_13.setText(QCoreApplication.translate("DempApp", u"T\u00ednh to\u00e1n tham s\u1ed1 \u0111\u00e1nh gi\u00e1 \u0111\u1ed9 n\u00f3ng ch\u1ee7 \u0111\u1ec1", None))
        self.radioButton_17.setText(QCoreApplication.translate("DempApp", u"\u0110\u00e1nh gi\u00e1 \u0111\u1ed9 n\u00f3ng theo ch\u1ee7 \u0111\u1ec1", None))
        self.pushButton_15.setText(QCoreApplication.translate("DempApp", u"X\u00e1c \u0111\u1ecbnh \u0111\u1ed9 n\u00f3ng ch\u1ee7 \u0111\u1ec1", None))
        self.label_35.setText(QCoreApplication.translate("DempApp", u"C\u00e1c tham s\u1ed1 c\u1ee7a m\u00f4 h\u00ecnh", None))
        self.label_36.setText(QCoreApplication.translate("DempApp", u"T\u1ed5ng s\u1ed1 trang tin:", None))
        self.label_37.setText(QCoreApplication.translate("DempApp", u"T\u1ed5ng s\u1ed1 b\u00e0i vi\u1ebft:", None))
        self.label_38.setText(QCoreApplication.translate("DempApp", u"S\u1ed1 c\u1ee5m ch\u1ee7 \u0111\u1ec1:", None))
        self.label_39.setText(QCoreApplication.translate("DempApp", u"B\u00e0i vi\u1ebft ph\u00e2n c\u1ee5m:", None))
        self.label_40.setText(QCoreApplication.translate("DempApp", u"S\u1ed1 \u0111i\u1ec3m nhi\u1ec5u:", None))
        self.label_41.setText(QCoreApplication.translate("DempApp", u"Tham s\u1ed1 eps:", None))
        self.label_42.setText(QCoreApplication.translate("DempApp", u"Tham s\u1ed1 Minpst:", None))
        self.label_43.setText(QCoreApplication.translate("DempApp", u"K\u1ebft qu\u1ea3 t\u00ednh to\u00e1n c\u00e1c tham s\u1ed1 d\u00f9ng \u0111\u1ec3 x\u00e1c \u0111\u1ecbnh \u0111\u1ed9 n\u00f3ng ch\u1ee7 \u0111\u1ec1", None))
        ___qtablewidgetitem6 = self.tableWidget_6.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("DempApp", u"Ch\u1ee7 \u0111\u1ec1(T)", None));
        ___qtablewidgetitem7 = self.tableWidget_6.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("DempApp", u"S\u1ed1 b\u00e0i vi\u1ebft(Ni)", None));
        ___qtablewidgetitem8 = self.tableWidget_6.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("DempApp", u"S\u1ed1 b\u00e0i vi\u1ebft Ti/Ki(Di)", None));
        ___qtablewidgetitem9 = self.tableWidget_6.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("DempApp", u"S\u1ed1 ng\u00e0y(M)", None));
        ___qtablewidgetitem10 = self.tableWidget_6.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("DempApp", u"S\u1ed1 trang XH(Ki)", None));
        ___qtablewidgetitem11 = self.tableWidget_6.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("DempApp", u"S\u1ed1 trang tin(K)", None));
        ___qtablewidgetitem12 = self.tableWidget_6.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("DempApp", u"T\u1ed5ng s\u1ed1 ngu\u1ed3n", None));
        self.label.setText(QCoreApplication.translate("DempApp", u"Truy xu\u1ea5t d\u1eef li\u1ec7u t\u1eeb Database", None))
        self.label_4.setText(QCoreApplication.translate("DempApp", u"Truy xu\u1ea5t d\u1eef li\u1ec7u t\u1eeb:", None))
        self.label_5.setText(QCoreApplication.translate("DempApp", u"\u0111\u1ebfn ng\u00e0y:", None))
        self.radioButton.setText(QCoreApplication.translate("DempApp", u"Truy xu\u1ea5t d\u1eef li\u1ec7u t\u1eeb Database", None))
        self.radioButton_2.setText(QCoreApplication.translate("DempApp", u"Lo\u1ea1i b\u1ecf HTML, l\u00e0m s\u1ea1ch d\u1eef li\u1ec7u", None))
        self.radioButton_3.setText(QCoreApplication.translate("DempApp", u"L\u01b0u d\u1eef li\u1ec7u hu\u1ea5n luy\u1ec7n", None))
        self.pushButton.setText(QCoreApplication.translate("DempApp", u"Th\u1ef1c hi\u1ec7n", None))
        self.pushButton_2.setText(QCoreApplication.translate("DempApp", u"L\u01b0u d\u1eef li\u1ec7u", None))
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("DempApp", u"Ngu\u1ed3n tin t\u1ee9c", None));
        self.label_6.setText(QCoreApplication.translate("DempApp", u"ID:", None))
        self.label_7.setText(QCoreApplication.translate("DempApp", u"Websites:", None))
        self.label_8.setText(QCoreApplication.translate("DempApp", u"Th\u1eddi gi\u1ea1n:", None))
        self.label_9.setText(QCoreApplication.translate("DempApp", u"Ti\u00eau \u0111\u1ec1:", None))
        self.label_10.setText(QCoreApplication.translate("DempApp", u"N\u1ed9i dung:", None))
    # retranslateUi

