from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import  QtGui
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

class PyQtScapyTableWidgetItem(QTableWidgetItem):
    # << Custom Main Widget >> #
    def __init__(self, text, data):
        super(PyQtScapyTableWidgetItem, self).__init__()
        self.text = ""
        self.data = ""    
        self.setText(text)
        self.setData(data)
        
        
    def setText(self, text):
        self.text = str(text)

    def text(self):
        return self.text
        
    def setData(self, data):
        self.data = data
