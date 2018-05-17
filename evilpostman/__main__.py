import sys
import logging

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

from .gui.mainwindow_ui import Ui_MainWindow
from .gui.dialog_ui  import Ui_Dialog
from .src.mainwindow import MainWindow

#class DialogWidget(QDialog, Ui_Dialog):
#    def __init__(self):
#        super(DialogWidget, self).__init__()
#        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

