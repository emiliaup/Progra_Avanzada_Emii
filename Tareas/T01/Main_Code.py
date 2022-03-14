from Delegacion import moralL, delegacionL, equipoL, medallasL, dineroL
from Delegacion import Delegaciones, IEEEsparta, DCCrotona
from Deporte import lista_deportistas_info
lista_deportistas = lista_deportistas_info
from beautifultable import BeautifulTable
table = BeautifulTable()

Seguir_juego = True
while Seguir_juego == True:
    print(f"Bienvenidos a DCCumbre Olimpiadas!")
    print(f" [0] Quieres jugar? \n [1] Salir")
    comenzar = str(input())
    
    if comenzar == "0":
        nombre = True
    #Tener info de participantes
        while nombre == True:
            nombre_entrenador = str(input("Cual va ser tu nombre? Solo numeros y letras: "))
            nombre_enemigo = str(input("Cual va ser el nombre del enemigo?? Solo numeros y letras: "))
            if nombre_enemigo.isalnum() and nombre_entrenador.isalnum():
                nombre = False
            
            print("En que delegacion quieres estar?")
            delegacion_jugador = str(input("[0] IEEEsparta [1] DCCrotona:  "))
            if delegacion_jugador == "0" or delegacion_jugador == "1" and nombre == False:
                if delegacion_jugador == "0":
                    delegacion_jugador = "IEEEsparta"
                else:
                    delegacion_jugador = "DCCrotona"
                
            else:
                nombre = True
                print("Hubo un error :/")

        from parametros import DIAS_COMPETENCIA
        dias_competencia = DIAS_COMPETENCIA
    # Obtener informacion parametros, 
        iee = IEEEsparta()
        dcc = DCCrotona()
        lista_iee = iee.calcular_fortalezas_debilidad()
        lista_dcc = dcc.calcular_fortalezas_debilidad()

        if delegacion_jugador == delegacionL[0] and delegacion_jugador == "IEEEsparta":
            la_delegacion_jugador = Delegaciones("IEEEsparta",nombre_entrenador,equipoL[0],
            medallasL[0],moralL[0],
            dineroL[0],True,lista_iee[0],lista_iee[1],lista_iee[2],lista_iee[3])
            la_delegacion_enemigo = Delegaciones("DCCrotona",nombre_enemigo,equipoL[1],medallasL[1],moralL[1],
            dineroL[1],True,lista_iee[0],lista_iee[1],lista_iee[2],lista_iee[3])
            
        elif delegacion_jugador == delegacionL[1] and delegacion_jugador == "IEEEsparta":
            la_delegacion_enemigo = Delegaciones("IEEEsparta",nombre_enemigo,equipoL[0],medallasL[0],moralL[0],
            dineroL[0],True,lista_dcc[0],lista_dcc[1],lista_dcc[2],lista_dcc[3])
            la_delegacion_jugador = Delegaciones("DCCrotona",nombre_entrenador,equipoL[1],medallasL[1],
            moralL[1], dineroL[1],True,lista_dcc[0],lista_dcc[1],lista_dcc[2],lista_dcc[3])
            
        elif delegacion_jugador == delegacionL[0] and delegacion_jugador == "DCCrotona":
            la_delegacion_jugador = Delegaciones("DCCrotona",nombre_entrenador,equipoL[0],medallasL[0],
            moralL[0],dineroL[0],True,lista_dcc[0],lista_dcc[1],lista_dcc[2],lista_dcc[3])
            la_delegacion_enemigo = Delegaciones("IEEEsparta",nombre_enemigo,equipoL[1],medallasL[1],moralL[1],
            dineroL[1],True,lista_dcc[0],lista_dcc[1],lista_dcc[2],lista_dcc[3])
            
        elif delegacion_jugador == delegacionL[1] and delegacion_jugador == "DCCrotona":
            la_delegacion_enemigo = Delegaciones("DCCrotona",nombre_enemigo,equipoL[0],medallasL[0],moralL[0],
            dineroL[0],True,lista_dcc[0],lista_dcc[1],lista_dcc[2],lista_dcc[3])
            la_delegacion_jugador = Delegaciones("IEEEsparta",nombre_entrenador,equipoL[1],medallasL[1],
            moralL[1], dineroL[1],True,lista_dcc[0],lista_dcc[1],lista_dcc[2],lista_dcc[3])
    # sacar deportistas equipo de tabla 
        equipo_deportistas = []
        
        for n in la_delegacion_jugador.equipo:
            L = []
            for i in range (0,len(lista_deportistas_info)):
                if lista_deportistas_info[i][0] == n:
                    L.append(lista_deportistas[i][0])
                    L.append(lista_deportistas[i][1])
                    L.append(lista_deportistas[i][2])
                    L.append(lista_deportistas[i][3])
                    L.append(lista_deportistas[i][4])
                    L.append(lista_deportistas[i][5])
                    L.append(lista_deportistas[i][6])
            equipo_deportistas.append(L)

        for deportista in la_delegacion_jugador.equipo:
            for dep in range(0,len(lista_deportistas_info)-1):
                if deportista == lista_deportistas_info[dep][0]:
                    lista_deportistas_info.pop(dep)


    #Empezar juego
        for dias in range (0,int(dias_competencia/2)):
            #Menu principal
            menu_principal = True
            while menu_principal == True:
                print("Menu Principal!!")
                print(f" [0] Menu entrenador \n [1] Simular competencias \n [2] Mostrar estado")
                respuesta_menu = str(input(f" [3] Salir de programa\n"))
                if respuesta_menu == "0":
                ## Menu Entrenador
                    menuE = True
                    while menuE == True:
                        print(f"\nMenu Entrenador \n [0] Fichar \n [1] Entrenador :) \n [2] Sanar <3")
                        print(" [3] Comprar Tecnologia ")
                        print(f" [4] Usar Habilidad especial uuuu \n [5] Volver al Menu \n [6] Salir del juego \n")
                        respuesta_menuE =input(str())

                        if respuesta_menuE == "0":
                            col = []

                            for lista in range(0,len(lista_deportistas_info)):
                                col.append(lista)
                                table.append_row(lista_deportistas_info[lista])
                            print(table)
                        
                            print(f"\n Que deportista quiere elegir?")
                            deportista_nuevo = input(str())
                            no = 2
                            for d in range(0,len(lista_deportistas_info)-1):
                                if deportista_nuevo == lista_deportistas_info[d][0]:
                                    la_delegacion_jugador.fichar_deportista(int(lista_deportistas_info[d][3]),
                                    lista_deportistas_info[d][0])
                                    no = 0
                                    print(f"yayyy ahora {lista_deportistas_info[d][0]}")
                                    print(f"esta en tu equipo! tu dinero: {la_delegacion_jugador.dinero}")
                                    lista_deportistas_info.pop(d)
                            if no != 0:
                                print("oopss escribio mal el nombre del deportista o no existe")
                            L = []
                            for i in range (0,len(lista_deportistas_info)):
                                if lista_deportistas_info[i][0] == n:
                                    L.append(lista_deportistas[i][0])
                                    L.append(lista_deportistas[i][2])
                                    L.append(lista_deportistas[i][3])
                                    L.append(lista_deportistas[i][4])
                                    L.append(lista_deportistas[i][5])
                                    L.append(lista_deportistas[i][6])
                            equipo_deportistas.append(L)
                        elif respuesta_menuE == "1":
                            print(f"que deportista quieres entrenar? \n {la_delegacion_jugador.equipo}")
                            entrenar_deportista = str(input())
                            for dep in la_delegacion_jugador.equipo:
                                if dep[0] == entrenar_deportista:
                                    resultado = la_delegacion_jugador.entrenar_deportista()
                                    print(f"yayy {entrenar_deportista} pudo entrenar")
                                    if resultado == True:
                                        dep[2]+= 1

                        elif respuesta_menuE == "2":
                            print(f"Que deportista quieres sanar?")
                            for a in range(0,len(equipo_deportistas)):
                                print(equipo_deportistas[a][0], equipo_deportistas[a][5])
                            deportista_sanar = str(input())
                            for dep in range(0,len(equipo_deportistas)):
                                if deportista_sanar == equipo_deportistas[dep][0]:
                                    sano_tf = la_delegacion_jugador.sanar_deportista(int(equipo_deportistas[dep][2]))
                                    if sano_tf == True:
                                        equipo_deportistas[dep][5] = True
                                        print(f"yayyy se sano {deportista_sanar}, {equipo_deportistas[dep][5]}")
                                    else:
                                        print("uyy q mala suerte no se sano :(")

                        elif respuesta_menuE == "3":
                            la_delegacion_jugador.comprar_tecnologia()
                        elif respuesta_menuE == "4":
                            habilidad_tf = la_delegacion_jugador.usar_habilidad_especial()
                            if habilidad_tf == True and la_delegacion_jugador.delegacion_n == "IEEEsparta":
                                for dep in range(0,len(la_delegacion_jugador.equipo)):
                                    equipo_deportistas[dep][2] = 100
                                    print(f"{equipo_deportistas[dep][0]} tiene {equipo_deportistas[dep][2]} de moral")
                        elif respuesta_menuE == "5":
                            menuE = False
                        elif respuesta_menuE == "6":
                            sys.exit("baii :)")
                        else: 
                            print("Perdon no te entendi")
                            menuE = True

                elif respuesta_menu == "2":
                    print(f'''
                    {la_delegacion_jugador.delegacion_n}
                    nombre delegacion: {la_delegacion_jugador.entrenador}
                    Moral de delegacion: {la_delegacion_jugador.moral}
                    Medallas de delegacion: {la_delegacion_jugador.medallas}
                    Dinero de delegacion: {la_delegacion_jugador.dinero}
                    ''')
                    col = []
                    for dep in range(0,len(equipo_deportistas)-1):
                        col.append(dep)
                        table.append_row(equipo_deportistas[dep])
                    print(table)

                    print(f'''
                    {la_delegacion_enemigo.delegacion_n}
                    nombre delegacion: {la_delegacion_enemigo.entrenador}
                    Moral de delegacion: {la_delegacion_enemigo.moral}
                    Medallas de delegacion: {la_delegacion_enemigo.medallas}
                    Dinero de delegacion: {la_delegacion_enemigo.dinero}
                    ''')
                    col = []
                    for dep in range(0,len(equipo_deportistas)-1):
                        col.append(dep)
                        table.append_row(equipo_deportistas[dep])
                    print(table)

                elif respuesta_menu == "3":
                    sys.exit("baii :)")

                elif respuesta_menu == "1":
                    #Simular competencia 
                    pass
                else: 
                    print("Perdon no te entendi, responde una de las alternativas")
    elif comenzar == "1":
        sys.exit("baii :)")
    
    else: 
        print("perdon no te entendi :o")