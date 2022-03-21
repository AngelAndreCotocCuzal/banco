from PyQt5 import QtCore, QtGui, QtWidgets
from imagenes import imagenes


class Ui_Eliminar(object):
    def setupUi(self, Eliminar):
        Eliminar.setObjectName("Eliminar")
        Eliminar.resize(421, 319)
        Eliminar.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Eliminar.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label = QtWidgets.QLabel(Eliminar)
        self.label.setGeometry(QtCore.QRect(370, 30, 41, 31))
        self.label.setStyleSheet("image: url(:/imagenes/cerrar.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Eliminar)
        self.label_2.setGeometry(QtCore.QRect(-130, 0, 671, 321))
        self.label_2.setStyleSheet("image: url(:/imagenes/fondo_proyecto.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Eliminar)
        self.label_3.setGeometry(QtCore.QRect(60, 80, 331, 61))
        self.label_3.setObjectName("label_3")
        self.lnx_celda = QtWidgets.QLineEdit(Eliminar)
        self.lnx_celda.setGeometry(QtCore.QRect(130, 150, 113, 41))
        self.lnx_celda.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lnx_celda.setObjectName("lnx_celda")
        self.btn_eliminar = QtWidgets.QPushButton(Eliminar)
        self.btn_eliminar.setGeometry(QtCore.QRect(140, 230, 93, 28))
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.lnx_celda.raise_()
        self.btn_eliminar.raise_()

        self.retranslateUi(Eliminar)
        QtCore.QMetaObject.connectSlotsByName(Eliminar)
        self.btn_eliminar.clicked.connect(self.eliminar_mandando)

    def retranslateUi(self, Eliminar):
        _translate = QtCore.QCoreApplication.translate
        Eliminar.setWindowTitle(_translate("Eliminar", "Form"))
        self.label_3.setText(_translate("Eliminar", "<html><head/><body><p><span style=\" "
                                                    "font-size:16pt; color:#ffffff;\">Que celda desea eliminar"
                                                    "</span></p><p><br/></p></body></html>"))
        self.lnx_celda.setPlaceholderText(_translate("Eliminar", "Numero"))
        self.btn_eliminar.setText(_translate("Eliminar", "Eliminar"))

    def eliminar_mandando(self):
        n = self.lnx_celda.text()
        return n

