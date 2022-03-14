from threading import Lock
from random import choice, shuffle, randint, choices
from mapa import Grafo, grafo_nodo
from beautifultable import BeautifulTable
import json 

with open('grafo.json') as file:
    data = json.load(file)
dimension_mapa = data["dimensiones_mapa"]
dic_hexagonos = data["hexagonos"]
dic_nodos = data["nodos"]

with open('parametros.json') as file:
    data = json.load(file)
    cantidad_jugadores = data["CANTIDAD_JUGADORES_PARTIDA"]
class Logica:

    log_in_lock = Lock()
    partida_lock = Lock()
    lista_jugadores_lock = Lock()

    def __init__(self):
        self.partida_en_proceso = False
        self.lista_jugadores_partida = []
        self.ronda = 0
        self.cantidad_jugadores = 0 
        self.table = BeautifulTable()
        self.table.columns.header = ["Cliente", "Evento", "Detalles"]
        self.ronda_de_jugador = None

    def inicializar_jugadores(self,lista_jugadores):
        shuffle(lista_jugadores)
        turno = 0
        for j in lista_jugadores:
            self.lista_jugadores_partida.append(j.color)
            j.turno = turno
            turno += 1
    
    def comenzar_juego(self, lista_jugadores):
        grafo_nodo.armar_conexiones()
        grafo_nodo.armar_poblados()
       
        for player in lista_jugadores:
            primer_carretera_bien = False
            segunda_carretera_bine = False
            while primer_carretera_bien == False and segunda_carretera_bine == False:
                num_random = randint(0,32)
                #poner primera carretera
                lista_conexion_carreteras = dic_nodos[str(num_random)]
                random_carretera = choice(lista_conexion_carreteras)
                #poner segunda carretera
                random_carretera0 = random_carretera
                lista_conexion_carreteras0 = dic_nodos[random_carretera]
                while random_carretera == random_carretera0 or num_random == random_carretera0:
                    random_carretera0 = choice(lista_conexion_carreteras0)

                #revisar que no haya tope con otro jugador 
                carretera_primera = grafo_nodo.revisar_carretera(num_random, random_carretera)
                carretera_segunda = grafo_nodo.revisar_carretera(num_random, random_carretera0)
                choza_dueno = grafo_nodo.revisar_choza(num_random)            
          
                if (
                    carretera_primera == "None" and str(carretera_segunda) == "None"
                    and choza_dueno == "None" and num_random != int(random_carretera0) 
                    and num_random != int(random_carretera) and 
                    random_carretera != int(random_carretera0) 
                ):
                    primer_carretera_bien = True
                    segunda_carretera_bine = True
            grafo_nodo.agregar_carretera(num_random, random_carretera, player.color)
            grafo_nodo.agregar_carretera(random_carretera, random_carretera0, player.color)
            grafo_nodo.agregar_poblacion(num_random, player.color)
                 
    
    def manejar_mensaje(self, mensaje, jugador, lista_jugadores):
        mensaje_final = []
        try:
            if mensaje == {} or mensaje == None:
                comando = "nada"
            else:
                comando = mensaje["comando"]
        except KeyError:
            return []
        ## Agregar nuevo jugador
        if comando == "nuevo_jugador":
            self.cantidad_jugadores += 1
            color = mensaje["color"]
            jugador.color = color
            self.log_in_lock.acquire()
            respuesta = {
                "comando" : "log_in_accepted",
                "color" : color,
                "para" : "todos",
                "cantidad_jugadores" : self.cantidad_jugadores
                }
            self.log_in_lock.release()
            mensaje_final.append(respuesta)
            if self.cantidad_jugadores == cantidad_jugadores:
                self.log("Todos",
                "Hay suficientes jugadores para comenzar el juego", "None")
        ## comenzar nuevo juego 
        elif comando == "empezar_juego":
            if self.partida_en_proceso == False:
                self.ronda += 1
                self.inicializar_jugadores(lista_jugadores)
                self.dict_recursos = grafo_nodo.mostrar_recursos()
                self.comenzar_juego(lista_jugadores)
                self.mapa_chozas = grafo_nodo.poblado
                self.mapa_carreteras = grafo_nodo.carreteras
                self.partida_en_proceso = True
                self.primer_turno = self.lista_jugadores_partida[0]
            respuesta1 = {
                "comando" : "empezar_juego",
                "para" : "no turno",
                "turno" : self.primer_turno,
                "recursos" : self.dict_recursos,
                "mapa_chozas" : self.mapa_chozas,
                "mapa_carreteras" : self.mapa_carreteras
                }
            respuesta2 = {
                "comando" : "empezar_juego",
                "para" : "turno",
                "turno" : self.primer_turno,
                "recursos" : self.dict_recursos,
                "mapa_chozas" : self.mapa_chozas,
                "mapa_carreteras" : self.mapa_carreteras
            }
            
            mensaje_final.append(respuesta1)
            mensaje_final.append(respuesta2)
            self.log(self.primer_turno,
            "Comienza la partida", f"Orden de turnos {self.lista_jugadores_partida}")
        elif comando == "desconecto_jugador":
            self.cantidad_jugadores -= 1
            if self.cantidad_jugadores < 0:
                self.cantidad_jugadores = 0
       

        return mensaje_final
    
    def log(self, cliente_mensaje, evento_mensaje, detalles_mensaje):
        lista_mensaje = [cliente_mensaje, evento_mensaje, detalles_mensaje]
        self.table.rows.append(lista_mensaje)
        print(self.table)