import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import plotly.graph_objects as go
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit ,QTableView, QDialog 
from PyQt5.QtCore import QAbstractTableModel, Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from scipy.stats import norm
from escenario_1.ventanaesc1 import *
from programa import *
from escenario_1.backendConclusion import *

class  VentanaEscenario1(QtWidgets.QMainWindow, Ui_ventanaEsc1 ):
    def __init__(self):
        super().__init__()
        #QAbstractTableModel.__init__(self)
        self.setupUi(self)
        self.boton_simular.clicked.connect(self.click_simular)
        self.pushButton_conclusion.clicked.connect(self.click_conclusion)
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
        global corridas
        corridas = int(self.lineEdit_Ncorridas.text())
        global trema
        trema = int(self.lineEdit_TREMA.text())

        global main 
        main= Inversion(media_flujo,desviacionE_flujo,media_inv,desviacionE_inv,corridas)
        global obj_inv
        obj_inv = Normal(media_inv,desviacionE_inv)
        global obj_flujosNetos
        obj_flujosNetos = Normal(media_flujo,desviacionE_flujo)
        global text_conclusion
        text_conclusion = main.evaluar()
        self.mostrar_popup()
    def mostrar_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Mensaje")
        msg.setText("Se cargaron los datos correctamente")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()
    def click_conclusion(self):
        try:
            self.ventanaEsc1_conclusion = VentanaConclusion()
            self.ventanaEsc1_conclusion.mostrar_conclusion(text_conclusion)
            self.ventanaEsc1_conclusion.exec_()
        except NameError:
            msg = QMessageBox()
            msg.setWindowTitle("Mensaje")
            msg.setText("No se puede mostrar la conclusion sin datos simulados")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()
    
    def click_histrogramaTIR(self):
        main.graficar_histrogramaTIR()
    def click_distAcumTIR(self):
        main.graficar_distAcumuladaTIR()
    def click_distNInvInicial(self):
        obj_inv.grafica_distnormal_Inv()
    def click_disNFlujos(self):
        obj_flujosNetos.grafica_distnormal_Flujo()
    def click_tablaS(self):
        self.model = pandasModel(tabla)
        self.view = QTableView()
        self.view.setModel(self.model)
        corridas_str = str(corridas)
        print(corridas_str)
        titulo = "Tabla: Resultado de simular "+ corridas_str + " corridas"
        print(titulo)
        self.view.setWindowTitle(titulo)
        self.view.resize(700, 600)
        self.view.show()
    def volver_home(self):
       self.close()
    def closeEvent(self,event):
        pregunta = QMessageBox.question(self,"Salir","¿Seguro que quieres salir?" , QMessageBox.Yes |QMessageBox.No)
        if pregunta == QMessageBox.Yes: 
            event.accept()
            QApplication.quit()
        else:
            event.ignore()        
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
    
    def grafica_distnormal_Inv(self):
        x_1 = np.linspace(norm(self.media, self.desviacion_e).ppf(0.01),
                  norm(self.media, self.desviacion_e).ppf(0.99), 10000)
        FDP_normal = norm(self.media, self.desviacion_e).pdf(x_1) # FDP
        plt.plot(x_1, FDP_normal, label='FDP nomal')
        plt.title('Función de Densidad de Probabilidad')
        plt.ylabel('probabilidad')
        plt.xlabel('valores')
        plt.show()
        plt.savefig("./escenario_1/imagen3.jpg")
    def grafica_distnormal_Flujo(self):
        normal = norm(self.media, self.desviacion_e)
        x = np.linspace(normal.ppf(0.01),
                        normal.ppf(0.99), 100)
        fp = normal.pdf(x) # Función de Probabilidad
        plt.plot(x, fp)
        plt.title('Distribución Normal')
        plt.ylabel('probabilidad')
        plt.xlabel('valores')
        plt.show()
        plt.savefig("./escenario_1/imagen4.jpg")
class Inversion():

    def __init__(self,media_flujo,desviacionE_flujo,media_inv,desviacionE_inv,corridas):
        self.tir = 0
        self.media_flujo =media_flujo
        self.desviacionE_flujo = desviacionE_flujo
        self.media_inv = media_inv
        self.desviacionE_inv = desviacionE_inv
        self.corridas = corridas
        self.data = pd.DataFrame()
    def evaluar(self):
        global tabla 
        tabla= self.construir_dataFrame()
        conclusion = self.probabilidad()
        return conclusion
    def calcular_tir(self):
        objt_inv= Normal(self.media_inv,self.desviacionE_inv,1)
        objt_flujos = Normal(self.media_flujo,self.desviacionE_flujo,5)
        inversion =objt_inv.generar_resultado()
        flujos_netos = objt_flujos.generar_resultado()
        aux_tir = np.rint(np.insert(flujos_netos,0,-inversion))
        tir = round((np.irr(aux_tir)*100), 3)
        corrida = np.append(aux_tir, tir, axis=None)
        
        return corrida
    def construir_dataFrame(self):
        data = pd.DataFrame(columns=['inversión_inicial', 'ingresos_año1', 'ingresos_año2','ingresos_año3', 'ingresos_año4','ingresos_año5', 'TIR'], index=range(self.corridas))
        #row = Inversion()
        for i in data.index :
            data.iloc[i] = self.calcular_tir()
        print("funciona!!!")
        data.to_excel(r'./escenario_1/export_dataframe.xlsx', index = False)
        return data
   
    def graficar_histrogramaTIR(self):
        #datos
        tabla.sort_values(by=['TIR'], inplace=True)
        tir_data = tabla['TIR']
        array = tir_data.to_numpy()
        fragmentos = np.around(np.linspace(array[0], array[-1], 21), 3 )
        bins = fragmentos.tolist()
        #grafico con solucion 1
        plt.hist(array, bins = bins, orientation='vertical')
        plt.title('Histograma TIR')
        plt.xlabel('valores del TIR')
        plt.ylabel('Total repeticiones')
        plt.show()
        plt.savefig("./escenario_1/imagen1.jpg")
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
        a = np.arange(tir_acu.shape[0])
        plt.plot(tir_acu.index.mid, tir_acu['fracción acumulada'])
        plt.title('Frecuencia acumulada TIR')
        plt.xlabel('valores del TIR')
        plt.ylabel('Frecuencia acumulada')
        plt.show()
        plt.savefig("./escenario_1/imagen2.jpg")

    def probabilidad(self):
        p_tir = tabla['TIR'].to_numpy()
        may_trema = p_tir[p_tir > trema]
        print(may_trema)
        porcentaje = len(may_trema) * 100 / corridas
        str_procentaje = str(porcentaje)
        print(porcentaje)
        if porcentaje >= 90:
            res = 'Los parametros indican que la inversión puede ser aceptada, superando un '+ str_procentaje + '% de exito'
        else:
            res = 'Los parametros indican que la inversión debe ser rechazada, dado que la probalidad de exito no supera el 90%, siendo la probalidad de exito solo  '+str_procentaje+'% '
        return res

class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

       
if __name__ == "__main__":

    app= QtWidgets.QApplication([])
    ventana_esc1= VentanaEscenario1()
    ventana_esc1.show()
    
    app.exec_()
    