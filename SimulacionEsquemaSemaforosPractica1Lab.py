'''
ELABORO: FRANCISCO JAVIER BLAS GARZA           MATRICULA:  1999491    CARRERA: ITS    GRUPO: 205     LABORATORIO DE SISTEMAS ADAPTATIVOS 
DOCENTE: Dra. Laura Patricia Del Bosque Vega                                   Martes V3     SEMESTRE AGOSTO - DICIEMBRE 2023 

ESTE CODIGO ESTA REALIZADO PARA LA PRACTICA 1 DEL LABORATORIO DE SISTEMAS ADAPTATIVOS 

CODIGO: REALIZADO EN PYTHON
GITHUB: LowFee1s

FECHA DE ELABORACION:    21 DE AGOSTO DEL 2023             FECHA DE FINALIZACION:    09 DE SEPTIEMBRE DEL 2023
'''

import random, time
import sys
import turtle
import threading
import pygame

# Valores default para los semaforos
defaultGreen = {0:5, 1:5, 2:5, 3:5}
defaultRed = 150
defaultYellow = 2

signals = []
noOfSignals = 4
currentGreen = 0   # Indica cual semaforo esta en verde al iniciar 
nextGreen = (currentGreen+1)%noOfSignals    # Indica cual semaforo seguida en prenderse (El orden)
currentYellow = 0   # Indica si el semaforo amarillo se enciendo 

speeds = {'car':0.25, 'truck':0.21,}  

# Coordenadas para los coches 
x = {'derecha':[0,0,0], 'abajo':[602,627,657], 'izquierda':[1400,1400,1400], 'arriba':[755,727,697]}    
y = {'derecha':[498,466,436], 'abajo':[0,0,0], 'izquierda':[348,370,398], 'arriba':[800,800,800]}

vehicles = {'derecha': {0:[], 1:[], 2:[], 'crossed':0}, 'abajo': {0:[], 1:[], 2:[], 'crossed':0}, 'izquierda': {0:[], 1:[], 2:[], 'crossed':0}, 'arriba': {0:[], 1:[], 2:[], 'crossed':0}}
vehicleTypes = {0:'car', 1:'truck'} 
directionNumbers = {0:'derecha', 1:'abajo', 2:'izquierda', 3:'arriba'} # Coordenadas de las direcciones

# Coordenadas de los semadoros y temporizadores
signalCoods = [(530,230),(810,230),(810,570),(530,570)]
signalTimerCoods = [(131,231),(541,111),(1271,277),(391,617)]

# Coordinates of stop lines
stopLines = {'derecha': 590, 'abajo': 330, 'izquierda': 800, 'arriba': 535}
defaultStop = {'derecha': 580, 'abajo': 320, 'izquierda': 810, 'arriba': 545}


# Espacio entre los coches
stoppingGap = 15    
movingGap = 15   

pygame.init()
simulation = pygame.sprite.Group()

# Clase de los semaforos, aqui basicamente se asigna los colores junto con sus imagenes de la carpeta signals (semaforos)
class TrafficSignal:
    def __init__(self, red, yellow, green):
        self.red = red
        self.yellow = yellow
        self.green = green
        self.signalText = ""
        
# Clase que genera el vehiculo dependiendo de varios parametros, como la velocidad, direccion el tipo de coche, entre otros.
class Vehicle(pygame.sprite.Sprite):
    def __init__(self, lane, vehicleClass, direction_number, direction):
        pygame.sprite.Sprite.__init__(self)
        self.lane = lane
        self.vehicleClass = vehicleClass
        self.speed = speeds[vehicleClass]
        self.direction_number = direction_number
        self.direction = direction
        self.x = x[direction][lane]
        self.y = y[direction][lane]
        self.crossed = 0
        vehicles[direction][lane].append(self)
        self.index = len(vehicles[direction][lane]) - 1
        path = "images/" + direction + "/" + vehicleClass + ".png"
        self.image = pygame.image.load(path)

        if(len(vehicles[direction][lane])>1 and vehicles[direction][lane][self.index-1].crossed==0):    
            if(direction=='derecha'):
                self.stop = vehicles[direction][lane][self.index-1].stop - vehicles[direction][lane][self.index-1].image.get_rect().width - stoppingGap         # Se colocan las coordenadas donde se estaciona 
            elif(direction=='izquierda'):                                                                                                                            # Para saber si viene otro vehiculo atras se estacione detras del de adelante y haya un espacion entre ellos
                self.stop = vehicles[direction][lane][self.index-1].stop + vehicles[direction][lane][self.index-1].image.get_rect().width + stoppingGap         # Dependiendo de la altura y anchura del coche 
            elif(direction=='abajo'):
                self.stop = vehicles[direction][lane][self.index-1].stop - vehicles[direction][lane][self.index-1].image.get_rect().height - stoppingGap
            elif(direction=='arriba'):
                self.stop = vehicles[direction][lane][self.index-1].stop + vehicles[direction][lane][self.index-1].image.get_rect().height + stoppingGap
        else:
            self.stop = defaultStop[direction]
            
        # Se crea un nuevo coche y si la direccion es respectivamente a derecha, arriba, etc. Se colocara la direccion y la coordenada donde se estacionara el coche.
        if(direction=='derecha'):
            temp = self.image.get_rect().width + stoppingGap    
            x[direction][lane] -= temp
        elif(direction=='izquierda'):
            temp = self.image.get_rect().width + stoppingGap
            x[direction][lane] += temp
        elif(direction=='abajo'):
            temp = self.image.get_rect().height + stoppingGap
            y[direction][lane] -= temp
        elif(direction=='arriba'):
            temp = self.image.get_rect().height + stoppingGap
            y[direction][lane] += temp
        simulation.add(self)

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        if(self.direction=='derecha'):
            if(self.crossed==0 and self.x+self.image.get_rect().width>stopLines[self.direction]):  
                self.crossed = 1
            if((self.x+self.image.get_rect().width<=self.stop or self.crossed == 1 or (currentGreen==0 and currentYellow==0)) and (self.index==0 or self.x+self.image.get_rect().width<(vehicles[self.direction][self.lane][self.index-1].x - movingGap))):                
            
                self.x += self.speed  # Se mueve el vehiculo
        elif(self.direction=='abajo'):
            if(self.crossed==0 and self.y+self.image.get_rect().height>stopLines[self.direction]):
                self.crossed = 1
            if((self.y+self.image.get_rect().height<=self.stop or self.crossed == 1 or (currentGreen==1 and currentYellow==0)) and (self.index==0 or self.y+self.image.get_rect().height<(vehicles[self.direction][self.lane][self.index-1].y - movingGap))):                
                self.y += self.speed
        elif(self.direction=='izquierda'):
            if(self.crossed==0 and self.x<stopLines[self.direction]):
                self.crossed = 1
            if((self.x>=self.stop or self.crossed == 1 or (currentGreen==2 and currentYellow==0)) and (self.index==0 or self.x>(vehicles[self.direction][self.lane][self.index-1].x + vehicles[self.direction][self.lane][self.index-1].image.get_rect().width + movingGap))):                
                self.x -= self.speed   
        elif(self.direction=='arriba'):
            if(self.crossed==0 and self.y<stopLines[self.direction]):
                self.crossed = 1
            if((self.y>=self.stop or self.crossed == 1 or (currentGreen==3 and currentYellow==0)) and (self.index==0 or self.y>(vehicles[self.direction][self.lane][self.index-1].y + vehicles[self.direction][self.lane][self.index-1].image.get_rect().height + movingGap))):                
                self.y -= self.speed

# Esta funcion es la inicializacion de los semaforos con los valores predeterminados.  
def initialize():
    ts1 = TrafficSignal(0, defaultYellow, defaultGreen[0])
    signals.append(ts1)
    ts2 = TrafficSignal(ts1.red+ts1.yellow+ts1.green, defaultYellow, defaultGreen[1])
    signals.append(ts2)
    ts3 = TrafficSignal(defaultRed, defaultYellow, defaultGreen[2])
    signals.append(ts3)
    ts4 = TrafficSignal(defaultRed, defaultYellow, defaultGreen[3])
    signals.append(ts4)
    repeat()

def repeat():
    global currentGreen, currentYellow, nextGreen
    while(signals[currentGreen].green>0):   # Este whule se realizara si el tiempo que tiene el semaforo verde es mayor a cero.
        updateValues()
        time.sleep(1)
    currentYellow = 1   # Se coloca el semaforo amarillo en on
    # Se resetea las coordenadas donde se paran las calles y los vehiculos 
    for i in range(0,3):
        for vehicle in vehicles[directionNumbers[currentGreen]][i]:
            vehicle.stop = defaultStop[directionNumbers[currentGreen]]
    while(signals[currentGreen].yellow>0):  # Este while se realizara si el tiempo del current amarillo sea mayor a cero.    
        updateValues()
        time.sleep(1)
    currentYellow = 0   # Se coloca la variable del semaforo amarillo en off
    
     # Se resetea todas los tiempos de los semaforos y se colocan los tiempos de las variables predeterminadas. 
    signals[currentGreen].green = defaultGreen[currentGreen]
    signals[currentGreen].yellow = defaultYellow
    signals[currentGreen].red = defaultRed
       
    currentGreen = nextGreen # Se coloca el siguiente tiempo del semaforo en verde (Lo preestablece).   
    nextGreen = (currentGreen+1)%noOfSignals    # Se coloca el siguiente el semaforo en verde. 
    signals[nextGreen].red = signals[currentGreen].yellow+signals[currentGreen].green    
    repeat()  

# Esta funcion actualiza los valores (Los currentTime = tiempos) de los semaforos despues de cada segundo. 
def updateValues():
    for i in range(0, noOfSignals):
        if(i==currentGreen):
            if(currentYellow==0):
                signals[i].green-=1
            else:
                signals[i].yellow-=1
        else:
            signals[i].red-=1

# Esta funcion es otra de las mas importantes ya que esta genera los coches en la simulacion. 
def generarVehiculos():
    while(True):
        vehicle_type = random.randint(0, 1)
        lane_number = random.randint(1,2)
        temp = random.randint(0,99)
        direction_number = 0
        dist = [25,50,75,100]
        if(temp<dist[0]):
            direction_number = 0
        elif(temp<dist[1]):
            direction_number = 1
        elif(temp<dist[2]):
            direction_number = 2
        elif(temp<dist[3]):
            direction_number = 3
        Vehicle(lane_number, vehicleTypes[vehicle_type], direction_number, directionNumbers[direction_number])
        time.sleep(1)

# Clase main la mas importante de todas ya que realiza todo esta. Manda a llamar las demas clases y funciones realizadas para realizarlas en la simulacion. 

class Main:
    thread1 = threading.Thread(name="initialization",target=initialize, args=())    # initialization
    thread1.daemon = True
    thread1.start()

    # colores 
    black = (0, 0, 0)
    white = (255, 255, 255)
    green = (0, 100, 0)
    yellow = (151, 151, 0)
    red = (100, 0, 0)

    # Window de la simulacion 
    screenWidth = 1350
    screenHeight = 670
    screenSize = (screenWidth, screenHeight)

    # Colocamos el background 
    background = pygame.image.load('images/Interseccion Realizado 17.png')

    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("FJBG - Martes V3 - Simulacion Practica 1 - 1999491 - Laboratorio de Sistemas Adaptativos")

    # Se cargan las imagenes de los semaforos (rojo, amarillo y verde).
    redSignal = pygame.image.load('images/semaforos/red.png')
    yellowSignal = pygame.image.load('images/semaforos/yellow.png')
    greenSignal = pygame.image.load('images/semaforos/green.png')
    font = pygame.font.Font(None, 30)

    thread2 = threading.Thread(name="generarVehiculos",target=generarVehiculos, args=())    # Se generan los coches
    thread2.daemon = True
    thread2.start()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.blit(background,(0,0))   # Se muestra la imagen del fondo en la simulacion
        for i in range(0,noOfSignals):  # Se muestra el semaforo y el tiempo que se coloco en el estado para el: verde, amarillo, o rojo
            if(i==currentGreen):
                if(currentYellow==1):
                    signals[i].signalText = "--"
                    screen.blit(yellowSignal, signalCoods[i])
                else:
                    signals[i].signalText = signals[i].green
                    screen.blit(greenSignal, signalCoods[i])
            else:
                if(signals[i].red<=10):
                    signals[i].signalText = "=="
                else:
                    signals[i].signalText = "--"
                screen.blit(redSignal, signalCoods[i])
        signalTexts = ["","","",""]

        # Se muestran los tiempos de los semaforos
        for i in range(0,noOfSignals):  
            if (i==currentGreen):
                if(currentYellow==1):
                    colorvar = yellow
                    colorvar11 = white
                else: 
                    colorvar = green
                    colorvar11 = white
            else:
                colorvar = red
                colorvar11 = white
            signalTexts[i] = font.render(str(signals[i].signalText), True, colorvar11, colorvar)
            screen.blit(signalTexts[i],signalTimerCoods[i])

        # Se muestran los coches
        for vehicle in simulation:  
            screen.blit(vehicle.image, [vehicle.x, vehicle.y])
            vehicle.move()
        pygame.display.update()

# Se llama la clase main, para que se realize la simulacion del sistema. 

Main()

'''
ELABORO: FRANCISCO JAVIER BLAS GARZA           MATRICULA:  1999491    CARRERA: ITS    GRUPO: 205     LABORATORIO DE SISTEMAS ADAPTATIVOS 
DOCENTE: Dra. Laura Patricia Del Bosque Vega                                   Martes V3     SEMESTRE AGOSTO - DICIEMBRE 2023 

ESTE CODIGO ESTA REALIZADO PARA LA PRACTICA 1 DEL LABORATORIO DE SISTEMAS ADAPTATIVOS 

CODIGO: REALIZADO EN PYTHON
GITHUB: LowFee1s

FECHA DE ELABORACION:     21 DE AGOSTO DEL 2023             FECHA DE FINALIZACION:     09 DE SEPTIEMBRE DEL 2023
'''
