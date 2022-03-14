#Formacion de Tablero [numero_filas, numero_col]
import random
import parametros

def TablaJ (numero_filas, numero_col):
    from parametros import NUM_BARCOS 
    num_barcos0 = NUM_BARCOS
    tabla_Jugador = []
# en los for in range no ocupe los numeros (como c y f )
    for c in range(0, numero_filas):
        tablaF = []
        for f in range(0,numero_col):
            tablaF.append(' ')
        tabla_Jugador.append(tablaF)
    
    while num_barcos0 != 0:
        numRandomC0 = random.randint(0,int(numero_col)-1)
        numRandomF0 = random.randint(0,int(numero_filas)-1)
        if tabla_Jugador[numRandomF0][numRandomC0] != "B":
            tabla_Jugador[numRandomF0][numRandomC0] = "B"
            num_barcos0 = num_barcos0 - 1
    return tabla_Jugador


def TablaO (numero_filas, numero_col):
    from parametros import NUM_BARCOS 
    num_barcos1 = NUM_BARCOS
    tabla_oponente = []

    for c in range(0, numero_filas):
        tablaO = []
        for f in range(0,numero_col):
            tablaO.append(' ')
        tabla_oponente.append(tablaO)

    while num_barcos1 != 0:
        numRandomC1 = random.randint(0,int(numero_col)-1)
        numRandomF1 = random.randint(0,int(numero_filas)-1)
        if tabla_oponente[numRandomF1][numRandomC1] != "B":
            tabla_oponente[numRandomF1][numRandomC1] = "B"
            num_barcos1 = num_barcos1 - 1
    return tabla_oponente