#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 11:18:05 2018

@author: afar
"""

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

from gui.dialog_modifiers_ui import Ui_DailogModifiers


class Modifiers(QDialog, Ui_DailogModifiers):
    def __init__(self, title:str, get_filters):
        super().__init__()
        self.title = title
        self.left = 10
        self.top = 10
        self.setupUi(self)
        self.setupWindow()
        self.show()
        self.get_filters = get_filters
        self.fields=[]
        self.protocols=[]
        self.vbox=None
        self.currentFilterlName=None
        self.currentFilterData=None
        self.filters_combo_box : QComboBox
        self.dictionary = {}
        
        
        
        for filtr in self.get_filters:
            self.filters_combo_box.addItem(str(filtr[0]), userData=filtr[1])
            print(filtr[0], filtr[1])
            
        
        self.filters_combo_box.model().sort(0)
        self.filters_combo_box.activated.connect(self.handleActivated)
        self.add_push_button.clicked.connect(self.createTabWithFilter)
        
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
        self.filters_combo_box : QComboBox
        self.dialog_buttons : QDialogButtonBox
    
        
    def getValues(self):
        
        self.tab_widget : QTabWidget
        tab_number=self.tab_widget.count()
        
        
        returned_list=[[]]
    
        for tab_num in range(0,self.tab_widget.count()):
            tab : QWidget = self.tab_widget.widget(tab_num)
            
            protocol_name = self.tab_widget.tabText(tab_num)
            
            returned_list[tab_num].append(protocol_name)
            
            fields = tab.findChildren(QLabel)
            values = tab.findChildren(QLineEdit)
            
            for field_num in range(0, len(fields)):
                tmp = [fields[field_num].text(), values[field_num].text()]
                returned_list[tab_num].append(tmp)
               
            returned_list.append([])
          
        del returned_list[-1]
        name = self.name_line_edit.text()
        self.dictionary[name] = returned_list
        
        # print(self.dictionary)
        return self.dictionary
            
        
    def handleActivated(self, index):
        self.currentFilterName = self.filters_combo_box.itemText(index)
        self.currentFilterData = self.filters_combo_box.itemData(index)
        print(self.currentFilterName)
        print(self.currentFilterData)
 
    
    def createTabWithFilter(self):
        """
            create space in new tab(tab_widget) for filter fields
            
        """

        if self.tab_widget.count() > 0:
            print("modyfikator może użyc tylko jeden filter")
            return False
        
        if self.currentFilterName == "" or self.currentFilterData is None:
            print("Wybierz poprawnycurrentFilterData filtr")
            return False
       
        """
        if not need_layers == None:
            
            for layer in need_layers:
                self.currentFilterName=layer
                self.current_tab = QWidget()
                self.current_tab.setObjectName("tab_"+str(self.currentFilterName))
        
                self.tab_widget.addTab(self.current_tab, self.currentFilterName)

                self.vert_tab = QtWidgets.QVBoxLayout(self.current_tab)
                self.vert_tab.setObjectName("ver_"+str(self.currentFilterName))
                print(self.vert_tab)
    
                self.mapProtocolFields()
                return True
           """ 
           
        for protocol_name in self.currentFilterData:
            for layer in conf.layers:
                protocol = None
                
                if layer.__name__ == protocol_name:
                    protocol = layer
                    print(protocol)
                    
                self.current_tab = QWidget()
                self.current_tab.setObjectName("tab_"+str(self.currentFilterName))
        
                self.tab_widget.addTab(self.current_tab, protocol.__name__)
                    
                self.vert_tab = QtWidgets.QVBoxLayout(self.current_tab)
                self.vert_tab.setObjectName("ver_"+str(self.currentFilterName))
                print(self.vert_tab)
                
                self.mapProtocolFields(protocol)
    
    
    
    def mapProtocolFields(self, protocol : Packet):
        """
            save to fields variable tuples contains 3 values on attribute 
                   (field_name, scapy_field_type, set/default_value) 
        """
        self.fields = []
        for i in protocol.fields_desc:
            self.fields.append((i.name, type(i), getattr(self.currentFilterData, i.name, 0)))
            self.addFilter() 
        

    def disable_text_box(self, state):
        print(state)
        if state == 0:
            pass
        else:
            pass
        pass
    

    def addFilter(self):
        self.vbox = QVBoxLayout()
        self.vbox.setObjectName("vbox_" + self.currentFilterName)

        for field in self.fields:

            hbox = QHBoxLayout()
            hbox.setObjectName(self.currentFilterName)
            
            # Dodaj QLabel o danej nazwie obiektu 
            label = QLabel(str(field[0]))
            label.width=200
            label.height=30
            label.maximumHeight=30
            label.maximumWidth=200
            hbox.addWidget(label)

            hbox.addWidget(QLineEdit())
   

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
    ex = Modifiers("Modifikatory", [["Nowa", ["TCP","IP"]], ["SUPER_UDP", ["UDP","IP"]]])
    ex.getValues()
    
    
    sys.exit(app.exec_())