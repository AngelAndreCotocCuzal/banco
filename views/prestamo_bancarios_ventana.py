from PyQt5 import QtCore, QtGui, QtWidgets
from solicitar_ventana import Ui_Form_solicitar
from aprobar_ventana import Ui_Form
# from planos_ventana import Ui_Form_planos
from planos_ventana_mostrar_2 import Ui_Form_planos
from fondo_imagen import Ui_Form_imagen
from fondo_imagen_1 import Ui_Form_img
from solicitar_final import Ui_Form_aprobar_fin
from planes_imagen_2 import Ui_Form_imagen
from imagenes import imagenes


class Ui_MainWindow_prestamo(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(978, 717)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-20, -40, 1021, 731))
        self.label.setStyleSheet("image: url(:/imagenes/fondo_proyecto.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 70, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btn_solicitar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_solicitar.setGeometry(QtCore.QRect(400, 210, 141, 61))
        self.btn_solicitar.setObjectName("btn_solicitar")
        self.btn_planes = QtWidgets.QPushButton(self.centralwidget)
        self.btn_planes.setGeometry(QtCore.QRect(400, 370, 131, 61))
        self.btn_planes.setObjectName("btn_planes")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btn_solicitar.clicked.connect(self.sol_view)
        self.btn_planes.clicked.connect(self.sol_planes)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; "
                                                      "color:#ffffff;\">Prestamos Bancarios</span></p></body></html>"))
        self.btn_solicitar.setText(_translate("MainWindow", "Solicitar"))
        self.btn_planes.setText(_translate("MainWindow", "Planes"))

    def sol_view(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_Form_aprobar_fin()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def sol_aprobar(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def sol_planes(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_Form_imagen()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

