
import plotly.graph_objects as go
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit ,QTableView, QDialog, QMessageBox 
#from PyQt5.Qtcore import QAbstractTableModel , Qt
import matplotlib.pyplot as plt
from programa import *
from escenario_1.conclusion import *
from escenario_1.Reportes import *
from escenario_1.convertidor import *
from escenario_1.backendEsc1 import *
class  VentanaConclusion(QtWidgets.QDialog, Ui_Conclusion_esc1 ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_descargarReporte.clicked.connect(self.click_DescargarInformeFinal)
        self.pushButton_descargarGraficos.clicked.connect(self.click_graficos)
        self.pushButton_descargarTabla.clicked.connect(self.click_tabla)
        self.obj_reportes=Reportes()
        self.obj_convertidor=Convertidor()
        self.pushButton_atras.clicked.connect(self.atras)
        self.conclusion = ""
        
    def click_graficos(self): 
        self.obj_reportes.reporteGraficosDescarga()
        
    def click_tabla(self):
        self.obj_convertidor.tablaPdfDescarga()
        
    def click_DescargarInformeFinal(self):
        print("Entro al boton")
        self.obj_reportes.crearCaratula()
        self.obj_convertidor.tablaPdf()
        print('paso la tabla')
        self.obj_reportes.reporteGraficos(self.conclusion)
        print('paso graficos')
        self.obj_reportes.reporteFinal()
        
    
    def mostrar_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Mensaje")
        msg.setText("Se creo el reporte correctamente")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    def mostrar_conclusion(self, conclusion):
        self.conclusion = conclusion
        self.textBrowser.setText(conclusion)
    def pase_de_reportes(self,main,obj_inv,obj_flujosNetos):
        main.graficar_histrogramaTIR()
        plt.close()
        main.graficar_distAcumuladaTIR()
        plt.close()
        obj_flujosNetos.grafica_distnormal_Flujo()
        plt.close()
        obj_inv.grafica_distnormal_Inv()
        plt.close()
        print('imprime reporte final')
    def atras(self):
        self.close()


        
if __name__ == "__main__":

    app= QtWidgets.QApplication([])
    ventana_conclusion = VentanaConclusion()
    ventana_conclusion.show()
    
    app.exec_()