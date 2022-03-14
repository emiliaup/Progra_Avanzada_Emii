# Tarea 03: DCColonos :school_satchel:

Antes que nada muchas gracias por corregir mi tarea, se que corrigiendo tareas uno se demora muuuuucho por eso te dejo uno de mis playlists favoritos de lofi para que te acompane :) (si esque te gusta lofi)
https://youtu.be/njxfE1qRA2g
Cancion favorita del playlist minuto 39:40 - 43:20

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```Main.py``` que se encuentra uno en Servidor y otro en Cliente. Nose como lo vas a ejecutar pero cuando ejecutaba el codigo via VSC me salia [access denied] los ayudantes me indicaron que era un problema de mi computador y la unica manera de que me funcione el codigo es ejecutandolo en el cmd con PY main.py (primero carpera servidor despues en la carpeta de cliente). Te explico esto porque nose si corre por VSC :( para que tengas ojo :)


**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

<Descripción de lo que hace y que **_no_** hace la tarea que entregaron junto
con detalles de último minuto y consideraciones como por ejemplo cambiar algo
en cierta línea del código o comentar una función>

### Cosas implementadas y no implementadas :white_check_mark: :x:

* <Networking<sub>0</sub>>: Hecha completa, pero porfis porfis cuando vayas a testear si clientes se pueden desconectar cierra el cmd del cliente no la ventana grafica sino no funciona :(  
* <Arquitectura Cliente - Servidor:<sub>1</sub>>: Hecha completa
* <Arquitectura Cliente - Servidor:<sub>2</sub>>: Hecha completa
* <Manejo de Bytes:<sub>3</sub>: Hecha completa
* <Interfaz gráfica<sub>4.0</sub>>:Semi hecha
    * <Modelación<sub>4.1</sub>>: Hech completa (segun yo todo bien)
    * <Sala de espera<sub>4.2</sub>>: Hech completa
    * <Sala de juego<sub>4.3</sub>>: Me falto hacer <comprar chozas>,
    <comprar cartas de desarrollo>,<carta de monopoli>, <Ventana para intercambiar recursos>,
    <accion invalida>, <dados>, tambine no pude cambiar el color de las carreteras :( que penita no me dio el tiempo
    * <Fin del juego<sub>4.4</sub>>: Hice la ventana de partida final con el boton de salirse,
    pero no la pude implementar bien en el juego :( no me dio el tiempo.

* <Grafo <sub>5.0</sub>>: Semi hecha
    * <Archivo <sub>5.1</sub>>:Hecha completa
    * <Modelacion <sub>5.2</sub>>:Hecha completa
    * <Funcionalidades <sub>5.3</sub>>: Hecha completa, pude hacer la carretera mas larga pero no la implemente en el juego, en la parte verde puse varios ejemplos si lo quieres testear con grafo_nodo.carretera_mas_larga() en mapa.py las ultimas lineas de codigo. Realmente perdon por el codigo feo :/ pero por lo menos hace el trabajo 
    
* <Reglas del DCColonos:<sub>6.0</sub>>: Hecha completa
    * <Lanzamiento de dados<sub>6.1</sub>>:No hecha
    * <Lanzamiento de dados<sub>6.2</sub>>:No hecha
    * <Turno<sub>6.3</sub>>: No hecha
    * <Sala de juego<sub>6.4</sub>>: No hecha
    * <Termino del juego<sub>6.5</sub>>: No hecha

* <General<sub>7</sub>>: Hecha completa
    * <Lanzamiento de dados<sub>7.1</sub>>:No hecha

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. Solo utilicé librerías permitidas, ademas ocupe qtDesing para hacer la parte grafica del juego
2. Utilice from beautifultable import BeautifulTable 

### Librerías propias 
Por otro lado, los módulos que fueron creados fueron los siguientes: 

* Carpeta Server : 
    * from logica import Logica: La clase Logica maneja la logica detras del juego
    * from mapa import Grafo, grafo_nodo: la clase Grafo es donde uno arma el Grafo y maneja las conexiones, los duenos de las carretera y los duenos de las chozas. El grafo_nodo = Grafo(grafo_nodos, grafo_hexagonos) es el grafo armado con el grafo nodos y grafo hexagonos dado en grafo.json
    * from jugadores import Jugador, Nombres: la clase Jugador es la informacion de cada jugador (su color, usuario, puntos...), la clase Nombres maneja las identidades de cada jugador - cliente. Si un cliente entra, la clase Nombres le asigna su color, nombre... y si un jugador se desconecta la clase Nombres guarda el color para que otro jugador nuevo puede utilizarlo. 
* Carpeta Cliente : 
    *  from interfaz import Controlador: la clase Controlador es el back end, donde controla todas las signals y la grafica. 
    * from ventana_inicio import Ventana_inicio: grafica del juego 
    * from sala_final import Sala_final: grafica sala final 
    * from sala_espera import Sala_espera: grafica de sala de espera 

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Considere que cuando la sala de espera esta llena en vez de automaticamente irse a la sala de juego uno tiene un boton para apretar y comenzar el juego.
2. Considere que el maximo de jugadores que pueden jugar es 4 porque ya no hay mas colores, no pueden existir 2 jugadores azules o rojos...

PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>


-------


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. Ocupe la AF05 para armar el NetWorking bien y la arquitectura cliente-servidor
2. AY011 para armar bien el Networking y la arquitectura cliente-servidor
3. AY09 para armar bien el grafo 
4. \<https://pypi.org/project/beautifultable/>: Ocupe este link para hacer el beautiful Table. Lo implemente en el Log server.py y logica.py



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).

MUCHAS GRACIASSSSS!!! 
https://youtu.be/MDn_Ik4RIYs
Cancion diciendo muchas gracias ^
Ojala te haya gustado mi juegoooo lo hice bello bonito aunque uno realmente no puede jugar
Tambien que rico saber que esta es mi ultima tarea y por fin puedo dormir :) 

saludos y suerte cn la correccion :) 