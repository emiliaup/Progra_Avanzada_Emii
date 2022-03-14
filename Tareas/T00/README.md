# Tarea 00T:
DCCombateNaval!!
Emilia Ureta
Seccion 4
Usuario Github: emiliaup

## Consideraciones generales :octocat:
En el codigo todo deberia de funcionar bien. Pude terminar todo y agregue unos titulos mas entretenidos para jugar. Ademas agregue muchas caras :) :0 :/ para que el juego muestre mas emocion. 

### Cosas implementadas y no implementadas 
:white_check_mark: :x:
Realice esta parte del ReadMe teniendo en consideración la división de puntaje entregada a los alumnos en el drive, disponible en el siguiente link: https://docs.google.com/spreadsheets/d/1gqXPvj3x03QBdiwI-KPZm82_Sc_H0723wSC33vvBjio/edit#gid=0

* Inicio del Programa
- Menu de Inicio: Hecha completa
- Funcionalidades: Hecha completa
 - Puntajes: Hecha completa

* Flujo del juego
- Menu de Juego: Hecha completa
- Tablero: Hecha completa
- Turnos: Hecha completa
- Bombas: Hecha completa
- Barcos: Hecha completa
- Oponente: Hecha completa

* Termino del juego
- fin del juego: Hecha completa
- puntajes: Hecha completa
 
 * Archivos:
 - Manejo de Archivos: Hecha completa
 
 * General:
 - Menu: Hecha completa
 - Parametros: Hecha completa
 - Modulos: Hecha completa
 - PEP8: Hecha completa

 * Descuentos:
 - ninguno 
 - Hay dos lineas que tienen 92 caracters (me dice mi computador) aunque parece que tienen mas pero revise muy bien que mi codigo no sea tan largo. :) 

## Ejecución :computer:

* El módulo principal de la tarea a ejecutar es  ```main.py```. 
Además se debe crear los siguientes archivos y directorios adicionales:
1. ```Bombas.py```: contiene todo los codigos de las bombas del jugador X, la cruz y la del diamante. 
2. ```puntajes.txt```: Guarda todos los puntajes, del enemigo y del jugador
3. ```parametros.py```: contiene los numeros de barcos NUM_BARCOS y el radio de explosion de las bombas especiales RADIO_EXP
4.  ```Tablero_completo.py```: Arma el tablero del jugador tabla_Jugador y el del enemigo tabla_opoenente. Importa la cantidad de barcos de parametros.py NUM_BARCOS para meterlos en la tabla de manera random. 
5. ```Ordenar_puntos.py```: Al final del juego ordena todos los puntos, del enemigo o el jugador, de mayor a menor y los guarda en el archivo puntajes.txt
6. ```Tablero.py```: Nos pasaron ese codigo para que este mas bonito.

### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. random -> random.randit
2. sys
3. Os -> open()

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```parametros```: Dan la cantidad de barcos que uno debe de tener en el tablero y el radio de las bombas especiales
2. ```Bombas```: sop las bombas del jugador, bomba normal y las especiales. 
3. ```Tablero completo```: Es para hacer el tablero con el numero de filas y columnas que el jugador quiera mas los barcos que se ponenen en lugares random.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:
1. Agregue los puntos del enemigo para motivar al jugador de ganar al enemigo1computador en vez de rendirse cada vez que uno este perdiendo. 

2. Supuse al rendirse el juego pregunta de nuevo si realmente uno se quiere rendir. Muchas veces uno apreta el 1 sin querer asique queria reafirmar. 

3, No hice un .gitgnore aunque en la puata nos indicaron que en esta tarea no sera evaluado.
## Referencias de código externo :book:

Ninguna referencia. Me demore tres dias en pensar en como hacer el diamante, pero lo logre. 

Muchas gracias por tomarte tu tiempo en ver mi juego y revisar todo. Ojala te guste :) 
Saludosss emiliaup