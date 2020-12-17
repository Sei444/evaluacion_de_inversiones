import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit
import numpy as np
from backendEsc1 import *

class escenario1_interfaz(QMainWindow):
    media_flujo = 0
    desviacionE_flujo =0
    media_inv = 0
    desviacionE_inv =0
    def __init__(self):
        super().__init__()
        uic.loadUi("ventanaesc1.ui", self)
        self.boton_simular.clicked.connect(self.click_simular)

    def click_simular(self):
        media_flujo = int(self.media_flujo.text())
        desviacionE_flujo = int(self.desviacionE_flujo.text())
        media_inv = int(self.media_inv.text())
        desviacionE_inv = int(self.desviacionE_inv.text())
        print("la media es : " , media_flujo , desviacionE_flujo , media_inv ,desviacionE_inv)
      
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = escenario1_interfaz()
    GUI.show()
   
    sys.exit(app.exec_())
