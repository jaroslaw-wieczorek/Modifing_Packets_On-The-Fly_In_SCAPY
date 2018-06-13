#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 20:48:16 2018

@author: afar
"""

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
        #self.setupUi(self)
        #self.set_fit_width()
        
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

        
    def set_start_tab_button_next(self, funct):
        self.start_tab_button_next.clicked.connect(funct)

    
    ### 1) SNIFF TAB ###
    def set_sniff_tab_button_back(self, funct):
        self.sniff_tab_button_back.clicked.connect(funct)

       
    def set_sniff_tab_button_create_filter_from_packet(self, funct):
        self.sniff_tab_button_create_filter_from_packet.clicked.connect(funct)

        
    def set_sniff_tab_button_next(self, funct):
        self.sniff_tab_button_next.clicked.connect(funct)


    def set_sniff_tab_button_sniff(self, funct):
        self.sniff_tab_button_sniff.clicked.connect(funct)


    def add_row_to_sniff_tab_list_of_packets(self, pkt):
        newRowNum = self.table_widget_list_of_users.rowCount()
        print("Nowy numer pakietu:", newRowNum)
        self.sniff_tab_list_of_packets.insertRow(newRowNum)
        self.sniff_tab_list_of_packets.setItem(newRowNum, 0, QTableWidgetItem(newRowNum))
        self.sniff_tab_list_of_packets.setItem(newRowNum, 1, QTableWidgetItem(pkt))

    
    ### 2) filter tab ###

    def set_filters_tab_button_back(self, funct):
        self.filters_tab_button_back.clicked.connect(funct)


    def set_filters_tab_button_create_filter(self, funct):
        self.filters_tab_button_create_filter.clicked.connect(funct)

        
    def set_filters_tab_button_next(self, funct):
        self.filters_tab_button_next.clicked.connect(funct)

    ### 3) Modify TAB ###
    def set_modified_tab_back(self, funct):
        self.modified_tab_back.clicked.connect(funct)


    def set_modified_tab_button_show(self, funct):
        self.modified_tab_button_show.clicked.connect(funct)


    def set_modified_tab_button_stop(self, funct):
        self.modified_tab_button_stop.clicked.connect(funct)
     
              
    def add_row_to_modified_tab_list_of_packets(self, pkt):
        newRowNum = self.table_widget_list_of_users.rowCount()
        print("Nowy numer pakietu:", newRowNum)
        self.modified_tab_list_of_packets.insertRow(newRowNum)
        self.modified_tab_list_of_packets.setItem(newRowNum, 0, QTableWidgetItem(newRowNum))
        self.modified_tab_list_of_packets.setItem(newRowNum, 1, QTableWidgetItem(pkt))
    
    
    
    def set_fit_width(self):
        self.modified_tab_list_of_packets.horizontalHeader().setStretchLastSection(True)
        self.sniff_tab_list_of_packets.horizontalHeader().setStretchLastSection(True)
        self.filters_tab_list_of_packets.horizontalHeader().setStretchLastSection(True)
        

    def close_event_message_box(self, event):
        print("event")
        reply = QMessageBox.question(self, 'Zamykanie',
            "Czy napewno chcesz zakończyć? ", QMessageBox.Yes, QMessageBox.No)
        
        return reply

    def nothing(self):
        print("Do nothing!")
        
        
