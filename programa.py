from ventana_principal import *
from escenario_1.backendEsc1 import *
from escenario_2.backendEsc2 import *
class VentanaPrincipal(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boton_elegir1.clicked.connect(self.abrir_escenario1)
        self.boton_elegir2.clicked.connect(self.abrir_escenario2) 
    def abrir_escenario1(self):
       self.ventana_esc1 = VentanaEscenario1()
       self.ventana_esc1.show()
    def abrir_escenario2(self):
       self.ventana_esc2 = VentanaEscenario2()
       self.ventana_esc2.show()
if __name__ == "__main__":
    app= QtWidgets.QApplication([])
    ventana_p = VentanaPrincipal()
    ventana_p.show()
    app.exec_()