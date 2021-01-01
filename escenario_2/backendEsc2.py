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

from escenario_2.ventanaesc2 import *
from programa import *
class  VentanaEscenario2(QtWidgets.QMainWindow, Ui_Escenario2 ):
    def __init__(self):
        super().__init__()
        #QAbstractTableModel.__init__(self)
        self.setupUi(self)
        self.pushButton_home.clicked.connect(self.volver_home)

        self.pushButton_simular.clicked.connect(self.click_simular)
        """self.pushButton_conclusion.clicked.connect(self.click_conclusion)

        self.pushButton_vpn.clicked.connect(self.click_histrogramaVPN)
        """
        self.pushButton_inv.clicked.connect(self.click_inversionInicial)
        self.pushButton_res.clicked.connect(self.click_valorRescate)
        self.pushButton_inf.clicked.connect(self.click_tasaInflacion)
        self.pushButton_neto.clicked.connect(self.click_flujoNeto)
        #self.pushButton_tabla.clicked.connect(self.click_tablaS)

        
    def click_simular(self):
        #inversion inicial
        inv_min = int(self.lineEdit_min_inv.text())
        inv_esp = int(self.lineEdit_esp_inv.text())
        inv_max = int(self.lineEdit_max_inv.text())
        #Valor de rescate
        res_min = int(self.lineEdit_min_res.text())
        res_esp = int(self.lineEdit_esp_res.text())
        res_max = int(self.lineEdit_max_res.text())
        #Inflacion
        inf_min = int(self.lineEdit_min_inf.text())
        inf_esp = int(self.lineEdit_esp_inf.text())
        inf_max = int(self.lineEdit_max_inf.text())
        #corridas
        corridas = int(self.lineEdit_corridas.text())
        #flujo neto
        flujo1 = int(self.lineEdit_1_neto.text()) 
        flujo2 = int(self.lineEdit_2_neto.text()) 
        flujo3 = int(self.lineEdit_3_neto.text()) 
        flujo4 = int(self.lineEdit_4_neto.text()) 
        flujo5 = int(self.lineEdit_5_neto.text()) 
        print("obteniendo resultados  : " , inv_min ,inv_esp, inv_max , "\n" ,res_min,res_esp,res_max, "\n", "inflacion", inf_min,inf_esp, inf_max)
        print("flujos:" , flujo1,flujo2,flujo3,flujo4,flujo5, "corridas" , corridas)
        self.mostrar_popup()

        #global main 
        #main= Inversion(media_flujo,desviacionE_flujo,media_inv,desviacionE_inv,corridas)
        #llamada a las distribuciones triangulares
        global obj_inv
        obj_inv = Triangular(inv_min,inv_esp,inv_max)
        global obj_res
        obj_inv = Triangular(res_min,res_esp,res_max)
        global obj_inf
        obj_inv = Triangular(inf_min,inf_esp,inf_max)
        #llamada a las distribucion uniforme
        global obj_flujos
        obj_flujos = Uniforme(flujo1,flujo2,flujo3,flujo4,flujo5)
        #print(main.evaluar())
    
    def mostrar_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Mensaje")
        msg.setText("Se cargaron los datos correctamente")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()
    """def click_histrogramaVPN(self):
        main.graficar_histrogramaTIR()"""
    def click_inversionInicial(self):
       try:
            obj_inv.grafica_distTriangular()
       except NameError:
            msg = QMessageBox()
            msg.setWindowTitle("Mensaje")
            msg.setText("No existen datos simulados de inversion inicial")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()

    def click_valorRescate(self):
        try:
            obj_res.grafica_distTriangular()
        except NameError:
            msg = QMessageBox()
            msg.setWindowTitle("Mensaje")
            msg.setText("No existen datos simulados de valor de Rescate")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()
        
    def click_tasaInflacion(self):
        try:
            obj_inf.grafica_distTriangular()
        except NameError:
            msg = QMessageBox()
            msg.setWindowTitle("Mensaje")
            msg.setText("No existen datos simulados de la tasa de inflacion")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()
        
    def click_flujoNeto(self):
        try:
            obj_flujos.grafica_distUniforme()
        except NameError:
            msg = QMessageBox()
            msg.setWindowTitle("Mensaje")
            msg.setText("No existen datos simulados de la tasa de inflacion")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()
        
    """def click_tablaS(self):
        main.graficar_tablaSimulacion()"""
       
    def volver_home(self):
       #self.ventana_principal = QMainWindow()
       #self.uiPrincipal = Ui_MainWindow()
       #self.uiPrincipal.setupUi(self.ventana_principal)
       self.close()    

    
class Distribucion:
    def __init__(self):
        self.res =0
        
#Clase distribucion triangular
class Triangular(Distribucion):
    def __init__(self, minimo, esperado,maximo):
        Distribucion.__init__(self)
        self.minimo = minimo
        self.esperado = esperado
        self.maximo = maximo
    #resultado para inversion inicial y de rescate
    def generar_resultado(self):
        res = np.around(np.random.triangular(self.minimo, self.esperado, self.maximo, 1), 0) # Meter datos Estimacion pesimista - probable - optimista
        res = res.astype(int)
        return res
    #resultado para inflacion
    def generar_resInf(self):
        #INFLACION
        inflacion = 1 - np.around(np.random.triangular(1-minimo, 1-esperado, 1-maximo, 1), 3) #Meter datos Estimacion pesimista - probable - optimista
        #inflacion = inflacion.astype(int)
        descuento = np.around(0.25+inflacion+(0.25*inflacion), 3)
    def grafica_distTriangular(self):
        """normal = norm(self.media, self.desviacion_e)
        x = np.linspace(normal.ppf(0.01),
                        normal.ppf(0.99), 100)
        fp = normal.pdf(x) # Función de Probabilidad
        plt.plot(x, fp)
        plt.title('Distribución Triangular')
        plt.ylabel('probabilidad')
        plt.xlabel('valores')
        plt.show()"""
        print("mostrar grafica distri")
        pass
class Uniforme(Distribucion):
    def __init__(self, flujo1, flujo2,flujo3,flujo4,flujo5):
        Distribucion.__init__(self)
        self.flujo1 = flujo1
        self.flujo2 = flujo2
        self.flujo3 = flujo3
        self.flujo4 = flujo4
        self.flujo5 = flujo5
    def generar_resultado(self):
        #INDICES
        indices = np.around(np.random.uniform(0,4,5), 0) # Meter DEL - AL, y cuantos datos se desea generar
        indices = indices.astype(int) #Convierte los valores del arrreglo a enteros
        #FLUJO
        flujo = [self.flujo1, self.flujo2, self.flujo3, self.flujo4, self.flujo5] #Meter los valores que tendra nuestro flujo

        #NUEVO FLUJO SEGUN INDICES (ARREGLO NUEVO)
        flujoNuevo = np.take(flujo,indices)
    def grafica_distUniforme(self):
        pass
class Inversion():

    def __init__(self,media_flujo,desviacionE_flujo,media_inv,desviacionE_inv,corridas):
        self.tir = 0
        self.media_flujo =media_flujo
        self.desviacionE_flujo = desviacionE_flujo
        self.media_inv = media_inv
        self.desviacionE_inv = desviacionE_inv
        self.corridas = corridas
        self.data = pd.DataFrame()
       # print("media flujo es:" , self.media_flujo, self.desviacionE_flujo)
        #self.figure = plt.figure(figsize=(10,5))
       # self.canvas = FigureCanvas(self.figure)
    def evaluar(self):
        global dataCorridas 
        dataCorridas= self.construir_dataFrame()
    #Que tendria que calcular?
    def calcular_VPN(self):
        
        pass
    def construir_dataFrame(self):
        #Corridas
        #corridas construye un dataframe de tamaño n difinido por --> range(n)
        data = pd.DataFrame(columns=  ["inv_ini", 'año_1', 'año_2', 'año_3', 'año_4', 'año_5', 'VPN', 'inflacion'], index = range(self.corridas))
        for i in data.index :
            data.iloc[i] = arreglo()
        print(data)
        return data
    """def graficar_tablaSimulacion(self):
        
        tabla2 = tabla.to_numpy()
        print("Imprimiendo tabla")
        print(tabla)
        
        #primera opcion

        fig, ax =plt.subplots(1,1)
        column_labels=['inversión_inicial', 'ingresos_año1', 'ingresos_año2','ingresos_año3', 'ingresos_año4','ingresos_año5', 'TIR']
        ax.axis('tight')
        ax.axis('off')
        ax.table(cellText=tabla2,colLabels=column_labels,loc="center")
        plt.show()
        #segunda opcion
        fig = go.Figure(data=[go.Table(
            header=dict(values=list(tabla.columns),
                        fill_color='paleturquoise',
                        align='left'),
            cells=dict(values=[tabla.inversión_inicial, tabla.ingresos_año1, tabla.ingresos_año2, tabla.ingresos_año3, tabla.ingresos_año4, tabla.ingresos_año5, tabla.TIR],
                    fill_color='lavender',
                    align='left'))
        ])
        fig.show()
        """
  
    def graficar_histrogramaVPN(self):
      # HISTOGRAMA VPN , cambie el nombre corridas por datacorridas
        dataCorridas.sort_values(by=['VPN'], inplace=True) # ordenar en dataframe de menor a mayor segun el VPN
        vpn_data = dataCorridas['VPN']
        tabla2 = dataCorridas.to_numpy()
        array = vpn_data.to_numpy()
        print(array)
        fragmentos = np.around(np.linspace(array[0], array[-1], 21), 3 )
        bins = fragmentos.tolist()
        print(bins)
        plt.hist(array, bins = bins, orientation='vertical')
        plt.title('Histograma VPN')
        plt.xlabel('valores del VPN')
        plt.ylabel('Total repeticiones')
        plt.show()
     

       
if __name__ == "__main__":

    app= QtWidgets.QApplication([])
    ventana_esc2 = VentanaEscenario2()
    ventana_esc2.show()
    
    app.exec_()