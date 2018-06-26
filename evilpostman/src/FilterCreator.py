#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 20:06:02 2018

@author: afar
"""
import os
import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets


from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QDialog

from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
from PyQt5.QtCore import QObject

from scapy.layers import *
from scapy.all import *


lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)
print(lib_path)

from gui.dialog_filters_ui import Ui_DailogFilter


class Filters(QDialog, Ui_DailogFilter):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.show()
        self.fields=[]
        self.protocols=[]
        self.vbox=None
        self.currentProtocol=None
        
        self.protocol_combo_box.addItem('IP - Protocol', userData=IP)
        self.protocol_combo_box.addItem('TCP - Protocol', userData=TCP)
        self.protocol_combo_box.addItem('UDP - Protocol', userData=UDP)
        self.protocol_combo_box.addItem('ARP - Protocol', userData=ARP)
        
         
        self.protocol_combo_box.activated.connect(self.handleActivated)
        self.add_push_button.clicked.connect(self.mapProtocolFields)
    
    
    def handleActivated(self, index):
        print(self.protocol_combo_box.itemText(index))
        print(self.protocol_combo_box.itemData(index))
        self.currentProtocol=self.protocol_combo_box.itemData(index)
    
    
    def mapProtocolFields(self):
        """
            save to fields variable tuples contains 3 values on attribute 
                   (field_name, scapy_field_type, set/default_value) 
        """
        for i in self.currentProtocol.fields_desc:
            self.fields.append((i.name, type(i), getattr(self.currentProtocol, i.name, 0)))
        
        self.addFilter()    
        
    def addFilter(self):
        if self.fields is None:
            return False
        self.vbox = QVBoxLayout()
        for field in self.fields:
            hbox = QHBoxLayout()
            hbox.setObjectName(str(field[0]))
            hbox.addWidget(QLabel(str(field[0])))
            hbox.addWidget(QLineEdit())
            hbox.addWidget(QCheckBox("filter on: "+str(field[0])))
            self.vbox.addStretch(1)
            self.vbox.addLayout(hbox)
        self.vertical_layout_2.addLayout(self.vbox)
        self.update()
        
    
    def addGui(self):
        self.vertical.addLayout(guiObject)
        self.update()

   
    
if __name__ == '__main__':
    app=QApplication.instance() 
    if not app: # create QApplication if it doesnt exist 
        app = QApplication(sys.argv)
    
   # t = Gui(TCP)
    

   # u = Gui(UDP)
    ex = Filters()
    
    sys.exit(app.exec_())