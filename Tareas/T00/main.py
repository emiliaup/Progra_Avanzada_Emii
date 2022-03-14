import random
import parametros
import Tablero_completo
import Bombas
import sys 

seguir_juego = True
while seguir_juego == True:

    print("\n","*"*5, "Menu de Inicio", "*"*5)
    print(f" \n Selecciona una opcion: \n [0] Iniciar Partida \n [1] Ver Ranking \n [2] Salir")
    respuesta_inicial = "None error "
    respuesta_inicial = str(input())
##Iniciar
    if respuesta_inicial == "0":
    #Nombre/ apodo
        nombreBien = False 
        tableroBien = False
        while nombreBien == False:
            print("Apodo para Jugador (minimo 5 caracters, solo numeros y letras)")
            nombre_jugador = str(input())
            nombreBien = nombre_jugador.isalnum()
            if nombreBien == False or len(nombre_jugador) < 5:
                print("oops hubo un error intente denuevo :)")
                nombreBien = False
                
            if nombreBien == True:
                print(f"Hola! {nombre_jugador} Listo? \n [0] Si listoo!")
                print(f" [1] noo cambiar nombre \n [2] Menu de inicio")
                respuesta_nombre = "None Error "
                respuesta_nombre = str(input())
                if respuesta_nombre == "0":
                        nombreBien = True
                        TodoB = True
                elif respuesta_nombre == "2":
                    nombreBien = True
                    TodoB = False
                    tableroBien = True
                    barcos_oponente = 0
                    barcos_jugador = 0
                
                else:
                    nombreBien = False
                    print("oops hubo un error")
                    #porte de Tablero
    
        while tableroBien == False:
            print(f"Arme su tablero! Elije el numero de filas y de columnas (minimo 3 y max 15)")
            numero_filas = str(input("filas = "))
            numero_col = str(input("columnas = "))
            if numero_col.isdigit() == False or numero_filas.isdigit()== False \
                or int(numero_filas) < 3 or int(numero_filas) > 15 or \
                    int(numero_col) < 3 or int(numero_col) > 15 :

                tableroBien == False
                print(f"[ {numero_filas} {numero_col} ] oops hubo un error :0 intenta de nuevo ")
                numero_col = int(numero_col)
                numero_filas = int(numero_filas)
            else:
                tableroBien = True
    ## Tablero_completo
        if TodoB == True:
            from Tablero_completo import TablaJ
            tabla_jugador = TablaJ(int(numero_filas),int(numero_col))

            from Tablero_completo import TablaO
            tabla_oponente = TablaO(int(numero_filas), int(numero_col))
            
            from parametros import NUM_BARCOS 
            NUM_B = NUM_BARCOS

            from parametros import RADIO_EXP
            num_r = RADIO_EXP
    ## Iniciar Juego
        
            barcos_oponente = NUM_B
            barcos_jugador = NUM_B
            Lista_Base = [
                ["A",0],["B",1],["C",2],["D",3],["E",4],["F",5],["G",6],["H",7],["I",8],
                ["J",9],["K",10],["L",11],["M",12],["N",13],["O",14]
                ]
            bomba_especial = 1

        while barcos_oponente != 0 and barcos_jugador != 0 and TodoB == True:
            hit_barco0 = True
            hit_barcos1 = True 
        # Repeticion de Jugador
            while hit_barco0 == True and barcos_oponente != 0 and barcos_jugador != 0:
                hit_barcos1 = True
                from tablero import print_tablero
                tabla_final = print_tablero(tabla_oponente, tabla_jugador)
                
                print("wow wow comencemos!", "\n", "[0] Tirar bomba jeje")
                print(" [1] Rendirme :0", "\n", "[2] Salir del juego")
                respuesta_nombre = "None error "
                respuesta_menu = str(input())

                if respuesta_menu == "1":
                    print(f"seguro que te quieres rendir?")
                    print(f" [0] siii \n [1] Noo ")
                    respuesta_rendir = str(input())
                    if respuesta_rendir == "0":
                        barcos_jugador = 0
                        print("ME RINDO")
                        hit_barco0 = False
                    else:
                        print("Sigue jugando! Tu puedes :)")
                elif respuesta_menu == "2":
                    sys.exit("Nos veremos de nuevo jeje :)")

                elif respuesta_menu == "0": 
                    Cordenadas_bien = False
                    while Cordenadas_bien == False:
                        print("Elija la cordenada [Numero, Letra]", "\n", "Numero: ")
                        numero_cordenada = "None error"
                        numero_j = "None Error"
                        numero_cordenada = str(input())
                        print("Letra: ")
                        letra_j = str(input())   
            
                        for l in Lista_Base:
                            if l[0] == letra_j.upper():
                                letra_cordenada = l[1]                      

                        if numero_cordenada.isdigit() == True and \
                            numero_cordenada.isalnum() == True and letra_j.isalpha() == True:

                            Cordenadas_bien = True
                            numero_cordenada = int(numero_cordenada)

                            if int(numero_cordenada) < int(numero_filas) and \
                                int(numero_cordenada) >= 0 and letra_cordenada < int(numero_col) and \
                                    letra_cordenada >= 0:
                                Cordenadas_bien = True
                                numero_cordenada = int(numero_cordenada)
                            else:
                                Cordenadas_bien = False
                                print("Su cordenada no existe, intente otra vez")

                    print("Elija su armaaa", "\n", "[0] Bomba Regular")
                    if bomba_especial == 1:
                        print(" [1] Bomba Especial jeje")
                        print("OjO que uno solo lo puede ocupar UNA vez por partida")
                    respuesta_bomba = "None error"
                    respuesta_bomba = str(input())
                ## Bomba normal
                    if respuesta_bomba == "0":
                        from Bombas import Bomba_Normal
                        resultado = Bomba_Normal(tabla_oponente, numero_cordenada, \
                             letra_cordenada, barcos_oponente)
                        hit = resultado[1]
                        tabla_oponente = resultado[0]
                        barcos_oponente = resultado[2]

                        if hit == True:
                            hit_barco0 = True
                        else:
                            hit_barco0 = False

                ## Bomba 1 Especial 
                    elif respuesta_bomba =="1" and bomba_especial == 1:
                        print("UUUU, que bomba especial quieres usar?")
                        print("[0] La X jeje XD", "\n", "[1] El Diamante <>")
                        print("[2] La mata Cruz T", "\n", "[3] Todavia ninguna jeje")
                        respuesta_bomba = "None error"
                        respuesta_bombaE = str(input())
                        let = letra_cordenada
                        num = int(numero_cordenada)

                        from Bombas import Bomba_Especiales
                        resultado2 = Bomba_Especiales(tabla_oponente,int(numero_col), \
                             int(numero_filas),respuesta_bombaE, num, let, num_r, barcos_oponente)

                        if resultado2 == None:
                            bomba_especial = 1
                            hit_barcos1 = False
                        else:
                            hit = resultado2[1]
                            bomba_especial = bomba_especial - 1
                            barcos_oponente = resultado2[2]
                            tabla_oponente = resultado2[0]
                            
                        if hit == True:
                            hit_barco0 = True
                        else:
                            hit_barco0 = False

                    else:
                        print("uyyyy no elijiste ninguna bomba")
                        hit_barcos1 = False

                else:
                    print("oopsss hubo un error, conteste de nuevo")
               
        ## Enemigo
            while hit_barcos1 == True and barcos_jugador != 0 and barcos_oponente != 0:
                numero_cordenadaO = random.randint(0,int(numero_filas)-1)
                letra_cordenadaO = random.randint(0,int(numero_col)-1)
                
                if tabla_jugador[int(numero_cordenadaO)][letra_cordenadaO] == "B":
                    barcos_jugador = barcos_jugador - 1                 
                    tabla_jugador[int(numero_cordenadaO)][letra_cordenadaO] = "F"
                    hit_barcos1 = True
                elif tabla_jugador[int(numero_cordenadaO)][letra_cordenadaO] == " ":
                    tabla_jugador[int(numero_cordenadaO)][letra_cordenadaO] = "X"
                    hit_barcos1 = False
                else:
                    hit_barcos1 = True

                for l in Lista_Base:
                    if l[1] == letra_cordenadaO:
                        letra1 = l[0]
                        ataque_e =tabla_jugador[int(numero_cordenadaO)][letra_cordenadaO]
                print(f"Cordenadas del enemigo [ {numero_cordenadaO} {letra1} ] {ataque_e} \n")
        ## ganadores 
            if barcos_oponente == 0:
                print(print_tablero(tabla_oponente, tabla_jugador))
                print(nombre_jugador, "YAY has ganado!! WOW")
                puntos = int(numero_filas) * int(numero_col) \
                    * NUM_B * (barcos_jugador - barcos_oponente)
                print(f"{nombre_jugador} ganaste {puntos} puntos!")
                from ordenar_puntos import Puntos_orden
                Puntos_orden(nombre_jugador, puntos)

                
                                   

            elif barcos_jugador == 0:
                print(print_tablero(tabla_oponente, tabla_jugador))
                print(nombre_jugador, "buuu has perdido :(")
                puntos = int(numero_filas) * int(numero_col) \
                    * NUM_B * (barcos_oponente - barcos_jugador)
                print(f"enemigo1computador gano {puntos} puntos")
                from ordenar_puntos import Puntos_orden
                Puntos_orden("enemigo1computador", puntos)
                


##Ranking
    elif respuesta_inicial == "1":
        pantalla_puntaje = True
        while pantalla_puntaje == True:
            with open('puntajes.txt', "rt") as puntajes:
                lista_puntajes = puntajes.readlines()
                listafinal_puntaje = []
            for l in lista_puntajes:
                listaP = l.strip().split(",")
                listafinal_puntaje.append(listaP)
        
            print("*"*5, "Ranking de Puntaje", "*"*5)
            MaxP = 5
            if len(listafinal_puntaje) < 5:
                MaxP = len(listafinal_puntaje)

            for p in range(0,MaxP):
                print((p+1), ")",listafinal_puntaje[p][0], ":", listafinal_puntaje[p][1] )
            print("[0] Quedarme pantalla de puntajes", "\n", "[1] Salir")
            respuesta_puntaje = str(input())

            if respuesta_puntaje == "1":
                pantalla_puntaje = False
            else:
                pantalla_puntaje = True

##Salir 
    elif respuesta_inicial == "2":
        salir_while = True
        while salir_while == True:
            print("seguro que quieres salir del programa? :(")
            print("[0] Noo, quiero seguir jugando!", "\n", "[1] Sii, nos vemos despues!")
            respuesta_salir = "None error "
            respuesta_salir = str(input())

            if respuesta_salir == "0":
                print("yayy!")
                salir_while = False
            elif respuesta_salir == "1":
                sys.exit("baii :)")
            else:
                print("perdon no entendi")
                salir_while = True
        
    ##Error
    else:
        print("hubo un error vuelve a intentarlo :)")
