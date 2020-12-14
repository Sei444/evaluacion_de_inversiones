import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit
import numpy as np



class Inversion():

    def __init__(self):
        self.tir = 0
    def calcular_tir(self,media_inv):
        objt_inv= Normal(self.media_inv,5000,1)
        objt_flujos = Normal(30000,3000,5)
        inversion =objt_inv.generar_resultado()
        flujos_netos = objt_flujos.generar_resultado()
        print(inversion)
        print(flujos_netos)
        tir = np.irr(np.insert(flujos_netos,0,-inversion))
        return tir
    

class Distribucion:
    def __init__(self):
        self.res =0

class Normal(Distribucion):
    def __init__(self, media, desviacion_e,cantidad_valor):
        Distribucion.__init__(self)
        self.media = media
        self.desviacion_e = desviacion_e
        self.cantidad_valor = cantidad_valor

    def generar_resultado(self):
        res = np.random.normal(self.media, self.desviacion_e,self.cantidad_valor)
        return res
 

 #llamada al main

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
      
    main = Inversion()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = escenario1_interfaz()
    GUI.show()
   
    sys.exit(app.exec_())