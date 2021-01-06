import sys
from reportlab.pdfgen import canvas
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import os
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 diálogos de archivos'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 800
        self.initUI()
 
    def initUI(self):
        #self.setWindowTitle(self.title)
        #self.setGeometry(self.left, self.top, self.width, self.height)
        self.saveFileDialog()
 
        
 

 
    def saveFileDialog(self):    
      
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
      
        fileName, _ = QFileDialog.getSaveFileName(self,"tituloventana","ReporteGraficos","All Files (*);;Text Files (.txt)", options=options)
        c = canvas.Canvas(fileName )
        c.setFont('Helvetica', 20)
        c.drawString(140,760,"Universidad Mayor de San Simón")
        c.setFont('Helvetica-Oblique', 20)
        c.drawString(140,740,"Facultad de Ciencias y Tecnología")
        c.setFont('Helvetica-Oblique', 40)
        c.drawString(90,450,"Reporte de la Simulacion")
        c.setFont('Helvetica-Oblique', 40)
        c.drawString(180,420,"de Inversiones")
        c.drawImage('./escenario_1/logo1.jpg', 30, 650, 100, 150)
        c.drawImage('./escenario_1/logo2.jpg', 460, 700, 100, 100)
        c.showPage()
        #with open(fileName, 'wt') as f:

        c.save()
        if fileName:
            print(fileName)
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())