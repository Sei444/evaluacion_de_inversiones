import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit
import numpy as np
from ventanaesc1 import *
from programa import *
class  VentanaEscenario1(QtWidgets.QMainWindow,Ui_ventanaEsc1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boton_simular.clicked.connect(self.click_simular)
        self.boton_home.clicked.connect(self.volver_home)

    def click_simular(self):
        media_flujo = int(self.media_flujo.text())
        desviacionE_flujo = int(self.desviacionE_flujo.text())
        media_inv = int(self.media_inv.text())
        desviacionE_inv = int(self.desviacionE_inv.text())
        print("la media es : " , media_flujo , desviacionE_flujo , media_inv ,desviacionE_inv)
        
        main = Inversion(media_flujo,desviacionE_flujo,media_inv,desviacionE_inv)
        print(main.calcular_tir())

    def volver_home(self):
       #self.ventana_principal = QMainWindow()
       #self.uiPrincipal = Ui_MainWindow()
       #self.uiPrincipal.setupUi(self.ventana_principal)
       self.close()
       self.atras = VentanaPrincipal()
       self.atras.show()
    

    
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
class Inversion():

    def __init__(self,media_flujo,desviacionE_flujo,media_inv,desviacionE_inv):
        self.tir = 0
        self.media_flujo =media_flujo
        self.desviacionE_flujo = desviacionE_flujo
        self.media_inv = media_inv
        self.desviacionE_inv = desviacionE_inv
        print("media flujo es:" , self.media_flujo, self.desviacionE_flujo)
    def calcular_tir(self):
        objt_inv= Normal(self.media_inv,self.desviacionE_inv,1)
        objt_flujos = Normal(self.media_flujo,self.desviacionE_flujo,5)
        inversion =objt_inv.generar_resultado()
        flujos_netos = objt_flujos.generar_resultado()
        print(inversion)
        print(flujos_netos)
        tir = np.irr(np.insert(flujos_netos,0,-inversion))
        return tir
    

if __name__ == "__main__":
    app= QtWidgets.QApplication([])
    ventana_esc1= VentanaEscenario1()
    ventana_esc1.show()
    app.exec_()