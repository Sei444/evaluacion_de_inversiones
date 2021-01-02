from reportlab.pdfgen import canvas

c = canvas.Canvas("./escenario_1/"+'Reporte1.pdf')
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
c.save()