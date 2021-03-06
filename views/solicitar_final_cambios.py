from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1002, 864)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-60, -510, 1081, 1751))
        self.label.setStyleSheet("image: url(:/imagenes/fondo_proyecto.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lnx_monto = QtWidgets.QLineEdit(Form)
        self.lnx_monto.setGeometry(QtCore.QRect(280, 80, 171, 31))
        self.lnx_monto.setObjectName("lnx_monto")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lnx_cuotas = QtWidgets.QComboBox(Form)
        self.lnx_cuotas.setGeometry(QtCore.QRect(280, 140, 161, 31))
        self.lnx_cuotas.setObjectName("lnx_cuotas")
        self.lnx_cuotas.addItem("")
        self.lnx_cuotas.addItem("")
        self.lnx_cuotas.addItem("")
        self.lnx_cuotas.addItem("")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 200, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lnx_ingresos = QtWidgets.QLineEdit(Form)
        self.lnx_ingresos.setGeometry(QtCore.QRect(280, 200, 171, 31))
        self.lnx_ingresos.setObjectName("lnx_ingresos")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 270, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btn_archivos = QtWidgets.QPushButton(Form)
        self.btn_archivos.setGeometry(QtCore.QRect(280, 260, 171, 31))
        self.btn_archivos.setObjectName("btn_archivos")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 330, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lnx_garantia = QtWidgets.QLineEdit(Form)
        self.lnx_garantia.setGeometry(QtCore.QRect(280, 330, 171, 31))
        self.lnx_garantia.setObjectName("lnx_garantia")
        self.btn_solicitar = QtWidgets.QPushButton(Form)
        self.btn_solicitar.setGeometry(QtCore.QRect(80, 400, 181, 41))
        self.btn_solicitar.setObjectName("btn_solicitar")
        self.btn_aprobar = QtWidgets.QPushButton(Form)
        self.btn_aprobar.setGeometry(QtCore.QRect(610, 130, 161, 61))
        self.btn_aprobar.setObjectName("btn_aprobar")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(590, 60, 231, 61))
        self.label_7.setObjectName("label_7")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(490, 210, 471, 191))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tabla_visualizar = QtWidgets.QTableWidget(Form)
        self.tabla_visualizar.setGeometry(QtCore.QRect(270, 510, 651, 191))
        self.tabla_visualizar.setObjectName("tabla_visualizar")
        self.tabla_visualizar.setColumnCount(0)
        self.tabla_visualizar.setRowCount(0)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(320, 460, 531, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.btn_visualizar = QtWidgets.QPushButton(Form)
        self.btn_visualizar.setGeometry(QtCore.QRect(660, 460, 121, 41))
        self.btn_visualizar.setObjectName("btn_visualizar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Monto solicitado: </span></p></body></html>"))
        self.lnx_monto.setPlaceholderText(_translate("Form", "Monto"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Numero de cuotas:</span></p><p><br/></p></body></html>"))
        self.lnx_cuotas.setItemText(0, _translate("Form", "3"))
        self.lnx_cuotas.setItemText(1, _translate("Form", "6"))
        self.lnx_cuotas.setItemText(2, _translate("Form", "12"))
        self.lnx_cuotas.setItemText(3, _translate("Form", "24"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Ingresos mensuales:</span></p><p><br/></p></body></html>"))
        self.lnx_ingresos.setPlaceholderText(_translate("Form", "Ingresos"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Archivos adjuntos:</span></p><p><br/></p></body></html>"))
        self.btn_archivos.setText(_translate("Form", "Ingrese pdf"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Garantias:</span></p></body></html>"))
        self.lnx_garantia.setPlaceholderText(_translate("Form", "Garantia"))
        self.btn_solicitar.setText(_translate("Form", "Solicitar Prestamo"))
        self.btn_aprobar.setText(_translate("Form", "Aprobar"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Aprobar Prestamos</span></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Visualizar Prestamos</span></p></body></html>"))
        self.btn_visualizar.setText(_translate("Form", "Visualizar"))
import imagenes_rc
