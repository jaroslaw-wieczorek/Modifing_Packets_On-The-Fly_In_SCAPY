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
    app.aboutToQuit.connect(mainapp.stop_capture)
    mainapp.handler.setButtonFunct(mainapp.handler.cap_button_sniff, mainapp.start_capture)

    mainapp.handler.setButtonFunct(mainapp.handler.info_button_next,
                             partial(mainapp.handler.tab_widget.setCurrentIndex, 1))

    mainapp.handler.setButtonFunct(mainapp.handler.cap_button_back,
                             partial(mainapp.handler.tab_widget.setCurrentIndex, 0))
    mainapp.handler.setButtonFunct(mainapp.handler.cap_button_next,
                             partial(mainapp.handler.tab_widget.setCurrentIndex, 2))
    
    mainapp.handler.setButtonFunct(mainapp.handler.filters_button_back,
                             partial(mainapp.handler.tab_widget.setCurrentIndex, 1))
    
    mainapp.handler.setButtonFunct(mainapp.handler.filters_button_next,
                             partial(mainapp.handler.tab_widget.setCurrentIndex, 3))
    
    mainapp.handler.setButtonFunct(mainapp.handler.modified_button_back,
                             partial(mainapp.handler.tab_widget.setCurrentIndex, 3))
    
    mainapp.handler.setButtonFunct(mainapp.handler.filters_button_next,
                             partial(mainapp.handler.tab_widget.setCurrentIndex, 3))

    mainapp.handler.setButtonFunct(mainapp.handler.modifiers_button_back,
                             partial(mainapp.handler.tab_widget.setCurrentIndex, 2))
    mainapp.handler.setButtonFunct(mainapp.handler.modifiers_button_next,
                             partial(mainapp.handler.tab_widget.setCurrentIndex, 4))
    
    mainapp.handler.setButtonFunct(mainapp.handler.modified_button_stop, mainapp.stop_capture)
    
    
    mainapp.handler.setButtonFunct(mainapp.handler.modified_button_show, partial(mainapp.handler.nothing))
    
    mainapp.handler.cap_list_of_packets.cellDoubleClicked['int','int'].connect(
            partial(mainapp.handler.cell_was_clicked))
    
    mainapp.handler.setButtonFunct(mainapp.handler.filters_button_create_filter, partial(mainapp.handler.filter_dialog))
    mainapp.handler.setButtonFunct(mainapp.handler.modifiers_button_create_modifier, partial(mainapp.handler.modifier_dialog))

    mainapp.closeEvent=mainapp.handler.close_event_message_box
    mainapp.handler.set_fit_width()
    mainapp.handler.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

 