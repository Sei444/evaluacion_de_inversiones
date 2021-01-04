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
from escenario_2.conclusion import *
from escenario_2.Reportes2 import *
from escenario_2.convertidor2 import *
class  VentanaConclusion(QtWidgets.QDialog, Ui_Conclusion ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
<<<<<<< HEAD
<<<<<<< HEAD:escenario_2/backendConclusion2.py
    def mostrar_conclusion(self, conclusion):
        self.textBrowser.setText(conclusion)
=======
=======
>>>>>>> 65b403460913a1536e09858e3e78c5960067409f
        self.pushButton_descargarReporte.clicked.connect(self.click_Descargar)
        self.obj_reportes=Reportes2()
        self.obj_convertidor=Convertidor2()
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
    
<<<<<<< HEAD

       
>>>>>>> 1cdcfd12d3b4946998000e98ddd301252f042a37:escenario_2/backendConclusion.py
=======
    
>>>>>>> 65b403460913a1536e09858e3e78c5960067409f
if __name__ == "__main__":

    app= QtWidgets.QApplication([])
    ventana_conclusion = VentanaConclusion()
    ventana_conclusion.show()
    
    app.exec_()