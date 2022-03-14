import socket
import threading
import json
import time
import random
from jugadores import Jugador, Nombres
from logica import Logica
from beautifultable import BeautifulTable

with open('parametros.json') as file:
    data = json.load(file)
    cantidad_jugadores = data["CANTIDAD_JUGADORES_PARTIDA"]

class Servidor:

    lista_jugadores_lock = threading.Lock()

    def __init__(self, port, host, log_activado=True):
        self.host = host
        self.port = port
        self.log_activado = log_activado
        self.log("Cliente", "Evento", "Detalles")
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen(cantidad_jugadores)
        self.log("None","Incializando servidor",f"Servidor escuchando en {self.host}:{self.port}")
        self.nombre = Nombres()
        self.logica = Logica()
        self.lista_jugadores = []
        self.sockets = {}
        self.todos_jugadores = []
        datos = self.nombre.nombres()
        self.datos_usuarios = self.nombre.crear_lista_jugadores(datos)
           

        thread = threading.Thread(target=self.aceptar_clientes)
        thread.start()

    def lista_clientes(self):
        
        self.lista_jugadores = self.datos_usuarios
        self.todos_jugadores.append(self.lista_jugadores[0])
        self.lista_jugadores.pop(0)
    
    def aceptar_clientes(self):
       
        while True: 
            client_socket, address = self.socket_server.accept()
            self.sockets[client_socket] = address
            self.log(address, "Se conecto un cliente", "Sala de espera")
            jugador = None

            self.lista_jugadores_lock.acquire()
            if (
                self.logica.partida_en_proceso == False and 
                len(self.todos_jugadores) < cantidad_jugadores
            ): 
                self.lista_clientes()
                for jugador in self.todos_jugadores:
                    if jugador.socket_cliente is None:
                        jugador.username = None
                        jugador.socket_cliente = client_socket
                        jugador.address = address

                        self.lista_jugadores_lock.release()
                        mensaje = {
                            "comando" : "nuevo_jugador",
                            "color" : jugador.color
                            }

                        mandar = self.logica.manejar_mensaje(mensaje, jugador, 
                        self.todos_jugadores)
                        self.enviar_a_todos(mandar)
                        break
                if jugador is not None:
               
                    listening_client_thread = threading.Thread( \
                        target=self.escuchar_cliente, \
                        args=(jugador, ), \
                        daemon=True)
                    listening_client_thread.start()
                else:              
                    self.log(address, "no se pudo ingresar el cliente", "None")
            else:              
                ### agregar error mucha gente
                self.lista_jugadores_lock.release()
                self.log(address, "No se pudo conectar cleinte",
                "mucha gente/ ya comenzo juego")
                mensaje = {
                    "comando" : "no_juego"
                }
                self.enviar(mensaje, client_socket)
    
    def recibir(self, socket_cliente):
        largo_respuesta = 0
        respuesta_bytes_largo = socket_cliente.recv(4)
        mensaje_primer_cunck = self.decodificar_mensaje(respuesta_bytes_largo)
        largo_respuesta = int.from_bytes(respuesta_bytes_largo, byteorder = "big")
        
        bytes_mensaje =bytearray()
        
        while len(bytes_mensaje) < largo_respuesta and largo_respuesta > 0:
            respuesta_little_bytes = socket_cliente.recv(4)
            tamano_chunk =min(largo_respuesta -len(bytes_mensaje), 60)
            bytes_mensaje += socket_cliente.recv(tamano_chunk)
        if largo_respuesta > 0:
            mensaje = self.decodificar_mensaje(bytes_mensaje)
        else:
            mensaje = {
                "comando" : "nada"
            }
        if mensaje["comando"] != "nada":
            self.log("recibir mensaje", mensaje, socket_cliente)
        return mensaje
    

    def escuchar_cliente(self, jugador):
        try:
            while True:
                mensaje = self.recibir(jugador.socket_cliente)
                lista_respuestas=self.logica.manejar_mensaje(mensaje,jugador,self.todos_jugadores)
                self.enviar_lista_respuestas(jugador, lista_respuestas)

        except ConnectionResetError:
            self.log(jugador.address, "Se desconecto un cliente", "None")
    
            self.nombre.jugador_desconecto(jugador.color)
            mensaje = {
                "comando" : "desconecto_jugador"
            }
            self.logica.manejar_mensaje(mensaje, jugador, self.todos_jugadores)
            self.eliminar_cliente(jugador)

        
        
    def enviar_lista_respuestas(self, jugador, mensaje_lista):

        for dict_respuestas in mensaje_lista:
            persona = dict_respuestas["para"]
            if persona == "todos":
                self.enviar_a_todos(dict_respuestas)
            elif persona == "turno":
                if jugador.color == dict_respuestas["turno"]:
                    self.enviar(dict_respuestas, jugador.socket_cliente)
            elif persona == "no turno":
                if jugador.color != dict_respuestas["turno"]:
                    self.enviar(dict_respuestas, jugador.socket_cliente)
    
    def enviar_a_todos(self, mensaje_lista):
        for mensaje in mensaje_lista:
            try:
                for jugador in self.todos_jugadores:
                    self.enviar(mensaje, jugador.socket_cliente)
            
            except ConnectionError:
                print("Error")
  
    def log(self, cliente_mensaje, evento_mensaje, detalles_mensaje):
        table = BeautifulTable()
        lista_mensaje = [cliente_mensaje, evento_mensaje, detalles_mensaje]
        table.rows.append(lista_mensaje)
        print(table)

    def enviar(self, mensaje, socket_cliente):
        self.log("mandar mensaje", mensaje, socket_cliente)
        msg_bytes = self.codificar_mensaje(mensaje)

        largo_de_msg = len(msg_bytes)
        bytes_mensaje =bytearray()
        orden_chunck = 0
        #mande 4 bytes del len del mensaje entero en big endian
        primer_chunck_big = len(msg_bytes).to_bytes(4, byteorder='big')
        socket_cliente.sendall(primer_chunck_big)
        
        if largo_de_msg <= 60 and largo_de_msg > 0:
            bytes_mensaje += msg_bytes
            # mande 60 bytes de mensaje (si es mas chico que 60 agregue 0)  
            # tambien mande el 4 chunck diciendo el largo del chunck mandado
            while len(bytes_mensaje) <= 64:
                bytes_mensaje += b'\x00'
            segundo_chunck_small = orden_chunck.to_bytes(4, byteorder='little')
            socket_cliente.sendall(segundo_chunck_small + bytes_mensaje) 
      


        elif largo_de_msg > 60:
         
            chunck_enviado = 0
            mensajes_enviados = 0
            while mensajes_enviados <= largo_de_msg:
                bytes_mensaje =bytearray()
                segundo_chunck = msg_bytes[chunck_enviado: chunck_enviado + 60]
                while len(segundo_chunck) < 60:
                    segundo_chunck += b'\x00'

                
                mensajes_enviados += len(segundo_chunck)
                chunck_enviado += 60
                bytes_mensaje += segundo_chunck
          
                primer_chunck_little = orden_chunck.to_bytes(4, byteorder='little')
                socket_cliente.sendall(primer_chunck_little) 
                socket_cliente.sendall(segundo_chunck)
                orden_chunck += 1
         
    @staticmethod
    def codificar_mensaje(mensaje):
    
        try:
            # Create JSON object
            json_mensaje = json.dumps(mensaje)
            # Encode JSON object
            bytes_mensaje = json_mensaje.encode()

            return bytes_mensaje
        except json.JSONDecodeError:
            return b""

    @staticmethod
    def decodificar_mensaje(bytes_mensaje):
        
        try:
            mensaje = json.loads(bytes_mensaje)
            return mensaje
        except json.JSONDecodeError:
            return dict()

    def eliminar_cliente(self, jugador):

        self.lista_jugadores_lock.acquire()
        jugador.socket_cliente.close()
        jugador.socket_cliente = None
        jugador.address = None
        for num in range (0,len(self.todos_jugadores)):
            if jugador == self.todos_jugadores[num]:
                self.todos_jugadores.pop(num)
    
        self.lista_jugadores_lock.release()