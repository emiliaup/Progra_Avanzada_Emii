from PyQt5.QtCore import QTimer, QThread, pyqtSignal, QUrl, QMimeData, Qt, QPointF
from PyQt5 import uic
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QGraphicsView, 
QGraphicsScene, QGraphicsEllipseItem, QPushButton,
QApplication, QHBoxLayout, QVBoxLayout,QGridLayout,QDialog,QProgressBar, QApplication)
import sys
from PyQt5.QtGui import QPixmap, QDrag, QPainter, QCursor
from random import shuffle, sample, randint, choice
from os import path
from time import sleep, time
from ventana_de_errores import Ventana_error_box
from parametros import (ALTO_CAPTURA, ALTO_FLECHA, VELOCIDAD_FLECHA, 
STYLESHEET_FLECHAS, SEMI_PATH_FELCHA, FELCHA_Y, LARGO_FLECHA)



class Flecha_juego(QThread):

    actualizar = pyqtSignal(QLabel, int, int)
    senal_flechas_en_y = pyqtSignal(QLabel,str,int)
    senal_flechas_no_y = pyqtSignal(QLabel,str,int)

    def __init__(self, parent, limite_x, limite_y, flecha_img, num_geox, pausa, tipo_f, velocidad):
        super().__init__()
        self.ruta_imagen = path.join(SEMI_PATH_FELCHA, flecha_img)  
        self.label = QLabel(parent)
        self.label.setGeometry(num_geox, FELCHA_Y, LARGO_FLECHA, ALTO_FLECHA)
        self.label.setPixmap(QPixmap(self.ruta_imagen))
        self.label.setScaledContents(True)
        self.label.setVisible(True)
        self.label.setStyleSheet(STYLESHEET_FLECHAS)
        self.limite_x = limite_x
        self.limite_y = limite_y
        self.pausa = pausa
        self.__posicion = (0, 0)
        self.posicion = (num_geox, 230)
        self.velocidad = velocidad
        self.tipo_flecha = tipo_f
        self.label.show()
        self.start()

    @property
    def posicion(self):
        return self.__posicion

    @posicion.setter
    def posicion(self, valor):
        self.__posicion = valor
        self.actualizar.emit(self.label, *self.posicion)

    def run(self):
        self.distancia = VELOCIDAD_FLECHA * 0.01
        if self.tipo_flecha == "_2":
            self.distancia = (VELOCIDAD_FLECHA * 2) * 0.01
        self.time_in = time()
        self.time_out = time()
        self.nn = 0
        self.ii = 0
        while self.posicion[1] < self.limite_y:
            self.time_out = time()
            sleep(0.01)
            nuevo_x = self.posicion[0] 
            nuevo_y = self.posicion[1] + self.distancia
            self.posicion = (nuevo_x, nuevo_y)

            if 650 <= self.posicion[1] <= (710 + ALTO_CAPTURA) and self.nn == 0:
                self.nn = 1
                self.senal_flechas_en_y.emit(self.label,self.tipo_flecha, nuevo_x)
            elif self.posicion[1] > (710 + ALTO_CAPTURA) and self.ii == 0:
                self.senal_flechas_no_y.emit(self.label,self.tipo_flecha, nuevo_x)
                self.ii = 1
            elif self.posicion[1] > self.limite_y:
                self.label.destroy()

