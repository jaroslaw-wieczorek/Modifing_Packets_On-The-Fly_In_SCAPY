import os
import sys
import logging

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

from .gui.dialog_ui  import Ui_Dialog
from .iterface import Window
from .nfqueue import QueuePacketCatcher

#class DialogWidget(QDialog, Ui_Dialog):
#    def __init__(self):
#        super(DialogWidget, self).__init__()
#        self.setupUi(self)




def main():
    app = QApplication(sys.argv)
    mainapp = QueuePacketCatcher()
    mainapp.set_button_funct(mainapp.cap_button_sniff, mainapp.start_capture)
    mainapp.set_fit_width()
    mainapp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

 