# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/afar/Modifing_Packets_On-The-Fly_In_SCAPY/evilpostman/gui/dialog_filters.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DailogFilter(object):
    def setupUi(self, DailogFilter):
        DailogFilter.setObjectName("DailogFilter")
        DailogFilter.resize(400, 500)
        DailogFilter.setMaximumSize(QtCore.QSize(400, 600))
        self.main_dialog_vertical_layout = QtWidgets.QVBoxLayout(DailogFilter)
        self.main_dialog_vertical_layout.setObjectName("main_dialog_vertical_layout")
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setObjectName("vertical_layout")
        self.title_label = QtWidgets.QLabel(DailogFilter)
        self.title_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.title_label.setObjectName("title_label")
        self.vertical_layout.addWidget(self.title_label)
        self.name_line_edit = QtWidgets.QLineEdit(DailogFilter)
        self.name_line_edit.setObjectName("name_line_edit")
        self.vertical_layout.addWidget(self.name_line_edit)
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontal_layout.setSpacing(6)
        self.horizontal_layout.setObjectName("horizontal_layout")
        self.protocol_combo_box = QtWidgets.QComboBox(DailogFilter)
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
        self.add_push_button = QtWidgets.QPushButton(DailogFilter)
        self.add_push_button.setMaximumSize(QtCore.QSize(100, 38))
        self.add_push_button.setObjectName("add_push_button")
        self.horizontal_layout.addWidget(self.add_push_button)
        self.vertical_layout.addLayout(self.horizontal_layout)
        self.main_dialog_vertical_layout.addLayout(self.vertical_layout)
        self.tab_widget = QtWidgets.QTabWidget(DailogFilter)
        self.tab_widget.setObjectName("tab_widget")
        self.main_dialog_vertical_layout.addWidget(self.tab_widget)
        self.dialog_buttons = QtWidgets.QDialogButtonBox(DailogFilter)
        self.dialog_buttons.setOrientation(QtCore.Qt.Horizontal)
        self.dialog_buttons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.dialog_buttons.setObjectName("dialog_buttons")
        self.main_dialog_vertical_layout.addWidget(self.dialog_buttons)

        self.retranslateUi(DailogFilter)
        self.protocol_combo_box.setCurrentIndex(-1)
        self.tab_widget.setCurrentIndex(-1)
        self.dialog_buttons.accepted.connect(DailogFilter.accept)
        self.dialog_buttons.rejected.connect(DailogFilter.reject)
        self.add_push_button.clicked.connect(DailogFilter.update)
        QtCore.QMetaObject.connectSlotsByName(DailogFilter)

    def retranslateUi(self, DailogFilter):
        _translate = QtCore.QCoreApplication.translate
        DailogFilter.setWindowTitle(_translate("DailogFilter", "Dialog"))
        self.title_label.setText(_translate("DailogFilter", "Tworzenie filtru"))
        self.name_line_edit.setText(_translate("DailogFilter", "Untitled_1"))
        self.name_line_edit.setPlaceholderText(_translate("DailogFilter", "Nazwa filtra"))
        self.add_push_button.setText(_translate("DailogFilter", "Add"))

