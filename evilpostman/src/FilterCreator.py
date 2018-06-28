#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 20:06:02 2018

@author: afar
"""
import os
import sys
from functools import partial

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
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QTabWidget


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
    def __init__(self, title : str):
        super().__init__()
        
        self.title = title
        self.left = 10
        self.top = 10
        self.setupUi(self)
        self.setupWindow()
        
        
        self.show()
        self.fields=[]
        self.protocols=[]
        self.vbox=None
        self.currentProtocolName=None
        self.currentProtocolData=None
        
        self.dictionary = {}
        

        for protocol in conf.layers:
            self.protocol_combo_box.addItem(protocol.__name__, userData=protocol)
        
        self.protocol_combo_box.model().sort(0)
         
        self.protocol_combo_box.activated.connect(self.handleActivated)
        self.add_push_button.clicked.connect(self.createTabWithProtocol)
        
        self.tab_widget.tabCloseRequested.connect(self.removeTab)
        self.tab_widget.setTabsClosable(True)
        
    
    def removeTab(self, index):
        widget = self.tab_widget.widget(index)
        if widget is not None:
            widget.deleteLater()
        self.tab_widget.removeTab(index) 
        
        
    def setupWindow(self):
        self.setWindowTitle(self.title)   
        self.tab_widget : QTabWidget
        self.vertical_layout : QVBoxLayout
        self.horizontal_layout : QHBoxLayout
        self.name_line_edit : QLineEdit
        self.add_push_button : QPushButton
        self.protocol_combo_box : QComboBox
        self.dialog_buttons : QDialogButtonBox
         
        
    def getValues(self):
        
        self.tab_widget : QTabWidget
        tab_number=self.tab_widget.count()
        
        
        returned_list=[[]]
    
        for tab_num in range(0,self.tab_widget.count()):
            tab : QWidget = self.tab_widget.widget(tab_num)
            
            protocol_name = self.tab_widget.tabText(tab_num)
            
            returned_list[tab_num].append(protocol_name)
            print(returned_list)
            
            fields = tab.findChildren(QLabel)
            values = tab.findChildren(QLineEdit)
            
            
            for field_num in range(0, len(fields)):
                tmp = [fields[field_num].text(), values[field_num].text()]
                returned_list[tab_num].append(tmp)
               
            returned_list.append([])
          
        del returned_list[-1]
       

        name = self.name_line_edit.text()
        self.dictionary[name] = returned_list
        
        print(self.dictionary)
        return self.dictionary
            
        
    def handleActivated(self, index):
        self.currentProtocolName = self.protocol_combo_box.itemText(index)
        self.currentProtocolData = self.protocol_combo_box.itemData(index)
        print(self.currentProtocolName)
        print(self.currentProtocolData)
 
    
    def createTabWithProtocol(self):
        """
            create space in new tab(tab_widget) for protocol fields
            
        """
        child = self.tab_widget.findChild(QWidget, "tab_"+str(self.currentProtocolName))
        print(child)
        if self.currentProtocolName == "" or self.currentProtocolData is None:
            print("Wybierz najpierw protokół")
            return False
        
        if not child is None:
            print("Już dodano ten protokół")
            return False
        
        self.current_tab = QWidget()
        self.current_tab.setObjectName("tab_"+str(self.currentProtocolName))
        
        self.tab_widget.addTab(self.current_tab, self.currentProtocolName)

        self.vert_tab = QtWidgets.QVBoxLayout(self.current_tab)
        self.vert_tab.setObjectName("ver_"+str(self.currentProtocolName))
        print(self.vert_tab)
    
        self.mapProtocolFields()
    
    
    
    def mapProtocolFields(self):
        """
            save to fields variable tuples contains 3 values on attribute 
                   (field_name, scapy_field_type, set/default_value) 
        """
        self.fields = []
        for i in self.currentProtocolData.fields_desc:
            self.fields.append((i.name, type(i), getattr(self.currentProtocolData, i.name, 0)))
        self.addFilter() 

        self.getValues()
            

    def addFilter(self):
        self.vbox = QVBoxLayout()
        self.vbox.setObjectName("vbox_" + self.currentProtocolName)

        for field in self.fields:

            hbox = QHBoxLayout()
            hbox.setObjectName(self.currentProtocolName)
            
            # Dodaj QLabel o danej nazwie obiektu 
            label = QLabel(self.currentProtocolName+"_"+str(field[0]))
            label.width=200
            label.height=30
            label.maximumHeight=30
            label.maximumWidth=200
            hbox.addWidget(label)
            
            hbox.addWidget(QLineEdit())
            hbox.addWidget(QCheckBox("use it"))
            self.vbox.addStretch(1)
            self.vbox.addLayout(hbox)
             
        self.vert_tab.addLayout(self.vbox)   
        self.update()
        


   
    
if __name__ == '__main__':
    app=QApplication.instance() 
    if not app: # create QApplication if it doesnt exist 
        app = QApplication(sys.argv)
    
   # t = Gui(TCP)
    

   # u = Gui(UDP)
    ex = Filters("Filters")
    ex.getValues()
    
    sys.exit(app.exec_())