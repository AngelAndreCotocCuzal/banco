from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(947, 693)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_name = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_name.setGeometry(QtCore.QRect(282, 54, 137, 24))
        self.txt_name.setObjectName("txt_name")
        self.txt_dic = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_dic.setGeometry(QtCore.QRect(282, 94, 137, 24))
        self.txt_dic.setObjectName("txt_dic")
        self.txt_phone = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_phone.setGeometry(QtCore.QRect(282, 134, 137, 24))
        self.txt_phone.setObjectName("txt_phone")
        self.txt_dpi = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_dpi.setGeometry(QtCore.QRect(282, 174, 137, 24))
        self.txt_dpi.setObjectName("txt_dpi")
        self.eleccion = QtWidgets.QComboBox(self.centralwidget)
        self.eleccion.setGeometry(QtCore.QRect(662, 105, 128, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.eleccion.setFont(font)
        self.eleccion.setObjectName("eleccion")
        self.eleccion.addItem("")
        self.eleccion.addItem("")
        self.eleccion.addItem("")
        self.eleccion.addItem("")
        self.eleccion.addItem("")
        self.txt_nit = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_nit.setGeometry(QtCore.QRect(662, 64, 137, 24))
        self.txt_nit.setObjectName("txt_nit")
        self.txt_ref = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_ref.setGeometry(QtCore.QRect(662, 144, 137, 24))
        self.txt_ref.setObjectName("txt_ref")
        self.lbl_name = QtWidgets.QLabel(self.centralwidget)
        self.lbl_name.setGeometry(QtCore.QRect(120, 50, 119, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_name.setFont(font)
        self.lbl_name.setObjectName("lbl_name")
        self.lbl_dic = QtWidgets.QLabel(self.centralwidget)
        self.lbl_dic.setGeometry(QtCore.QRect(120, 90, 136, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_dic.setFont(font)
        self.lbl_dic.setObjectName("lbl_dic")
        self.lbl_phone = QtWidgets.QLabel(self.centralwidget)
        self.lbl_phone.setGeometry(QtCore.QRect(120, 130, 128, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_phone.setFont(font)
        self.lbl_phone.setObjectName("lbl_phone")
        self.lbl_dpi = QtWidgets.QLabel(self.centralwidget)
        self.lbl_dpi.setGeometry(QtCore.QRect(120, 170, 55, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_dpi.setFont(font)
        self.lbl_dpi.setObjectName("lbl_dpi")
        self.lbl_nit = QtWidgets.QLabel(self.centralwidget)
        self.lbl_nit.setGeometry(QtCore.QRect(500, 60, 50, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_nit.setFont(font)
        self.lbl_nit.setObjectName("lbl_nit")
        self.lbl_archivos = QtWidgets.QLabel(self.centralwidget)
        self.lbl_archivos.setGeometry(QtCore.QRect(500, 100, 126, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_archivos.setFont(font)
        self.lbl_archivos.setObjectName("lbl_archivos")
        self.lbl_ref = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ref.setGeometry(QtCore.QRect(500, 140, 155, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_ref.setFont(font)
        self.lbl_ref.setObjectName("lbl_ref")
        self.btn_crear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_crear.setGeometry(QtCore.QRect(310, 230, 151, 51))
        self.btn_crear.setObjectName("btn_crear")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(160, 320, 621, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.btn_editar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_editar.setGeometry(QtCore.QRect(470, 230, 151, 51))
        self.btn_editar.setObjectName("btn_editar")
        self.btn_actua = QtWidgets.QPushButton(self.centralwidget)
        self.btn_actua.setGeometry(QtCore.QRect(150, 230, 151, 51))
        self.btn_actua.setObjectName("btn_actua")
        self.btn_crear_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_crear_4.setGeometry(QtCore.QRect(630, 230, 151, 51))
        self.btn_crear_4.setObjectName("btn_crear_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_crear.clicked.connect(self.guardar)
        self.btn_actua.clicked.connect(self.actualizar)
        self.btn_crear_4.clicked.connect(self.eliminar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.txt_name.setPlaceholderText(_translate("MainWindow", "Nombre"))
        self.txt_dic.setPlaceholderText(_translate("MainWindow", "Dirección"))
        self.txt_phone.setPlaceholderText(_translate("MainWindow", "Telefono"))
        self.txt_dpi.setPlaceholderText(_translate("MainWindow", "Dpi"))
        self.eleccion.setItemText(0, _translate("MainWindow", "Luz"))
        self.eleccion.setItemText(1, _translate("MainWindow", "Agua"))
        self.eleccion.setItemText(2, _translate("MainWindow", "Internet"))
        self.eleccion.setItemText(3, _translate("MainWindow", "Telefono"))
        self.eleccion.setItemText(4, _translate("MainWindow", "Estado de cuenta"))
        self.txt_nit.setPlaceholderText(_translate("MainWindow", "Nit"))
        self.txt_ref.setPlaceholderText(_translate("MainWindow", "Referencia"))
        self.lbl_name.setText(_translate("MainWindow", "Nombre:"))
        self.lbl_dic.setText(_translate("MainWindow", "Dirección:"))
        self.lbl_phone.setText(_translate("MainWindow", "Telefono:"))
        self.lbl_dpi.setText(_translate("MainWindow", "Dpi:"))
        self.lbl_nit.setText(_translate("MainWindow", "Nit:"))
        self.lbl_archivos.setText(_translate("MainWindow", "Archivos:"))
        self.lbl_ref.setText(_translate("MainWindow", "Referencia:"))
        self.btn_crear.setText(_translate("MainWindow", "Crear"))
        self.btn_editar.setText(_translate("MainWindow", "Editar"))
        self.btn_actua.setText(_translate("MainWindow", "Actualizar"))
        self.btn_crear_4.setText(_translate("MainWindow", "Eliminar"))

    def guardar(self):
        df = pd.read_csv('registros.csv')

        n = self.txt_name.text()  # ----- Nombre
        d = self.txt_dic.text()  # ----- dirección
        t = self.txt_phone.text()  # ----- Telefono
        dpi = self.txt_dpi.text()  # ----- Numero de Dpi
        nit = self.txt_nit.text()  # ----- Numero de Nit
        ar = self.eleccion.currentText()  # ----- Archivos adjuntos
        ref = self.txt_ref.text()  # ----- Referencias personales

        registro = [(n, d, t, dpi, nit, ar, ref)]
        df1 = pd.DataFrame(registro, columns=[
            'Nombre', 'Direccion', 'Telefono', 'Dpi', 'Nit', 'Facturas', 'Referencias'])

        df = df.append(df1, ignore_index=True)

        eliminar_colum = [col for col in df.columns if 'Unnamed' in col]
        df.drop(eliminar_colum, axis='columns', inplace=True)

        df.to_csv('registros.csv')

        self.tableWidget.setColumnCount(len(df.columns))
        self.tableWidget.setRowCount(len(df))
        self.tableWidget.setHorizontalHeaderLabels(df.columns)

        for i in range(len(df)):
            for j in range(len(df.columns)):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(df.iat[i, j])))

    def actualizar(self):
        self.guardar()
        self.eliminar()

    def eliminar(self):
        df = pd.read_csv('registros.csv')
        filas = len(df.index)
        df.drop(df.index[[filas - 1]], inplace=True)
        df.to_csv('registros.csv')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
