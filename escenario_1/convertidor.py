from win32com.client import Dispatch
import win32api
class Convertidor():
    def tablaPdf(self):
        input_file = r'D:\UMSS\Semestre-Final\Taller de simu\Software\evaluacion_de_inversiones\escenario_1\export_dataframe.xlsx'
        #give your file name with valid path 
        output_file = r'D:\UMSS\Semestre-Final\Taller de simu\Software\evaluacion_de_inversiones\escenario_1\Report\Reportes\Reporte2.pdf'
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
