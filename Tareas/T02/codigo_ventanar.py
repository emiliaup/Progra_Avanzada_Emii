import PyQt5.QtGui as gui 
import PyQt5.QtCore as core
from PyQt5 import uic
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
QApplication, QHBoxLayout, QVBoxLayout,QGridLayout,QDialog,QProgressBar)
from parametros import PATH_RANKING, PATH_VENTANA_RANKING
from PyQt5.QtCore import pyqtSignal
import sys

window_name, base_class = uic.loadUiType(PATH_VENTANA_RANKING)

class MainWindow2(window_name, base_class):

    senal_inicio = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.botton_ranking_goback.clicked.connect(self.inicio)
        
    def archivo_ranking(self):
        lista_final = []
        with open(PATH_RANKING, "r") as puntajes:
            self.puntos = puntajes.readlines()
        for l in self.puntos:
            self.lista_p = l.strip().split(" ")
            lista_final.append(self.lista_p)
        for i in lista_final:
            i[1] = int(i[2])
        lista_final.sort(key = lambda x: x[2], reverse = True)
        text_final = ""
        for p in lista_final:
            text_final += (f"{p[0]}, {p[2]} \n")
        self.ranking_list.setText(text_final)
        puntajes.close()
           
        self.show()

    def inicio(self):
        self.senal_inicio.emit()
        self.close()