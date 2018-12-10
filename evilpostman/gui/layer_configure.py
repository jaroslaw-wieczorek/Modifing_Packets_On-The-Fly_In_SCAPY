#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 15:44:17 2018

@author: afar
"""

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

from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
from PyQt5.QtCore import QObject

from scapy.layers import *
from scapy.all import *

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
        self.vertical=QVBoxLayout()
        self.setLayout(self.vertical)
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
        
        
    def addToInterface(self, guiObject):
        self.vertical.addLayout(guiObject)
        self.update()


class Gui(QObject):
 
    def __init__(self,Protocol):
        super().__init__()
        
        self.title = Protocol().name
        self.title_label = QLabel(self.title+" filter")
        self.fields=[]
        self.protocol = Protocol()
        self.mapProtocolFields()
        self.labels=[]
       
        
        print(self.fields)
        self.create_interface()
        
    def dumpFilterTCP(self):
        self.protocol_dump = Protocol()
        pass
    
    
    def getNameProtocol(self):
        self.title
    
    
    def mapProtocolFields(self):
        """
            save to fields variable tuples contains 3 values on attribute 
                   (field_name, scapy_field_type, set/default_value) 
        """
        for i in self.protocol.fields_desc:
            self.fields.append((i.name, type(i), getattr(self.protocol, i.name, 0)))
            
        self.create_interface()
        
    def create_interface(self):
        
        self.vbox = QVBoxLayout()
        for field in self.fields:
            hbox = QHBoxLayout()
            hbox.setObjectName(str(field[0]))
            hbox.addWidget(QLabel(str(field[0])))
            hbox.addWidget(QLineEdit())
            hbox.addWidget(QCheckBox("filter on: "+str(field[0])))
            self.vbox.addStretch(1)
            self.vbox.addLayout(hbox)
        
        
if __name__ == '__main__':
    app=QtWidgets.QApplication.instance() 
    if not app: # create QApplication if it doesnt exist 
        app = QtWidgets.QApplication(sys.argv)
    
    t = Gui(TCP)
    
    print("################")
    u = Gui(UDP)
    ex = App()
    ex.addToInterface(t.vbox)
    
    sys.exit(app.exec_())
  