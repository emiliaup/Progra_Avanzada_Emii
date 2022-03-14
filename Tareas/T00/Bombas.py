## Este archivo hace las bombas Bomba_Normal y las Bomba_Especiales
def Bomba_Normal (tabla_o,numero_cordenada, letra_cordenada, barcos_oponente):
    if tabla_o[int(numero_cordenada)][letra_cordenada] == "B":
        barcos_oponente = barcos_oponente - 1                 
        tabla_o[int(numero_cordenada)][letra_cordenada] = "F"
        Repite = True
    elif tabla_o[int(numero_cordenada)][letra_cordenada] == " ":
        tabla_o[int(numero_cordenada)][letra_cordenada] = "X"
        Repite = False
    elif tabla_o[int(numero_cordenada)][letra_cordenada] == "F" or \
         tabla_o[int(numero_cordenada)][letra_cordenada] == "X":
        Repite = True
        print("opppsss ya ocupaste esta cordenada")
    else:
        Repite = False

    return [tabla_o, Repite, barcos_oponente]



def Bomba_Especiales (tabla_oponente,numero_col, numero_filas, \
    Respuesta_BE, num, let,num_r, barcos_oponente):
    Repite2 = False
    ## El punto en si de la cordenada que se eligio 
    if let < int(numero_col) and let >= 0 and num < int(numero_filas) and num >= 0:
        if tabla_oponente[num][let] == "B":
            barcos_oponente = barcos_oponente - 1                 
            tabla_oponente[num][let] = "F"
        elif tabla_oponente[num][let] == ' ':
            tabla_oponente[num][let] = "X"
        else:
            print("uyy ya atacaste aca :/")
            return
    else: 
        print("oopppsss sus cordenadas estan fuera de la guerra")
        return
    letD = let
    letI = let
    numD = num
    numI = num
    # let = letras num = numeros D = derecha I = izquierda
## Bomba X 
    if Respuesta_BE == "0":
        while num_r != 1 and barcos_oponente != 0:
            num_r = num_r - 1
            if letD+1 < int(numero_col) and numD+1 < int(numero_filas) and \
                letD+1 >= 0 and numD+1 >= 0 :
                if tabla_oponente[numD+1][letD+1] == "B":
                    Repite2 = True
                    barcos_oponente = barcos_oponente - 1                 
                    tabla_oponente[numD+1][letD+1] = "F"
                elif tabla_oponente[numD+1][letD+1] == ' ':
                    tabla_oponente[numD+1][letD+1] = "X"
                
            if letI-1 >= 0 and numD+1 < int(numero_filas):
                if tabla_oponente[numD+1][letI-1] == "B":
                    Repite2 = True
                    barcos_oponente = barcos_oponente - 1                 
                    tabla_oponente[numD+1][letI-1] = "F"
                elif tabla_oponente[numD+1][letI-1] == ' ':
                    tabla_oponente[numD+1][letI-1] = "X"
               
            if letD+1 < int(numero_col) and numI-1 < int(numero_filas) and \
                 numI-1 >= 0:
                if tabla_oponente[numI-1][letD+1] == "B":
                    Repite2 = True
                    barcos_oponente = barcos_oponente - 1                 
                    tabla_oponente[numI-1][letD+1] = "F"
                elif tabla_oponente[numI-1][letD+1] == ' ':
                    tabla_oponente[numI-1][letD+1] = "X"
                
            if letI-1 >= 0 and numI-1 >= 0:
                if tabla_oponente[numI-1][letI-1] == "B":
                    Repite2 = True
                    barcos_oponente = barcos_oponente - 1                 
                    tabla_oponente[numI-1][letI-1] = "F"
                elif tabla_oponente[numI-1][letI-1] == ' ':
                    tabla_oponente[numI-1][letI-1] = "X"
                
            letD = letD + 1
            letI = letI - 1
            numD = numD + 1
            numI = numI - 1
        return [tabla_oponente, Repite2, barcos_oponente]
        # devuelve la tabla, si se repite o no (bool)  y la cantidad de barcos que quedan 
## Bomba <> 
    elif Respuesta_BE == "1":
        numr1 = num_r
        numr2 = num_r
        let1 = let - num_r
        N = num

        for arriba in range(0,numr1):
            for l in range(1,numr1*2):
                L = l + (let - numr1)
                if L >= 0 and L < numero_col and N >= 0 and N < numero_filas:
                    if tabla_oponente[N][L] == "B":
                        Repite2 = True
                        barcos_oponente = barcos_oponente - 1                 
                        tabla_oponente[N][L] = "F"
                    elif tabla_oponente[N][L] == ' ':
                        tabla_oponente[N][L] = "X"
            N += 1
            numr1 -= 1
        
        L = let - num_r
        N = num

        for a in range(0,numr2):
            for l in range(1,numr2*2):
                L = l + let - numr2
                if L >= 0 and L < numero_col and N >= 0 and N < numero_filas:
                    if tabla_oponente[N][L] == "B":
                        Repite2 = True
                        barcos_oponente = barcos_oponente - 1                 
                        tabla_oponente[N][L] = "F"
                    elif tabla_oponente[N][L] == ' ':
                        tabla_oponente[N][L] = "X"
            N -= 1
            numr2 -= 1

        return [tabla_oponente, Repite2, barcos_oponente]
        #devuelve la tabla, si se repite o no (bool)  y la cantidad de barcos que quedan 

## Bomba Cruz    
    elif Respuesta_BE == "2":
        while num_r != 1 and barcos_oponente != 0:
            num_r = num_r - 1
            if letD+1 < int(numero_col):
                if tabla_oponente[num][letD+1] == "B":
                    Repite2 = True
                    barcos_oponente = barcos_oponente -1                
                    tabla_oponente[num][letD+1] = "F"
                elif tabla_oponente[num][letD+1] == ' ':
                    tabla_oponente[num][letD+1] = "X"

            if letI-1 >= 0:
                if tabla_oponente[num][letI-1] == "B":
                    Repite2 = True
                    barcos_oponente = barcos_oponente - 1                 
                    tabla_oponente[num][letI-1] = "F"
                elif tabla_oponente[num][letI-1] == ' ':
                    tabla_oponente[num][letI-1] = "X"
                
            if numD+1 < int(numero_filas):
                if tabla_oponente[numD+1][let] == "B":
                    Repite2 = True
                    barcos_oponente = barcos_oponente - 1                 
                    tabla_oponente[numD+1][let] = "F"
                elif tabla_oponente[numD+1][let] == ' ':
                    tabla_oponente[numD+1][let] = "X"
            if numI-1 >= 0:
                if tabla_oponente[numI-1][let] == "B":
                    Repite2 = True
                    barcos_oponente = barcos_oponente - 1                 
                    tabla_oponente[numI-1][let] = "F"
                elif tabla_oponente[numI-1][let] == ' ':
                    tabla_oponente[numI-1][let] = "X"
            letD = letD +1
            letI = letI-1
            numD = numD +1
            numI = numI-1
        return [tabla_oponente, Repite2, barcos_oponente]
        # devuelve la tabla, si se repite o no (bool)  y la cantidad de barcos que quedan 
    else:
        ("Elija otra vez su ataque")
        return 
    