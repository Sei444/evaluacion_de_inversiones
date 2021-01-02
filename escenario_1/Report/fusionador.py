from PyPDF2 import PdfFileMerger
import os
loc = "./escenario_1/"
pdfs = [loc+archivo for archivo in os.listdir(loc) if archivo.endswith(".pdf")]
nombre_archivo_salida = "ReporteFinal.pdf"
fusionador = PdfFileMerger()

for pdf in pdfs:
    fusionador.append(open(pdf, 'rb'))

with open("./escenario_1/Report/"+nombre_archivo_salida, 'wb') as salida:
    fusionador.write(salida)