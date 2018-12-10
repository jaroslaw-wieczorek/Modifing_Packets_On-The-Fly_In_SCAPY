from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import  QtGui
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

class PyQtScapyTableWidgetItem(QTableWidgetItem):
    # << Custom Main Widget >> #
    def __init__(self, text):
        super(PyQtScapyTableWidgetItem).__init__()
        