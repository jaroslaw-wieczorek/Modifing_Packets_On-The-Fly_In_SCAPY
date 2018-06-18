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
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()


class Gui(QObject):
 
    def __init__(self):
        super().__init__()
        
        self.title = 'TCP'
        self.title_label = QLabel(self.title+" filter")
        self.fields=["nowa"]
        self.tcp = TCP()
        self.getFieldsNames()
        print(self.fields)
        
    def dumpFilterTCP(self):
        tcp_filter = TCP()
        pass
    
    def getFieldsNames(self):
        for i in self.tcp.fields_desc:
            self.fields.append(i.name)
            self.fields.append(getattr(self.tcp, i.name, 0))
            
            
        
 
     
if __name__ == '__main__':
    app=QtWidgets.QApplication.instance() 
    if not app: # create QApplication if it doesnt exist 
        app = QtWidgets.QApplication(sys.argv)
    t = Gui()
    ex = App()
    sys.exit(app.exec_())
  