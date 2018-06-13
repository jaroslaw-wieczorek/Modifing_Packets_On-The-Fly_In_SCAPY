import os
import sys
import logging

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

from .gui.dialog_ui  import Ui_Dialog
from .iterface import Window

#class DialogWidget(QDialog, Ui_Dialog):
#    def __init__(self):
#        super(DialogWidget, self).__init__()
#        self.setupUi(self)



def backupIPTables(directory, filename):
    if not os.path.exists(directory):
        try:
            os.makedirs(str(directory))
            os.popen("iptables-save > "+str(directory)+"/"+str(filename))
        except Exception as e:
            raise e 


def restoreIPTables(directory, filename):
    if not os.path.exists(directory):
        try:
            os.makedirs(str(directory))
            os.popen("iptables-restore "+str(directory)+"/"+str(filename))
        except Exception as e:
            raise e 


def main():
    directory = "iptables-backup"
    backup = "backup"
    
    backupIPTables(directory, backup)
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec_())
    
    restoreIPTables(directory, backup)

if __name__ == "__main__":
    main()

 