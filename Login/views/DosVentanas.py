import sys
from PyQt5 import uic, QtWidgets
from segunda import Ui_segunda

qtCreatorFile = "Login_view.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.ventana = QtWidgets.QMainWindow()
        self.setupUi(self)
        self.Create_Account_Button.clicked.connect(self.abrir)

    def abrir(self):
        self.ui= Ui_segunda()
        self.ui.setupUi(self.ventana)
        self.ventana.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
