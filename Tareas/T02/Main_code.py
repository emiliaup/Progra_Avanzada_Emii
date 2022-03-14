from codigo_ventana_inicio import MainWindow
from codigo_ventana_juego import MainWindow1
from codigo_ventanar import MainWindow2
from codigo_ventana_resumen import Resumen
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
QApplication, QHBoxLayout, QVBoxLayout,QGridLayout,QDialog,QProgressBar)
import sys
from PyQt5.Qt import Qt
from time import sleep
from PyQt5.QtCore import pyqtSignal

if __name__ == '__main__':
    app = QApplication([])
    ventana_i = MainWindow()
    ventana_g = MainWindow1()
    ventana_r = MainWindow2()
    ventana_resumen = Resumen()
    
    ventana_i.senal_abrir_ventanag.connect(ventana_g.nombre_usurario)
    ventana_i.senal_abrir_ventanar.connect(ventana_r.archivo_ranking)
    ventana_g.senal_resumen.connect(ventana_resumen.resumen_total)
    ventana_g.senal_ventanai.connect(ventana_i.nuevo_juego)
    ventana_resumen.senal_ventanag.connect(ventana_g.nueva_ronda)
    ventana_resumen.senal_ventana_i.connect(ventana_i.nuevo_juego)
    ventana_r.senal_inicio.connect(ventana_i.nuevo_juego)

    sys.exit(app.exec_())
    