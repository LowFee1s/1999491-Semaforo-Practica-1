# 1999491-Semaforo-Practica-1
Este es un sistema de un semáforo con calles y coches realizado, esto para una práctica de laboratorio de la materia del laboratorio de sistemas adaptativos.

**PRACTICA DE CONTROL DE SEMAFOROS** </p><p>
Carrera: ITS</p><p>
<a name="_toc145146763"></a>**Laboratorio de Sistemas Adaptativos**</p><p>
Martes V3 </p><p>
Grupo: 205</p><p>
08 – Septiembre - 2023</p><p></p><p>Martes V3 </p><p>


**INDICE**


# **Tabla de contenido de la practica 1**

[**Introducción	3**](#_toc145146764)

[**Practica de control de semáforos	4**](#_toc145146765)

[**Desarrollo	4**](#_toc145146766)

[**Diseño del cruce para esta práctica.	4**](#_toc145146767)

[**Matriz y Grafo de conflictos sobre el sistema.	5**](#_toc145146768)

[**Diseño de la solución	6**](#_toc145146769)

[**Código de la función que genera un vehículo:	7**](#_toc145146770)

[**Código de la función main (Que es la más importante de todos):	8**](#_toc145146771)

[**Video y Ligas del Código	10**](#_toc145146772)

[**Conclusión	11**](#_toc145146773)

[**Bibliografía	11**](#_toc145146774)






##



## <a name="_toc145146764"></a>**Introducción**
##
En esta práctica programaremos un sistema auto ajuste, Como dice el nombre de la practica elaboraremos un sistema de control de semáforos auto ajustable a cualquier parámetro. Esto consiste en diseñar un cruce de calles y tenemos que controlar el tráfico de cada calle con su respectivo semáforo, esto para brindar la prioridad a las calles con más tráfico que hay. Obviamente no solo es el tráfico de la calle, si no también hay que evitar que 2 o más semáforos se enciendan a la vez, esto para prevenir choques. En estas calles puede variar básicamente el tráfico dependiendo de la hora y el lugar, Por lo que hay que considerar estos parámetros igual.  


El objetivo que se tiene en esta práctica es implementar este sistema que se auto ajuste a las necesidades para un tipo de cruce de calles parecido, con esto minimizar el tráfico que se ocasiona y también este se puede adaptar y sea muy beneficioso para las personas que transitan en unas calles como las mencionadas. Para realizar todo esto usaremos el lenguaje de programación Python junto con su librería pygame para realizar el diseño y el sistema de esto mencionado.


## <a name="_toc145146765"></a>**Practica de control de semáforos**

### <a name="_toc145146766"></a>**Desarrollo**

![](Aspose.Words.028b548f-73e7-4b2a-a81a-f1fc6263e209.010.png)Bueno para empezar lo primero que realice sobre esta práctica fue diseñar el cruce que iba tener mi trabajo, al igual que el grafo y su matriz de conflictos. Gracias a esto para saber cuáles calles van a ser las principales y las más transitadas y una vez conociendo esto, ahora si saber cuáles poner al mismo tiempo de color verde y cuáles no. Con esto para no provocar un choque ni tener cualquier tipo de problemas a un futuro.
### <a name="_toc145146767"></a>**Diseño del cruce para esta práctica.**

Una vez que obtuve este diseño, realizar el diseño de la matriz y el grafo para cumplir con lo establecido en el sistema y en la práctica misma. Y saber lo que tenía que realizar para completar este sistema mencionado.

A continuación, mostrare como quedo y realice la matriz de conflicto y el grafo de este sistema.

<table><tr><th colspan="6" rowspan="2">"Matriz de conflictos sobre el sistema de control de semáforos"</th></tr>
<tr><td valign="bottom"></td></tr>
<tr><td><b>Numero de combinaciones</b></td><td><b>A</b></td><td><b>B</b></td><td><b>C</b></td><td><b>D</b></td><td><b>Salida</b></td><td></td></tr>
<tr><td><b><i>1</i></b></td><td>0</td><td>0</td><td>0</td><td>0</td><td valign="bottom"><b><i>Todos los semáforos están en rojo</i></b></td><td></td></tr>
<tr><td><b><i>2</i></b></td><td>0</td><td>0</td><td>0</td><td>1</td><td valign="bottom"><b><i>D en verde</i></b></td><td></td></tr>
<tr><td><b><i>3</i></b></td><td>0</td><td>0</td><td>1</td><td>0</td><td valign="bottom"><b><i>C en verde</i></b></td><td></td></tr>
<tr><td><b><i>4</i></b></td><td>0</td><td>0</td><td>1</td><td>1</td><td valign="bottom"><b><i>Choque</i></b></td><td></td></tr>
<tr><td><b><i>5</i></b></td><td>0</td><td>1</td><td>0</td><td>0</td><td valign="bottom"><b><i>B en verde</i></b></td><td></td></tr>
<tr><td><b><i>6</i></b></td><td>0</td><td>1</td><td>0</td><td>1</td><td valign="bottom"><b><i>Choque</i></b></td><td></td></tr>
<tr><td><b><i>7</i></b></td><td>0</td><td>1</td><td>1</td><td>0</td><td valign="bottom"><b><i>Choque</i></b></td><td></td></tr>
<tr><td><b><i>8</i></b></td><td>0</td><td>1</td><td>1</td><td>1</td><td valign="bottom"><b><i>Choque</i></b></td><td></td></tr>
<tr><td><b><i>9</i></b></td><td>1</td><td>0</td><td>0</td><td>0</td><td valign="bottom"><b><i>A en verde</i></b></td><td></td></tr>
<tr><td><b><i>10</i></b></td><td>1</td><td>0</td><td>0</td><td>1</td><td valign="bottom"><b><i>Choque</i></b></td><td></td></tr>
<tr><td><b><i>11</i></b></td><td>1</td><td>0</td><td>1</td><td>0</td><td valign="bottom"><b><i>Choque</i></b></td><td></td></tr>
<tr><td><b><i>12</i></b></td><td>1</td><td>0</td><td>1</td><td>1</td><td valign="bottom"><b><i>Choque</i></b></td><td></td></tr>
<tr><td><b><i>13</i></b></td><td>1</td><td>1</td><td>0</td><td>0</td><td valign="bottom"><b><i>Choque</i></b></td><td></td></tr>
<tr><td><b><i>14</i></b></td><td>1</td><td>1</td><td>0</td><td>1</td><td valign="bottom"><b><i>Choque</i></b></td><td></td></tr>
<tr><td><b><i>15</i></b></td><td>1</td><td>1</td><td>1</td><td>0</td><td valign="bottom"><b><i>Choque</i></b></td><td></td></tr>
<tr><td><b><i>16</i></b></td><td>1</td><td>1</td><td>1</td><td>1</td><td valign="bottom"><b><i>Choque</i></b></td><td></td></tr>
</table>

### <a name="_toc145146768"></a>**Matriz y Grafo de conflictos sobre el sistema.**
![](Aspose.Words.028b548f-73e7-4b2a-a81a-f1fc6263e209.011.png)Bueno como podemos observar en la matriz de conflictos y el grafo, en la matriz nos indica que solamente hay 4 formas correctas para que se ponga el semáforo de color verde y los coches pasen como podemos observar, que son las combinaciones **2, 3, 5 y 9**, ya que de lo contrario prenderían más de 1 semáforo y pasaría un choque y obviamente eso lo queremos evitar. En la combinación 1 se colocan todos en “rojo” y en las otras combinaciones solamente está el semáforo correspondiente en “verde”, y los demás en “rojo”, Por ejemplo, en la combinación 2: Solamente enciende el carril D en “verde” y los demás se colocan en “rojo”.

### <a name="_toc145146769"></a>**Diseño de la solución**
###
Bueno una vez ya teniendo tanto el diseño de la calle, la matriz y el grafo de conflictos, primero empecé declarando las variables para este sistema, obviamente una de las más importante es las posiciones. Ya que con estas variables se posicionarán correctamente tanto los coches como los semáforos para este sistema y además declarar las coordenadas de cada una de las líneas donde esperarán los coches cuando está en rojo. 

*# Valores default para los semáforos*

defaultGreen = {0:10, 1:10, 2:10, 3:10}

defaultRed = 150

defaultYellow = 5

*# Coordenadas para los coches* 

x = {'right':[0,0,0], 'down':[602,627,657], 'left':[1400,1400,1400], 'up':[755,727,697]}    

y = {'right':[498,466,436], 'down':[0,0,0], 'left':[348,370,398], 'up':[800,800,800]}

directionNumbers = {0:'right', 1:'down', 2:'left', 3:'up'} *# Coordenadas de las direcciones*

Ya una vez declarando todas las variables utilizadas, continue con iniciar una simulación en una librería de Python llamada pygame, con esto para que otorgue una ventana y crear un grupo donde se realizara esta simulación sobre el sistema. Cabe mencionar que los coches que aparecen en la simulación son totalmente aleatorios ya que hay una variable que contiene número aleatorio, cada vez que se ejecuta, con esto generando un número y por medio de una condición indica que el número que salió generara un coche a la derecha, izquierda, arriba o abajo dependiendo del número que salió en esa generación. 

Bueno una vez comentado esto se realizan varias funciones que contienen lo que va a realizar cada una de ellas. Por ejemplo, la función Vehículo, contiene las variables que se van a asignar a esa función, como la velocidad, el tipo de coche, la dirección que comente anteriormente (por medio de un numero aleatorio), entre otras cosas para el coche. 

También los cambios en los semáforos son por medio de tiempos por ejemplo inicia el lado izquierdo, luego se espera 10 segundos para cambiar y así respectivamente (Cabe aclarar que unos tienen más tiempo por el tráfico que se acumula en esa calle) para tener un control y no tener errores a la hora de usarse en las calles. Luego se realizan todas las demás funciones para que se realice esta simulación. A continuación, las funciones más importantes: 
### <a name="_toc145146770"></a>Código de la función que genera un vehículo:
###
def **generarVehiculos**():

`    `while(True):

`        `vehicle\_type = 0

`        `lane\_number = random.randint(1,2)

`        `temp = random.randint(0,99)

`        `direction\_number = 0

`        `dist = [25,50,75,100]

`        `if(temp<dist[0]):

`            `direction\_number = 0

`        `elif(temp<dist[1]):

`            `direction\_number = 1

`        `elif(temp<dist[2]):

`            `direction\_number = 2

`        `elif(temp<dist[3]):

`            `direction\_number = 3

`        `Vehicle(lane\_number, vehicleTypes[vehicle\_type], direction\_number, directionNumbers[direction\_number])

`        `time.**sleep**(1)

Como ya mencioné esta función realicé una generación de un nuevo vehículo que pasa en la simulación lo genera por medio de un while y dentro las variables random, que son para saber de qué lado aparecerá en la simulación y además manda a llamar a la clase vehículo, para pasarle las variables y con esto generar una dirección, el tipo de vehículo y la dirección que tomará. Y con un sleep para cada vez que se ejecute la función se espere 1 segundo. Como podemos notar la dirección 0 es derecha, 1 es arriba, 2 es izquierda y 3 es abajo. Dependiendo de el numero que salga como ya mencioné se le colocara la dirección a este vehículo. Ya para concluir con este diseño de la solución también otra de las funciones más importante obviamente es la clase main, que es lo que hace que corra el sistema y se realice todo correcto en esta simulación que es el siguiente código:
### <a name="_toc145146771"></a>Código de la función main (Que es la más importante de todos): 

class Main:

`    `thread1 = threading.Thread(*name*="initialization",*target*=**initialize**, *args*=())    

`    `thread1.daemon = True

`    `thread1.**start**()

`    `*# Pantalla de la simulacion* 

`    `screenWidth = 1350

`    `screenHeight = 670

`    `screenSize = (screenWidth, screenHeight)

`    `*# Colocamos el background* 

`    `background = pygame.image.**load**('images/Interseccion Realizado 17.png')

`    `screen = pygame.display.**set\_mode**(screenSize)

`    `pygame.display.**set\_caption**("SIMULACION PRACTICA 1 - 1999491")

`    `*# Se cargan las imagenes de los semaforos (ROJO, AMARILLO Y VERDE)*

`    `redSignal = pygame.image.**load**('images/signals/red.png')

`    `yellowSignal = pygame.image.**load**('images/signals/yellow.png')

`    `greenSignal = pygame.image.**load**('images/signals/green.png')

`    `font = pygame.font.Font(None, 30)

`    `thread2 = threading.Thread(*name*="generarVehiculos",*target*=**generarVehiculos**, *args*=())    *# Se generan los coches*

`    `thread2.daemon = True

`    `thread2.**start**()

`    `while True:

`        `for event in pygame.event.**get**():

`            `if event.type == pygame.QUIT:

`                `sys.**exit**()

`        `screen.**blit**(background,(0,0))   *# Se muestra la imagen del fondo en la simulacion*

`        `for i in range(0,noOfSignals):  *# Se muestra el semaforo y el tiempo que se coloco en el estado para el: verde, amarillo, o rojo*

`            `if(i==currentGreen):

`                `if(currentYellow==1):

`                    `signals[i].signalText = signals[i].yellow

`                    `screen.**blit**(yellowSignal, signalCoods[i])

`                `else:

`                    `signals[i].signalText = signals[i].green

`                    `screen.**blit**(greenSignal, signalCoods[i])

`            `else:

`                `if(signals[i].red<=10):

`                    `signals[i].signalText = signals[i].red

`                `else:

`                    `signals[i].signalText = "---"

`                `screen.**blit**(redSignal, signalCoods[i])

`        `signalTexts = ["","","",""]

`        `*# Se muestran los tiempos de los semaforos*

`        `for i in range(0,noOfSignals):  

`            `signalTexts[i] = font.**render**(str(signals[i].signalText), True, white, black)

`            `screen.**blit**(signalTexts[i],signalTimerCoods[i])

`        `*# Se muestran los coches*

`        `for vehicle in simulation:  

`            `screen.**blit**(vehicle.image, [vehicle.x, vehicle.y])

`            `vehicle.move()

`        `pygame.display.**update**()

Bueno como Podemos observar se crea una variable que tiene un objeto (Threading) pasando atributos para que se guarden y después sean utilizados, luego inicia la variable thread1 que tiene las variables del inicio, después se asignan valores para la pantalla y se coloca la imagen de el diseño del cruce que realice. Con esto ahora si podemos colocar las imágenes de los semáforos y generamos otra variable de thread2 pasándole la función que genere los coches, con esto dentro de un while se ejecuten las siguientes cosas: 

- Se muestre el fondo (Diseño del cruce).   
- Se muestre los semáforos del color que le corresponde por medio de las condiciones que se generaron en las otras funciones. Se inicia el de arriba y luego el de debajo después de 10 segundos y así sucesivamente se realizan, cada uno esta programado para que no haya errores, ni se prendan a la vez.  
- También se muestre los temporizadores arriba de los semáforos.  
- Y por último obviamente se muestren los coches y despliegue la modificación que se realizó en la simulación.     

Con esto se generará todas las cosas en esta simulación, obviamente hay mas cosas que hacen que funcione correctamente, pero solamente estoy poniendo lo más importante, lo que me tomo más tiempo y lo importante.
### <a name="_toc145146772"></a>Video y Ligas del Código



Ya para concluir con esta actividad a continuación veremos el video de la simulación y además las ligas donde subí mi código y el blog de la practica 1 por si gustan para que lo puedan observar:

https://youtu.be/Rgf2tU6GgTQ

https://practica1labsistemasadaptativos.netlify.app/

####
####
####
####
####
####
####
####
####
####
####
####
####
####
####
####
####
####

####




## <a name="_toc145146773"></a>**Conclusión**

Como conclusión pues me parece muy interesante e importante como es que se realizan este tipo de sistemas ya que tienen que tener una precisión y además una buena programación por detrás para que a la hora de que este en producción el sistema o en este caso en las calles pues tiene que tener una buena programación y además lógica ya que como vemos si más de dos semáforos se encienden por error de cualquier tipo entonces hay un choque o puede haberlo y esto obviamente debemos evitarlo y mejorar los sistemas de este tipo de situaciones realizado. Para concluir yo opino que al realizar este tipo de sistemas de auto ajuste hay que tener todo muy bien, y además de checarlo antes y saber todos los tipos de parámetros para saber que hay que realizar, me pareció muy interesante e importante la actividad en lo realizado,
## <a name="_toc145146774"></a>**Bibliografía**


- Juan. (2022, 3 noviembre). Cómo usar hilos (Threads) en Python - Código Pitón. Código Pitón. [**https://www.codigopiton.com/como-usar-hilos-o-threads-en-python/**](https://www.codigopiton.com/como-usar-hilos-o-threads-en-python/)

- Coursera. (2023). ¿Qué es Python y para qué se usa? guía para principiantes. Coursera. [**https://www.coursera.org/mx/articles/what-is-python-used-for-a-beginners-guide-to-using-python**](https://www.coursera.org/mx/articles/what-is-python-used-for-a-beginners-guide-to-using-python)

- **Inicialización, finalización e hilos — Documentación de Python - 3.8.17. (s. f.). <https://docs.python.org/es/3.8/c-api/init.html>** 

- Dotnet-Bot. (s. f.). Semaphore clase (System.Threading). Microsoft Learn. [**https://learn.microsoft.com/es-es/dotnet/api/system.threading.semaphore?view=net-7.0**](https://learn.microsoft.com/es-es/dotnet/api/system.threading.semaphore?view=net-7.0)
8 de septiembre de 2023














