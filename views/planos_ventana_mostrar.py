from PyQt5 import QtCore, QtGui, QtWidgets
from imagenes import imagenes


class Ui_Form_planos(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(773, 597)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 751, 541))
        self.label.setStyleSheet("image: url(:/prefijoNuevo/planes_fin.png);")
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
