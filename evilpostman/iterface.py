#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 20:48:16 2018

@author: afar
"""
from scapy.all import *
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon, QImage
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

import os
import sys


# importing data accc
lib_path = os.path.abspath(os.path.join(__file__, '..', ))
sys.path.append(lib_path)
print(lib_path)

from evilpostman.pyqt_scapy_item  import PyQtScapyTableWidgetItem

from evilpostman.src.FilterCreator import Filters
from gui.mainwindow_ui import Ui_MainWindow



class Window(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(QMainWindow, self).__init__()
     
        
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

    
    def set_button_funct(self, button, funct):
        button.clicked.connect(funct)
    
    
    def openFilterCreator(self):
        title = "Kreator filtrów"
        self.filters = Filters(title)
        if self.filters.exec_() == QDialog.Accepted:
            print("HELLO")
            tmp_dict=self.filters.getValues()
        
        
    def openModifiersCreator(self):
        pass
        
   
    def add_row_to_cap_list_packets(self, pkt):
        newRowNum = self.cap_list_packets.rowCount()
        print("Nowy numer pakietu:", newRowNum)
        self.cap_list_packets.insertRow(newRowNum)
        item = QTableWidgetItem(pkt.summary())
      #  print(item.flags())
        item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
        self.cap_list_packets.setItem(newRowNum, 0, item)
        
            
        
    #def add_row_to_filt_list_packets(self, newFilter):
    #    newRowNum = self.filter_list_packets.rowCount()
    #    print("Nowy numer pakietu:", newRowNum)
    #    self.cap_list_packets.insertRow(newRowNum)
    #    self.cap_list_packets.setItem(newRowNum, 0, QTableWidgetItem(newFilter))
    #    self.cap_list_packets.setItem(newRowNum, 1, QTableWidgetItem(True))
     
              
    def add_row_to_mod_list_packets (self, pkt):
        newRowNum = self.mod_list_packets.rowCount()
        print("Nowy numer pakietu:", newRowNum)
        self.modified_list_packets.insertRow(newRowNum)
        self.modified_list_packets.setItem(newRowNum, 0, QTableWidgetItem(pkt.summary()))
    
    def get_packet_from_cap_list(self, row):
        #self.tab_widget.
        pass
    
    # DEBUG method
    def cell_was_clicked(self, row, column):
        print("Row %d and Column %d was clicked" % (row, column))
        item = self.cap_list_packets.itemAt(row, column)
        self.pkt = item.text()
        print(self.pkt)
    
    def set_fit_width(self):
        self.modified_list_packets.horizontalHeader().setStretchLastSection(True)
        self.cap_list_packets.horizontalHeader().setStretchLastSection(True)
        self.filters_list_of_filters.horizontalHeader().setStretchLastSection(True)
        

    def close_event_message_box(self, event):
        print("event")
        reply = QMessageBox.question(self, 'Zamykanie',
            "Czy napewno chcesz zakończyć? ", QMessageBox.Yes, QMessageBox.No)
        
        
        


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

 