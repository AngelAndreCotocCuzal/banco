from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint
from eliminar import Ui_Eliminar
from imagenes import imagenes
import pandas as pd
import sys


class Ui_Crear_Window(object):
    def setupUi(self, Crear_Window):
        Crear_Window.setObjectName("Crear_Window")
        Crear_Window.resize(947, 693)
        Crear_Window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Crear_Window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(Crear_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_name = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_name.setGeometry(QtCore.QRect(282, 54, 137, 24))
        self.txt_name.setLayoutDirection(QtCore.Qt.LeftToRight)
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-20, -140, 1031, 921))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("image: url(:/imagenes/fondo_proyecto.png);")
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.btn_cerrar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cerrar.setGeometry(QtCore.QRect(890, 20, 41, 31))
        self.btn_cerrar.setStyleSheet("image: url(:/imagenes/cerrar.png);")
        self.btn_cerrar.setText("")
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.label.raise_()
        self.txt_name.raise_()
        self.txt_dic.raise_()
        self.txt_phone.raise_()
        self.txt_dpi.raise_()
        self.eleccion.raise_()
        self.txt_nit.raise_()
        self.txt_ref.raise_()
        self.lbl_name.raise_()
        self.lbl_dic.raise_()
        self.lbl_phone.raise_()
        self.lbl_dpi.raise_()
        self.lbl_nit.raise_()
        self.lbl_archivos.raise_()
        self.lbl_ref.raise_()
        self.btn_crear.raise_()
        self.tableWidget.raise_()
        self.btn_editar.raise_()
        self.btn_actua.raise_()
        self.btn_crear_4.raise_()
        self.btn_cerrar.raise_()
        Crear_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Crear_Window)
        self.statusbar.setObjectName("statusbar")
        Crear_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Crear_Window)
        QtCore.QMetaObject.connectSlotsByName(Crear_Window)
        self.btn_crear.clicked.connect(self.guardar)
        self.btn_actua.clicked.connect(self.actualizar)
        self.btn_crear_4.clicked.connect(self.eliminar)
        self.btn_cerrar.clicked.connect(self.cerrar)
        self.btn_editar.clicked.connect(self.abrir)

    def retranslateUi(self, Crear_Window):
        _translate = QtCore.QCoreApplication.translate
        Crear_Window.setWindowTitle(_translate("Crear_Window", "MainWindow"))
        self.txt_name.setPlaceholderText(_translate("Crear_Window", "Nombre"))
        self.txt_dic.setPlaceholderText(_translate("Crear_Window", "Dirección"))
        self.txt_phone.setPlaceholderText(_translate("Crear_Window", "Telefono"))
        self.txt_dpi.setPlaceholderText(_translate("Crear_Window", "Dpi"))
        self.eleccion.setItemText(0, _translate("Crear_Window", "Luz"))
        self.eleccion.setItemText(1, _translate("Crear_Window", "Agua"))
        self.eleccion.setItemText(2, _translate("Crear_Window", "Internet"))
        self.eleccion.setItemText(3, _translate("Crear_Window", "Telefono"))
        self.eleccion.setItemText(4, _translate("Crear_Window", "Estado de cuenta"))
        self.txt_nit.setPlaceholderText(_translate("Crear_Window", "Nit"))
        self.txt_ref.setPlaceholderText(_translate("Crear_Window", "Referencia"))
        self.lbl_name.setText(_translate("Crear_Window", "<html><head/><body><p><span style=\" "
                                                         "color:#ffffff;\">Nombre:</span></p></body></html>"))
        self.lbl_dic.setText(_translate("Crear_Window", "<html><head/><body><p><span style=\" "
                                                        "color:#ffffff;\">Dirección:</span></p></body></html>"))
        self.lbl_phone.setText(_translate("Crear_Window", "<html><head/><body><p><span style=\" "
                                                          "color:#ffffff;\">Telefono:</span></p></body></html>"))
        self.lbl_dpi.setText(_translate("Crear_Window", "<html><head/><body><p><span style=\" "
                                                        "color:#ffffff;\">Dpi:</span></p></body></html>"))
        self.lbl_nit.setText(_translate("Crear_Window", "<html><head/><body><p><span style=\" "
                                                        "color:#ffffff;\">Nit:</span></p></body></html>"))
        self.lbl_archivos.setText(_translate("Crear_Window", "<html><head/><body><p><span style=\" "
                                                             "color:#ffffff;\">Archivos:</span></p></body></html>"))
        self.lbl_ref.setText(_translate("Crear_Window", "<html><head/><body><p><span style=\" "
                                                        "color:#ffffff;\">Referencia:</span></p></body></html>"))
        self.btn_crear.setText(_translate("Crear_Window", "Crear"))
        self.btn_editar.setText(_translate("Crear_Window", "Editar"))
        self.btn_actua.setText(_translate("Crear_Window", "Actualizar"))
        self.btn_crear_4.setText(_translate("Crear_Window", "Eliminar"))

    def guardar(self):
        df = pd.read_csv('asociados.csv')

        n1 = str(randint(0, 9))
        n2 = str(randint(0, 9))
        n3 = str(randint(0, 9))
        n4 = str(randint(0, 9))
        cod = n1 + n2 + n3 + n4  # ------- Codigo

        n = self.txt_name.text()  # ----- Nombre
        d = self.txt_dic.text()  # ----- dirección
        t = self.txt_phone.text()  # ----- Telefono
        dpi = self.txt_dpi.text()  # ----- Numero de Dpi
        nit = self.txt_nit.text()  # ----- Numero de Nit
        ar = self.eleccion.currentText()  # ----- Archivos adjuntos
        ref = self.txt_ref.text()  # ----- Referencias personales

        registro = [(cod, n, d, t, dpi, nit, ar, ref)]

        df1 = pd.DataFrame(registro, columns=[
            'Codigo', 'Nombre', 'Direccion', 'Telefono', 'Dpi', 'Nit', 'Facturas', 'Referencas'])

        df = df.append(df1, ignore_index=True)

        eliminar_colum = [col for col in df.columns if 'Unnamed' in col]
        df.drop(eliminar_colum, axis='columns', inplace=True)

        df.to_csv('asociados.csv')
        self.tableWidget.setColumnCount(len(df.columns))
        self.tableWidget.setRowCount(len(df))
        self.tableWidget.setHorizontalHeaderLabels(df.columns)

        for i in range(len(df)):
            for j in range(len(df.columns)):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(df.iat[i, j])))

    def actualizar(self):  # ---- Actualizar no funciona
        # ----- EL de eliminar no agarra el dato
        self.guardar()
        self.eliminar()

    def eliminar(self):
        df = pd.read_csv('registros.csv')
        filas = len(df.index)
        df.drop(df.index[[filas - 1]], inplace=True)
        df.to_csv('registros.csv')

    # def eliminar_celda(self):
    #    df = pd.read_csv('registros.csv')
    #    fila = self.txt_eliminar_celda.text()
    #    filas = len(df.index)
    #    df.drop(df.index[[filas - 1]], inplace=True)
    #    df.to_csv('registros.csv')

    def abrir(self):
        self.borrar = QtWidgets.QMainWindow()
        self.ui = Ui_Eliminar()
        self.ui.setupUi(self.borrar)
        self.borrar.show()

    def cerrar(self):
        sys.exit(0)

