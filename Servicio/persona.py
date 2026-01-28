from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox

from Dominio.persona import Persona
from vtnPrincipal import Ui_MainWindow



class PersonaServicio(QMainWindow):
    '''
    clase que genera la logica de los objetos personas
    '''

    def __init__(self):
        super(PersonaServicio, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
        self.ui.txtCedula.setValidator(QIntValidator())

        regex = QRegularExpression(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        email_validator = QRegularExpressionValidator(regex)
        self.ui.txtEmail.setValidator(email_validator)

    def guardar(self):
        nombre = self.ui.txtNombre.text()
        apellido = self.ui.txtApellido.text()
        cedula = self.ui.txtCedula.text()
        sexo = self.ui.cmbSexo.currentText()
        email = self.ui.txtEmail.text()

        if nombre == "":
            QMessageBox.warning(self, 'Advertencia', 'Debe ingresar el nombre')
        elif apellido == "":
            QMessageBox.warning(self, 'Advertencia', 'Debe ingresar el apellido')
        elif cedula == "":
            QMessageBox.warning(self, 'Advertencia', 'Debe ingresar la cédula')
        elif len(cedula) <10:
            QMessageBox.warning(self, 'Advertencia', 'Debe ingresar los 10 dígitos')
        elif email == "":
            QMessageBox.warning(self, 'Advertencia', 'Debe ingresar el email')
        elif not self.ui.txtEmail.hasAcceptableInput():
            QMessageBox.warning(self, 'Advertencia', 'El email ingresado no es válido')
        elif sexo == "Seleccionar":
            QMessageBox.warning(self, "advertencia", "Debe seleccionar")

        else:
            persona = Persona(nombre=nombre, apellido=apellido, cedula=cedula, email=email, sexo=sexo)
            print(persona)

            self.ui.statusbar.showMessage('Información guardada', 3000)

            self.ui.txtNombre.setText('')
            self.ui.txtApellido.setText('')
            self.ui.txtCedula.setText('')
            self.ui.txtEmail.setText('')
            self.ui.cmbSexo.setCurrentText("Seleccionar")

    def limpiar(self):
        nombre = self.ui.txtNombre.clear()
        apellido = self.ui.txtApellido.clear()
        cedula = self.ui.txtCedula.clear()
        email = self.ui.txtEmail.clear()
        sexo = self.ui.cmbSexo.setCurrentText("Seleccionar")