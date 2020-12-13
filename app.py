
import sys
from PyQt5 import uic 
from PyQt5.QtWidgets import QMainWindow, QApplication

class principal (QMainWindow):
  def __init__(self):
    super().__init__()
    uic.loadUi("ventanaP.ui",self)

if __name__== '__main__':
  app = QApplication(sys.argv)
  ventana = principal()
  ventana.show()
  sys.exit(app.exec_())