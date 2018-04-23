import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

from .gui.mainwindow_ui import Ui_MainWindow
from .gui.dialog_ui  import Ui_Dialog

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


class DialogWidget(QDialog, Ui_Dialog):
    def __init__(self):
        super(DialogWidget, self).__init__()
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    dialog = DialogWidget()
    dialog.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

