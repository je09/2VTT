# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/Harder/Documents/Code/Py/Projects/2VTT lite/UI_Designer files/settings.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_tabWidget(object):
    def setupUi(self, tabWidget):
        tabWidget.setObjectName("tabWidget")
        tabWidget.resize(404, 161)
        tabWidget.setMinimumSize(QtCore.QSize(404, 161))
        tabWidget.setMaximumSize(QtCore.QSize(404, 161))
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.checkLogging = QtWidgets.QCheckBox(self.tab)
        self.checkLogging.setGeometry(QtCore.QRect(10, 0, 381, 20))
        self.checkLogging.setObjectName("checkLogging")
        self.saveButton = QtWidgets.QPushButton(self.tab)
        self.saveButton.setGeometry(QtCore.QRect(140, 105, 113, 32))
        self.saveButton.setObjectName("saveButton")
        tabWidget.addTab(self.tab, "")

        self.retranslateUi(tabWidget)
        tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(tabWidget)

    def retranslateUi(self, tabWidget):
        _translate = QtCore.QCoreApplication.translate
        tabWidget.setWindowTitle(_translate("tabWidget", "Prefences"))
        self.checkLogging.setText(_translate("tabWidget", "Logging in journal"))
        self.saveButton.setText(_translate("tabWidget", "Save"))
        tabWidget.setTabText(tabWidget.indexOf(self.tab), _translate("tabWidget", "Programm settings"))

