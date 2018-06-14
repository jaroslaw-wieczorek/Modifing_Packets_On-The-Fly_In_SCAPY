# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/afar/Modifing_Packets_On-The-Fly_In_SCAPY/evilpostman/gui/dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(605, 256)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 70, 312, 88))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontal_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout.setObjectName("horizontal_layout")
        self.field_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.field_label.setObjectName("field_label")
        self.horizontal_layout.addWidget(self.field_label)
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setObjectName("vertical_layout")
        self.field_box_use_filter = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.field_box_use_filter.setObjectName("field_box_use_filter")
        self.vertical_layout.addWidget(self.field_box_use_filter)
        self.field_line_edit_filter = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.field_line_edit_filter.setObjectName("field_line_edit_filter")
        self.vertical_layout.addWidget(self.field_line_edit_filter)
        self.horizontal_layout.addLayout(self.vertical_layout)
        self.vertical_layout_2 = QtWidgets.QVBoxLayout()
        self.vertical_layout_2.setObjectName("vertical_layout_2")
        self.field_box_use_filter_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.field_box_use_filter_2.setObjectName("field_box_use_filter_2")
        self.vertical_layout_2.addWidget(self.field_box_use_filter_2)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.vertical_layout_2.addWidget(self.lineEdit)
        self.horizontal_layout.addLayout(self.vertical_layout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.field_label.setText(_translate("Dialog", "POLE:"))
        self.field_box_use_filter.setText(_translate("Dialog", "Zastosuj filtr"))
        self.field_box_use_filter_2.setText(_translate("Dialog", "Zastąp wartością"))

