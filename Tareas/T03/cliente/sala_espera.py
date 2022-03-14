import sys
import random
import PyQt5.QtWidgets as widgets
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5 import uic
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QGraphicsView,
QGraphicsScene, QGraphicsEllipseItem, QPushButton, QApplication, 
QHBoxLayout, QVBoxLayout,QGridLayout,QDialog,QProgressBar, QApplication)
import sys
from PyQt5.QtGui import QPixmap, QDrag, QPainter, QCursor
import json

with open('parametros.json') as file:
    data = json.load(file)
path_sala_espera = data["PATH_SALA_DE_ESPERA"]
path_choza_azul = data["PATH_CHOZA_AZUL"]
path_choza_rojo = data["PATH_CHOZA_ROJO"]
path_choza_verde = data["PATH_CHOZA_VERDE"]
path_choza_violeta = data["PATH_CHOZA_VIOLETA"] 
background_color = data["BACKGROUND_COLOR"]

window_name, base_class = uic.loadUiType(path_sala_espera)

class Sala_espera(window_name, base_class):

    empezar_juego_signal = pyqtSignal(dict)
    actualizar_jugadores_signal = pyqtSignal(str, bool, int)
    nuevo_jugador_senal = pyqtSignal(dict)
    no_juego_senal = pyqtSignal()


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.no_partida.hide()
        self.salir_botton.hide()
        self.violeta_jugador.hide()
        self.botton_comenzar_juego.hide()
        self.enviar_mensaje_nuevo_jugador()
        self.actualizar_jugadores_signal.connect(self.agregar_jugador)
        self.botton_comenzar_juego.clicked.connect(self.boton_empujado)
        self.no_juego_senal.connect(self.no_juego)
        self.salir_botton.clicked.connect(self.salir)

    def salir(self, event):
        sys.exit()
 
    def enviar_mensaje_nuevo_jugador(self):
        dict_ = {
            "comando" : "log_in"
        }
        self.nuevo_jugador_senal.emit(dict_)

    def agregar_jugador(self, color, cantidad_jugadores, cantidad_j):
      
        if cantidad_jugadores:
            self.botton_comenzar_juego.show()
        if color == "azul":
            path_de_choza = path_choza_azul
        elif color == "verde":
            path_de_choza = path_choza_verde
        elif color == "rojo":
            path_de_choza = path_choza_rojo
        elif color == "violeta":
            path_de_choza = path_choza_violeta
        self.label_choza = QLabel(self)
        self.label_choza.setGeometry(390,290,211,211)
        self.label_choza.setStyleSheet(background_color)
        self.label_choza.setPixmap(QPixmap(path_de_choza))
        self.label_choza.setScaledContents(True)
        
        mensaje = "Cantidad de jugadores conectados:" + str(cantidad_j)
        self.stats_jugadores_conectados.setText(mensaje)
        self.show()

       
    def comenzar_juego_botton(self, comenzar):
        if comenzar == True:
            self.botton_comenzar_juego.show()
    
    def boton_empujado(self):
        mensaje = {
            "comando" : "empezar_juego"
        }
        self.empezar_juego_signal.emit(mensaje)

    def no_juego(self):
        self.no_partida.show()
        self.salir_botton.show()
        self.show()
        
if __name__ == '__main__':
    app = widgets.QApplication([])
    window = Sala_espera()
    sys.exit(app.exec_())
