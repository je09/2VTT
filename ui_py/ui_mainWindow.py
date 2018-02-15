# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/Harder/Documents/Code/Py/Projects/2VTT lite/UI_Designer files/design_new.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(342, 600)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(234234, 1308))
        MainWindow.setWindowTitle("2VTT")
        MainWindow.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.convertButton = QtWidgets.QPushButton(self.centralwidget)
        self.convertButton.setGeometry(QtCore.QRect(0, 550, 341, 32))
        self.convertButton.setObjectName("convertButton")
        self.fileList = QtWidgets.QListWidget(self.centralwidget)
        self.fileList.setGeometry(QtCore.QRect(1, 0, 340, 521))
        self.fileList.setObjectName("fileList")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(0, 525, 341, 32))
        self.clearButton.setObjectName("clearButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 342, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.actionPrefences = QtWidgets.QAction(MainWindow)
        self.actionPrefences.setMenuRole(QtWidgets.QAction.PreferencesRole)
        self.actionPrefences.setObjectName("actionPrefences")
        self.actionAbout_2VTT = QtWidgets.QAction(MainWindow)
        self.actionAbout_2VTT.setObjectName("actionAbout_2VTT")
        self.menuFile.addAction(self.actionAbout_2VTT)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrefences)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.convertButton.setText(_translate("MainWindow", "Convert it!"))
        self.clearButton.setText(_translate("MainWindow", "Clear the list!"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionPrefences.setText(_translate("MainWindow", "Prefences"))
        self.actionPrefences.setShortcut(_translate("MainWindow", "Ctrl+,"))
        self.actionAbout_2VTT.setText(_translate("MainWindow", "About 2VTT"))

