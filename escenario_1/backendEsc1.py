import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import plotly.graph_objects as go
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit ,QTableView, QDialog
#from PyQt5.Qtcore import QAbstractTableModel , Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from scipy.stats import norm

from escenario_1.ventanaesc1 import *
from programa import *
class  VentanaEscenario1(QtWidgets.QMainWindow, Ui_ventanaEsc1, ):
    def __init__(self):
        super().__init__()
        #QAbstractTableModel.__init__(self)
        self.setupUi(self)
        self.boton_simular.clicked.connect(self.click_simular)
        self.boton_home.clicked.connect(self.volver_home)
        self.pushButton_histoTIR.clicked.connect(self.click_histrogramaTIR)
        self.pushButton_distAcuTIR.clicked.connect(self.click_distAcumTIR)
        self.pushButton_distNInvIni.clicked.connect(self.click_distNInvInicial)
        self.pushButton_distNFlujoNeto.clicked.connect(self.click_disNFlujos)
        self.pushButton_tablaS.clicked.connect(self.click_tablaS)
        
    def click_simular(self):
        media_flujo = int(self.media_flujo.text())
        desviacionE_flujo = int(self.desviacionE_flujo.text())
        media_inv = int(self.media_inv.text())
        desviacionE_inv = int(self.desviacionE_inv.text())
        corridas = int(self.lineEdit_Ncorridas.text())
        #años =int(self.lineEdit_anios.text()) 
        print("la media es : " , media_flujo , desviacionE_flujo , media_inv ,desviacionE_inv,corridas)
        
        global main 
        main= Inversion(media_flujo,desviacionE_flujo,media_inv,desviacionE_inv,corridas)
        global obj_inv
        obj_inv = Normal(media_inv,desviacionE_inv)
        global obj_flujosNetos
        obj_flujosNetos = Normal(media_flujo,desviacionE_flujo)
        print(main.evaluar())
        
    def click_histrogramaTIR(self):
        main.graficar_histrogramaTIR()
    def click_distAcumTIR(self):
        main.graficar_distAcumuladaTIR()
    def click_distNInvInicial(self):
        obj_inv.grafica_distnormal()
    def click_disNFlujos(self):
        obj_flujosNetos.grafica_distnormal()
    def click_tablaS(self):
        main.graficar_tablaSimulacion()
       
    def volver_home(self):
       #self.ventana_principal = QMainWindow()
       #self.uiPrincipal = Ui_MainWindow()
       #self.uiPrincipal.setupUi(self.ventana_principal)
       self.close()    

    
class Distribucion:
    def __init__(self):
        self.res =0
        

class Normal(Distribucion):
    def __init__(self, media, desviacion_e,cantidad_valor =0):
        Distribucion.__init__(self)
        self.media = media
        self.desviacion_e = desviacion_e
        self.cantidad_valor = cantidad_valor

    def generar_resultado(self):
        res = np.random.normal(self.media, self.desviacion_e,self.cantidad_valor)
        return res
    def grafica_distnormal(self):
        normal = norm(self.media, self.desviacion_e)
        x = np.linspace(normal.ppf(0.01),
                        normal.ppf(0.99), 100)
        fp = normal.pdf(x) # Función de Probabilidad
        plt.plot(x, fp)
        plt.title('Distribución Normal')
        plt.ylabel('probabilidad')
        plt.xlabel('valores')
        plt.show()
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
        global tabla 
        tabla= self.construir_dataFrame()
    def calcular_tir(self):
        objt_inv= Normal(self.media_inv,self.desviacionE_inv,1)
        objt_flujos = Normal(self.media_flujo,self.desviacionE_flujo,5)
        inversion =objt_inv.generar_resultado()
        flujos_netos = objt_flujos.generar_resultado()
        aux_tir = np.rint(np.insert(flujos_netos,0,-inversion))
        tir = round((np.irr(aux_tir)*100), 3)
        corrida = np.append(aux_tir, tir, axis=None)
        print("Calculo la tir")
        return corrida
    def construir_dataFrame(self):
        data = pd.DataFrame(columns=['inversión_inicial', 'ingresos_año1', 'ingresos_año2','ingresos_año3', 'ingresos_año4','ingresos_año5', 'TIR'], index=range(self.corridas))
        #row = Inversion()
        for i in data.index :
            data.iloc[i] = self.calcular_tir()
            print("funciona!!!")
        return data
    def graficar_tablaSimulacion(self):
        
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
        """fig = go.Figure(data=[go.Table(
            header=dict(values=list(tabla.columns),
                        fill_color='paleturquoise',
                        align='left'),
            cells=dict(values=[tabla.inversión_inicial, tabla.ingresos_año1, tabla.ingresos_año2, tabla.ingresos_año3, tabla.ingresos_año4, tabla.ingresos_año5, tabla.TIR],
                    fill_color='lavender',
                    align='left'))
        ])
        fig.show()
        """
  
    def graficar_histrogramaTIR(self):
        #datos
        tabla.sort_values(by=['TIR'], inplace=True)
        tir_data = tabla['TIR']
        array = tir_data.to_numpy()
        print("el array tir es: ",array)
        fragmentos = np.around(np.linspace(array[0], array[-1], 21), 3 )
        bins = fragmentos.tolist()
        print(bins)

        #grafico con solucion 1
        plt.hist(array, bins = bins, orientation='horizontal')
        plt.title('Histograma TIR')
        plt.xlabel('valores del TIR')
        plt.ylabel('Total repeticiones')
        plt.show()
        plt.show()
        #grafico con solucion 2
        """figure = Figure()
        scene = QtWidgets.QGraphicsScene()
        view = QtWidgets.QGraphicsView(scene)
        
        axes = figure.gca()
        axes.hist(array, bins = bins, orientation='horizontal')
        axes.set_title('Histograma TIR')
        #axes.xlabel('valores del TIR')
        #axes.ylabel('Total repeticiones')
        axes.grid(True)
        canvas = FigureCanvas(figure)
        proxy_widget = scene.addWidget(canvas)
        view.resize(640,480)
        view.show()
        """
    def graficar_distAcumuladaTIR(self):
        tabla.sort_values(by=['TIR'], inplace=True)
        tir_data = tabla['TIR']
        array = tir_data.to_numpy()
        tir_acu = pd.DataFrame(columns= ['limite inf','limite sup', 'fracción', 'fracción acumulada'], index= range(20))
        freq = (array[-1] - array[0])/20               # Amplitud de los intervalos
        inf = array.min()        # Limite inferior del primer intervalo
        dif = (array.min() - array.max()) % freq or freq
        sup = array.max() + dif  # Limite superior del último intervalo

        intervals = pd.interval_range(
            start=inf,
            end=sup,
            freq=freq,
            closed="left"
            )
        tir_acu = pd.DataFrame(index= intervals)

        tir_acu["fracción"] = round((pd.cut(array, bins= intervals).value_counts())/(self.corridas),3)
        tir_acu["fracción acumulada"] = tir_acu["fracción"].cumsum()
        print(tir_acu)
        a = np.arange(tir_acu.shape[0])
        plt.plot(tir_acu.index.mid, tir_acu['fracción acumulada'])
        plt.title('Frecuencia acumulada TIR')
        plt.xlabel('valores del TIR')
        plt.ylabel('Frecuencia acumulada')
        plt.show()

       
if __name__ == "__main__":

    app= QtWidgets.QApplication([])
    ventana_esc1= VentanaEscenario1()
    ventana_esc1.show()
    
    app.exec_()