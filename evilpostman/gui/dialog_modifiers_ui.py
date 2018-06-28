# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/afar/Modifing_Packets_On-The-Fly_In_SCAPY/evilpostman/gui/dialog_modifiers.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DailogModifiers(object):
    def setupUi(self, DailogModifiers):
        DailogModifiers.setObjectName("DailogModifiers")
        DailogModifiers.resize(400, 500)
        DailogModifiers.setMaximumSize(QtCore.QSize(400, 600))
        self.main_dialog_vertical_layout = QtWidgets.QVBoxLayout(DailogModifiers)
        self.main_dialog_vertical_layout.setObjectName("main_dialog_vertical_layout")
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setObjectName("vertical_layout")
        self.title_label = QtWidgets.QLabel(DailogModifiers)
        self.title_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.title_label.setObjectName("title_label")
        self.vertical_layout.addWidget(self.title_label)
        self.name_line_edit = QtWidgets.QLineEdit(DailogModifiers)
        self.name_line_edit.setObjectName("name_line_edit")
        self.vertical_layout.addWidget(self.name_line_edit)
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontal_layout.setSpacing(6)
        self.horizontal_layout.setObjectName("horizontal_layout")
        self.protocol_combo_box = QtWidgets.QComboBox(DailogModifiers)
        self.protocol_combo_box.setMaximumSize(QtCore.QSize(16777215, 35))
        self.protocol_combo_box.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.protocol_combo_box.setEditable(False)
        self.protocol_combo_box.setCurrentText("")
        self.protocol_combo_box.setMaxCount(100)
        self.protocol_combo_box.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.protocol_combo_box.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.protocol_combo_box.setMinimumContentsLength(2)
        self.protocol_combo_box.setFrame(True)
        self.protocol_combo_box.setModelColumn(0)
        self.protocol_combo_box.setObjectName("protocol_combo_box")
        self.protocol_combo_box.addItem("")
        self.protocol_combo_box.setItemText(0, "")
        self.horizontal_layout.addWidget(self.protocol_combo_box)
        self.add_push_button = QtWidgets.QPushButton(DailogModifiers)
        self.add_push_button.setMaximumSize(QtCore.QSize(100, 38))
        self.add_push_button.setObjectName("add_push_button")
        self.horizontal_layout.addWidget(self.add_push_button)
        self.vertical_layout.addLayout(self.horizontal_layout)
        self.main_dialog_vertical_layout.addLayout(self.vertical_layout)
        self.tab_widget = QtWidgets.QTabWidget(DailogModifiers)
        self.tab_widget.setObjectName("tab_widget")
        self.main_dialog_vertical_layout.addWidget(self.tab_widget)
        self.dialog_buttons = QtWidgets.QDialogButtonBox(DailogModifiers)
        self.dialog_buttons.setOrientation(QtCore.Qt.Horizontal)
        self.dialog_buttons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.dialog_buttons.setObjectName("dialog_buttons")
        self.main_dialog_vertical_layout.addWidget(self.dialog_buttons)

        self.retranslateUi(DailogModifiers)
        self.protocol_combo_box.setCurrentIndex(-1)
        self.tab_widget.setCurrentIndex(-1)
        self.dialog_buttons.accepted.connect(DailogModifiers.accept)
        self.dialog_buttons.rejected.connect(DailogModifiers.reject)
        self.add_push_button.clicked.connect(DailogModifiers.update)
        QtCore.QMetaObject.connectSlotsByName(DailogModifiers)

    def retranslateUi(self, DailogModifiers):
        _translate = QtCore.QCoreApplication.translate
        DailogModifiers.setWindowTitle(_translate("DailogModifiers", "Dialog"))
        self.title_label.setText(_translate("DailogModifiers", "Tworzenie modyfikatora"))
        self.name_line_edit.setText(_translate("DailogModifiers", "Untitled_1"))
        self.name_line_edit.setPlaceholderText(_translate("DailogModifiers", "Nazwa filtra"))
        self.add_push_button.setText(_translate("DailogModifiers", "Wybierz"))

