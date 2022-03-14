import PyQt5.QtGui as gui 
import PyQt5.QtCore as core
from PyQt5 import uic
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSignal
from codigo_ventana_juego import MainWindow1
from codigo_ventanar import MainWindow2
from ventana_de_errores import Ventana_error_nombre
from parametros import PATH_VENTANA_INICIO

window_name, base_class = uic.loadUiType(PATH_VENTANA_INICIO)


class MainWindow(window_name, base_class):
    senal_abrir_ventanag = pyqtSignal(str)  
    senal_abrir_ventanar = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.botton_begin_game.clicked.connect(self.entrar_juego)
        self.botton_ranking.clicked.connect(self.entrar_ranking)

        self.show()
    def entrar_juego(self):
        if self.penguin_name.text().isalnum() and self.senal_abrir_ventanag:
            self.senal_abrir_ventanag.emit(self.penguin_name.text())
            self.close()
            
        else:
            self.ventana_error = Ventana_error_nombre()

    def entrar_ranking(self):
        if self.senal_abrir_ventanar:
            self.senal_abrir_ventanar.emit()
            self.close()
    def nuevo_juego(self):
        print("nuevo juego")
        self.show()