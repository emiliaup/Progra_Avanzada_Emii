import os
# ordena los puntos con sort y los devuelve a puntajes.txt bien

def Puntos_orden(nombre_jugador, puntos):

    with open('puntajes.txt', "rt") as puntaje:
        lista_puntaje = puntaje.readlines()
        listafinal_puntaje = []
    for l in lista_puntaje:
        listaP = l.strip().split(",")
        listafinal_puntaje.append(listaP)


    listafinal_puntaje.append([nombre_jugador, puntos])

    for l in listafinal_puntaje:
        l[1] = int(l[1])
        
    listafinal_puntaje.sort(key = lambda x: x[1], reverse = True)

    with open ('puntajes.txt', "w") as puntaje: 
        for i in listafinal_puntaje: 
            linea = i[0] + ", " + str(i[1]) +"\n"
            puntaje.write(linea) 
        puntaje.close()

    return listafinal_puntaje