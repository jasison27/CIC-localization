from PyQt4 import QtGui
from zones_ui import Ui_zones
from config import Config

class ZonesWindow(QtGui.QDialog):

    def __init__(self,parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_zones()
        self.ui.setupUi(self)
        self.init_table()
        self.ui.saveButton.clicked.connect(self.save_table)
        self.ui.addButton_2.clicked.connect(self.addItem)
        self.ui.removeButton_3.clicked.connect(self.removeItem)

    def init_table(self):
        i = 0
        while i < len(Config.zones):
            i = i + 1
            self.ui.tableWidget.insertRow(0)
        i = 0
        for v in Config.zones:
            item = QtGui.QTableWidgetItem("%d"%v[0])
            self.ui.tableWidget.setItem(i,0,item)
            item1 = QtGui.QTableWidgetItem("%d"%v[1])
            self.ui.tableWidget.setItem(i,1,item1)
            item2 = QtGui.QTableWidgetItem("%d"%v[2])
            self.ui.tableWidget.setItem(i,2,item2)
            item3 = QtGui.QTableWidgetItem("%d"%v[3])
            self.ui.tableWidget.setItem(i,3,item3)
            i = i + 1


    def save_table(self):
        i = 0
        json = []
        while i < self.ui.tableWidget.rowCount():
             temp = []
             temp.append(float(self.ui.tableWidget.item(i,0).text()))
             temp.append(float(self.ui.tableWidget.item(i,1).text()))
             temp.append(float(self.ui.tableWidget.item(i,2).text()))
             temp.append(float(self.ui.tableWidget.item(i,3).text()))
             json.append(temp)
             i += 1

        Config.zones = json
        Config.save_config()
        QtGui.QMessageBox.warning(self,"Message","The settings have been saved")
        self.close()

    def addItem(self):
        self.ui.tableWidget.insertRow(0)


    def removeItem(self):
        row = self.ui.tableWidget.currentRow()
        if row == -1:
            return
        self.ui.tableWidget.removeRow(row)
