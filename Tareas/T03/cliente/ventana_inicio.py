import sys
import random
import PyQt5.QtWidgets as widgets
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5 import uic
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QGraphicsView,
QGraphicsScene, QGraphicsEllipseItem, QPushButton, QApplication, 
QHBoxLayout, QVBoxLayout,QGridLayout,QDialog,QProgressBar, QApplication)
import sys
from PyQt5.QtGui import QPixmap
import json


with open('parametros.json') as file:
    data = json.load(file)
path_sala_juego = data["PATH_SALA_JUEGO"]
path_choza_azul = data["PATH_CHOZA_AZUL"]
path_choza_rojo = data["PATH_CHOZA_ROJO"]
path_choza_verde = data["PATH_CHOZA_VERDE"]
path_choza_violeta = data["PATH_CHOZA_VIOLETA"] 
path_arcilla = data["PATH_ARCILLA_GRILLA"]
path_madera = data["PATH_ARCILLA_MADERA"]
path_trigo = data["PATH_ARCILLA_TRIGO"]

window_name, base_class = uic.loadUiType(path_sala_juego)

class Ventana_inicio(window_name, base_class):

    send_msg_signal = pyqtSignal(dict)
    dados_signal = pyqtSignal(bool, dict, str, dict, dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.botton_exit.clicked.connect(self.salir)
        self.dados_signal.connect(self.botton_turno)
        self.lista_de_hex = [self.hex_0, self.hex_1,self.hex_2,self.hex_3,self.hex_4,
        self.hex_5,self.hex_6,self.hex_7,self.hex_8,self.hex_9]
        self.lista_num = [self.num_0, self.num_1,self.num_2,self.num_3,self.num_4,
        self.num_5,self.num_6,self.num_7,self.num_8,self.num_9]

        self.lista_coneccion = [self.label_0_1, self.label_0_4, self.label_1_5, self.label_2_3,
        self.label_2_6, self.label_3_7, self.label_4_9, self.label_5_6, self.label_5_10, 
        self.label_6_11, self.label_7_8, self.label_7_12, self.label_8_13, self.label_9_10, 
        self.label_9_14, self.label_10_15, self.label_11_12, self.label_11_16, self.label_12_17, 
        self.label_13_18, self.label_14_19, self.label_15_16, self.label_15_20, self.label_16_21, 
        self.label_17_18, self.label_17_22, self.label_18_23, self.label_19_20, self.label_19_24, 
        self.label_20_25, self.label_21_22, self.label_21_26, self.label_22_27, self.label_23_28, 
        self.label_24_29, self.label_25_26, self.label_25_30, self.label_26_31, self.label_27_28,
        self.label_27_32, self.label_29_30, self.label_31_32]

        self.lista_choza = [self.choza_0, self.choza_1, self.choza_2, self.choza_3, self.choza_4,
        self.choza_5,self.choza_6,self.choza_7,self.choza_8,self.choza_9,self.choza_10,
        self.choza_11,self.choza_12,self.choza_13,self.choza_14,self.choza_15,self.choza_16,
        self.choza_17,self.choza_18,self.choza_19,self.choza_20,self.choza_21,self.choza_22,
        self.choza_23,self.choza_24,self.choza_25,self.choza_26,self.choza_27,self.choza_28,
        self.choza_29,self.choza_30,self.choza_31,self.choza_32]

      
        self.arcilla = path_arcilla
        self.trigo = path_trigo
        self.madera = path_madera
        self.rojo_choza = path_choza_rojo
        self.azul_choza = path_choza_azul
        self.verde_choza = path_choza_verde
        self.violeta_choza = path_choza_violeta
        self.mapa_ya_preparado = False


    def salir(self, event):
        sys.exit()
    
    def botton_turno(self, turno, recursos_dict, 
    lista_turnos, mapa_chozas, mapa_carreteras):
        mensaje_stats = "Turno de Jugador:" + str(lista_turnos)
    
        self.stats_jugadores.setText(mensaje_stats)
        self.mapa_carreteras_chozas(mapa_chozas, mapa_carreteras)
        if str(turno) == "False":
            self.botton_dado.setDisabled(False)
        else:
            self.botton_dado.setDisabled(True)
        self.show()
        
        if self.mapa_ya_preparado is False:
            self.mapa_ya_preparado = True
            self.preparar_mapa(recursos_dict)

        
    def preparar_mapa(self, recursos_dict):
        for i in range(0,10):
            recurso = recursos_dict[str(i)] 
            label_hex = self.lista_de_hex[i]
            label_num = self.lista_num[i]
      
            if recurso[1] == "arcilla":
                ruta = self.arcilla
            elif recurso[1] == "trigo":
                ruta = self.trigo
            elif recurso[1] == "madera":
                ruta = self.madera
            label_hex.setPixmap(QPixmap(ruta))
            label_num.setText(str(recurso[0]))
       

    def mapa_carreteras_chozas(self, dic_chozas, dic_carreteras):
          
        for key, value in dic_chozas.items():
            nombre_choza = value[0]
            dueno_choza = value[1]
            if str(dueno_choza) != "None":
                if str(dueno_choza) == "rojo":
                    self.lista_choza[int(key)].setPixmap(QPixmap(self.rojo_choza))
                    self.lista_choza[int(key)].show()
                elif str(dueno_choza) == "azul":
                    self.lista_choza[int(key)].setPixmap(QPixmap(self.azul_choza))
                    self.lista_choza[int(key)].show()
                elif str(dueno_choza) == "verde":
                    self.lista_choza[int(key)].setPixmap(QPixmap(self.verde_choza))
                    self.lista_choza[int(key)].show()
                elif str(dueno_choza) == "violeta":
                    self.lista_choza[int(key)].setPixmap(QPixmap(self.violeta_choza))
                    self.lista_choza[int(key)].show()
            else:
                self.lista_choza[int(key)].hide()

        num = 0
        for label, dueno in dic_carreteras.items():
            if str(dueno) == "None":
                self.lista_coneccion[num].hide()
            else:
                self.lista_coneccion[num].show()
            num += 1

    def send_msg_to_client(self):
        data = {    
            "type"  :   "chat", \
            "username"  :   self.username, \
            "data"  :   self.userInputWidget.toPlainText() \
                }
        self.send_msg_signal.emit(data)
        self.userInputWidget.setPlainText('')
    

if __name__ == '__main__':
    app = widgets.QApplication([])
    window = Ventana_inicio()
    sys.exit(app.exec_())
