#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 20:48:16 2018

@author: afar
"""
from scapy.all import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon, QImage
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

import os
import sys

# importing data accc
lib_path = os.path.abspath(os.path.join(__file__, '..', ))
sys.path.append(lib_path)
print(lib_path)


from gui.mainwindow_ui import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(QMainWindow, self).__init__()     
        self.setupUi(self)
        self.set_fit_width()
        newFilter = "dupa"
        self.add_row_to_cap_list_packets(newFilter)
     
        
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

    
    def set_button_funct(self, button, funct):
        button.clicked.connect(funct)
        P()
   
    def add_row_to_cap_list_packets(self, pkt):
        newRowNum = self.cap_list_packets.rowCount()
        print("Nowy numer pakietu:", newRowNum)
        self.cap_list_packets.insertRow(newRowNum)
        self.cap_list_packets.setItem(newRowNum, 0, QTableWidgetItem(pkt.summary()))
            
        
    def add_row_to_filt_list_packets(self, newFilter):
        newRowNum = self.filt_list_packets.rowCount()
        print("Nowy numer pakietu:", newRowNum)
        self.filt_list_packets.insertRow(newRowNum)
        self.filt_list_packets.setItem(newRowNum, 0, QTableWidgetItem(newFilter))
        self.filt_list_packets.setItem(newRowNum, 1, QTableWidgetItem(True))
     
              
    def add_row_to_mod_list_packets(self, pkt):
        newRowNum = self.mod_list_packets.rowCount()
        print("Nowy numer pakietu:", newRowNum)
        self.mod_list_packets.insertRow(newRowNum)
        self.mod_list_packets.setItem(newRowNum, 0, QTableWidgetItem(pkt.summary()))
    
    
    
    def set_fit_width(self):
        self.mod_list_packets.horizontalHeader().setStretchLastSection(True)
        self.cap_list_packets.horizontalHeader().setStretchLastSection(True)
        self.filt_list_packets.horizontalHeader().setStretchLastSection(True)
        

    def close_event_message_box(self, event):
        print("event")
        reply = QMessageBox.question(self, 'Zamykanie',
            "Czy napewno chcesz zakończyć? ", QMessageBox.Yes, QMessageBox.No)
        
        return reply

    def nothing(self):
        print("Do nothing!")
        
"""        
"""

def main():
    
    app = QApplication(sys.argv)
    mainapp = Window()
    mainapp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

 