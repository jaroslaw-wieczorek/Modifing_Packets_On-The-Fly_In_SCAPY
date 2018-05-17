# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/afar/Modifing_Packets_On-The-Fly_In_SCAPY/evilpostman/gui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(471, 802)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.StartTab = QtWidgets.QWidget()
        self.StartTab.setObjectName("StartTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.StartTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.StartTab)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_opis1_3 = QtWidgets.QLabel(self.StartTab)
        self.label_opis1_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_opis1_3.setWordWrap(True)
        self.label_opis1_3.setObjectName("label_opis1_3")
        self.gridLayout_8.addWidget(self.label_opis1_3, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_8.addItem(spacerItem, 4, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem2, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem3, 3, 2, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.StartTab)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_8.addWidget(self.radioButton, 1, 0, 1, 2)
        self.verticalLayout_4.addLayout(self.gridLayout_8)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 3, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 2, 1, 1, 1)
        self.label_opis1 = QtWidgets.QLabel(self.StartTab)
        self.label_opis1.setMinimumSize(QtCore.QSize(0, 0))
        self.label_opis1.setWordWrap(True)
        self.label_opis1.setObjectName("label_opis1")
        self.gridLayout_2.addWidget(self.label_opis1, 3, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 3, 2, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.StartTab)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_2.addWidget(self.radioButton_2, 1, 0, 1, 2)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.checkBox = QtWidgets.QCheckBox(self.StartTab)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_4.addWidget(self.checkBox)
        self.pushButton_next = QtWidgets.QPushButton(self.StartTab)
        self.pushButton_next.setObjectName("pushButton_next")
        self.verticalLayout_4.addWidget(self.pushButton_next)
        self.tabWidget.addTab(self.StartTab, "")
        self.przechywcone = QtWidgets.QWidget()
        self.przechywcone.setObjectName("przechywcone")
        self.gridLayout = QtWidgets.QGridLayout(self.przechywcone)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.listWidget = QtWidgets.QListWidget(self.przechywcone)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_7.addWidget(self.listWidget)
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.przechywcone)
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.horizontalLayout_7.addWidget(self.verticalScrollBar_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.przechywcone)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.przechywcone)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.przechywcone, "")
        self.Ethernet = QtWidgets.QWidget()
        self.Ethernet.setObjectName("Ethernet")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Ethernet)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.Ethernet)
        self.stackedWidget_3.setMinimumSize(QtCore.QSize(300, 300))
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setMinimumSize(QtCore.QSize(500, 0))
        self.page_7.setObjectName("page_7")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_7)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.page_7)
        self.textBrowser_4.setMinimumSize(QtCore.QSize(300, 300))
        self.textBrowser_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Droid Sans Fallback")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setStyleSheet("font: 10pt \"Droid Sans Fallback\";")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.gridLayout_5.addWidget(self.textBrowser_4, 0, 0, 1, 1)
        self.stackedWidget_3.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_8)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.page_8)
        self.textBrowser_7.setMinimumSize(QtCore.QSize(300, 300))
        self.textBrowser_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Droid Sans Fallback")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textBrowser_7.setFont(font)
        self.textBrowser_7.setStyleSheet("font: 10pt \"Droid Sans Fallback\";")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.horizontalLayout_2.addWidget(self.textBrowser_7)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.page_8)
        self.label_7.setMinimumSize(QtCore.QSize(0, 0))
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.page_8)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_8.addWidget(self.lineEdit_7)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.page_8)
        self.label_8.setMinimumSize(QtCore.QSize(0, 0))
        self.label_8.setWordWrap(False)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.page_8)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_9.addWidget(self.lineEdit_8)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.page_8)
        self.label_9.setMinimumSize(QtCore.QSize(0, 0))
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.page_8)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_10.addWidget(self.lineEdit_9)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.pushButton = QtWidgets.QPushButton(self.page_8)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_5.addWidget(self.pushButton)
        self.stackedWidget_3.addWidget(self.page_8)
        self.verticalLayout_3.addWidget(self.stackedWidget_3)
        self.tabWidget.addTab(self.Ethernet, "")
        self.IP = QtWidgets.QWidget()
        self.IP.setObjectName("IP")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.IP)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget_5 = QtWidgets.QStackedWidget(self.IP)
        self.stackedWidget_5.setMinimumSize(QtCore.QSize(300, 300))
        self.stackedWidget_5.setObjectName("stackedWidget_5")
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setMinimumSize(QtCore.QSize(500, 0))
        self.page_11.setObjectName("page_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.page_11)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.page_11)
        self.textBrowser_6.setMinimumSize(QtCore.QSize(300, 300))
        self.textBrowser_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Droid Sans Fallback")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textBrowser_6.setFont(font)
        self.textBrowser_6.setStyleSheet("font: 10pt \"Droid Sans Fallback\";")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.horizontalLayout_6.addWidget(self.textBrowser_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_13 = QtWidgets.QLabel(self.page_11)
        self.label_13.setMinimumSize(QtCore.QSize(0, 0))
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_14.addWidget(self.label_13)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.page_11)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.horizontalLayout_14.addWidget(self.lineEdit_13)
        self.verticalLayout_11.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_17 = QtWidgets.QLabel(self.page_11)
        self.label_17.setMinimumSize(QtCore.QSize(0, 0))
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_18.addWidget(self.label_17)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.page_11)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.horizontalLayout_18.addWidget(self.lineEdit_17)
        self.verticalLayout_11.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_16 = QtWidgets.QLabel(self.page_11)
        self.label_16.setMinimumSize(QtCore.QSize(0, 0))
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_17.addWidget(self.label_16)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.page_11)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.horizontalLayout_17.addWidget(self.lineEdit_16)
        self.verticalLayout_11.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_14 = QtWidgets.QLabel(self.page_11)
        self.label_14.setMinimumSize(QtCore.QSize(0, 0))
        self.label_14.setWordWrap(False)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_15.addWidget(self.label_14)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.page_11)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.horizontalLayout_15.addWidget(self.lineEdit_14)
        self.verticalLayout_11.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_15 = QtWidgets.QLabel(self.page_11)
        self.label_15.setMinimumSize(QtCore.QSize(0, 0))
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_16.addWidget(self.label_15)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.page_11)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.horizontalLayout_16.addWidget(self.lineEdit_15)
        self.verticalLayout_11.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_5.addLayout(self.verticalLayout_11)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.page_11)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalLayout_5.addWidget(self.verticalScrollBar)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.stackedWidget_5.addWidget(self.page_11)
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setObjectName("page_12")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_12)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.page_12)
        self.textBrowser_8.setMinimumSize(QtCore.QSize(300, 300))
        self.textBrowser_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Droid Sans Fallback")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textBrowser_8.setFont(font)
        self.textBrowser_8.setStyleSheet("font: 10pt \"Droid Sans Fallback\";")
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.gridLayout_4.addWidget(self.textBrowser_8, 0, 0, 1, 1)
        self.stackedWidget_5.addWidget(self.page_12)
        self.verticalLayout.addWidget(self.stackedWidget_5)
        self.tabWidget.addTab(self.IP, "")
        self.UDP = QtWidgets.QWidget()
        self.UDP.setObjectName("UDP")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.UDP)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_10 = QtWidgets.QLabel(self.UDP)
        self.label_10.setMinimumSize(QtCore.QSize(0, 0))
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_11.addWidget(self.label_10)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.UDP)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_11.addWidget(self.lineEdit_10)
        self.verticalLayout_9.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_11 = QtWidgets.QLabel(self.UDP)
        self.label_11.setMinimumSize(QtCore.QSize(0, 0))
        self.label_11.setWordWrap(False)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_12.addWidget(self.label_11)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.UDP)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_12.addWidget(self.lineEdit_11)
        self.verticalLayout_9.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_18 = QtWidgets.QLabel(self.UDP)
        self.label_18.setMinimumSize(QtCore.QSize(0, 0))
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_18.setWordWrap(True)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_19.addWidget(self.label_18)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.UDP)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.horizontalLayout_19.addWidget(self.lineEdit_18)
        self.verticalLayout_9.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_12 = QtWidgets.QLabel(self.UDP)
        self.label_12.setMinimumSize(QtCore.QSize(0, 0))
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_13.addWidget(self.label_12)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.UDP)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout_13.addWidget(self.lineEdit_12)
        self.verticalLayout_9.addLayout(self.horizontalLayout_13)
        self.gridLayout_7.addLayout(self.verticalLayout_9, 0, 1, 1, 1)
        self.stackedWidget_4 = QtWidgets.QStackedWidget(self.UDP)
        self.stackedWidget_4.setMinimumSize(QtCore.QSize(300, 300))
        self.stackedWidget_4.setObjectName("stackedWidget_4")
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setMinimumSize(QtCore.QSize(500, 0))
        self.page_9.setObjectName("page_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_9)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.page_9)
        self.textBrowser_5.setMinimumSize(QtCore.QSize(300, 300))
        self.textBrowser_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Droid Sans Fallback")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textBrowser_5.setFont(font)
        self.textBrowser_5.setStyleSheet("font: 10pt \"Droid Sans Fallback\";")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.verticalLayout_8.addWidget(self.textBrowser_5)
        self.stackedWidget_4.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_10)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.graphicsView = QtWidgets.QGraphicsView(self.page_10)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_6.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.stackedWidget_4.addWidget(self.page_10)
        self.gridLayout_7.addWidget(self.stackedWidget_4, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.tabWidget.addTab(self.UDP, "")
        self.verticalLayout_6.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 471, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(1)
        self.stackedWidget_5.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(1)
        self.pushButton_2.clicked.connect(self.pushButton_2.update)
        self.pushButton_3.clicked.connect(self.tabWidget.update)
        self.listWidget.itemChanged['QListWidgetItem*'].connect(self.pushButton_3.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_7, self.lineEdit_8)
        MainWindow.setTabOrder(self.lineEdit_8, self.lineEdit_9)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EvilPostman"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Tryb działania modyfikatora pakietów:</span></p></body></html>"))
        self.label_opis1_3.setText(_translate("MainWindow", "<html><head/><body><p>Po wybraniu tego trybu, modyfikacja pakietów przebiega<br>w nasŧępujący sposób:</p><p>1) Przechodzimy dalej i włączamy przechwytywanie pakietów </p><p>2) Wybieramy pakiet z listy przechwyconych pakietów </p><p>3) Modyfikujemy pakiet używając wygenerowanych zakładek </p><p>4) Wysyłamy pakiet<br/></p></body></html>"))
        self.radioButton.setText(_translate("MainWindow", "Ręczna edycja wybranego pakietu &z listy przechwyconych:"))
        self.label_opis1.setText(_translate("MainWindow", "<html><head/><body><p>Po wybraniu tego trybu, modyfikacja pakietów przebiega<br>w nasŧępujący sposób:</p><p>1) Przechodzimy dalej i włączamy przechwytywanie pakietów </p><p>2) Wybieramy pakiet z listy przechwyconych pakietów </p><p>3) Modyfikujemy pakiet używając wygenerowanych zakładek </p><p>4) Wysyłamy pakiet<br/></p></body></html>"))
        self.radioButton_2.setText(_translate("MainWindow", "Auto&matyczne filtorwanie przechyconych pakietów:"))
        self.checkBox.setText(_translate("MainWindow", "Automatyczne przesyłanie zmodyfikownaych pakietów"))
        self.pushButton_next.setText(_translate("MainWindow", "Dalej"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.StartTab), _translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "Włącza przechwytywanie pakietów"))
        self.pushButton_3.setText(_translate("MainWindow", "Edytuj wybrany pakiet"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.przechywcone), _translate("MainWindow", "Przechwycone"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans Fallback\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  +-----------------------------+</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  |                              |</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  |     Destination_Addr      |</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   |            (6 octets)          | </p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  |                              |</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  |                              |</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  |                              |</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  +-----------------------------+</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  |                              |</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  |          Source_Addr           |</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   |            (6 octets)              | </p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  |                             |</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  |                              |</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  |                              |</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  +------------------------------+</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  |                              |</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  |  Ether_Type  (2 octets) |</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  |                              |</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  +------------------------------+</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  |                              |</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  |               payload      |</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  |                               |</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  +------------------------------+</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  |                        |</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  |             Checksum          |</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  |                               |</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  +------------------------------+</p></body></html>"))
        self.textBrowser_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans Fallback\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"10\" cellpadding=\"0\">\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0000</p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#00d1ff;\">34BA9A27E383A44E3152B7480800</span>45B0</p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4..\'...N1R.H..E.</p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0010</p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">009ED8BB400040118BDEC0A8000A05C8</p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">....@.@.........</p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0020</p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0E8B9AA1CAE7008A3D61</p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">........=a</p></td></tr></table></body></html>"))
        self.label_7.setText(_translate("MainWindow", "src:"))
        self.label_8.setText(_translate("MainWindow", "dst:"))
        self.label_9.setText(_translate("MainWindow", "type:"))
        self.pushButton.setText(_translate("MainWindow", "Wyślij"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Ethernet), _translate("MainWindow", "Ethernet"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans Fallback\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"10\" cellpadding=\"0\">\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0000</p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">34BA9A27E383A44E3152B7480800<span style=\" font-weight:600; color:#ae00ff;\">45B0</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4..\'...N1R.H..E.</p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0010</p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ae00ff;\">009ED8BB400040118BDEC0A8000A05C8</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ae00ff;\">....@.@.........</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0020</p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ae00ff;\">0E8B</span>9AA1CAE7008A3D61</p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">........=a</p></td></tr></table></body></html>"))
        self.label_13.setText(_translate("MainWindow", "frag:"))
        self.label_17.setText(_translate("MainWindow", "src:"))
        self.label_16.setText(_translate("MainWindow", "proto:"))
        self.label_14.setText(_translate("MainWindow", "tos:"))
        self.label_15.setText(_translate("MainWindow", "dst:"))
        self.textBrowser_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans Fallback\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.IP), _translate("MainWindow", "IP"))
        self.label_10.setText(_translate("MainWindow", "dport:"))
        self.label_11.setText(_translate("MainWindow", "sport:"))
        self.label_18.setText(_translate("MainWindow", "len:"))
        self.label_12.setText(_translate("MainWindow", "chksum:"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans Fallback\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"10\" cellpadding=\"0\">\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0000</p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">34BA9A27E383A44E3152B748080045B0</p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4..\'...N1R.H..E.</p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0010</p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">009ED8BB400040118BDEC0A8000A05C8</p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">....@.@.........</p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0020</p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0E8B<span style=\" font-weight:600; color:#73d216;\">9AA1CAE7008A3D61</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">..<span style=\" font-weight:600; color:#73d216;\">......=a</span></p></td></tr></table></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.UDP), _translate("MainWindow", "UDP"))

