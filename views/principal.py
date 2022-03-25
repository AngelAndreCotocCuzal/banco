from PyQt5 import QtCore, QtGui, QtWidgets, uic
from imagenes import imagenes
from crear import Ui_Crear_Window
from prestamo_bancarios_ventana import Ui_MainWindow_prestamo


class Ui_MainWindow_principal(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 880)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, -60, 1091, 871))
        self.label.setStyleSheet("image: url(:/imagenes/fondo_proyecto.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.btn_cerrar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cerrar.setGeometry(QtCore.QRect(1030, 50, 31, 31))
        self.btn_cerrar.setStyleSheet("image: url(:/imagenes/cerrar.png);")
        self.btn_cerrar.setText("")
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 100, 441, 111))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btn_gestion = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gestion.setGeometry(QtCore.QRect(440, 230, 201, 81))
        self.btn_gestion.setObjectName("btn_gestion")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 400, 201, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 690, 641, 41))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btn_cerrar.clicked.connect(self.cerrar)
        self.btn_gestion.clicked.connect(self.abrir)
        self.pushButton_2.clicked.connect(self.abrir1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; "
                                                      "color:#ffffff;\">Que desea organizar</span></p></body></html>"))
        self.btn_gestion.setText(_translate("MainWindow", "Gestion de asociado"))
        self.pushButton_2.setText(_translate("MainWindow", "Prestamos bancarios"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" "
                                                      "font-size:10pt; color:#ffffff;\">Derechos a los estudiantes: "
                                                      "Gerardo, Diego, Angel</span></p></body></html>"))

    def abrir(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_Crear_Window()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def abrir1(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_prestamo()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def cerrar(self):
        sys.exit(0)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_principal()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
