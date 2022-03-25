from PyQt5 import QtCore, QtGui, QtWidgets
from imagenes import imagenes


class Ui_Form_imagen(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1662, 1458)
        Form.setStyleSheet("image: url(:/imagenes/planes_fin.png);")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

