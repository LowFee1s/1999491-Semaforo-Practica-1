from turtle import *
import time
import turtle

t=Turtle()
S1=Turtle()
S2=Turtle()
S3=Turtle()
S4=Turtle()
screen=t.getscreen()
setup(1100,650,0,0)
screensize(1000,600)
colormode(255)

#fondo carretera
t.fillcolor(83,72,83)
t.begin_fill()
t.penup()
t.goto(-500,300)
t.pendown()
t.goto(500,300)
t.goto(500,-300)
t.goto(-500,-300)
t.goto(-500,300)
t.end_fill()


t.fillcolor(0,150,0)
t.penup() #csi
t.goto(-500,300)
t.pendown()
t.begin_fill()
t.goto(-100,300)
t.goto(-100,100)
t.goto(-500,100)
t.goto(-500,300)
t.end_fill()

t.fillcolor(0,150,0)
t.penup() #csd
t.goto(100,300)
t.pendown()
t.begin_fill()
t.goto(500,300)
t.goto(500,100)
t.goto(100,100)
t.goto(100,300)
t.end_fill()

t.fillcolor(0,150,0)
t.penup() #cid
t.goto(100,-100)
t.pendown()
t.begin_fill()
t.goto(500,-100)
t.goto(500,-300)
t.goto(100,-300)
t.goto(100,-100)
t.end_fill()

t.fillcolor(0,150,0)
t.penup()
t.goto(-100,-100)
t.pendown()
t.begin_fill()
t.goto(-500,-100)
t.goto(-500,-300)
t.goto(-100,-300)
t.goto(-100,-100)
t.end_fill()

#banquetas
t.penup() #bsi
t.goto(-100,100)
t.fillcolor(179,166,177)
t.pendown()
t.begin_fill()
t.goto(-100,300)
t.goto(-150,300)
t.goto(-150,150)
t.goto(-500,150)
t.goto(-500,100)
t.goto(-100,100)
t.end_fill()

t.penup()#bsd
t.goto(100,100)
t.fillcolor(179,166,177)
t.pendown()
t.begin_fill()
t.goto(100,300)
t.goto(150,300)
t.goto(150,150)
t.goto(500,150)
t.goto(500,100)
t.goto(100,100)

t.end_fill()

t.penup()#bid
t.goto(100,-100)
t.fillcolor(179,166,177)
t.pendown()
t.begin_fill()
t.goto(500,-100)
t.goto(500,-150)
t.goto(150,-150)
t.goto(150,-300)
t.goto(100,-300)
t.goto(100,-100)
t.end_fill()

t.penup()#bii
t.goto(-100,-100)
t.fillcolor(179,166,177)
t.pendown()
t.begin_fill()
t.goto(-500,-100)
t.goto(-500,-150)
t.goto(-150,-150)
t.goto(-150,-300)
t.goto(-100,-300)
t.goto(-100,-100)
t.end_fill()

#franjas
t.penup()
t.goto(0,300)
t.pencolor("white")
t.pensize(10)
t.pendown()
t.rt(90)
for i in range(4):
 t.fd(30)
 t.penup()
 t.fd(30)
 t.pendown()
 
t.penup()
t.goto(0,-300)
t.pendown()
t.rt(180)
for i in range(4):
 t.fd(30)
 t.penup()
 t.fd(30)
 t.pendown()
 
t.penup()
t.goto(-500,0)
t.pendown()
t.rt(90)
for i in range(6):
 t.fd(30)
 t.penup()
 t.fd(30)
 t.pendown()
 
t.penup()
t.goto(500,0)
t.pendown()
t.rt(180)
for i in range(6):
 t.fd(30)
 t.penup()
 t.fd(30)
 t.pendown()

t.rt(180)
t.pensize(1)
#semaforo 1
t.pencolor("black")
t.penup()
t.fillcolor("black")
t.goto(-100,100)
t.pendown()
t.begin_fill()
t.goto(0,100)
t.goto(0,130)
t.goto(-100,130)
t.goto(-100,100)
t.end_fill()

t.penup()
t.goto(-30,115)
t.dot(20,0,50,0) #verde

t.goto(-60,115)
t.dot(20,50,50,0) #amarillo

t.goto(-90,115) 
t.dot(20,50,0,0) #rojo

#semaforo 2
t.penup()
t.fillcolor("black")
t.goto(100,100)
t.pendown()
t.begin_fill()
t.goto(130,100)
t.goto(130,0)
t.goto(100,0)
t.goto(100,100)
t.end_fill()

t.penup()
t.goto(115,30)
t.dot(20,0,50,0) #verde

t.goto(115,60)
t.dot(20,50,50,0)#amarillo

t.goto(115,90)
t.dot(20,50,0,0) #rojo

#semaforo 3
t.penup()
t.fillcolor("black")
t.goto(100,-100)
t.pendown()
t.begin_fill()
t.goto(100,-130)
t.goto(0,-130)
t.goto(0,-100)
t.goto(100,-100)
t.end_fill()

t.penup()
t.goto(30,-115)
t.dot(20,0,50,0) #verde

t.goto(60,-115)
t.dot(20,50,50,0) #amarillo

t.goto(90,-115)
t.dot(20,50,0,0) #rojo

#semaforo 4
t.penup()
t.fillcolor("black")
t.goto(-100,-100)
t.pendown()
t.begin_fill()
t.goto(-100,0)
t.goto(-130,0)
t.goto(-130,-100)
t.goto(-100,-100)
t.end_fill()

t.penup()
t.goto(-115,-30)
t.dot(20,0,50,0) #verde

t.goto(-115,-60)
t.dot(20,50,50,0) #amarillo

t.goto(-115,-90)
t.dot(20,50,0,0) #rojo

#posicionando las tortugas coches

S1.shape("triangle")
S2.shape("triangle")
S3.shape("triangle")
S4.shape("triangle")

S1.penup()
S2.penup()
S3.penup()
S4.penup()

S1.goto(-50,300)
S1.rt(90)
S2.goto(500,50)
S2.rt(180)
S3.goto(50,-300)
S3.lt(90)
S4.goto(-500,-50)


t.hideturtle()
for i in range(2):
 t.penup()
 t.goto(-30,115)
 t.dot(20,0,255,0)#verde prendido del semaforo 1
 t.goto(115,90)
 t.dot(20,255,0,0)
 t.goto(90,-115)
 t.dot(20,255,0,0)
 t.goto(-115,-90)
 t.dot(20,255,0,0)

 for i in range(3):
  a=2
  S1.shapesize(a*1,a*3,a*3)
  S1.speed(2)
  S1.showturtle()
  S1.fd(600)
  S1.hideturtle()
  S1.goto(-50,300)
  time.sleep(1)
  a=a+1
 
 time.sleep(0.1) 
 
 t.goto(-30,115)
 t.dot(20,0,50,0)
 t.goto(-60,115)
 t.dot(20,255,255,0)
 
 time.sleep(1)
 t.goto(-60,115)
 t.dot(20,50,50,0)
 t.goto(-90,115)
 t.dot(20,255,0,0)#enciende rojo de semaforo 1
 t.goto(115,90)
 t.dot(20,50,0,0)
 t.goto(115,30)
 t.dot(20,0,255,0) #enciende verde de semaforo 2

 for i in range(4):
  b=3
  S2.shapesize(b*1.33,b*1,b*2)
  S2.speed(2)
  S2.showturtle()
  S2.fd(1000)
  S2.hideturtle()
  S2.goto(500,50)
  time.sleep(1)
  b=b+1
 
 time.sleep(0.1)
 
 t.goto(115,30)
 t.dot(20,0,50,0) #apaga verde de semaforo 2
 t.goto(115,60)
 t.dot(20,255,255,0)#enciende amarillo de semaforo 2 #seguirle de aqui
 

 time.sleep(1)
 
 t.goto(115,60)
 t.dot(20,50,50,0)#apago amarillo de semaforo 2 #seguirle de aqui
 t.goto(115,90)
 t.dot(20,255,0,0)#enciendo rojo de semaforo 2
 t.goto(90,-115)
 t.dot(20,50,0,0)#apago rojo de semaforo 3
 t.goto(30,-115)
 t.dot(20,0,255,0)#prendo verde de semaforo 3

 for i in range(2):
  c=1.5
  S3.shapesize(c*1.5,c*2.5,c*3.5)
  S3.speed(2)
  S3.showturtle()
  S3.fd(600)
  S3.hideturtle()
  S3.goto(50,-300)
  time.sleep(1)
  c=c+1
 
 time.sleep(0.1)
 
 t.goto(30,-115)
 t.dot(20,0,50,0)#prendo verde de semaforo 3
 t.goto(60,-115)
 t.dot(20,255,255,0)#prendo amarillo de semaforo 3

 time.sleep(1)
 
 t.goto(60,-115)
 t.dot(20,50,50,0)#apago amarillo de semaforo 3
 t.goto(90,-115)
 t.dot(20,255,0,0)#prendo rojo de semaforo 3
 t.goto(-115,-90)
 t.dot(20,50,0,0)#apago rojo de semaforo 4
 t.goto(-115,-30)
 t.dot(20,0,255,0) #prendo verde de semaforo 4
 
 for i in range(3):
  d=2.33
  S4.shapesize(d*1,d*4,d*1.333)
  S4.speed(2)
  S4.showturtle()
  S4.fd(1000)
  S4.hideturtle()
  S4.goto(-500,-50)
  time.sleep(1)
  d=d+1
 
 
 time.sleep(0.1)
 
 t.goto(-115,-30)
 t.dot(20,0,50,0) #apago verde de semaforo 4
 t.goto(-115,-60)
 t.dot(20,255,255,0)#prendo amarillo de semaforo 4

 time.sleep(1)
 
 t.goto(-115,-60)
 t.dot(20,50,50,0)#apago amarillo de semaforo 4
 t.goto(-115,-90)
 t.dot(20,255,0,0)#prendo rojo de semaforo 4
 t.goto(-90,115)
 t.dot(20,50,0,0)#apago rojo de semaforo 1


t.goto(115,90)
t.dot(20,50,0,0)
t.goto(90,-115)
t.dot(20,50,0,0)
t.goto(-115,-90)
t.dot(20,50,0,0)

S1.showturtle()
S1.goto(0,0)
S2.showturtle()
S2.goto(10,0)
S2.pencolor("white")
S2.write("¡¡¡CHOQUE MORTAL!!!!",False,"center",("arial",20,"bold italic"))

screen.exitonclick()