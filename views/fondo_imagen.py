from PyQt5 import QtCore, QtGui, QtWidgets
from imagenes import imagenes


class Ui_Form_imagen(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(752, 517)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 50, 681, 371))
        self.label.setStyleSheet("image: url(:/imagenes/planes_fin_yaaa.png);")
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

