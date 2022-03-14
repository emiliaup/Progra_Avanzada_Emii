from PyQt5.QtCore import QTimer, QThread, pyqtSignal, QUrl, QMimeData, Qt, QPointF
from PyQt5 import uic
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QGraphicsView,
QGraphicsScene, QGraphicsEllipseItem, QPushButton, QApplication, 
QHBoxLayout, QVBoxLayout,QGridLayout,QDialog,QProgressBar, QApplication)
import sys
from PyQt5.QtGui import QPixmap, QDrag, QPainter, QCursor
from random import shuffle, sample, randint, choice
from os import path
from time import sleep, time
from parametros import (STYLESHEET_PENGUIN, PATH_PENGUIN_AMARILLO, 
GEO_PENGUIN_AMARILLO1, PATH_PENGUIN_BLUE, GEO_PENGUIN_BLUE1, 
PATH_PENGUIN_MORADO, GEO_PENGUIN_MORADO1, PATH_PENGUIN_ROJO, 
GEO_PENGUIN_ROJO1, PATH_PENGUIN_VERDE, GEO_PENGUIN_VERDE1,
GEO_PENGUIN_AMARILLO0,  GEO_PENGUIN_BLUE0, 
GEO_PENGUIN_MORADO0, GEO_PENGUIN_ROJO0, GEO_PENGUIN_VERDE0,
PENGUIN_CUADRADO)

class MainWindow3(QLabel):
    def __init__(self,parent):
        super().__init__(parent)
        parent.penguin_amarillo = QLabel(parent)
        parent.penguin_amarillo.setPixmap(QPixmap(PATH_PENGUIN_AMARILLO))
        parent.penguin_amarillo.setGeometry(GEO_PENGUIN_AMARILLO0, GEO_PENGUIN_AMARILLO1,
         PENGUIN_CUADRADO, PENGUIN_CUADRADO)
        parent.penguin_amarillo.setStyleSheet(STYLESHEET_PENGUIN)
        parent.penguin_amarillo.setScaledContents(True)
        parent.penguin_amarillo.setVisible(True)

        parent.penguin_blue = QLabel(parent)
        parent.penguin_blue.setGeometry(GEO_PENGUIN_BLUE0, GEO_PENGUIN_BLUE1,
         PENGUIN_CUADRADO, PENGUIN_CUADRADO)
        parent.penguin_blue.setStyleSheet(STYLESHEET_PENGUIN)
        parent.penguin_blue.setPixmap(QPixmap(PATH_PENGUIN_BLUE))
        parent.penguin_blue.setScaledContents(True)

        parent.penguin_morado = QLabel(parent)
        parent.penguin_morado.setGeometry(GEO_PENGUIN_MORADO0, GEO_PENGUIN_MORADO1,
         PENGUIN_CUADRADO, PENGUIN_CUADRADO)
        parent.penguin_morado.setStyleSheet(STYLESHEET_PENGUIN)
        parent.penguin_morado.setPixmap(QPixmap(PATH_PENGUIN_MORADO))
        parent.penguin_morado.setScaledContents(True)

        parent.penguin_rojo = QLabel(parent)
        parent.penguin_rojo.setGeometry(GEO_PENGUIN_ROJO0, GEO_PENGUIN_ROJO1,
         PENGUIN_CUADRADO, PENGUIN_CUADRADO)
        parent.penguin_rojo.setStyleSheet(STYLESHEET_PENGUIN)
        parent.penguin_rojo.setPixmap(QPixmap(PATH_PENGUIN_ROJO))
        parent.penguin_rojo.setScaledContents(True)

        parent.penguin_verde = QLabel(parent)
        parent.penguin_verde.setGeometry(GEO_PENGUIN_VERDE0, GEO_PENGUIN_VERDE1,
         PENGUIN_CUADRADO, PENGUIN_CUADRADO)
        parent.penguin_verde.setStyleSheet(STYLESHEET_PENGUIN)
        parent.penguin_verde.setPixmap(QPixmap(PATH_PENGUIN_VERDE))
        parent.penguin_verde.setScaledContents(True)

    def mousePressEvent(parent, event):
        if event.key() == Qt.Key_M:
            print("MMM")
    def mousePressEvent(parent,event):
        print("pressed")

    def mostrar_penguins(parent):
        print("SEE")
        parent.penguin_amarillo.show()
    def keyPressEvent(self,event):
        print("seeee")

    