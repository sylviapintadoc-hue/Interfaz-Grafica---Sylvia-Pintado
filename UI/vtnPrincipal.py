# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QComboBox, QLabel, QLineEdit,
                               QMenuBar, QPushButton, QStatusBar, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(443, 709)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblNombre = QLabel(self.centralwidget)
        self.lblNombre.setObjectName(u"lblNombre")
        self.lblNombre.setGeometry(QRect(40, 30, 71, 31))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lblNombre.setFont(font)
        self.lblNombre.setMouseTracking(False)
        self.lblNombre.setTabletTracking(False)
        self.txtNombre = QLineEdit(self.centralwidget)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setGeometry(QRect(120, 30, 251, 31))
        self.lblApellido = QLabel(self.centralwidget)
        self.lblApellido.setObjectName(u"lblApellido")
        self.lblApellido.setGeometry(QRect(40, 80, 71, 31))
        self.lblApellido.setFont(font)
        self.txtApellido = QLineEdit(self.centralwidget)
        self.txtApellido.setObjectName(u"txtApellido")
        self.txtApellido.setGeometry(QRect(120, 80, 251, 31))
        self.txtEmail = QLineEdit(self.centralwidget)
        self.txtEmail.setObjectName(u"txtEmail")
        self.txtEmail.setGeometry(QRect(120, 180, 251, 31))
        self.txtCedula = QLineEdit(self.centralwidget)
        self.txtCedula.setObjectName(u"txtCedula")
        self.txtCedula.setGeometry(QRect(120, 130, 251, 31))
        self.lblCedula = QLabel(self.centralwidget)
        self.lblCedula.setObjectName(u"lblCedula")
        self.lblCedula.setGeometry(QRect(40, 130, 71, 31))
        self.lblCedula.setFont(font)
        self.lblEmail = QLabel(self.centralwidget)
        self.lblEmail.setObjectName(u"lblEmail")
        self.lblEmail.setGeometry(QRect(40, 180, 71, 31))
        self.lblEmail.setFont(font)
        self.lblSexo = QLabel(self.centralwidget)
        self.lblSexo.setObjectName(u"lblSexo")
        self.lblSexo.setGeometry(QRect(40, 230, 71, 31))
        self.lblSexo.setFont(font)
        self.cmbSexo = QComboBox(self.centralwidget)
        self.cmbSexo.addItem("")
        self.cmbSexo.addItem("")
        self.cmbSexo.addItem("")
        self.cmbSexo.addItem("")
        self.cmbSexo.setObjectName(u"cmbSexo")
        self.cmbSexo.setGeometry(QRect(120, 230, 161, 31))
        self.btnGuardar = QPushButton(self.centralwidget)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(120, 290, 81, 31))
        self.btnLimpiar = QPushButton(self.centralwidget)
        self.btnLimpiar.setObjectName(u"btnLimpiar")
        self.btnLimpiar.setGeometry(QRect(250, 290, 81, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 443, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblNombre.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.lblApellido.setText(QCoreApplication.translate("MainWindow", u"Apellido:", None))
        self.lblCedula.setText(QCoreApplication.translate("MainWindow", u"Cedula:", None))
        self.lblEmail.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.lblSexo.setText(QCoreApplication.translate("MainWindow", u"Sexo:", None))
        self.cmbSexo.setItemText(0, QCoreApplication.translate("MainWindow", u"Seleccionar ", None))
        self.cmbSexo.setItemText(1, QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.cmbSexo.setItemText(2, QCoreApplication.translate("MainWindow", u"Femenino", None))
        self.cmbSexo.setItemText(3, QCoreApplication.translate("MainWindow", u"Prefiero no decirlo", None))

        self.btnGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.btnLimpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
    # retranslateUi
