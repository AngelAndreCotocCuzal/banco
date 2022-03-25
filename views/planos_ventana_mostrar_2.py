from PyQt5 import QtCore, QtGui, QtWidgets
from imagenes import imagenes


class Ui_Form_planos(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(773, 597)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 751, 541))
        self.label.setStyleSheet("image: url(:/imagenes/planes_fin.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(530, 410, 55, 16))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(450, 530, 251, 21))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\""
                                                " color:#ffffff;\">Cochito Seguro:Angel, Abdo, Gerardo</span></p></body></html>"))

