# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TeknobolYoutube.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TeknobolYoutubeDowndloader(object):
    def setupUi(self, TeknobolYoutubeDowndloader):
        TeknobolYoutubeDowndloader.setObjectName("TeknobolYoutubeDowndloader")
        TeknobolYoutubeDowndloader.resize(714, 395)
        TeknobolYoutubeDowndloader.setMaximumSize(QtCore.QSize(714, 395))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../WnZ6H0JJ.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TeknobolYoutubeDowndloader.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(TeknobolYoutubeDowndloader)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, -43, 751, 171))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 80, 671, 241))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.layoutWidget = QtWidgets.QWidget(self.tab_1)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 14, 661, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_1)
        self.layoutWidget1.setGeometry(QtCore.QRect(1, 73, 661, 131))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget1)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 14, 661, 51))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_3.setGeometry(QtCore.QRect(1, 73, 661, 131))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.progressBar_2 = QtWidgets.QProgressBar(self.layoutWidget_3)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setTextVisible(False)
        self.progressBar_2.setObjectName("progressBar_2")
        self.verticalLayout_2.addWidget(self.progressBar_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(23, 327, 671, 16))
        self.label_6.setObjectName("label_6")
        TeknobolYoutubeDowndloader.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TeknobolYoutubeDowndloader)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 714, 26))
        self.menubar.setObjectName("menubar")
        TeknobolYoutubeDowndloader.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TeknobolYoutubeDowndloader)
        self.statusbar.setObjectName("statusbar")
        TeknobolYoutubeDowndloader.setStatusBar(self.statusbar)

        self.retranslateUi(TeknobolYoutubeDowndloader)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(TeknobolYoutubeDowndloader)

    def retranslateUi(self, TeknobolYoutubeDowndloader):
        _translate = QtCore.QCoreApplication.translate
        TeknobolYoutubeDowndloader.setWindowTitle(_translate("TeknobolYoutubeDowndloader", "TeknoBol Youtube Downloader - v2.0"))
        self.label_2.setText(_translate("TeknobolYoutubeDowndloader", "TeknoBol Youtube Downloader"))
        self.label.setText(_translate("TeknobolYoutubeDowndloader", "Uzantı"))
        self.pushButton.setText(_translate("TeknobolYoutubeDowndloader", "İndir"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("TeknobolYoutubeDowndloader", "MP4"))
        self.label_4.setText(_translate("TeknobolYoutubeDowndloader", "Uzantı"))
        self.pushButton_2.setText(_translate("TeknobolYoutubeDowndloader", "İndir"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("TeknobolYoutubeDowndloader", "MP3"))
        self.label_6.setText(_translate("TeknobolYoutubeDowndloader", "Copyright © TeknoBol, 2017-2020. Tüm hakları saklıdır.                                                  instagram.com/TeknoBol"))

