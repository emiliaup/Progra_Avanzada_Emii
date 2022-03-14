# Tarea 02 : DCCumbia club penguin :)


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

**Antes que nada MUCHAS GRACIASSSSS**

## Consideraciones generales :octocat:

<Descripción de lo que hace y que **_no_** hace la tarea que entregaron junto
con detalles de último minuto y consideraciones como por ejemplo cambiar algo
en cierta línea del código o comentar una función>

### Cosas implementadas y no implementadas :white_check_mark: :x:

* Ventana Inicio: esta bien implementada y la hice bonita :) ojala te guste
*  Ventana Ranking: bella bonita aunque si tienes mas de 20 ranking metido se empieza a poner feo y se esconden algunos puntos jeje sorry
* Generales: todo bien. Lo unico esque mi codigo puede ser un poco lento en el sentido de que cuando pones salir no se cierra de una, tiens 
que esperar un poco. Uno no puede comprar pinguinos :( que sad pero por lo menos los puedes ver. https://youtu.be/_F071LHZIeE
* Fase de pre-ronda: Como no puedes comprar penguins no va a salir un error por no comprar un pinguino pero si va a salir un error
si no tienes la dificultad y cancion
* Fase de ronda/ post ronda: Todo bien. Lo unico esque las estadisticas paran de actualizarse despues de hacer flehcas, se calcula bien al final pero en la parte de arriba de las estadisticas no se actualizan por dos segundos. Wow Wowwww a bailar https://youtu.be/ssz67DKR3mc
* Pinguirin: buu no pude hacer nada con los pinguinos (sad song https://youtu.be/_F071LHZIeE ) No alcance 
* Flechas: todas las flechas se implementan correctamente excepto le de hielo, no congela nada :( 
* Funcionalidades: Todos funcionan bien excepto el Pausa que no pausa las flechas de una se demora un poco y ademas deja de producir flechas pero no para las flechas que ya aparecieron. Uno tiene que tener paciencia con mi codigo cuando para es fragil (it is fragile https://youtu.be/fikqx9k1ZK4 ) jeje
* General: supongo que todo bien, ocupe qt design. 


## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```Main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```SOlo en el main tienes que ejecutar el codigo y todo queda perfect, tienes que tener todos los archicvos .py y las songs y sprites en la misma carpeta eso es todo``` 


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```pyqt5```: ```Casi todas mis funciones para senales, qt design, threads... etc```
2. ```random```: ```para random, choice``` 
3. ```sys```
4. ```os```
5. ```time```: ```Para sleep y time ```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```librería_1```: Contiene a ```ClaseA```, ```ClaseB```, (ser general, tampoco es necesario especificar cada una)...
2. ```librería_2```: Hecha para <insertar descripción **breve** de lo que hace o qué contiene>
3. ...

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Descripción/consideración 1 y justificación del por qué es válido/a> 


PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>



* ventanas y lo que cada uno hace:
* Codigo_ventana_inicio.py: muestra la ventana de inicio
* codigo_ventana_r.py: Muestra en ranking y lee el archivo txt y muestra los puntos de mayor a menor
* codigo_ventana_juego: Juego de flechas 
* flechas_pinguinps_threads: Es el Thread que va creando las flechas y se van moviendo. Iba hacer el thread de los pinguinos que se mueven ahi pero no alcance :( que penita. 
* continuation_juegp.py: Mi Ventana de juego era muy largo, entonces es la continuacion. Iba a continuar con el drag and drop y todo de los pinguinos en esa pagina pero por falta de timepo no pude. 
* flechas_confirmar.py: Hace la probabilidad de las flechas (si sale dorada, de x2, normal o hielo) y ademas las arma para despues mandarlo a la ventana de juego y despues ponerlo en el Qthread. 
* codigo_ventana_resumen.py: es el resumen de cada ronda. 
* parametros.py: todas las variables 

** Importanteeeee perdonnnnnn subi los parametros despues mientras escribia este README porque sin querer los puse en mi gitignore perdon perdonnnnnnnnnn tiene todas las constantes y los paths perdon se me fueeeee < https://youtu.be/cxduYSjj7Ww >  :(( ** 

** Perdon por escribir mal algunas cosas (como pinguinps y juegp ). Lo escribo mal y note que estaba mal el ultimo dia y me dio nervio cambiarlo y que mi codigo no funcionara. Tambien, perdon por las variables de mi codigo esta en spanglish (mitad espanol y mitad ingles https://youtu.be/bP0CSjvVU1w ). 



Si quieren ser más formales, pueden usar alguna convención de documentación. Google tiene la suya, Python tiene otra y hay muchas más. La de Python es la [PEP287, conocida como reST](https://www.python.org/dev/peps/pep-0287/). Lo más básico es documentar así:

Lo importante es que expliquen qué hace la función y que si saben que alguna parte puede quedar complicada de entender o tienen alguna función mágica usen los comentarios/documentación para que el ayudante entienda sus intenciones.

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. <https://stackoverflow.com/questions/42845981/trying-adding-a-sound-event-using-qmediaplayer> Esto lo ocupe para poner la cancion, esta en codigo_ventana_juego.
2. Contenidos, ocupe el ejemplo de la comida de la semana 9 de los contenidos. 
3. Ocupe mi T00 para ayudarme sobre el ranking en como guardarlo y mostrarlo bien



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).

## Finalmente MUCHAS GRACIASSS por todooo,  y por tu tiempo. Se que es mucha pega leer todo. Ojala te haya gustado mi juego y ademas los videos que agregue :) y realmente perdon por lo de los parametros se me fue y sinquerer los puse en mi gitignore perdon perdon.

'''
https://youtu.be/hfWBZvy10PM

^^ despedida final de club penguin, que penita :( mejor juego de la infancia. 
''' 