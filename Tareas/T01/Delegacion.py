from abc import ABC, abstractmethod
import random

with open('delegaciones.csv', "rt") as deleg:
    info_delegacion = deleg.readlines()
    lista_delegacion_info = []
    for l in info_delegacion:
        listaD = l.strip().split(",")
        lista_delegacion_info.append(listaD)

moralL = []
delegacionL = []
equipoL = []
medallasL = []
dineroL = []

for i in range (0,len(lista_delegacion_info[0])):
    if lista_delegacion_info[0][i] == "Delegacion":
        delegacionL.append(lista_delegacion_info[1][i])
        delegacionL.append(lista_delegacion_info[2][i])
    elif lista_delegacion_info[0][i] == "Moral":
        moralL.append(lista_delegacion_info[1][i])
        moralL.append(lista_delegacion_info[2][i])
    elif lista_delegacion_info[0][i] == "Equipo":
        listaL1 = lista_delegacion_info[1][i].split(";")
        listaL2 = lista_delegacion_info[2][i].split(";")
        equipoL.append(listaL1)
        equipoL.append(listaL2)
    elif lista_delegacion_info[0][i] == "Medallas":
        medallasL.append(lista_delegacion_info[1][i])
        medallasL.append(lista_delegacion_info[2][i])
    elif lista_delegacion_info[0][i] == "Dinero":
        dineroL.append(lista_delegacion_info[1][i])
        dineroL.append(lista_delegacion_info[2][i])

info_IEEEsparta = []
info_DCCrotona = []

if delegacionL[0] == "DCCrotona":
    info_DCCrotona.append(equipoL[0])
    info_DCCrotona.append(medallasL[0])
    info_DCCrotona.append(moralL[0])
    info_DCCrotona.append(dineroL[0])
    info_IEEEsparta.append(equipoL[1])
    info_IEEEsparta.append(medallasL[1])
    info_IEEEsparta.append(moralL[1])
    info_IEEEsparta.append(dineroL[1])
elif delegacionL[1]== "DCCrotona":
    info_IEEEsparta.append(equipoL[0])
    info_IEEEsparta.append(medallasL[0])
    info_IEEEsparta.append(moralL[0])
    info_IEEEsparta.append(dineroL[0])
    info_DCCrotona.append(equipoL[1])
    info_DCCrotona.append(medallasL[1])
    info_DCCrotona.append(moralL[1])
    info_DCCrotona.append(dineroL[1])


import random
class IEEEsparta:

    def __init__(self):
        self.excelencias_respeto_I = 0
        self.implementos_deportivos_I = 0
        self.implementos_medicos_I = 0
        self.entrenamiento_deportivo_I = 1.7

    def calcular_fortalezas_debilidad(self):
        excelencias_r = round(random.uniform(0.4, 0.8),2)
        self.excelencias_respeto_I += excelencias_r
        implementos_d = round(random.uniform(0.3, 0.7),2)
        self.implementos_deportivos_I += implementos_d
        implementos_m = round(random.uniform(0.2, 0.6),2)
        self.implementos_medicos_I += implementos_m
        return [self.excelencias_respeto_I,self.implementos_deportivos_I, self.implementos_medicos_I,
         self.entrenamiento_deportivo_I]
class DCCrotona:

    def __init__(self):
        self.excelencias_respeto_D = 0
        self.implementos_deportivos_D = 0
        self.implementos_medicos_D = 0
        self.entrenamiento_deportivo_D = 1.7


    def calcular_fortalezas_debilidad(self):
        excelencias_r = round(random.uniform(0.3, 0.7),2)
        self.excelencias_respeto_D += excelencias_r
        implementos_d = round(random.uniform(0.2, 0.6),2)
        self.implementos_deportivos_D += implementos_d
        implementos_m = round(random.uniform(0.4, 0.8),2)
        self.implementos_medicos_D += implementos_m
        return [self.excelencias_respeto_D,self.implementos_deportivos_D, self.implementos_medicos_D, 
        self.entrenamiento_deportivo_D]
       
class Delegaciones:

    def __init__(self,delegacion,entrenador, equipo, medallas, moral,
     dinero,habilidad_especial_TF, excelencias_respeto, implementos_deportivos, 
     implementos_medicos, entrenamiento_deportivo):
        self.delegacion_n = delegacion
        self.entrenador = entrenador
        self.medallas = int(medallas)
        self.equipo = equipo 
        self.moral = float(moral)
        self.dinero = int(dinero)
        self.habilidad_especial_TF = habilidad_especial_TF
        self.excelencias_respeto = excelencias_respeto
        self.implementos_deportivos = implementos_deportivos
        self.implementos_medicos = implementos_medicos
        self.entrenamiento_deportivo = entrenamiento_deportivo

    
    def fichar_deportista(self, precio, deportista):
       
        if self.moral > 20 and precio < self.dinero:
            self.dinero = self.dinero - precio
            self.equipo.append(deportista)
        elif self.moral < 20 or precio > self.dinero:
            print(f"La moral de tu delegacion esta muy baja {self.moral} o no tienes diner {self.dinero}")
        
    def entrenar_deportista(self):
        if self.dinero >= 30:
            self.dinero -= 30
            return True
        else:
            print("oops no tienes el dinero suficiente")
            return False

    def sanar_deportista(self,moral_deportista):
        if self.dinero >= 30:
            self.dinero -= 30
            resultado_sanar = (moral_deportista * (self.implementos_medicos + self.excelencias_respeto))/200
            numero_random_sanar = round(random.uniform(0, 1), 2)
            if numero_random_sanar <= resultado_sanar:
                print("Yayy se sano")
                return True
            else:
                print("que malaaa suerte no se pudo sanar")
        else:
            print("uyyy no se pudo sanar:/")
            return False
    # Poner True a deportista sano

    def comprar_tecnologia(self):
        if self.dinero >= 20:
            self.dinero -= 20 
            self.implementos_medicos += (self.implementos_medicos * 0.10)
            self.implementos_deportivos += (self.implementos_deportivos *0.10)
            print(f"se compro la tech!, ahora tienes {self.dinero}")
        else:
            print("no tienes suficiente $ :/")

    def usar_habilidad_especial(self):
        if self.dinero >= 20 and self.delegacion_n == "IEEEsparta" and self.habilidad_especial_TF != False:
            self.dinero -= 20
            print("AAAAaa grito de batalla!")
            self.habilidad_especial_TF = False
            return True
        ## toda la moral de los deportistas 100%s
        elif self.dinero >= 20 and self.delegacion_n == "DCCrotona" and self.habilidad_especial_TF != False:
            self.dinero -= 20
            print("yayyy tenemos una medalla mas!")
            self.medallas += 1
            self.dinero += 100
            self.habilidad_especial_TF = False
            return True
        else:
            print(f"oops hubo un error, ya ocupaste tu habilidad especial {self.habilidad_especial_TF}") 
            print(" no tienes dinero suficiente", self.dinero)
