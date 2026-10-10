import turtle as tr
import random as rd

tr.setup(830, 800)
tr.bgcolor("#081353")
tr.speed(0)

def posicion(x,y, p, c=str("black")):
    tr.penup()
    tr.goto(x,y)
    tr.pendown()
    tr.pensize(p)
    tr.pencolor(c)

def penseth(s, p):
    tr.seth(s)
    tr.pensize(p)
    
def lineas(cantidad, largo, x1, x2, y1, y2, a1, a2, p= 1):
    tr.pensize(p)
    for _ in range(cantidad):
        x = rd.randint(x1, x2)
        y = rd.randint(y1, y2)
        angulo = rd.randint(a1, a2)
        tr.penup()
        tr.goto(x, y)
        tr.setheading(angulo)
        tr.pendown()
        tr.fd(largo)

def puntos_aleatorios(c, x1, x2, y1, y2,t_min=0.5, t_max =2,colores=None):
    tr.penup()
    tr.shape("circle")
    if colores is None:
        colores = ["#B2C2E4","#000757", "#000000","#494949","#FFFFFF"]
    for _ in range(c):
        x = rd.randint(x1, x2)
        y = rd.randint(y1, y2)
        tr.goto(x, y)
        tamaño = rd.uniform(t_min, t_max)
        tr.shapesize(tamaño)
        tr.color(rd.choice(colores))
        tr.stamp()

puntos_aleatorios(150, -500, 500, -500, 500, 0.1, 0.3)    

tr.pen(shown=False)
#Luna()
tr.color("black","#f2d06b")
posicion(0, 308, 6, "black")
tr.begin_fill()
tr.seth(3); tr.circle(-238)
tr.end_fill()


#Pasto
tr.color("black","#5f664c")
posicion(-415, 100, 4, "black")
tr.begin_fill()
tr.seth(355); tr.circle(-60, 35)
tr.seth(300); tr.circle(10, 80)
tr.seth(324); tr.circle(160, 31)
tr.seth(20); tr.circle(-28, 70)
tr.seth(300); tr.circle(30, 50)
tr.seth(321); tr.circle(60, 25)
tr.seth(347); tr.circle(-135, 60)#(-115.71,-74.67)
tr.seth(290); tr.circle(-45, 30)
tr.seth(278); tr.circle(-115, 30)
tr.seth(232); tr.circle(-175, 53)
tr.seth(226); tr.circle(10, 40)
tr.seth(300); tr.circle(-12, 90)
tr.seth(216); tr.circle(-200, 32)
tr.seth(218); tr.circle(12, 70)
tr.seth(300); tr.circle(-5, 60)
tr.seth(240); tr.circle(-50, 55)
tr.goto(-415, 100)
tr.end_fill()

lineas(60, 100, -450, -120, -170, 0, 179, 181)
lineas(40, 60, -450, -200, -230, -170, 181, 182)


#Parte de abajo acantilado
tr.color("black","#5a3117")
posicion(-115.71, -74.67, 3)
tr.begin_fill()
tr.seth(290); tr.circle(-45, 30)
tr.seth(278); tr.circle(-115, 30)
tr.seth(232); tr.circle(-175, 53)
penseth(270, 6); tr.circle(-350, 40)
tr.rt(180); tr.circle(350, 40)
penseth(226, 3); tr.circle(10, 40)
tr.seth(300); tr.circle(-12, 90)
tr.seth(216); tr.circle(-200, 32)
tr.seth(218); tr.circle(12, 70)
penseth(275, 6); tr.circle(-350, 25)
tr.lt(180); tr.circle(350, 25)
penseth(300, 3); tr.circle(-5, 25)
tr.seth(240); tr.circle(-50, 55)
tr.seth(270); tr.fd(105)
tr.seth(340); tr.circle(125, 50)
tr.seth(27); tr.circle(350, 15)
tr.seth(37); tr.circle(50, 30)
tr.seth(70); tr.circle(-275, 20)
tr.seth(43); tr.circle(230, 43)
tr.goto(-115.71, -74.67)
tr.end_fill()


#Personaje
tr.color("black", "#1A1919")
posicion(-161, 0, 3, "black")
tr.begin_fill()
tr.seth(237); tr.circle(80, 30)
tr.seth(270); tr.circle(-110, 20)
tr.seth(265); tr.circle(25, 100)
tr.seth(4); tr.circle(-75, 25)
tr.seth(0); tr.circle(-13, 100)
tr.seth(274); tr.fd(55)
tr.seth(347); tr.circle(105, 23)
tr.seth(100); tr.circle(25, 30)
tr.seth(352); tr.circle(14, 82)
tr.seth(167); tr.circle(-23, 55)
tr.seth(87); tr.circle(310, 11)
tr.seth(90); tr.circle(20, 90)
tr.seth(170); tr.fd(14)
tr.seth(178); tr.circle(-17, 90)
tr.seth(95); tr.circle(-150, 13)
tr.seth(130); tr.fd(13)
tr.seth(130); tr.circle(-3, 150)
tr.seth(320); tr.circle(3, 120)
tr.seth(84); tr.circle(-12, 61)
tr.seth(94); tr.circle(-35, 37)
tr.seth(135); tr.circle(45, 47)
tr.seth(191); tr.circle(20, 90)
tr.seth(327); tr.circle(-15, 120)
tr.goto(-161, 0)
tr.end_fill()



tr.done()