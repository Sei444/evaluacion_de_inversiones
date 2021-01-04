import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit ,QTableView, QDialog, QMessageBox
from programa import *
from escenario_2.conclusion import *
from escenario_2.Reportes import *
from escenario_2.convertidor import *
class  VentanaConclusion(QtWidgets.QDialog, Ui_Conclusion ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_descargarReporte.clicked.connect(self.click_Descargar)
        self.obj_reportes=Reportes()
        self.obj_convertidor=Convertidor()
        self.pushButton_atras.clicked.connect(self.atras)
    
    def click_Descargar(self):
        print("Entro al boton")
        self.obj_reportes.crearCaratula()
        self.obj_convertidor.tablaPdf()
        self.obj_reportes.reporteGraficos()
        self.obj_reportes.reporteFinal()
        self.mostrar_popup()
    def mostrar_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Mensaje")
        msg.setText("Se creo el reporte correctamente")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()
    def mostrar_conclusion(self, conclusion):
        self.textBrowser.setText(conclusion)
        
    def atras(self):
        
        self.close()

        
    

       
if __name__ == "__main__":

    app= QtWidgets.QApplication([])
    ventana_conclusion = VentanaConclusion()
    ventana_conclusion.show()
    
    app.exec_()