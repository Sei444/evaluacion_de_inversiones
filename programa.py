from ventana_principal import *
from ventanaesc1 import *
from backendEsc1 import *
class VentanaPrincipal(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boton_elegir1.clicked.connect(self.abrir_escenario1)
       
    def abrir_escenario1(self):
       self.ventana_esc1 = VentanaEscenario1()
       self.ventana_esc1.show()
      
    def Escenario2(self):
        pass

if __name__ == "__main__":
    app= QtWidgets.QApplication([])
    ventana_p = VentanaPrincipal()
    ventana_p.show()
    app.exec_()