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
from escenario_2.backendConclusion import *
class  VentanaEscenario2(QtWidgets.QMainWindow, Ui_Escenario2 ):
    def __init__(self):
        super().__init__()
        #QAbstractTableModel.__init__(self)
        self.setupUi(self)
        self.pushButton_home.clicked.connect(self.volver_home)

        self.pushButton_simular.clicked.connect(self.click_simular)
        self.pushButton_coclusion.clicked.connect(self.click_conclusion)
        self.pushButton_vpn.clicked.connect(self.click_histrogramaVPN)
        self.pushButton_inv.clicked.connect(self.click_inversionInicial)
        self.pushButton_res.clicked.connect(self.click_valorRescate)
        self.pushButton_inf.clicked.connect(self.click_tasaInflacion)
        self.pushButton_neto.clicked.connect(self.click_flujoNeto)
        #self.pushButton_tabla.clicked.connect(self.click_tablaS)
        self.ventana_conclusion = VentanaConclusion()

        
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
        global corridas
        corridas = int(self.lineEdit_corridas.text())
        #flujo neto
        flujo1 = int(self.lineEdit_1_neto.text()) 
        flujo2 = int(self.lineEdit_2_neto.text()) 
        flujo3 = int(self.lineEdit_3_neto.text()) 
        flujo4 = int(self.lineEdit_4_neto.text()) 
        flujo5 = int(self.lineEdit_5_neto.text())
        #tasa de descuento
        global t_descuento
        t_descuento = int(self.lineEdit_tasadescuento.text())
    
        self.mostrar_popup()

        #llamada a las distribuciones triangulares
        global obj_inv
        obj_inv = Triangular(inv_min,inv_esp,inv_max)
        global obj_res
        obj_res = Triangular(res_min,res_esp,res_max)
        global obj_inf
        obj_inf = Triangular(inf_min,inf_esp,inf_max)
        #llamada a las distribucion uniforme
        global obj_flujos
        obj_flujos = Uniforme(flujo1,flujo2,flujo3,flujo4,flujo5)

        global main 
        main = Inversion()
        main.evaluar()
    
    def mostrar_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Mensaje")
        msg.setText("Se cargaron los datos correctamente")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()
    """def click_histrogramaVPN(self):
        main.graficar_histrogramaTIR()"""
    def click_histrogramaVPN(self):
        main.graficar_histrogramaVPN()
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
    def click_conclusion(self):
        
        self.ventana_conclusion.exec_()

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
        print('inflacion :')
        inflacion = 100 - (np.around(np.random.triangular(100 - self.minimo, 100 - self.esperado, 100 - self.maximo, 1), 0)) #Meter datos Estimacion pesimista - probable - optimista
        #inflacion = inflacion.astype(int)
        print(inflacion)
        return inflacion
    def grafica_distTriangular(self):
        x = np.array([self.minimo, self.esperado ,self.maximo])
        y = np.array([0, 2/(self.maximo - self.minimo) ,0])
        plt.triplot(x,y)
        plt.show()
        print("mostrar grafica distri")
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
        indices = np.random.uniform(0,1,5) * 5
        indices = indices.astype(int)
        print(indices)
        #FLUJO
        flujo = [self.flujo1, self.flujo2, self.flujo3, self.flujo4, self.flujo5] #Meter los valores que tendra nuestro flujo
        #NUEVO FLUJO SEGUN INDICES (ARREGLO NUEVO)
        flujoNuevo = np.take(flujo,(indices))
        return flujoNuevo
    def grafica_distUniforme(self):
        #datos

        flujo_data = dataCorridas.iloc[:,[1,2,3,4,5,8]]
        print(flujo_data['valor_de_rescate'])
        array = np.concatenate( (flujo_data['año_1'].to_numpy(), flujo_data['año_2'].to_numpy(), flujo_data['año_3'].to_numpy(), flujo_data['año_4'].to_numpy(), (flujo_data['año_5'].to_numpy()-flujo_data['valor_de_rescate'].to_numpy())), axis = None)
        print("el array tir es: ",array)

        #grafico con solucion 1
        plt.hist(array, bins = 5, orientation='vertical')
        plt.title('Histograma Flujo Neto')
        plt.xlabel('valores del Flujo Neto')
        plt.ylabel('Total repeticiones')
        plt.show()
class Inversion():

    def __init__(self):
        pass
       # print("media flujo es:" , self.media_flujo, self.desviacionE_flujo)
        #self.figure = plt.figure(figsize=(10,5))
       # self.canvas = FigureCanvas(self.figure)
    def evaluar(self):
        print('EVALUAR')
        global dataCorridas 
        dataCorridas = self.construir_dataFrame()
    #Que tendria que calcular?
    def calcular_VPN(self, descuento, arregloFinal):
        return np.npv(descuento,arregloFinal)
    def arreglo(self):
        inv = obj_inv.generar_resultado()
        print(inv)
        flujo = obj_flujos.generar_resultado()
        print(flujo)
        rescate = obj_res.generar_resultado()
        print(rescate)
        inflacion = obj_inf.generar_resInf()/100
        print(inflacion)
        descuento = np.around(t_descuento/100 + inflacion+(t_descuento/100 * inflacion), 8)
        print(descuento)
        flujo[4] = np.take(flujo,4) + rescate
        arregloFinal = np.concatenate((inv,flujo),axis=0)
        print(arregloFinal)
        vpn =  self.calcular_VPN(descuento,arregloFinal)
        print(vpn)
        res = np.concatenate((arregloFinal, vpn, inflacion, rescate, descuento), axis = None)
        print(res)
        return res    
    def construir_dataFrame(self):
        print('Hola construir dataframe')
        #Corridas
        #corridas construye un dataframe de tamaño n difinido por --> range(n)
        data = pd.DataFrame(columns=  ['inv_ini', 'año_1', 'año_2', 'año_3', 'año_4', 'año_5', 'VPN', 'inflacion', 'valor_de_rescate', 'tasa_de_descuento'], index = range(corridas))
        for i in data.index :
            data.iloc[i] = self.arreglo()
            print(data.iloc[i])
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
        vpn_data = dataCorridas['VPN']
        np_vpn_data = vpn_data.to_numpy()
        print(np_vpn_data)
        plt.hist(np_vpn_data, bins = 20, orientation='vertical')
        plt.title('Histograma VPN')
        plt.xlabel('valores del VPN')
        plt.ylabel('Total repeticiones')
        plt.show()
     

       
if __name__ == "__main__":

    app= QtWidgets.QApplication([])
    ventana_esc2 = VentanaEscenario2()
    ventana_esc2.show()
    
    app.exec_()