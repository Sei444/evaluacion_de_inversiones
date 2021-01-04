import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import plotly.graph_objects as go
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit ,QTableView, QDialog, QMessageBox
from PyQt5.QtCore import QAbstractTableModel, Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from scipy.stats import norm
from escenario_2.ventanaesc2 import *
from programa import *
from escenario_2.backendConclusion2 import *
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
        self.pushButton_tabla.clicked.connect(self.click_tablaS)
        self.pushButton_tabla2.clicked.connect(self.click_tablaS2)
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
        global text_conclusion
        text_conclusion = main.evaluar()
    def click_conclusion(self):
        self.ventanaEsc2_conclusion = VentanaConclusion()
        self.ventanaEsc2_conclusion.mostrar_conclusion(text_conclusion)
        self.ventanaEsc2_conclusion.exec_()
    def mostrar_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Mensaje")
        msg.setText("Se cargaron los datos correctamente")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()
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
            obj_inf.grafica_distTriangular_inf()
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
    def click_conclusion(self):
        self.ventanaEsc1_conclusion = VentanaConclusion()
        self.ventanaEsc1_conclusion.mostrar_conclusion(text_conclusion)
        self.ventanaEsc1_conclusion.exec_()
    def volver_home(self):
       #cerrar ventana 
       self.close()
    def click_tablaS(self):
        #ventana emergente con tabla de los datos DATAFRAME corridas
        flujo = dataCorridas.iloc[:,[1,2,3,4,5,6,7]]
        self.model = pandasModel(flujo)
        self.view = QTableView()
        self.view.setModel(self.model)
        corridas_str = str(corridas)
        titulo = "Tabla: Resultado de simular "+ corridas_str + " corridas"
        self.view.setWindowTitle(titulo)
        self.view.resize(1000, 600)
        self.view.show()
    def click_tablaS2(self):
        #ventana emergente con tabla de los datos DATAFRAME corridas
        flujo_data = dataCorridas.iloc[:,[1,2,3,4,5,8]]
        flujo_data['año_5']= flujo_data['año_5'] - flujo_data['valor_de_rescate']
        flujo_data = flujo_data.iloc[:,[0,1,2,3,4]]
        print(flujo_data)
        flujo_data = flujo_data * 100 / 40
        self.model = pandasModel(flujo_data)
        self.view = QTableView()
        self.view.setModel(self.model)
        titulo = "Tabla: Resultado flujo neto antes de impuestos"
        self.view.setWindowTitle(titulo)
        self.view.resize(1000, 600)
        self.view.show()
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
        inflacion = 100 - (np.around(np.random.triangular(100 - self.minimo, 100 - self.esperado, 100 - self.maximo, 1), 0)) #Meter datos Estimacion pesimista - probable - optimista
        return inflacion
    def grafica_distTriangular(self):
        x = np.array([self.minimo, self.esperado ,self.maximo])
        y = np.array([0, 2/(self.maximo - self.minimo) ,0])
        plt.triplot(x,y)
        plt.show()
    def grafica_distTriangular_inf(self):
        x = np.array([self.maximo, self.esperado ,self.minimo])
        y = np.array([0, 2/(self.minimo - self.maximo) ,0])
        plt.triplot(x,y)
        plt.show()
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
        #FLUJO
        flujo = [self.flujo1, self.flujo2, self.flujo3, self.flujo4, self.flujo5] #Meter los valores que tendra nuestro flujo
        #NUEVO FLUJO SEGUN INDICES (ARREGLO NUEVO)
        flujoNuevo = np.take(flujo,(indices))
        return flujoNuevo
    def grafica_distUniforme(self):
        #datos
        flujo_data = dataCorridas.iloc[:,[1,2,3,4,5,8]]
        array = np.concatenate( (flujo_data['año_1'].to_numpy(), flujo_data['año_2'].to_numpy(), flujo_data['año_3'].to_numpy(), flujo_data['año_4'].to_numpy(), (flujo_data['año_5'].to_numpy()-flujo_data['valor_de_rescate'].to_numpy())), axis = None)
        #grafico con solucion 1
        plt.hist(array, bins = 5, orientation='vertical')
        plt.title('Histograma Flujo Neto')
        plt.xlabel('valores del Flujo Neto')
        plt.ylabel('Total repeticiones')
        plt.show()
class Inversion():

    def __init__(self):
        pass
    
    def evaluar(self):
        global dataCorridas 
        dataCorridas = self.construir_dataFrame()
        conclusion = self.probabilidad()
        return conclusion
    def calcular_VPN(self, descuento, arregloFinal):
        return np.npv(descuento,arregloFinal)
    def arreglo(self):
        inv = obj_inv.generar_resultado()
        flujo = obj_flujos.generar_resultado()
        rescate = obj_res.generar_resultado()
        inflacion = obj_inf.generar_resInf()/100
        descuento = np.around(t_descuento/100 + inflacion+(t_descuento/100 * inflacion), 8)
        flujo[4] = np.take(flujo,4) + rescate
        arregloFinal = np.concatenate((inv,flujo),axis=0)
        vpn =  self.calcular_VPN(descuento,arregloFinal)
        res = np.concatenate((arregloFinal, vpn, inflacion, rescate, descuento), axis = None)
        return res    
    def construir_dataFrame(self):
        #construye un dataframe de tamaño n difinido por --> range(n)
        data = pd.DataFrame(columns=  ['inv_ini', 'año_1', 'año_2', 'año_3', 'año_4', 'año_5', 'VPN', 'inflacion', 'valor_de_rescate', 'tasa_de_descuento'], index = range(corridas))
        for i in data.index :
            data.iloc[i] = self.arreglo()
        return data
    def graficar_histrogramaVPN(self):
      # HISTOGRAMA VPN , cambie el nombre corridas por datacorridas
        vpn_data = dataCorridas['VPN']
        np_vpn_data = vpn_data.to_numpy()
        plt.hist(np_vpn_data, bins = 20, orientation='vertical')
        plt.title('Histograma VPN')
        plt.xlabel('valores del VPN')
        plt.ylabel('Total repeticiones')
        plt.show()
    def probabilidad(self):
        p_vpn = dataCorridas['VPN'].to_numpy()
        may_01 = p_vpn[p_vpn > 0.1]
        print(may_01)
        porcentaje = len(may_01) * 100 / corridas
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
    ventana_esc2 = VentanaEscenario2()
    ventana_esc2.show()
    
    app.exec_()