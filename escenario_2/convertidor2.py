from win32com.client import Dispatch
import win32api
import os
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
class Convertidor2(QWidget):

    def  __init__(self):
        super().__init__()

    def tablaPdf(self):
        #input_file = r'D:\UMSS\Semestre-Final\Taller de simu\Software\evaluacion_de_inversiones\escenario_2\export_dataframe.xlsx'
        #give your file name with valid path 
        input_file = os.getcwd() + '\escenario_2\export_dataframe.xlsx'
        #output_file = r'D:\UMSS\Semestre-Final\Taller de simu\Software\evaluacion_de_inversiones\escenario_2\Report\Reportes\Reporte2.pdf'
        #give valid output file name and path
        output_file = os.getcwd() + '\escenario_2\Report\Reportes\Reporte2.pdf'
        app = Dispatch("Excel.Application")
        app.Interactive = False
        app.Visible = False
        Workbook = app.Workbooks.Open(input_file)
        try:
            Workbook.ActiveSheet.ExportAsFixedFormat(0, output_file)
        except Exception as e:
            print("Failed to convert in PDF format.Please confirm environment meets all the requirements  and try again")
            print(str(e))
        finally:
            Workbook.Close()
            app.Quit()

    def tablaPdfDescarga(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
      
        fileName, _ = QFileDialog.getSaveFileName(self,"Guardar Tabla..","ReporteTabla.pdf","All Files (*);;Text Files (*.pdf)", options=options)
        input_file = r'D:\UMSS\Semestre-Final\Taller de simu\Software\evaluacion_de_inversiones\escenario_2\export_dataframe.xlsx'
        #give your file name with valid path 
        output_file = fileName
        #give valid output file name and path
        app = Dispatch("Excel.Application")
        app.Interactive = False
        app.Visible = False
        Workbook = app.Workbooks.Open(input_file)
        try:
            Workbook.ActiveSheet.ExportAsFixedFormat(0, output_file)
        except Exception as e:
            print("Failed to convert in PDF format.Please confirm environment meets all the requirements  and try again")
            print(str(e))
        finally:
            Workbook.Close()
            app.Quit()