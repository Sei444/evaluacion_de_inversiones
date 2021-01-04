# Importamos la libreria canvas del paquete reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
# abrimos el pdf 
c = canvas.Canvas("./escenario_1/"+'Reporte3.pdf')
#Fuente y el tamaño = ?
c.setFont('Helvetica-Oblique', 50)
# Dibujamos texto: (X,Y,Texto)
c.drawString(225,450,"Graficos")
c.showPage()
c.setFont('Helvetica', 30)
# Dibujamos texto: (X,Y,Texto)
c.drawString(125,760,"Grafico del Histograma TIR")
# Dibujamos una imagen (IMAGEN, X,Y, WIDTH, HEIGH)
c.drawImage('./escenario_1/imagen1.jpg', 10, 175, 600, 500)
c.showPage()
#//
c.setFont('Helvetica', 30)
c.drawString(30,760,"Grafico de la Distribucion Acumulada TIR")
c.drawImage('./escenario_1/imagen1.jpg', 10, 175, 600, 500)
c.showPage()
#//
c.setFont('Helvetica', 30)
c.drawString(128,760,"Grafico del Flujo Neto")
c.drawImage('./escenario_1/imagen3.jpg', 10, 175, 600, 500)
c.showPage()
#//
c.setFont('Helvetica', 30)
c.drawString(110,760,"Grafico de la Inversion Normal")
c.drawImage('./escenario_1/imagen4.jpg', 10, 175, 600, 500)
c.showPage()
#Conclusion
c.setFont('Helvetica-Oblique', 50)
c.drawString(200,450,"Conclusion")
c.showPage()
#Mensaje
my_text = "Los resultados de esta simulacion para la inversion de este negocio da a concluir \nque el proyecto es rentable para llevarlo a cabo ya que se muestra en los graficos\nque se logra un valor de ingresos aceptables."
textobject = c.beginText(2*cm, 29.7 * cm - 2 * cm)
for line in my_text.splitlines(False):
    textobject.textLine(line.rstrip())
c.drawText(textobject)
c.save()
