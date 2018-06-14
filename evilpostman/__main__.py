import os
import sys
import logging
from functools import partial

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
    
    mainapp.set_button_funct(mainapp.info_button_next,
                             partial(mainapp.tab_widget.setCurrentIndex, 1))

    mainapp.set_button_funct(mainapp.cap_button_back,
                             partial(mainapp.tab_widget.setCurrentIndex, 0))
    mainapp.set_button_funct(mainapp.cap_button_next,
                             partial(mainapp.tab_widget.setCurrentIndex, 2))
    
    mainapp.set_button_funct(mainapp.filt_button_back,
                             partial(mainapp.tab_widget.setCurrentIndex, 1))
    
    mainapp.set_button_funct(mainapp.filt_button_next,
                             partial(mainapp.tab_widget.setCurrentIndex, 3))
    
    mainapp.set_button_funct(mainapp.mod_button_back,
                             partial(mainapp.tab_widget.setCurrentIndex, 2))
    
    mainapp.set_button_funct(mainapp.mod_button_stop, mainapp.start_capture)
    
    
    mainapp.set_button_funct(mainapp.mod_button_show, partial(mainapp.nothing))
    
    mainapp.cap_list_packets.cellDoubleClicked['int','int'].connect(
            partial(mainapp.cell_was_clicked))
    
    
    mainapp.set_fit_width()
    mainapp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

 