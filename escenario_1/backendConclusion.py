import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import plotly.graph_objects as go
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit ,QTableView, QDialog, QMessageBox
#from PyQt5.Qtcore import QAbstractTableModel , Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from scipy.stats import norm
from programa import *
from escenario_1.conclusion import *
from escenario_1.Reportes import *
from escenario_1.convertidor import *

class  VentanaConclusion(QtWidgets.QDialog, Ui_Conclusion_esc1 ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_descargarReporte.clicked.connect(self.click_Descargar)
        self.obj_reportes=Reportes()
        self.obj_convertidor=Convertidor()
    
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

        

        
    

       
if __name__ == "__main__":

    app= QtWidgets.QApplication([])
    ventana_conclusion = VentanaConclusion()
    ventana_conclusion.show()
    
    app.exec_()