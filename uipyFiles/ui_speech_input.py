# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiFiles/SpeechInput.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SpeechInput(object):
    def setupUi(self, SpeechInput):
        SpeechInput.setObjectName("SpeechInput")
        SpeechInput.resize(495, 434)
        self.gridLayout_3 = QtWidgets.QGridLayout(SpeechInput)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_2.setContentsMargins(0, 0, 0, -1)
        self.formLayout_2.setHorizontalSpacing(0)
        self.formLayout_2.setVerticalSpacing(1)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_10 = QtWidgets.QLabel(SpeechInput)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.text_output = QtWidgets.QPlainTextEdit(SpeechInput)
        self.text_output.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.text_output.setFont(font)
        self.text_output.setPlainText("")
        self.text_output.setObjectName("text_output")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.text_output)
        self.btn_start = QtWidgets.QPushButton(SpeechInput)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_start.setFont(font)
        self.btn_start.setObjectName("btn_start")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.btn_start)
        self.eng_enabled = QtWidgets.QRadioButton(SpeechInput)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eng_enabled.setFont(font)
        self.eng_enabled.setObjectName("eng_enabled")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.eng_enabled)
        self.rus_enabled = QtWidgets.QRadioButton(SpeechInput)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rus_enabled.setFont(font)
        self.rus_enabled.setObjectName("rus_enabled")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.rus_enabled)
        self.gridLayout_3.addLayout(self.formLayout_2, 0, 0, 1, 1)

        self.retranslateUi(SpeechInput)
        QtCore.QMetaObject.connectSlotsByName(SpeechInput)

    def retranslateUi(self, SpeechInput):
        _translate = QtCore.QCoreApplication.translate
        SpeechInput.setWindowTitle(_translate("SpeechInput", "Form"))
        self.btn_start.setText(_translate("SpeechInput", "Record"))
        self.eng_enabled.setText(_translate("SpeechInput", "English"))
        self.rus_enabled.setText(_translate("SpeechInput", "Russian"))

