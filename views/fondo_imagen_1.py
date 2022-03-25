from PyQt5 import QtCore, QtGui, QtWidgets
from imagenes import imagenes


class Ui_Form_img(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(752, 517)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 50, 681, 371))
        self.label.setStyleSheet("image: url(:/imagenes/fondo_proyecto.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(220, 120, 301, 211))
        self.label_2.setStyleSheet("image: url(:/imagenes/planes_de_prestamo.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

