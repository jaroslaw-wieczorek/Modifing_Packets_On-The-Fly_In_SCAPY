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
        DailogFilter.resize(464, 388)
        self.verticalLayout = QtWidgets.QVBoxLayout(DailogFilter)
        self.verticalLayout.setObjectName("verticalLayout")
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setObjectName("vertical_layout")
        self.label = QtWidgets.QLabel(DailogFilter)
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setObjectName("label")
        self.vertical_layout.addWidget(self.label)
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontal_layout.setSpacing(6)
        self.horizontal_layout.setObjectName("horizontal_layout")
        self.protocol_combo_box = QtWidgets.QComboBox(DailogFilter)
        self.protocol_combo_box.setMaximumSize(QtCore.QSize(16777215, 35))
        self.protocol_combo_box.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.protocol_combo_box.setMinimumContentsLength(2)
        self.protocol_combo_box.setObjectName("protocol_combo_box")
        self.protocol_combo_box.addItem("")
        self.protocol_combo_box.setItemText(0, "")
        self.horizontal_layout.addWidget(self.protocol_combo_box)
        self.add_push_button = QtWidgets.QPushButton(DailogFilter)
        self.add_push_button.setMaximumSize(QtCore.QSize(100, 38))
        self.add_push_button.setObjectName("add_push_button")
        self.horizontal_layout.addWidget(self.add_push_button)
        self.vertical_layout.addLayout(self.horizontal_layout)
        self.verticalLayout.addLayout(self.vertical_layout)
        self.vertical_layout_2 = QtWidgets.QVBoxLayout()
        self.vertical_layout_2.setObjectName("vertical_layout_2")
        self.verticalLayout.addLayout(self.vertical_layout_2)
        self.dialog_buttons = QtWidgets.QDialogButtonBox(DailogFilter)
        self.dialog_buttons.setOrientation(QtCore.Qt.Horizontal)
        self.dialog_buttons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.dialog_buttons.setObjectName("dialog_buttons")
        self.verticalLayout.addWidget(self.dialog_buttons)

        self.retranslateUi(DailogFilter)
        self.dialog_buttons.accepted.connect(DailogFilter.accept)
        self.dialog_buttons.rejected.connect(DailogFilter.reject)
        self.add_push_button.clicked.connect(DailogFilter.update)
        QtCore.QMetaObject.connectSlotsByName(DailogFilter)

    def retranslateUi(self, DailogFilter):
        _translate = QtCore.QCoreApplication.translate
        DailogFilter.setWindowTitle(_translate("DailogFilter", "Dialog"))
        self.label.setText(_translate("DailogFilter", "Tworzenie filtru"))
        self.add_push_button.setText(_translate("DailogFilter", "Add"))

