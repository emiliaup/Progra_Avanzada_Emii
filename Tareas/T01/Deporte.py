with open('deportistas.csv', "rt") as depo:
    info_depo = depo.readlines()

lista_deportistas_info = []
for l in info_depo:
    listaD = l.strip().split(",")
    lista_deportistas_info.append(listaD)


class Deportista:

    def __init__(self,velociada,resistencia,felxibilidad,moral_deportista,lesionado,precio):
        self.velociada = velocidad
        self.resistencia = resistencia
        self.felxibilidad = felxibilidad
        self.lesionado = lesionado 
        self.precio = precio 
        self.moral_deportista = moral_deportista
        
with open('deportistas.csv', "rt") as depo:
    info_depo = depo.readlines()

    lista_deportistas_info = []
    for l in info_depo:
        listaD = l.strip().split(",")
        lista_deportistas_info.append(listaD)
lista_deportistas_info

class Deportista:

    def __init__(self,velociada,resistencia,felxibilidad,moral_deportista,lesionado,precio):
        self.velociada = velocidad
        self.resistencia = resistencia
        self.felxibilidad = felxibilidad
        self.lesionado = lesionado 
        self.precio = precio 
        self.moral_deportista = moral_deportista
        

class Deportes(Deportista):

    def validez_competencia(self, deportista_iee, deportista2_dcc):

        pass

    def atletismo(self, deportista1, deportista2):
        self.riesgo = 0.2
        puntaje1 = ((0.55 *deportista1[4]) +(0.2 * deportista1[6]) + (0.25 * deportista1[2]))
        puntaje2 = ((0.55 *deportista2[4]) +(0.2 * deportista2[6]) + (0.25 * deportista2[2]))
        if puntaje1 > puntaje2:
            print(f"woww gano {deportista1[0]}")
            return deportista1[0]
        else:
            print(f"wow wow gani {deportista2[0]}")
            return deportista2

    def ciclismo(self, deportista1, deportista2):
        self.riesgo = 0.35
        puntaje1 = ((0.47 *deportista1[4]) +(0.36 * deportista1[6]) + (0.17 * deportista1[1]))
        puntaje2 = ((0.47 *deportista2[4]) +(0.36 * deportista2[6]) + (0.17 * deportista2[1]))
        if puntaje1 > puntaje2:
            print(f"woww gano {deportista1[0]}")
            return deportista1[0]
        else:
            print(f"wow wow gani {deportista2[0]}")
            return deportista2
    def gimnasia (self, deportista1, deportista2):
        self.riesgo = 0.3
        puntaje1 = ((0.5 * deportista1[1])+ (0.3*deportista1[6])+(0.2*deportista1[2]))
        puntaje2 = ((0.5 * deportista2[1])+ (0.3*deportista2[6])+(0.2*deportista2[2]))
        if puntaje1 > puntaje2:
            print(f"woww gano {deportista1[0]}")
            return deportista1[0]
        else:
            print(f"wow wow gani {deportista2[0]}")
            return deportista2
    
    def natacion (self, deportista1,deportista2):
        self.riesgo = 0.25
        puntaje1 = ((deportista1[4])+(deportista1[6])+(deportista1[2]))
        puntaje1 = ((deportista1[4])+(deportista1[6])+(deportista1[2]))
        if puntaje1 > puntaje2:
            print(f"woww gano {deportista1[0]}")
            return deportista1[0]
        else:
            print(f"wow wow gani {deportista2[0]}")
            return deportista2
    
#nombre,flexibilidad,moral,precio,velocidad,lesionado,resistencia
'''
class Campeonato(Deportista):

    def __init__(self):
        super().__init__()

    def realizar_competencia(self):

    def premiar_deportista(self):

    def nivel_moral(self):

'''