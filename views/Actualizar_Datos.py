from PyQt5 import QtCore, QtGui, QtWidgets
from segunda import d

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(376, 547)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 831, 531))
        self.label_6.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.512, y1:0, x2:0.532, y2:1, stop:0.174129 rgba(17, 37, 232, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(80, 30, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.email_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.email_2.setGeometry(QtCore.QRect(40, 100, 291, 41))
        self.email_2.setText("")
        self.email_2.setAlignment(QtCore.Qt.AlignCenter)
        self.email_2.setObjectName("email_2")
        self.New_Password = QtWidgets.QLineEdit(self.centralwidget)
        self.New_Password.setGeometry(QtCore.QRect(40, 180, 291, 41))
        self.New_Password.setText("")
        self.New_Password.setAlignment(QtCore.Qt.AlignCenter)
        self.New_Password.setObjectName("New_Password")
        self.cambiar_nombre = QtWidgets.QLineEdit(self.centralwidget)
        self.cambiar_nombre.setGeometry(QtCore.QRect(40, 240, 291, 41))
        self.cambiar_nombre.setText("")
        self.cambiar_nombre.setAlignment(QtCore.Qt.AlignCenter)
        self.cambiar_nombre.setObjectName("Cambiar_Nombre")
        self.Create_Account_Button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Create_Account_Button_3.setGeometry(QtCore.QRect(70, 320, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Create_Account_Button_3.setFont(font)
        self.Create_Account_Button_3.setStyleSheet("background-color: rgb(69, 87, 255);\n"
"color: rgb(255, 255, 255);")
        self.Create_Account_Button_3.setObjectName("Create_Account_Button_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.Create_Account_Button_3.clicked.connect(self.cambiar_nombre)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "Actualizar Datos"))
        self.email_2.setPlaceholderText(_translate("MainWindow", "Correo Electronico"))
        self.New_Password.setPlaceholderText(_translate("MainWindow", "New Password"))
        self.cambiar_nombre.setPlaceholderText(_translate("MainWindow", "Cambiar Nombre"))
        self.Create_Account_Button_3.setText(_translate("MainWindow", "Actualizar Datos"))

    def Cambiar_Nombre(self):
        self.correo = self.email_2.text()
        self.contrasena = self.New_Password.text()
        self.nombre = self.cambiar_nombre.text()

        d.cambiar_nombre(self.correo, self.nombre)
        d.cambiar_password(self.correo, self.contrasena)



