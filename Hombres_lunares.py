import turtle as tr
import random as rd

tr.bgcolor("#07145C")
tr.setup(840, 860)
tr.speed(0)
tr.tracer(0)

def posicion(x,y, p, c=str("black")):
    tr.penup()
    tr.goto(x,y)
    tr.pendown()
    tr.pensize(p)
    tr.pencolor(c)
    
def penseth(s, p):
    tr.seth(s)
    tr.pensize(p)
    
def circulo_profundidad(x, y, radio):
    tr.penup()
    tr.goto(x, y - radio)
    tr.pendown()
    tr.color("#2b6574")
    tr.begin_fill()
    tr.circle(radio)
    tr.end_fill()

    tr.penup()
    tr.goto(x + radio*0.2, y - radio*0.7)
    tr.pendown()
    tr.color("#3193ac")
    tr.begin_fill()
    tr.circle(radio * 0.6)
    tr.end_fill()
    
    tr.penup()
    tr.goto(x + radio*0.3, y - radio*0.4)
    tr.pendown()
    tr.color("#377f8f")
    tr.begin_fill()
    tr.circle(radio * 0.3)
    tr.end_fill()

def aliens_cuadricula(x1, x2, y1, y2, cantidad, escala):
    posiciones = []
    min_dist = 120 * escala
    intentos = 0
    max_intentos = 1000  
    while len(posiciones) < cantidad and intentos < max_intentos:
        x = rd.randint(x1, x2)
        y = rd.randint(y1, y2)
        valido = True
        
        for (px, py) in posiciones:
            distancia = ((x - px)**2 + (y - py)**2)**0.5
            if distancia < min_dist:
                valido = False
                break
        if valido:
            posiciones.append((x, y))
            dibujo(tr, x, y, escala)
        intentos += 1

def fondo():
    for _ in range(35):
        x = rd.randint(-500, 500)
        y = rd.randint(-450, 450)
        r = rd.randint(70, 120)
        circulo_profundidad(x, y, r)

fondo()
    
def dibujo(tr, x, y, escala=1, color="black"):
    def pos(px, py, grosor=1):
        tr.penup()
        tr.goto(x + px * escala, y + py * escala)
        tr.pendown()
        tr.pensize(grosor * escala)
        tr.pencolor(color)

    # -------- CUERPO --------
    tr.color("#000000","#CCEB77")
    pos(-85, -53, 2.5)
    tr.begin_fill()
    tr.seth(95); tr.circle(-600 * escala, 17)
    tr.seth(77); tr.circle(-300 * escala, 30)
    tr.seth(50); tr.circle(-70 * escala, 110)
    tr.seth(302); tr.circle(-150 * escala, 30)
    tr.seth(273); tr.circle(-400 * escala, 20)
    tr.seth(252); tr.circle(800 * escala, 8.4)
    tr.seth(262); tr.circle(20 * escala, 110)
    tr.seth(11); tr.circle(-70 * escala, 37)
    tr.seth(325); tr.circle(-14 * escala, 160)
    tr.seth(178); tr.circle(-250 * escala, 14)

    tr.pensize(1.5 * escala)
    tr.seth(120); tr.circle(-30 * escala, 35)
    tr.lt(180); tr.circle(30 * escala, 35)

    tr.pensize(2.5 * escala)
    tr.seth(303); tr.circle(60 * escala, 40)
    tr.seth(325); tr.circle(-60 * escala, 15)
    tr.seth(315); tr.circle(-11 * escala, 150)
    tr.seth(168); tr.circle(-80 * escala, 52)
    tr.seth(100); tr.circle(11 * escala, 170)
    tr.seth(275); tr.circle(50 * escala, 45)
    tr.seth(320); tr.circle(-60 * escala, 25)
    tr.seth(285); tr.circle(-11 * escala, 140)
    tr.seth(165); tr.circle(-45 * escala, 70)
    tr.seth(110); tr.fd(18 * escala)
    tr.seth(95); tr.circle(16.5 * escala, 170)
    tr.seth(260); tr.fd(10 * escala)
    tr.seth(260); tr.circle(-80 * escala, 35)
    tr.seth(220); tr.circle(-14 * escala, 150)
    tr.seth(63); tr.circle(-60 * escala, 13)
    tr.seth(35); tr.circle(40 * escala, 105)
    tr.seth(150); tr.circle(19 * escala, 80)
    tr.seth(230); tr.fd(20 * escala)
    tr.seth(240); tr.circle(-50 * escala, 70)
    tr.seth(180); tr.circle(-13 * escala, 150)
    tr.seth(40); tr.circle(-40 * escala, 35)
    tr.seth(20); tr.circle(60 * escala, 55)
    tr.lt(180); tr.circle(-60 * escala, 10)
    tr.seth(199); tr.circle(-130 * escala, 28)
    tr.seth(170); tr.circle(-12 * escala, 120)
    tr.seth(50); tr.circle(-33 * escala, 70)
    tr.seth(350); tr.circle(35 * escala, 65)
    tr.end_fill()

    # -------- OJO --------
    tr.color("#000000","#F0CEE8")
    pos(-8, 60, 2.5)
    tr.begin_fill()
    tr.seth(113); tr.circle(-150 * escala, 65)
    tr.seth(59); tr.circle(-32 * escala, 140)
    tr.seth(290); tr.circle(-150 * escala, 65)
    tr.seth(230); tr.circle(-30 * escala, 130)
    tr.end_fill()

    # -------- PUPILA --------
    tr.color("#000000","#330038")
    pos(45, 160, 1.5)
    tr.begin_fill()
    tr.seth(111); tr.fd(5 * escala)
    tr.seth(240); tr.fd(6 * escala)
    tr.seth(240); tr.circle(-3.5 * escala, 180)
    tr.seth(74); tr.fd(8.5 * escala)
    tr.seth(160); tr.fd(4 * escala)
    tr.seth(155); tr.circle(-5 * escala, 180)
    tr.seth(95); tr.fd(7 * escala)
    tr.seth(90); tr.circle(-4 * escala, 180)
    tr.seth(285); tr.fd(5 * escala)
    tr.seth(50); tr.fd(7 * escala)
    tr.seth(50); tr.circle(-3.6 * escala, 180)
    tr.seth(250); tr.fd(7 * escala)
    tr.seth(300); tr.fd(6 * escala)
    tr.seth(300); tr.circle(-5 * escala, 180)
    tr.end_fill()

    pos(25, 240, 1.5)
    tr.seth(30); tr.circle(-48 * escala, 120)

    pos(-16, 59, 1.5)
    tr.seth(290); tr.circle(40 * escala, 85)

    tr.color("#000000","#DBEEA7")
    tr.penup()
    tr.begin_fill()
    tr.goto(x + (-43 * escala), y + (114 * escala))
    tr.setheading(280); tr.circle(150 * escala, 25)
    tr.setheading(309); tr.circle(75 * escala, 70)
    tr.setheading(23); tr.circle(-16 * escala, 180)
    tr.setheading(200); tr.circle(-100 * escala, 105)
    tr.setheading(100); tr.circle(-75 * escala, 20)
    tr.setheading(85); tr.circle(-6 * escala, 160)
    tr.end_fill()
    tr.pendown()

    # -------- DIENTES --------
    tr.color("#000000","#FFFFFF")
    pos(-50, 110, 2.5)
    tr.seth(287); tr.circle(-150 * escala, 14)
    tr.seth(295); tr.circle(175 * escala, 20)
    tr.seth(325); tr.circle(75 * escala, 65)
    
    pos(-43.65, 73.99, 2)
    tr.begin_fill()
    tr.seth(295); tr.circle(175 * escala, 20)
    tr.seth(325); tr.circle(75 * escala, 57)
    tr.seth(273); tr.circle(-50 * escala, 28)
    tr.seth(265); tr.circle(-2 * escala, 180)
    tr.seth(90); tr.fd(3 * escala)
    tr.seth(262); tr.circle(-60 * escala, 31)
    tr.seth(256); tr.circle(-5 * escala, 170)
    tr.seth(88); tr.circle(55 * escala, 15)
    tr.seth(261); tr.circle(-55 * escala, 33)
    tr.seth(230); tr.circle(-9 * escala, 120)
    tr.seth(95); tr.circle(-100 * escala, 15)
    tr.seth(91); tr.circle(-100 * escala, 18)
    tr.seth(263); tr.circle(-100 * escala, 15)
    tr.seth(250); tr.circle(-100 * escala, 13)
    tr.seth(251); tr.circle(-11 * escala, 160)
    tr.seth(110); tr.circle(-55 * escala, 40)
    tr.seth(80); tr.circle(0.5 * escala, 180)
    tr.seth(250); tr.circle(-75 * escala, 10)
    tr.seth(248); tr.circle(-6 * escala, 160)
    tr.seth(110); tr.circle(-88 * escala, 52)
    tr.end_fill()

aliens_cuadricula(200, 500, 225, 500, 25, 0.1)
aliens_cuadricula(50, 200, 225, 450, 15, 0.15)
aliens_cuadricula(150, 450, 75, 225, 13, 0.15)
aliens_cuadricula(250, 450, -325, 100, 15, 0.18)
aliens_cuadricula(100, 300, -400, 125, 10, 0.23)
aliens_cuadricula(0, 200, -160, 50, 7, 0.3)
aliens_cuadricula(-150, 150, 50, 190, 7, 0.26)
aliens_cuadricula(-125, -120, -25, 25, 1, 0.46)
aliens_cuadricula(25, 50, -350, -325, 1, 0.46)
aliens_cuadricula(-100, -75, -250, -200, 1, 0.6)


tr.done()