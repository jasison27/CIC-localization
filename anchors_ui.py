# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anchors.ui'
#
# Created: Tue Aug 19 15:19:01 2014
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

class Ui_anchors(object):
    def setupUi(self, anchors):
        anchors.setObjectName(_fromUtf8("anchors"))
        anchors.resize(532, 261)
        self.tableWidget = QtGui.QTableWidget(anchors)
        self.tableWidget.setGeometry(QtCore.QRect(0, 30, 531, 192))
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.label = QtGui.QLabel(anchors)
        self.label.setGeometry(QtCore.QRect(0, 10, 131, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Aharoni"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.layoutWidget = QtGui.QWidget(anchors)
        self.layoutWidget.setGeometry(QtCore.QRect(280, 230, 245, 27))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.saveButton_3 = QtGui.QPushButton(self.layoutWidget)
        self.saveButton_3.setObjectName(_fromUtf8("saveButton_3"))
        self.gridLayout.addWidget(self.saveButton_3, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.removeButton_2 = QtGui.QPushButton(self.layoutWidget)
        self.removeButton_2.setObjectName(_fromUtf8("removeButton_2"))
        self.gridLayout.addWidget(self.removeButton_2, 0, 2, 1, 1)

        self.retranslateUi(anchors)
        QtCore.QMetaObject.connectSlotsByName(anchors)

    def retranslateUi(self, anchors):
        anchors.setWindowTitle(_translate("anchors", "Dialog", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("anchors", "TagID", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("anchors", "X", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("anchors", "Y", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("anchors", "Z", None))
        self.label.setText(_translate("anchors", "Current Anchors:", None))
        self.saveButton_3.setText(_translate("anchors", "Save", None))
        self.pushButton.setText(_translate("anchors", "Add", None))
        self.removeButton_2.setText(_translate("anchors", "Remove", None))

