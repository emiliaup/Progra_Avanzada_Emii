from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PyQt5 import uic
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
QApplication, QHBoxLayout, QVBoxLayout,QGridLayout,QDialog,QProgressBar)
import sys
from parametros import PROB_FLECHA_DORADA, PROB_FLECHA_HIELO, PROB_FLECHA_X2, PROB_NORMAL
from random import shuffle, choice, sample
from parametros import ERROR_GEO

class Ventana_error_nombre(QWidget):
    def __init__ (self):
        super().__init__()
        self.init_gui()
    
    def init_gui(self):
        self.setGeometry(ERROR_GEO, ERROR_GEO, ERROR_GEO, ERROR_GEO)
        self.setWindowTitle("Error Username")
        self.texto = QLabel("Error!! su usuario debe ser compuesto de solo numeros y letras",self)
        box = QVBoxLayout()
        box.addWidget(self.texto)
        self.show()

class Ventana_error_box(QWidget):
    def __init__ (self):
        super().__init__()
        self.init_gui()
    
    def init_gui(self):
        self.setGeometry(ERROR_GEO, ERROR_GEO, ERROR_GEO, ERROR_GEO)
        self.setWindowTitle("Error")
        txt = "Error!! Debes elegit la dificultad y cancion (y supuestamente pinguinos)"
        self.texto = QLabel(txt,self)
        box = QVBoxLayout()
        box.addWidget(self.texto)
        self.show()

class Ventana_error_penguin(QWidget):
    def __init__ (self):
        super().__init__()
        self.init_gui()
    
    def init_gui(self):
        self.setGeometry(ERROR_GEO, ERROR_GEO, ERROR_GEO, ERROR_GEO)
        self.setWindowTitle("Error")
        self.texto = QLabel("Error!! No tiene dinero suficiente",self)
        box = QVBoxLayout()
        box.addWidget(self.texto)
        self.show()

        
