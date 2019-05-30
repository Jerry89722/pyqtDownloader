# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt_downloader.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!


# 这个文件文件由pyqt_downloader.ui文件生成, 生成命令如下 :
# pyuic5 pyqt_downloader.ui -o pyqt_downloader_ui.py

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Downloader(object):
    def setupUi(self, Downloader):
        Downloader.setObjectName("Downloader")
        Downloader.resize(800, 600)
        self.mainWidget = QtWidgets.QWidget(Downloader)
        self.mainWidget.setObjectName("mainWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.urlWidget = QtWidgets.QWidget(self.mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.urlWidget.sizePolicy().hasHeightForWidth())
        self.urlWidget.setSizePolicy(sizePolicy)
        self.urlWidget.setObjectName("urlWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.urlWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.urlHBoxLayout = QtWidgets.QHBoxLayout()
        self.urlHBoxLayout.setObjectName("urlHBoxLayout")
        self.urlLable = QtWidgets.QLabel(self.urlWidget)
        self.urlLable.setObjectName("urlLable")
        self.urlHBoxLayout.addWidget(self.urlLable)
        self.urlLineText = QtWidgets.QLineEdit(self.urlWidget)
        self.urlLineText.setObjectName("urlLineText")
        self.urlHBoxLayout.addWidget(self.urlLineText)
        self.downloadPBtn = QtWidgets.QPushButton(self.urlWidget)
        self.downloadPBtn.setObjectName("downloadPBtn")
        self.urlHBoxLayout.addWidget(self.downloadPBtn)
        self.verticalLayout_2.addLayout(self.urlHBoxLayout)
        self.verticalLayout.addWidget(self.urlWidget)
        self.listWidget = QtWidgets.QWidget(self.mainWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.listWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listScrollArea = QtWidgets.QScrollArea(self.listWidget)
        self.listScrollArea.setWidgetResizable(True)
        self.listScrollArea.setObjectName("listScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 762, 511))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.listTreeWidget = QtWidgets.QTreeWidget(self.scrollAreaWidgetContents)
        self.listTreeWidget.setObjectName("listTreeWidget")
        self.verticalLayout_4.addWidget(self.listTreeWidget)
        self.listScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.listScrollArea)
        self.verticalLayout.addWidget(self.listWidget)
        Downloader.setCentralWidget(self.mainWidget)

        self.retranslateUi(Downloader)
        QtCore.QMetaObject.connectSlotsByName(Downloader)

    def retranslateUi(self, Downloader):
        _translate = QtCore.QCoreApplication.translate
        Downloader.setWindowTitle(_translate("Downloader", "pyqt Downloader"))
        self.urlLable.setText(_translate("Downloader", "url:"))
        self.downloadPBtn.setText(_translate("Downloader", "Download"))
        self.listTreeWidget.headerItem().setText(0, _translate("Downloader", "No."))
        self.listTreeWidget.headerItem().setText(1, _translate("Downloader", "name"))
        self.listTreeWidget.headerItem().setText(2, _translate("Downloader", "time"))
        self.listTreeWidget.headerItem().setText(3, _translate("Downloader", "percent"))


