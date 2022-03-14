from functools import partial
from PyQt5.QtCore import pyqtSignal, QObject, QTimer
from ventana_inicio import Ventana_inicio
from sala_final import Sala_final
from sala_espera import Sala_espera
import json

with open('parametros.json') as file:
    data = json.load(file)
    cantidad_jugadores = data["CANTIDAD_JUGADORES_PARTIDA"]

class Controlador(QObject):
    mostrar_sala_juego_signal = pyqtSignal(bool, dict, str, dict, dict)

    def __init__(self, parent):
        super().__init__()

        self.ventana_j = Ventana_inicio()
        self.sala_f = Sala_final()
        self.sala_e = Sala_espera()

        self.sala_e.hide()
        self.sala_f.hide()
        self.ventana_j.hide()

        #senales
        self.sala_e.empezar_juego_signal.connect(parent.enviar)
        self.sala_e.nuevo_jugador_senal.connect(parent.enviar)
        self.mostrar_sala_juego_signal.connect(self.mostrar_sala_juego)


    def mostrar_sala_juego(self, bool_botton, recursos, lista_t, mapa_ch, mapa_carr):
        self.ventana_j.dados_signal.emit(bool_botton, recursos,lista_t, mapa_ch,mapa_carr)
        self.sala_e.hide()
        
    
    def error_coneccion(self):
        print("error coneccion")

####### MENSAJE #####

    def manejar_mensaje(self, mensaje):
            
        try:
            comando = mensaje["comando"]
    
        except KeyError:
            return []

        if comando == "log_in_accepted":
            color = mensaje["color"]
            cantidad_j = mensaje["cantidad_jugadores"]
            if mensaje["cantidad_jugadores"] == cantidad_jugadores:
                tope_de_jugadores = True
            else:
                tope_de_jugadores = False
            self.sala_e.actualizar_jugadores_signal.emit(color, tope_de_jugadores,cantidad_j)
       
        elif comando == "empezar_juego":
            
            turno = mensaje["para"]
            recursos = mensaje["recursos"]
            lista_turno = mensaje["turno"]
            mapa_chozas = mensaje["mapa_chozas"]
            mapa_carreteras = mensaje["mapa_carreteras"]
            if turno == "no turno":
                bool_turno = True
            elif turno == "turno":
                bool_turno = False
            self.mostrar_sala_juego_signal.emit(bool_turno, recursos,
            lista_turno, mapa_chozas, mapa_carreteras)

        elif comando == "no_juego":
            self.sala_e.no_juego_senal.emit()





