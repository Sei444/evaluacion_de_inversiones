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
class  VentanaConclusion(QtWidgets.QDialog, Ui_Conclusion_esc1 ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def mostrar_conclusion(self, conclusion):
        self.textBrowser.setText(conclusion)
        
if __name__ == "__main__":

    app= QtWidgets.QApplication([])
    ventana_conclusion = VentanaConclusion()
    ventana_conclusion.show()
    
    app.exec_()