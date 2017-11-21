# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dynamics.ui'
#
# Created: Wed Aug 20 11:43:44 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_dynamic(object):
    def setupUi(self, dynamic):
        dynamic.setObjectName(_fromUtf8("dynamic"))
        dynamic.resize(481, 259)
        font = QtGui.QFont()
        font.setPointSize(9)
        dynamic.setFont(font)
        self.label = QtGui.QLabel(dynamic)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.layoutWidget = QtGui.QWidget(dynamic)
        self.layoutWidget.setGeometry(QtCore.QRect(210, 230, 245, 27))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.saveButton_3 = QtGui.QPushButton(self.layoutWidget)
        self.saveButton_3.setObjectName(_fromUtf8("saveButton_3"))
        self.horizontalLayout.addWidget(self.saveButton_3)
        self.removeButton = QtGui.QPushButton(self.layoutWidget)
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.horizontalLayout.addWidget(self.removeButton)
        self.addButton_2 = QtGui.QPushButton(self.layoutWidget)
        self.addButton_2.setObjectName(_fromUtf8("addButton_2"))
        self.horizontalLayout.addWidget(self.addButton_2)
        self.tableWidget = QtGui.QTableWidget(dynamic)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 461, 192))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)

        self.retranslateUi(dynamic)
        QtCore.QMetaObject.connectSlotsByName(dynamic)

    def retranslateUi(self, dynamic):
        dynamic.setWindowTitle(_translate("dynamic", "Dialog", None))
        self.label.setText(_translate("dynamic", "Dynamic Tags:", None))
        self.saveButton_3.setText(_translate("dynamic", "Save", None))
        self.removeButton.setText(_translate("dynamic", "Remove", None))
        self.addButton_2.setText(_translate("dynamic", "Add", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("dynamic", "TAG ID", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("dynamic", "Radius", None))

