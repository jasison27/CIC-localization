from PyQt4 import QtGui
from dynamics_ui import Ui_dynamic
from config import Config
class DynamicsWindow(QtGui.QDialog):

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_dynamic()
        self.ui.setupUi(self)
        self.init_table()
        self.ui.addButton_2.clicked.connect(self.addItem)
        self.ui.removeButton.clicked.connect(self.removeItem)
        self.ui.saveButton_3.clicked.connect(self.saveItem)

    def addItem(self):
        self.ui.tableWidget.insertRow(0)


    def saveItem(self):
        i = 0
        json = {}
        while i < self.ui.tableWidget.rowCount():
             json[self.ui.tableWidget.item(i,0).text()] = float(self.ui.tableWidget.item(i,1).text())
             i += 1

        Config.dynamic_tags = json
        Config.save_config()
        QtGui.QMessageBox.warning(self,"Message","The settings have been saved")
        self.close()

    def removeItem(self):
        row = self.ui.tableWidget.currentRow()
        if row == -1:
            return
        self.ui.tableWidget.removeRow(row)


    def init_table(self):
        i = 0
        while i < len(Config.dynamic_tags):
            i = i + 1
            self.ui.tableWidget.insertRow(0)
        i = 0
        for k,v in Config.dynamic_tags.items():
            item = QtGui.QTableWidgetItem(k)
            self.ui.tableWidget.setItem(i,0,item)
            item1 = QtGui.QTableWidgetItem("%d"%v)
            self.ui.tableWidget.setItem(i,1,item1)
            i = i + 1