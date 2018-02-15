# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/Harder/Documents/Code/Py/Projects/2VTT lite/UI_Designer files/about_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(421, 210)
        Form.setMinimumSize(QtCore.QSize(421, 210))
        Form.setMaximumSize(QtCore.QSize(421, 210))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 140, 421, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(0, 160, 421, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(-1, 180, 421, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 421, 151))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("icon.icns"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "About"))
        self.label.setText(_translate("Form", "2VTT v.0.9"))
        self.label_3.setText(_translate("Form", "by je09"))
        self.label_2.setText(_translate("Form", "https://github.com/je09/2VTT"))
