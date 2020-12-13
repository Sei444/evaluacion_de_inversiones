import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class escenario1_interfaz(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("ventanaEsc1.ui", self)

    def fn_guardar(self):
        self.lineEdit.getText()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = escenario1_interfaz()
    GUI.show()
    sys.exit(app.exec_())