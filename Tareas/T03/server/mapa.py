import json
from random import shuffle, choice
from generador_grilla import GeneradorGrillaHexagonal 

with open('grafo.json') as file:
    data = json.load(file)
dimension_mapa = data["dimensiones_mapa"]
dic_hexagonos = data["hexagonos"]
dic_nodos = data["nodos"]

numero_de_hex = [2,3,4,5,6,8,9,10,11,12]
shuffle(numero_de_hex)
recurso = ["trigo", "madera", "arcilla"]
recurso_extra = choice(recurso)
lista_recursos=["trigo","madera","trigo","madera","arcilla","arcilla","trigo","madera","arcilla"]
lista_recursos.append(recurso_extra)
shuffle(lista_recursos)


class Grafo:
    def __init__(self, lista_adyacencia=None, lista_adyacencia_hex=None):
        self.lista_adyacencia = lista_adyacencia or {}
        self.lista_adyacencia_hex = lista_adyacencia_hex or {}
        self.carreteras = {}
        self.poblado = {}
        self.ruta_visitadas = []
        self.nodos_recorridos = []
        self.ruta_mas_larga = []

    def armar_conexiones(self):
        for key, value in self.lista_adyacencia.items():
            valor1 = key
            for num in value:
                valor2 = num
                if int(valor1) > int(valor2):
                    mensaje = "label_" + str(valor2) + "_" + str(valor1)
                    self.carreteras[mensaje] = "None"
                else:
                    mensaje = "label_" + str(valor1) + "_" + str(valor2)
                    self.carreteras[mensaje] = "None"
        
    def armar_poblados(self):
        for key, value in self.lista_adyacencia.items():
            mensaje = "choza_" + key
            self.poblado[key] = [mensaje, "None"]

    def agregar_poblacion(self, numero_nodo, color_jugador):
        #Perdon lo feo pero esto verifica que hay dos carreteras y ademas q no haya una 
        #poblacion al lado de un nodo
        numero_carreteras_final = 0
        ya_hay_choza = False
        for vecinos in self.carreteras:
            color_carretera = self.carreteras[vecinos]
            lista_palabra = vecinos.split('_')
            nodo1 = lista_palabra[-1]
            nodo2 = lista_palabra[-2]
            numero_carreteras = 0
            choza2 = self.poblado[nodo2][1]
            choza1 = self.poblado[nodo1][1]
            if int(nodo1) == int(numero_nodo) and color_carretera == color_jugador:
    
                numero_nodo = int(nodo1)
                numero_carreteras_final += 1
                for vecinos in self.carreteras:
                    color_carretera = self.carreteras[vecinos]
                    lista_palabra = vecinos.split('_')
                    nodo3 = lista_palabra[-1]
                    nodo4 = lista_palabra[-2]
                    if int(nodo3) == int(numero_nodo) and color_carretera == color_jugador:
                        numero_carreteras += 1 
                    elif int(nodo4) == int(numero_nodo) and color_carretera == color_jugador:
                        numero_carreteras += 1 
                numero_carreteras_final += numero_carreteras   
            elif int(nodo2) == int(numero_nodo) and color_carretera == color_jugador:
                numero_carreteras_final += 1
                numero_nodo = int(nodo2)
                for vecinos in self.carreteras:
                    color_carretera = self.carreteras[vecinos]
                    lista_palabra = vecinos.split('_')
                    nodo3 = lista_palabra[-1]
                    nodo4 = lista_palabra[-2]
                    if int(nodo3) == int(numero_nodo) and color_carretera == color_jugador:
                        numero_carreteras += 1 
                    elif int(nodo4) == int(numero_nodo) and color_carretera == color_jugador:
                        numero_carreteras += 1 
                numero_carreteras_final += numero_carreteras
            else:
                if numero_carreteras < 2:
                    numero_carreteras = 0
            if choza1 != "None" and choza2 != "None":
                ya_hay_choza = True

        if numero_carreteras_final >= 2 and ya_hay_choza == False:
            #Hice esto para que quede igual al dic original
            msg = "choza_" + str(numero_nodo)
            value = [msg,color_jugador]
            self.poblado[str(numero_nodo)] = value
            return True

        else:
            print("No hay carreteras suficientes")
            print("o ya hay un poblado en el nodo en un sus vecinos")    
            return False

    def agregar_carretera(self, nodo0, nodo1, color):
        duneo_carretera = self.revisar_carretera(nodo0, nodo1)
         ## Agrega carreteras 
        if duneo_carretera == "None":
            nodo0 = int(nodo0)
            nodo1 = int(nodo1)
            for vecinos in self.carreteras:
                lista_palabra = vecinos.split('_')
                nodo2 = lista_palabra[-1]
                nodo3 = lista_palabra[-2]
                if nodo0 == int(nodo2) and nodo1 == int(nodo3) :
                    self.carreteras[vecinos] = color
                elif nodo1 == int(nodo2) and nodo0 == int(nodo3):
                    self.carreteras[vecinos] = color
        else:
            print(f"Carretera{nodo0, nodo1} ya tiene dueno")
            print(duneo_carretera)


    def revisar_carretera(self,numero0,numero1):
        # return el dueno de cierta carretera
        if int(numero0) < int(numero1):
            num0 = numero0
            num1 = numero1
        else: 
            num0 = numero1
            num1 = numero0
        for label, carretera in self.carreteras.items():
            numero = "label_" + str(num0) + "_" + str(num1)
            if label == numero:
                return carretera
    
    def revisar_choza(self, numero_choza):
        for key, value in self.poblado.items():
            dueno_choza = value[1]
            if int(key) == int(numero_choza):
                return dueno_choza

    def mostrar_recursos(self):
        dict_recrusos = {}
        for key, value in self.lista_adyacencia_hex.items():
            new_value = value[-1]
            dict_recrusos[key] = new_value
            
        return dict_recrusos

    def carretera_mas_larga(self):
        for vecinos , dueno in self.carreteras.items():
            #Va por todos los nodos y por sus conecciones
            self.carretera_visitadas = []
            self.ruta_larga_de_jugador = []
            lista_palabra = vecinos.split('_')
            nodo1 = lista_palabra[-1]
            nodo2 = lista_palabra[-2]
            if str(dueno) != "None":
                self.ruta_visitadas.append([dueno,[]])
                self.recorrer_carreteras(nodo1, dueno)
                self.recorrer_carreteras(nodo2, dueno)

        ganador_dueno = ""
        ruta_mas_larga = 0    
        for ganador in self.ruta_visitadas:
            dueno1 = ganador[0]
            ruta_larga = len(ganador[1])
            if int(ruta_larga) > ruta_mas_larga:
                ruta_mas_larga = ruta_larga
                ganador_dueno = dueno1
            elif int(ruta_larga) == ruta_mas_larga and dueno1 not in ganador_dueno:
                ganador_dueno = "empate " + ganador_dueno +" y "+ dueno1

        print(f"La ruta mas larga es de color {ganador_dueno}")
        print(f"la ruta es de largo {ruta_mas_larga}")

        ## si quieres visualizar las conecciones bien puedes ocupar esto:
        '''
        conex_repetidas = []
        for ganador in self.ruta_visitadas:
            if len(ganador[1]) > 0 and ganador[1] not in conex_repetidas :
                conex_repetidas.append(ganador[1])
                print("dueno", ganador[0])
                print("ruta",ganador[1])
        '''

    def recorrer_carreteras(self, nodo, dueno):
        nodo_str = str(nodo)
        #Hice un loop que se llama a si mismo para que vaya entrando a las conecciones
        # y revisando las conecciones de las conecciones perdon lo feo jeje
        if nodo not in self.nodos_recorridos:
            self.nodos_recorridos.append(nodo)
            lista_conecciones = self.lista_adyacencia[nodo_str]
            for nodo1 in lista_conecciones:
                dueno_carretera = self.revisar_carretera(nodo, nodo1)
                if int(nodo) > int(nodo1):
                    msg = str(nodo1) + "->" + str(nodo)
                else:
                    msg = str(nodo) + "->" + str(nodo1)
    
                if msg not in self.carretera_visitadas:
                    self.carretera_visitadas.append(msg)
                    if dueno_carretera == dueno:
                        self.ruta_larga_de_jugador.append(msg)
                        ##substituye la carretera mas larga antes por la nueva encontrada
                        for num in range(0, len(self.ruta_visitadas)):
                            if (
                                self.ruta_visitadas[num][0] == dueno and
                                len(self.ruta_larga_de_jugador) > 
                                len(self.ruta_visitadas[num][1])
                                ):

                                self.ruta_visitadas.pop(num)   
                                lista = []
                                lista.append(dueno)
                                lista.append(self.ruta_larga_de_jugador)
                                self.ruta_visitadas.append(lista)
                             
                        self.recorrer_carreteras(nodo1, dueno)
                        #recorro las conecciones de las conecciones 
        
    def __repr__(self):
        texto_nodos = []
        for nodo, vecinos in self.lista_adyacencia_hex.items():
            texto_nodos.append(f"Vecinos {nodo}: {vecinos[0:-2]}.")
        return "\n".join(texto_nodos)



## Perdon lo feo pero aca preparo el grafo para
## jugar con dict de recursos, conexiones y mas:)

n = 0
for key, value in dic_hexagonos.items():
    lista_info = [numero_de_hex[n],lista_recursos[n]]
    dic_hexagonos[key].append(lista_info)
    n += 1
  
amistades ={}
for numero in range(0,10):
    lista_vecinos = dic_hexagonos[str(numero)]
    nombre =  str(numero)
    amistades[nombre] = lista_vecinos

grafo_nodo = Grafo(dic_nodos, amistades)
grafo_nodo.armar_conexiones()
grafo_nodo.armar_poblados()

#####################
## Aca abajo puedes testear la carretera mas larga agregando carreteras
# y despues ejecutando grafo_nodo.carretera_mas_larga()

'''
grafo_nodo.agregar_carretera(0,1,"azul")
grafo_nodo.agregar_carretera(1,5,"azul")
grafo_nodo.agregar_poblacion(5, "azul")

grafo_nodo.agregar_carretera(13,18,"rojo")
grafo_nodo.agregar_carretera(18,23,"rojo")
grafo_nodo.agregar_carretera(23,28,"rojo")
grafo_nodo.agregar_carretera(18,17,"verde")
grafo_nodo.agregar_poblacion(18,"verde")
grafo_nodo.agregar_carretera(5,6,"azul")
grafo_nodo.agregar_carretera(6,11,"rojo")


grafo_nodo.carretera_mas_larga()

'''