# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\user\Desktop\plugincatastro\crear_capas\crear_capas_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreadorCapasDialogBase(object):
    def setupUi(self, CreadorCapasDialogBase):
        CreadorCapasDialogBase.setObjectName("CreadorCapasDialogBase")
        CreadorCapasDialogBase.resize(506, 214)
        self.label = QtWidgets.QLabel(CreadorCapasDialogBase)
        self.label.setGeometry(QtCore.QRect(20, 40, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.procesarsncp = QtWidgets.QPushButton(CreadorCapasDialogBase)
        self.procesarsncp.setGeometry(QtCore.QRect(170, 150, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans ExtraBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.procesarsncp.setFont(font)
        self.procesarsncp.setObjectName("procesarsncp")
        self.carpeta = QtWidgets.QLineEdit(CreadorCapasDialogBase)
        self.carpeta.setGeometry(QtCore.QRect(180, 40, 261, 31))
        self.carpeta.setAutoFillBackground(False)
        self.carpeta.setObjectName("carpeta")
        self.buscar = QtWidgets.QPushButton(CreadorCapasDialogBase)
        self.buscar.setGeometry(QtCore.QRect(450, 40, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.buscar.setFont(font)
        self.buscar.setObjectName("buscar")
        self.label_2 = QtWidgets.QLabel(CreadorCapasDialogBase)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(CreadorCapasDialogBase)
        self.comboBox.setGeometry(QtCore.QRect(180, 91, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(CreadorCapasDialogBase)
        QtCore.QMetaObject.connectSlotsByName(CreadorCapasDialogBase)

    def retranslateUi(self, CreadorCapasDialogBase):
        _translate = QtCore.QCoreApplication.translate
        CreadorCapasDialogBase.setWindowTitle(_translate("CreadorCapasDialogBase", "Creador de Capas SNCP"))
        self.label.setText(_translate("CreadorCapasDialogBase", "INGRESE FOLDER : "))
        self.procesarsncp.setText(_translate("CreadorCapasDialogBase", "Crear Capas"))
        self.carpeta.setText(_translate("CreadorCapasDialogBase", "Buscar Folder para Base de Datos GPKG"))
        self.buscar.setText(_translate("CreadorCapasDialogBase", "..."))
        self.label_2.setText(_translate("CreadorCapasDialogBase", "PROYECCION :"))
