import turtle as tr
import random as rd
import time as tm

tr.bgcolor("#cecdcd")
tr.setup(790, 1010)
tr.speed(0)

def posicion(x,y, p, c=str("black")):
    tr.penup()
    tr.goto(x,y)
    tr.pendown()
    tr.pensize(p)
    tr.pencolor(c)
    
def estampas(x,y,l,w,i,f=str("classic"),b=str("#000000"),c=str("#000000")):
    tr.penup()
    tr.goto(x,y)
    tr.pendown()
    tr.shape(f)
    tr.shapesize(stretch_len= l, stretch_wid= w)
    tr.pencolor(b)
    tr.fillcolor(c)
    tr.tilt(i)
    tr.stamp()
    
def penseth(s, p):
    tr.seth(s)
    tr.pensize(p)

def lluvia(cantidad, largo, x1, x2, y1, y2):
    for _ in range(cantidad):
        x = rd.randint(x1, x2)
        y = rd.randint(y1, y2)
        angulo = rd.randint(267, 273)
        tr.penup()
        tr.goto(x, y)
        tr.setheading(angulo)
        tr.pendown()
        tr.fd(largo)
    
tr.pensize(2)
def lineas_aleatorias(cantidad, x1, x2, y1, y2, largo=30):
    for _ in range(cantidad):
        x = rd.randint(x1, x2)
        y = rd.randint(y1, y2)
        angulo = rd.choice([2, 358])
        tr.penup()
        tr.goto(x, y)
        tr.setheading(angulo)
        tr.pendown()
        tr.fd(largo)

lluvia(350, 35, -325, 300, -330, 235)

#Nube
tr.color("black","#3a3a3a")
posicion(6, 215, 10)
tr.begin_fill()
tr.seth(231); tr.circle(-83, 108)
tr.seth(210); tr.circle(-57, 72)
tr.seth(97); tr.circle(-20, 45)
tr.seth(202); tr.circle(-275, 22)
tr.seth(183); tr.circle(-55, 70)
tr.seth(112); tr.circle(-20, 70)
tr.seth(46); tr.circle(-235, 20)
tr.seth(170); tr.circle(-250, 8)
tr.seth(155); tr.circle(-33, 120)
tr.seth(45); tr.circle(-125, 80)
tr.lt(180); tr.circle(125, 14)
tr.seth(120); tr.circle(-40, 110)
tr.seth(15); tr.circle(-135, 53)
tr.seth(82); tr.fd(14)
tr.seth(45); tr.circle(-92, 110)
tr.seth(250); tr.fd(31)
tr.seth(22); tr.fd(42)
tr.seth(3); tr.circle(-125, 28)
tr.seth(348); tr.circle(-35, 123)
tr.seth(2); tr.circle(-80, 40)
tr.seth(340); tr.circle(-36, 120)
tr.seth(213); tr.circle(-100, 35)
tr.rt(180); tr.circle(100, 8)
tr.seth(338); tr.circle(-50, 60)
tr.seth(267); tr.circle(-45, 100)
tr.seth(165); tr.circle(-120, 33)
tr.seth(273); tr.circle(-30, 70)
tr.seth(215); tr.circle(-100, 80)
tr.goto(6, 215)
tr.end_fill()

#Personaje
tr.color("black","#c8c8c8")
posicion(48, -205, 12)
tr.begin_fill()
tr.seth(310); tr.circle(-130, 55)
tr.rt(180); tr.circle(130, 45)
penseth(298, 8); tr.circle(-80, 70)
tr.seth(227); tr.circle(-100, 41)
penseth(270, 16), tr.fd(21)
penseth(270, 10); tr.fd(18)
penseth(270, 12); tr.fd(20)
tr.rt(180); tr.fd(20)
penseth(90, 10); tr.fd(18)
penseth(90, 16); tr.fd(21)
penseth(190, 8); tr.circle(-200, 26)
penseth(270, 16); tr.fd(21)
penseth(270, 10); tr.fd(18) 
penseth(270, 12); tr.fd(20)
tr.rt(180); tr.fd(20)
penseth(90, 10); tr.fd(18)
penseth(90, 16); tr.fd(21)
penseth(175, 8); tr.circle(-85, 110)
penseth(240, 12); tr.circle(130, 45)
tr.lt(180); tr.circle(-130, 65)
tr.goto(48, -205)
tr.end_fill()

tr.color("black","#cfcfcf")
posicion(100, -42, 7)
tr.begin_fill()
tr.seth(139); tr.circle(235, 68)
tr.seth(194); tr.circle(90, 135)
tr.seth(330); tr.circle(300, 53)
tr.seth(20); tr.circle(85, 130)
tr.end_fill()

estampas(-145, -140, 0.8, 0.8, 0, "circle")
estampas(20, -165, 0.55, 0.55, 0, "circle")


#Suelo
tr.pensize(2)
lineas_aleatorias(120, -325, 150, -410, -380, 30)
lineas_aleatorias(100, -255, 95, -430, -410, 30)
lineas_aleatorias(75, -205, 55, -450, -430, 25)
lineas_aleatorias(50, -150, 20, -470, -450)
lineas_aleatorias(25, -90, 0, -490, -471, 25)


#Espiral
esp = tr.Turtle()

esp.hideturtle()
esp.speed(10)
esp.pensize(1)
esp.pencolor("#911919")
tr.tracer(0)

radio = 0
while True:

    esp.clear()
    esp.penup()
    esp.goto(8, -268)
    esp.setheading(0)
    esp.pendown()

    radio = 0

    for i in range(50):
        esp.circle(radio, 80)
        radio += 0.5
        tr.update()
        tm.sleep(0.02)
