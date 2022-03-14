import socket
import threading
import json
import random
import string
from PyQt5.QtCore import pyqtSignal, QObject
from interfaz import Controlador


class Cliente(QObject):


    def __init__(self, port, host):
        super().__init__()
        self.port = port
        self.host = host
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.controlador = Controlador(self)
        
        try:
            self.socket_cliente.connect((self.host, self.port))
            self.conectado = True
            thread = threading.Thread(target=self.escuchar_thread, daemon=True)
            thread.start()

        except ConnectionError:
            print(f"No se pudo conectar a {self.host}:{self.port}")
            self.controlador.mostrar_sala_espera_full()
            self.controlador.error_coneccion()
            self.socket_cliente.close()

 
    def escuchar_thread(self):
        try:
            while self.conectado:
                mensaje = self.recibir()
                self.controlador.manejar_mensaje(mensaje)

        except ConnectionResetError:
            print("Error de conexión con el servidor")
        finally:
            self.socket_cliente.close()

    def enviar(self, mensaje):
        orden_chunck = 0
        msg_bytes = self.codificar_mensaje(mensaje)
        largo_de_msg = len(msg_bytes)
        bytes_mensaje =bytearray()
        #mande 4 bytes del len del mensaje entero en big endian
        primer_chunck_big = len(msg_bytes).to_bytes(4, byteorder='big')
        self.socket_cliente.sendall(primer_chunck_big)
        
        if largo_de_msg <= 60 and largo_de_msg > 0:
            bytes_mensaje += msg_bytes
            # mande 60 bytes de mensaje (si es mas chico que 60 agregue 0)  
            # tambien mande el 4 chunck diciendo el largo del chunck mandado
            while len(bytes_mensaje) <= 64:
                bytes_mensaje += b'\x00'
            segundo_chunck_small = orden_chunck.to_bytes(4, byteorder='little')
            self.socket_cliente.sendall(segundo_chunck_small + bytes_mensaje) 


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
                self.socket_cliente.sendall(primer_chunck_little) 
                self.socket_cliente.sendall(segundo_chunck) 
                orden_chunck += 1
    
    def recibir(self):
    
        largo_respuesta = 0
        respuesta_bytes_largo = self.socket_cliente.recv(4)
        largo_respuesta = int.from_bytes(respuesta_bytes_largo, byteorder = "big")
        
        bytes_mensaje =bytearray()
      
        while len(bytes_mensaje) < largo_respuesta and largo_respuesta > 0:
            respuesta_little_bytes = self.socket_cliente.recv(4)
            tamano_chunk =min(largo_respuesta -len(bytes_mensaje), 60)
            bytes_mensaje += self.socket_cliente.recv(tamano_chunk)
        if largo_respuesta > 0:
            mensaje = self.decodificar_mensaje(bytes_mensaje)
        else:
            mensaje = {
                "comando" : "nada"
            }

        return mensaje

    @staticmethod
    def codificar_mensaje(mensaje):

        try:
            # Create JSON object
            json_mensaje = json.dumps(mensaje)
            # Encode JSON object
            bytes_mensaje = json_mensaje.encode('utf-8')
         

            return bytes_mensaje
        except json.JSONDecodeError:
            return b""

    @staticmethod
    def decodificar_mensaje(bytes_mensaje):
        largo = int.from_bytes(bytes_mensaje, byteorder = "big")
        if largo != 0:
            try:
                mensaje = json.loads(bytes_mensaje)
                return mensaje
            except json.JSONDecodeError:
                return dict()



if __name__ == '__main__':
    port = 3245
    host = 'localhost'
    client = Cliente(port, host)

