from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from imagenes import imagenes
import json


class Ui_Form_solicitar(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(979, 657)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-60, -30, 1081, 691))
        self.label.setStyleSheet("image: url(:/imagenes/fondo_proyecto.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 90, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lnx_monto = QtWidgets.QLineEdit(Form)
        self.lnx_monto.setGeometry(QtCore.QRect(420, 90, 181, 41))
        self.lnx_monto.setObjectName("lnx_monto")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(100, 180, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lnx_cuotas = QtWidgets.QComboBox(Form)
        self.lnx_cuotas.setGeometry(QtCore.QRect(420, 170, 181, 41))
        self.lnx_cuotas.setObjectName("lnx_cuotas")
        self.lnx_cuotas.addItem("")
        self.lnx_cuotas.addItem("")
        self.lnx_cuotas.addItem("")
        self.lnx_cuotas.addItem("")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(100, 270, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lnx_ingresos = QtWidgets.QLineEdit(Form)
        self.lnx_ingresos.setGeometry(QtCore.QRect(420, 260, 181, 41))
        self.lnx_ingresos.setObjectName("lnx_ingresos")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(100, 350, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btn_archivos = QtWidgets.QPushButton(Form)
        self.btn_archivos.setGeometry(QtCore.QRect(420, 350, 181, 41))
        self.btn_archivos.setObjectName("btn_archivos")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(100, 420, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lnx_garantia = QtWidgets.QLineEdit(Form)
        self.lnx_garantia.setGeometry(QtCore.QRect(420, 430, 181, 41))
        self.lnx_garantia.setObjectName("lnx_garantia")
        self.btn_solicitar = QtWidgets.QPushButton(Form)
        self.btn_solicitar.setGeometry(QtCore.QRect(260, 500, 201, 61))
        self.btn_solicitar.setObjectName("btn_solicitar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.btn_solicitar.clicked.connect(self.guardar)
        self.btn_archivos.clicked.connect(self.pdf_abrir)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\""
                                                ">Monto solicitado: </span></p></body></html>"))
        self.lnx_monto.setPlaceholderText(_translate("Form", "Monto"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\""
                                                ">Numero de cuotas:</span></p><p><br/></p></body></html>"))
        self.lnx_cuotas.setItemText(0, _translate("Form", "3"))
        self.lnx_cuotas.setItemText(1, _translate("Form", "6"))
        self.lnx_cuotas.setItemText(2, _translate("Form", "12"))
        self.lnx_cuotas.setItemText(3, _translate("Form", "24"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\""
                                                ">Ingresos mensuales:</span></p><p><br/></p></body></html>"))
        self.lnx_ingresos.setPlaceholderText(_translate("Form", "Ingresos"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\""
                                                ">Archivos adjuntos:</span></p><p><br/></p></body></html>"))
        self.btn_archivos.setText(_translate("Form", "Ingrese pdf"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\""
                                                ">Garantias:</span></p></body></html>"))
        self.lnx_garantia.setPlaceholderText(_translate("Form", "Garantia"))
        self.btn_solicitar.setText(_translate("Form", "Solicitar Prestamo"))

    def guardar(self):
        self.monto = self.lnx_monto.text()
        self.cuotas = self.lnx_cuotas.currentText()
        self.ingresos = self.lnx_ingresos.text()
        self.archivos = None
        self.garantia = self.lnx_garantia.text()

    def pdf_abrir(self):
        path = QtWidgets.QFileDialog.getOpenFileName()[0]
        self.archivos.setText(path)
