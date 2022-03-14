from threading import Lock  
from random import shuffle
import json

class Jugador:
     
    lock_juegos = Lock()
    def __init__(self, usuario, color):
        self.username = usuario
        self.puntos_victoria = 0
        self.color = color
        self.address = None
        self.socket_cliente = None
        self.turno = 0

class Nombres:

    def __init__(self):
        self.lista_nombres = [] 
        self.lista_color =["azul","rojo","verde","violeta"]    
        self.lista_jugadores = []
      

    def nombres(self):
        with open('parametros.json') as file:
            data = json.load(file)
        cantidad_jugadores = data["CANTIDAD_JUGADORES_PARTIDA"]
        shuffle(self.lista_color)

        for i in range(0,int(cantidad_jugadores)):
            self.lista_nombre = []
            nombre = "jugador_hermoso_" + str(i)
            color = self.lista_color[0]
            self.lista_color.pop(0)
            self.lista_nombre.append(color)
            self.lista_nombre.append(nombre)
            self.lista_nombres.append(self.lista_nombre)
            shuffle(self.lista_nombres)
  
        
        return self.lista_nombres

    def nuevo_jugador(self):
        self.jugador = self.lista_nombres[0]
        self.lista_nombres.pop(0)
        return self.jugador
    
    def agregar_jugador_pendiente(self, lista_jugadores, adress):
        #[Nombre, color, adress]
        for num in range (0,len(lista_jugadores)):
            if adress in lista_jugadores[num]:
                lista_nueva = [lista_jugadores[0],lista_jugadores[1]]
                self.lista_nombres.append(lista_nueva)
                lista_jugadores.pop(num)

    def jugador_desconecto(self,color):
        usuario = "Amigo"
        jugador = Jugador(usuario, color)
        self.lista_jugadores.append(jugador)

    def crear_lista_jugadores(self,lista_nombres):
        for dato in self.lista_nombres:
            jugador = Jugador(dato[1],dato[0])
            self.lista_jugadores.append(jugador)
        return self.lista_jugadores
