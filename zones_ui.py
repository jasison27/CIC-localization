# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zones.ui'
#
# Created: Wed Aug 20 12:00:47 2014
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

class Ui_zones(object):
    def setupUi(self, zones):
        zones.setObjectName(_fromUtf8("zones"))
        zones.resize(635, 261)
        self.label = QtGui.QLabel(zones)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.tableWidget = QtGui.QTableWidget(zones)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 611, 192))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(0)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.layoutWidget = QtGui.QWidget(zones)
        self.layoutWidget.setGeometry(QtCore.QRect(270, 230, 245, 27))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.addButton_2 = QtGui.QPushButton(self.layoutWidget)
        self.addButton_2.setObjectName(_fromUtf8("addButton_2"))
        self.horizontalLayout.addWidget(self.addButton_2)
        self.removeButton_3 = QtGui.QPushButton(self.layoutWidget)
        self.removeButton_3.setObjectName(_fromUtf8("removeButton_3"))
        self.horizontalLayout.addWidget(self.removeButton_3)
        self.saveButton = QtGui.QPushButton(self.layoutWidget)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout.addWidget(self.saveButton)

        self.retranslateUi(zones)
        QtCore.QMetaObject.connectSlotsByName(zones)

    def retranslateUi(self, zones):
        zones.setWindowTitle(_translate("zones", "Dialog", None))
        self.label.setText(_translate("zones", "Dangerous Zones:", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("zones", "Left X", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("zones", "Left Y", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("zones", "Right X", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("zones", "Right Y", None))
        self.addButton_2.setText(_translate("zones", "Add", None))
        self.removeButton_3.setText(_translate("zones", "Remove", None))
        self.saveButton.setText(_translate("zones", "Save", None))

