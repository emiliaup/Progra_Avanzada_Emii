from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PyQt5 import uic
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
QApplication, QHBoxLayout, QVBoxLayout,QGridLayout,QDialog,QProgressBar)
import sys
from parametros import PROB_FLECHA_DORADA, PROB_FLECHA_HIELO, PROB_FLECHA_X2, PROB_NORMAL
from random import shuffle, choice, sample

class Probabilidades:
    def __init__(self):
        self.prob_normal = int(PROB_NORMAL* 100) 
        self.l_normal = []
        self.prob_x2 = int(PROB_FLECHA_X2* 100) 
        self.l_x2 = []
        self.prob_dorada = int(PROB_FLECHA_DORADA* 100) 
        self.l_dorada = []
        self.prob_hielo = int(PROB_FLECHA_HIELO* 100) 
        self.l_hielo = []

    def flecha_prob(self):
        for i in range(0,self.prob_normal*100):
            self.l_normal.append("_6")

        for i in range(0,self.prob_x2*100):
            self.l_x2.append("_1")

        for i in range(0,self.prob_dorada*100):
            self.l_dorada.append("_2")
            
        for i in range(0,self.prob_hielo*100):
            self.l_hielo.append("_8")
        
        self.lista_prob = self.l_hielo + self.l_dorada + self.l_normal + self.l_x2
        
        return self.lista_prob
        
class Info_Flechas:
    def __init__(self):
        self.letter_l =["left","right","up","down"]
        pp = Probabilidades()
        self.numero_l = pp.flecha_prob()
        self.num = choice(self.numero_l)
        # num 6 = normal, 1 = x2, 2 = dorada, 8 = hielo
        self.let = choice(self.letter_l)
        self.f_l = []
        
    def flecha_info(self):
        self.flecha_final = self.let + self.num
    
        if self.let == "left":
            self.geox = 30
        elif self.let == "right":
            self.geox = 190
        elif self.let == "up":
            self.geox = 110
        elif self.let == "down":
            self.geox = 270
        
        if self.num == "_6":
            self.tipo_flecha = "normal"
        if self.num == "_1":
            self.tipo_flecha = "x2"
        if self.num == "_2":
            self.tipo_flecha = "dorada"
        if self.num == "_8":
            self.tipo_flecha = "hielo"

        self.f_l.append(self.let)
        self.f_l.append(self.num)
        self.f_l.append(self.geox)
        self.f_l.append(self.flecha_final)

        return self.f_l
        #self.senal_lista_info.emit(self.f_l)
