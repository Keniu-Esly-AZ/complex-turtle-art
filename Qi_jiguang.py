import turtle as tr
import random as rd

tr.setup(800, 980)
#tr.tracer(0,0)
tr.speed(0)


def nube(x, y, r, p):
    tr.penup()
    tr.goto(x, y)
    tr.pendown()
    tr.color("#aaaaaa")
    tr.fillcolor("#e8e4de")
    tr.begin_fill()
    tr.seth(0)
    paso = 360 / p
    for i in range(p):
        tr.seth(i * paso)
        tr.circle(-r, 360 // p)
        tr.left(60)
        tr.circle(r, 1)
    tr.end_fill()

def nube_realista(x, y, escala):
    bolitas = [
        (0,        0,      escala * 1.0),
        (escala*1.1, escala*0.3, escala * 0.9),
        (-escala*1.0, escala*0.2, escala * 0.85),
        (escala*2.0, escala*0.1, escala * 0.75),
        (-escala*1.9, escala*0.0, escala * 0.7),
        (escala*0.5, escala*0.9, escala * 0.8),
        (-escala*0.4, escala*0.8, escala * 0.75),
        (escala*1.5, escala*0.7, escala * 0.65),
        (-escala*1.4, escala*0.6, escala * 0.6),
    ]
    for (cx, cy, r) in bolitas:
        tr.penup()
        tr.goto(x + cx, y + cy)
        tr.pendown()
        tr.color("#999999")
        tr.fillcolor("#edeae4")
        tr.begin_fill()
        tr.circle(r)
        tr.end_fill()

def montana_circular(cx, cy, rx, ry, color_fill, color_borde, base_y=-490):
    tr.penup()
    tr.goto(cx - rx, base_y)
    tr.pendown()
    tr.color(color_borde)
    tr.fillcolor(color_fill)
    tr.pensize(1.2)
    tr.begin_fill()
    pasos = 80
    for i in range(pasos + 1):
        angulo = (180 / pasos) * i   
        rad = angulo * 3.14159 / 180
        px = cx + rx * (-(1) + 2 * i/pasos)
        py = cy + ry * (1 - (2*i/pasos - 1)**2) ** 0.5 
        tr.goto(px, py)
    tr.goto(cx + rx, base_y)
    tr.goto(cx - rx, base_y)
    tr.end_fill()

def montana_ondulada(picos, color_fill, color_borde, base_y=-490):
    tr.penup()
    tr.goto(picos[0][0], base_y)
    tr.pendown()
    tr.color(color_borde)
    tr.fillcolor(color_fill)
    tr.pensize(1.2)
    tr.begin_fill()
    tr.goto(picos[0][0], picos[0][1])

    for i in range(len(picos) - 1):
        x0, y0 = picos[i]
        x1, y1 = picos[i+1]
        pasos = 30
        for s in range(pasos + 1):
            frac = s / pasos
            cx1 = x0 + (x1 - x0) * 0.3
            cy1 = max(y0, y1) + rd.uniform(20, 50)
            cx2 = x0 + (x1 - x0) * 0.7
            cy2 = max(y0, y1) + rd.uniform(20, 50)
            bx = ((1-frac)**3 * x0 + 3*(1-frac)**2*frac * cx1 +
                  3*(1-frac)*frac**2 * cx2 + frac**3 * x1)
            by = ((1-frac)**3 * y0 + 3*(1-frac)**2*frac * cy1 +
                  3*(1-frac)*frac**2 * cy2 + frac**3 * y1)
            tr.goto(bx, by)

    tr.goto(picos[-1][0], base_y)
    tr.goto(picos[0][0],  base_y)
    tr.end_fill()

def dibujar_paisaje():
    rd.seed(7)

    tr.bgcolor("#dde8f0")

    montana_circular(-200, -30, 420, 200, "#c8d4b4", "#a0b088")
    montana_circular(200,  20,  380, 230, "#b8c8a0", "#90a878")

    rd.seed(5)
    picos_m3 = [
        (-400, -80), (-300, 30), (-180, 60), (-60, 10),
        (60, 70), (180, 20), (300, 60), (400, 10)
    ]
    montana_ondulada(picos_m3, "#a8ba90", "#7a9860")
    rd.seed(9)
    picos_m4 = [
        (-400, -130), (-300, -50), (-160, -20), (-40, -70),
        (80, -30), (200, -60), (320, -40), (400, -100)
    ]
    montana_ondulada(picos_m4, "#98aa80", "#688058")
    nubes_realistas = [
        (-280, 310, 22),
        (-60,  330, 28),
        (160,  320, 24),
        (340,  305, 18),
        (-380, 285, 16),
        (50,   280, 15),
    ]
    for (nx, ny, esc) in nubes_realistas:
        nube_realista(nx, ny, esc)
    nubes_extra = [
        (-160, 350, 14, 9),
        (260,  340, 16, 9),
        (-20,  360, 12, 8),
    ]
    for (nx, ny, nr, np_) in nubes_extra:
        nube(nx, ny, nr, np_)

dibujar_paisaje()



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
    

#Penacho
tr.color("black","#7C1717")
posicion(5.57,207.57, 2.5, "black")
tr.begin_fill()
tr.seth(110); tr.circle(20, 100)
tr.seth(202); tr.circle(60, 38)
tr.rt(180); tr.circle(-60, 28)
tr.seth(230); tr.circle(120, 37)
tr.seth(265); tr.circle(-100, 35)
tr.lt(180); tr.circle(100, 10)
tr.seth(255); tr.circle(100, 25)
tr.seth(270); tr.circle(-80, 60)
tr.rt(180); tr.circle(80, 30)
tr.seth(240); tr.circle(110, 35)
tr.rt(193); tr.circle(-110, 35)
tr.seth(272); tr.circle(-120, 50)
tr.rt(189); tr.circle(120, 5)
tr.seth(276); tr.circle(-120, 15)
tr.seth(10); tr.fd(150)
tr.goto(5.57,207.57)
tr.end_fill()

def cola_caballo(x, y, mechones=40):
    tr.pencolor("black"); tr.pensize(2)
    for i in range(mechones):
        tr.penup()
        tr.goto(x + rd.uniform(-5,5), y + rd.uniform(-5,5))
        tr.pendown()

        tr.seth(110 + rd.uniform(-5,5))
        tr.circle(rd.uniform(15,25), rd.uniform(170,210))

def curvas_area(x1, x2, y1, y2, cantidad=80):
    tr.pensize(3)
    for i in range(cantidad):
        x = rd.uniform(x1, x2)
        y = rd.uniform(y1, y2)
        tr.penup()
        tr.goto(x, y)
        tr.pendown()
        tr.seth(rd.uniform(250,290))
        radio = rd.uniform(80,45)
        angulo = rd.uniform(20,25)
        if rd.choice([True, False]):
            radio = -radio
        tr.circle(radio, angulo)


cola_caballo(8,189,14)
curvas_area(-75,25,-55,158, 55)


##
tr.color("black","#928E8E")
posicion(131.63,-82.50, 3, "black")
tr.begin_fill()
tr.seth(80); tr.fd(15)
tr.seth(160); tr.fd(7)
tr.seth(90); tr.circle(60, 26)
tr.seth(140); tr.fd(25)
tr.seth(269); tr.circle(-80, 34)
tr.seth(227); tr.circle(70, 22)
tr.seth(129); tr.circle(70, 27)
tr.seth(156); tr.circle(-90, 38)
tr.seth(223); tr.fd(24)
tr.seth(300); tr.circle(-60, 17)
tr.seth(210); tr.fd(9)
tr.goto(-11.86,-74.98)
tr.seth(332); tr.circle(170, 50)
tr.end_fill()



#Cuello
tr.color("black","#E0A36A")
posicion(102.43,-22.96, 2, "black")
tr.begin_fill()
tr.seth(269); tr.circle(-80, 34)
tr.seth(227); tr.circle(70, 22)
tr.seth(129); tr.circle(70, 27)
tr.seth(156); tr.circle(-90, 38)
tr.seth(60); tr.fd(50)
tr.goto(102.43,-22.96)
tr.end_fill()


#Casco
tr.color("black","#B87F06")
posicion(71, 13, 3, "black")
tr.begin_fill()
tr.seth(130); tr.circle(-115, 36)
tr.seth(110); tr.circle(-20, 90)
tr.seth(23); tr.circle(-120, 37)
tr.seth(95); tr.circle(80, 27)
tr.seth(180); tr.fd(3)
tr.seth(119); tr.circle(87, 68)#(30.70,190.10)
tr.seth(204); tr.circle(90, 70)
tr.seth(263); tr.circle(100, 30)
tr.seth(290); tr.circle(-250, 11)
tr.seth(19); tr.circle(-180, 24)
tr.end_fill()

tr.color("black","#642C16")
posicion(7.67,175.29, 3, "black")
tr.begin_fill()
tr.seth(5); tr.circle(-80, 55)
tr.seth(184); tr.circle(60, 50)
tr.seth(240); tr.circle(75, 50)
tr.seth(280); tr.circle(125, 17.5)
tr.seth(183); tr.circle(100, 22)
tr.seth(99); tr.circle(250, 15)
tr.seth(94); tr.circle(-180, 20)
tr.seth(63); tr.circle(-120, 22)
tr.goto(7.67, 175.29)
tr.end_fill()

tr.color("black","#E49520")
posicion(30.70,190.10, 2, "black")
tr.begin_fill()
tr.seth(100); tr.circle(10, 68)
tr.seth(130); tr.fd(15)
tr.seth(185); tr.circle(23, 80)
tr.seth(310); tr.fd(15)
tr.seth(60); tr.circle(-50, 25)
tr.rt(180); tr.circle(50, 25)
tr.seth(220); tr.circle(7, 75)
tr.seth(53); tr.circle(-55, 40)
tr.end_fill()


tr.color("black","#9C6C23")
posicion(57,13.71, 3, "black")
tr.begin_fill()
tr.seth(270); tr.fd(43)
tr.seth(270); tr.circle(-7, 170)
tr.seth(90); tr.fd(8)
tr.rt(180); tr.fd(8)
tr.seth(270); tr.circle(-7.3, 175)
tr.seth(80); tr.fd(8)
tr.lt(183); tr.fd(8)
tr.seth(268); tr.circle(-6.8, 170)
tr.seth(90); tr.fd(7)
tr.rt(193); tr.fd(8)
tr.seth(263); tr.circle(-7, 180)
tr.seth(80); tr.fd(5)
tr.lt(180); tr.fd(4)
tr.seth(260); tr.circle(-5, 140)
tr.seth(68); tr.circle(150, 14)
tr.seth(22); tr.circle(-135, 24)
tr.end_fill()


posicion(57.00,-9.29, 2, "black")
tr.seth(270); tr.circle(-7, 170)
tr.seth(90); tr.fd(4)
tr.rt(180); tr.fd(4)
tr.seth(270); tr.circle(-7.3, 175)
tr.seth(80); tr.fd(4)
tr.lt(183); tr.fd(4)
tr.seth(268); tr.circle(-6.8, 170)
tr.seth(90); tr.fd(4)
tr.rt(193); tr.fd(5)
tr.seth(263); tr.circle(-7, 180)
tr.seth(80); tr.fd(5)
tr.lt(180); tr.fd(4)


tr.color("black","#301313")
posicion(44.38,78.90, 2, "black")
tr.begin_fill()
tr.seth(110); tr.circle(-20, 90)
tr.seth(23); tr.circle(-120, 37)
tr.seth(305); tr.circle(-15, 70)
tr.seth(105); tr.circle(20, 30)
tr.seth(170); tr.circle(120, 10)
tr.seth(184); tr.circle(85, 30)
tr.seth(200);  tr.circle(40, 35)
tr.goto(44.38, 78.90)
tr.end_fill()


tr.color("black","#9C6C23")
posicion(113.46,-27.16, 2, "black")
tr.begin_fill()
tr.seth(3); tr.circle(14.7, 75)
tr.seth(90); tr.circle(-50, 15)
tr.seth(58); tr.circle(35, 30)
tr.seth(93); tr.circle(-50, 15)
tr.seth(66), tr.circle(43, 50)
tr.seth(107); tr.circle(-16, 35)
tr.seth(310); tr.circle(-40, 40)
tr.seth(270); tr.circle(40, 30)
tr.seth(283); tr.fd(8)
tr.seth(200); tr.fd(9)
tr.seth(305); tr.circle(-40, 60)
tr.seth(250); tr.circle(-20, 30); tr.pencolor("black")
tr.seth(300); tr.circle(-2, 210)
tr.seth(270); tr.circle(-3, 180)
tr.seth(250); tr.circle(-3,5, 180)
tr.seth(250); tr.circle(-3.5, 120)
tr.seth(160); tr.circle(-25, 30)
tr.end_fill()


#Rostro
tr.color("black","#E0A36A")
posicion(132.25,93.30, 2, "black")
tr.begin_fill()
tr.seth(105); tr.circle(20, 30)
tr.seth(170); tr.circle(120, 10)
tr.seth(184); tr.circle(85, 30)
tr.seth(200);  tr.circle(40, 35)
tr.seth(277); tr.circle(115, 35)
tr.seth(173); tr.circle(50, 20)
tr.seth(270); tr.fd(15), tr.pensize(3.5)
tr.seth(315); tr.circle(80, 45); tr.pensize(2)
tr.seth(3); tr.circle(14.7, 75)
tr.seth(90); tr.circle(-50, 15)
tr.seth(58); tr.circle(35, 30)
tr.seth(93); tr.circle(-50, 15)
tr.seth(66), tr.circle(43, 50)
tr.seth(107); tr.circle(-16, 40)
tr.seth(70); tr.circle(20, 60)
tr.end_fill()


#Facciones
tr.color("black","black")
posicion(69, 85, 1, "black")
tr.begin_fill()
tr.seth(35); tr.fd(15)
tr.seth(355); tr.circle(-80, 18)
tr.seth(280); tr.circle(-5, 140)
tr.seth(162); tr.circle(60, 28)
tr.end_fill()

posicion(117, 85, 1, "black")
tr.begin_fill()
tr.seth(55); tr.circle(-16, 78)
tr.seth(270); tr.fd(4)
tr.seth(150); tr.circle(14, 90)
tr.goto(117, 85)
tr.end_fill()

tr.color("black","white")
posicion(77, 69, 0.8, "black")
tr.begin_fill()
tr.seth(53); tr.circle(-14, 100)
tr.seth(210); tr.circle(-25, 55)
tr.goto(77, 69)
tr.end_fill()

tr.color("black","white")
posicion(118, 68, 0.8, "black")
tr.begin_fill()
tr.seth(80); tr.circle(-10, 115)
tr.seth(235); tr.circle(-16, 60)
tr.end_fill()

tr.color("black","black")
posicion(75, 69, 1.5, "black")
tr.begin_fill()
tr.seth(25); tr.fd(19)
tr.seth(320); tr.circle(-20, 40)
tr.lt(180); tr.circle(20, 20)
tr.seth(275); tr.circle(-4, 180)
tr.seth(120); tr.circle(-10, 15)
tr.goto(75, 69)
tr.end_fill()

posicion(118, 68, 1.5, "black")
tr.begin_fill()
tr.seth(80); tr.circle(-10, 105)
tr.seth(305); tr.circle(-4, 180)
tr.seth(100); tr.circle(-6, 60)
tr.end_fill()

posicion(117, 82, 1.7, "black")
tr.seth(255); tr.circle(23, 50)
tr.seth(290); tr.fd(15)

posicion(121, 30, 3.3, "black")
tr.seth(50); tr.fd(5)

posicion(118, 33, 1, "black")
tr.begin_fill()
tr.seth(80); tr.circle(4, 140)
tr.seth(220); tr.circle(8, 70)
tr.seth(160); tr.circle(-10, 75); tr.pensize(1.6)
tr.rt(180); tr.circle(10, 75); tr.pensize(1)
tr.seth(75); tr.circle(-8, 80)
tr.end_fill()


"""tr.color("black","#E4AB76")
posicion(104.00,11.00, 1.2, "black")
tr.begin_fill()
tr.seth(60); tr.circle(-25, 22)
tr.seth(325); tr.circle(7, 75)
tr.seth(330); tr.circle(-20, 20)
tr.seth(250); tr.circle(-20, 20)
tr.seth(140); tr.circle(7, 75)
tr.seth(150); tr.circle(-20, 25)
tr.end_fill()
"""
posicion(106.00,13, 2, "black")
tr.seth(0); tr.fd(16)



#Armadura
tr.color("black","#633007")
posicion(-85, -455, 4, "black")
tr.begin_fill()
tr.seth(73); tr.circle(450, 15)#(-65.95,-346.98) Laso sintura
tr.seth(85.3); tr.circle(750, 9.2)#(-63.46,-254.13) Laso pecho
tr.seth(20); tr.circle(38, 70)
tr.seth(88); tr.fd(32)
tr.seth(91); tr.circle(-25, 85)
tr.seth(11); tr.circle(-400, 24)
tr.seth(351); tr.circle(-25, 85)
tr.seth(276.5); tr.fd(34)
tr.seth(278.5); tr.circle(40, 41)
tr.seth(266); tr.circle(750, 9.2)
tr.seth(270); tr.circle(450, 16)
tr.goto(-85, -455)
tr.end_fill()


tr.color("black","red")
posicion(-65.95,-346.98, 6, "black")
tr.begin_fill()
tr.seth(10); tr.circle(-250, 19)
tr.seth(340); tr.circle(-75, 25)
tr.lt(180); tr.circle(75, 5)
tr.seth(13); tr.circle(-150, 31)
tr.seth(200); tr.circle(40, 25)
tr.rt(180); tr.circle(-40, 25)
tr.seth(13); tr.circle(-220, 19)
tr.seth(275); tr.fd(26)
tr.seth(175); tr.circle(1000, 7)
tr.seth(170); tr.circle(750, 10.8)
tr.seth(92); tr.fd(23)
tr.goto(-65.95, -346.98)
tr.end_fill()

posicion(193.97,-384.25, 6, "black")
tr.begin_fill()
tr.seth(175); tr.circle(1000, 7)
tr.seth(170); tr.circle(750, 10.8)
tr.seth(262); tr.fd(30)
tr.seth(0); tr.circle(-1000, 6)
tr.seth(310); tr.fd(7)
tr.seth(252); tr.fd(50)
tr.seth(355); tr.fd(14)
tr.seth(72); tr.fd(50)
tr.seth(345); tr.fd(7)
tr.seth(259); tr.fd(46)
tr.seth(0); tr.fd(32)
tr.seth(93); tr.fd(44)
tr.seth(30); tr.fd(10)
tr.seth(280); tr.fd(50)
tr.seth(0); tr.fd(20)
tr.seth(95); tr.circle(120, 25)
tr.seth(353); tr.circle(750, 7.5)
tr.goto(193.97, -384.35)
tr.end_fill()


posicion(-63.46,-254.13, 4, "black")
tr.begin_fill()
tr.seth(27); tr.circle(-600, 14)
tr.seth(345); tr.circle(-500, 14)
tr.seth(265); tr.fd(24)
tr.seth(149); tr.circle(500, 13)
tr.seth(191), tr.circle(600, 14.5)
tr.goto(-63.46, -254)
tr.end_fill()


posicion(-65.40,-218.84, 4, "black")
tr.begin_fill()
tr.seth(20); tr.circle(38, 70)
tr.seth(88); tr.fd(32)
tr.seth(91); tr.circle(-25, 85)
tr.seth(11); tr.circle(-400, 24)
tr.seth(351); tr.circle(-25, 85)
tr.seth(276.5); tr.fd(34)
tr.seth(278.5); tr.circle(40, 41)
tr.seth(270); tr.fd(13)
tr.seth(160); tr.circle(-40, 60)
tr.seth(96); tr.fd(34)
tr.seth(96); tr.circle(20, 80)
tr.seth(170); tr.circle(500, 17.3)
tr.seth(180); tr.circle(20, 80)
tr.seth(266); tr.fd(34)
tr.seth(260); tr.circle(-45, 66)
tr.goto(-65.40, -218.84)
tr.end_fill()


estampas(70, -390, 3.5, 3.1, 350, "circle","black","#9B7804")
estampas(70, -390, 2.6, 2.2, 350, "circle","black","#9B7804")
estampas(70, -223, 4.2, 5.3, 5, "circle","black","#9B7804")
estampas(70, -130, 2.6, 1, 1, "square","black","#D3A612")
tr.pen(shown=False)


tr.color("black","red")
posicion(-65.40, -218.84, 2, "black")
tr.begin_fill()
tr.seth(20); tr.circle(38, 70)
tr.seth(88); tr.fd(32)
tr.seth(91); tr.circle(-25, 65)#parte interna (-25.24,-128.25)
tr.seth(113); tr.fd(55)
tr.seth(225); tr.circle(-13, 115)
tr.seth(302.12); tr.circle(-150, 38)
tr.seth(275); tr.circle(-50, 60)
tr.goto(-65.40, -218.84)
tr.end_fill()

posicion(187.87,-213.48, 2, "black")
tr.begin_fill()
tr.seth(140); tr.circle(-40, 41)
tr.seth(97); tr.fd(39)
tr.seth(97); tr.circle(25, 58)
tr.seth(80); tr.fd(55)
tr.seth(320); tr.circle(14, 65)
tr.seth(300); tr.circle(-50, 25)
tr.seth(254); tr.circle(200, 25)
tr.seth(290); tr.circle(60, 17)
tr.goto(187.87, -213.48)
tr.end_fill()


tr.color("black","brown")
posicion(-25.24,-128.25, 3, "black")
tr.begin_fill()
tr.seth(113); tr.fd(55)
tr.seth(20); tr.fd(35)
tr.seth(280); tr.circle(100, 37)
tr.goto(-25.24, -128.25)
tr.end_fill()

posicion(155.07,-130.78, 3, "black")
tr.begin_fill()
tr.seth(80); tr.fd(53)
tr.seth(163); tr.fd(32)
tr.seth(272); tr.circle(-100, 33)
tr.goto(155.07, -130.78)
tr.end_fill()


tr.color("black","red")
posicion(-46.73,-77.62, 4, "black")
tr.begin_fill()
tr.seth(225); tr.circle(-13, 115)
tr.seth(110); tr.fd(3)
tr.seth(193); tr.fd(25)
tr.seth(50); tr.circle(-75, 28)
tr.seth(20); tr.fd(48)
tr.seth(310); tr.circle(-60, 28)
tr.goto(-46.73, -77.62)
tr.end_fill()

posicion(164.62,-76.61, 4, "black")
tr.begin_fill()
tr.seth(320); tr.circle(14, 65)
tr.seth(120); tr.fd(5)
tr.seth(320); tr.circle(4.5, 180)
tr.seth(120); tr.fd(11)
tr.seth(160); tr.fd(58)
tr.seth(298); tr.circle(-60, 28)
tr.goto(164.62, -76.61)
tr.end_fill()


tr.color("black","#6E0707")
posicion(16.44,-121.42, 1.5, "black")
tr.begin_fill()
tr.seth(7); tr.circle(-400, 14.7)
tr.seth(60); tr.circle(100, 24)
tr.seth(202); tr.circle(-170, 50)
tr.seth(280); tr.circle(100, 5)
tr.seth(332); tr.circle(170, 48)
tr.lt(180); tr.circle(-170, 20)
tr.seth(270); tr.fd(16)
tr.rt(180); tr.fd(16)
tr.seth(180); tr.circle(-170, 28)
tr.seth(290); tr.circle(100, 26)
tr.end_fill()


tr.color("black","#928E8E")
posicion(131.63,-82.50, 3, "black")
tr.begin_fill()
tr.seth(80); tr.fd(15)
tr.seth(160); tr.fd(7)
tr.seth(90); tr.circle(60, 26)
tr.seth(140); tr.fd(25)
tr.seth(269); tr.circle(-80, 34)
tr.seth(227); tr.circle(70, 22)
tr.seth(129); tr.circle(70, 27)
tr.seth(156); tr.circle(-90, 38)
tr.seth(223); tr.fd(24)
tr.seth(300); tr.circle(-60, 17)
tr.seth(210); tr.fd(9)
tr.goto(-11.86,-74.98)
tr.seth(332); tr.circle(170, 50)
tr.end_fill()


#Hombreras
tr.color("black","#612306")
posicion(-68.14,-72.87, 2, "black")
tr.begin_fill()
tr.seth(302.12); tr.circle(-150, 26)
tr.seth(233); tr.circle(90, 25)
tr.seth(258); tr.circle(-400, 16)
tr.seth(200); tr.circle(-150, 5)
tr.seth(180); tr.circle(-90, 46.4)
tr.seth(66); tr.circle(350, 10)
tr.seth(78); tr.circle(-350, 10)
tr.seth(347); tr.circle(70, 61)
tr.goto(-68.14, -72.87)
tr.end_fill()

posicion(179.54,-78.57, 2, "black")
tr.begin_fill()
tr.seth(300); tr.circle(-50, 25)
tr.seth(254); tr.circle(200, 13)
tr.seth(315); tr.circle(-60, 30)
tr.seth(283); tr.circle(500, 14.8)
tr.seth(10); tr.circle(95, 40)
tr.seth(118); tr.circle(-300, 10)
tr.seth(103); tr.circle(350, 12.4)
tr.seth(186); tr.circle(-70, 55)
tr.goto(179.54, -78.57)
tr.end_fill()

tr.color("black","red")
posicion(-68.14,-72.87, 2, "black")
tr.begin_fill()
tr.seth(302.12); tr.circle(-150, 26)
tr.seth(233); tr.circle(90, 25)
tr.seth(258); tr.circle(-400, 16)
tr.seth(200); tr.circle(-150, 5)
tr.seth(180); tr.circle(-90, 46.4)
tr.seth(66); tr.circle(350, 10)
tr.seth(78); tr.circle(-350, 10)
tr.seth(355); tr.fd(8)
tr.seth(258); tr.circle(-600, 10.1)
tr.seth(327); tr.circle(140, 25)
tr.seth(74); tr.circle(-850, 6)
tr.seth(75); tr.circle(-200, 13)
tr.seth(98); tr.circle(60, 23)
tr.goto(-68.14, -72.87)
tr.end_fill()


posicion(179.54,-78.57, 2, "black")
tr.begin_fill()
tr.seth(300); tr.circle(-50, 25)
tr.seth(254); tr.circle(200, 13)
tr.seth(315); tr.circle(-60, 30)
tr.seth(283); tr.circle(500, 14.8)
tr.seth(10); tr.circle(95, 40)
tr.seth(118); tr.circle(-300, 4)
tr.seth(220); tr.circle(-150, 19)
tr.seth(116); tr.circle(-600, 10)
tr.seth(95); tr.circle(50, 57)
tr.seth(268); tr.fd(10)
tr.end_fill()

tr.color("black","#B64011")
posicion(-140.23,-136.68,3, "black")
tr.begin_fill()
tr.seth(347); tr.circle(70, 61)
tr.goto(-68.14, -72.87)
tr.seth(110); tr.fd(3)
tr.seth(184); tr.circle(70, 40)
tr.seth(220); tr.circle(250, 12)
tr.seth(250); tr.circle(7, 140)
tr.end_fill()

posicion(249.98,-139.46, 3, "black")
tr.begin_fill()
tr.seth(186); tr.circle(-70, 55)
tr.goto(179.54, -78.57)
tr.seth(110); tr.circle(-5, 160)
tr.seth(350); tr.circle(-60, 45)
tr.seth(318); tr.circle(-150, 16)
tr.seth(310); tr.circle(-4, 140)
tr.end_fill()



#Brazos
tr.color("black","#351A04")
posicion(-63.09,-277.68, 3, "black")
tr.begin_fill()
tr.seth(91); tr.circle(750, 5)
tr.seth(30); tr.circle(40, 60)
tr.seth(76); tr.circle(100, 23)
tr.seth(233); tr.circle(90, 25)
tr.seth(258); tr.circle(-400, 16)
tr.seth(200); tr.circle(-150, 5)
tr.seth(180); tr.circle(-90, 43.5)
tr.seth(225); tr.circle(30, 55)
tr.seth(170); tr.circle(45, 50)
tr.seth(228); tr.circle(55, 140)
tr.seth(320); tr.circle(15, 90)
tr.seth(340); tr.circle(17, 100)
tr.seth(357); tr.circle(40, 16)
tr.seth(37); tr.circle(125, 17)
tr.seth(43); tr.circle(10, 80)
tr.seth(120); tr.circle(-6, 140)
tr.seth(15); tr.circle(10, 60)
tr.seth(79); tr.circle(100, 16)
tr.seth(90); tr.circle(-8, 95)
tr.end_fill()


tr.color("black","#800F0F")
posicion(-170.56,-384.72, 3, "black")
tr.begin_fill()
tr.seth(355); tr.circle(30, 80)
tr.seth(68); tr.circle(50, 55)
tr.seth(106); tr.circle(50, 90)#(-205.24,-282.36)
tr.seth(190); tr.circle(35, 80)
tr.seth(259); tr.circle(80, 50)
tr.seth(320); tr.circle(45, 36)
tr.goto(-170.56, -384.72)
tr.end_fill()

posicion(-170.56, -384.72, 3, "black")
tr.seth(33); tr.circle(50, 100)

tr.color("black","#180E0E")
posicion(-205.24,-282.36,  3, "black")
tr.begin_fill()
tr.seth(198); tr.circle(35, 80)
tr.seth(260); tr.circle(80, 30)
tr.seth(300); tr.circle(60, 30)
tr.seth(350); tr.circle(45, 120)
tr.seth(100); tr.circle(50, 80)
tr.end_fill()


tr.color("black","#351A04")
posicion(188.67,-328.55, 3, "black")
tr.begin_fill()
tr.seth(95); tr.circle(-750, 9.8)
tr.seth(120); tr.circle(-60, 30)
tr.seth(97); tr.circle(-120, 12)
tr.seth(315); tr.circle(-60, 30)
tr.seth(283); tr.circle(500, 14.8)
tr.seth(10); tr.circle(95, 26)
tr.seth(295); tr.circle(-115, 19)
tr.seth(340); tr.circle(-18, 122)
tr.seth(350); tr.circle(-15, 130)
tr.seth(250); tr.circle(3, 80)
tr.seth(281); tr.circle(-750, 6.5)
tr.seth(175); tr.circle(150, 30)
tr.seth(95); tr.circle(140, 23)
tr.seth(113); tr.circle(-65, 32)
tr.seth(175); tr.circle(-11, 130)
tr.seth(170); tr.circle(-20, 70)
tr.seth(87); tr.circle(25, 40)
tr.end_fill()


tr.color("black","#E79D57")
posicion(-158.64,-310.63, 2 , "black")
tr.begin_fill()
tr.seth(295); tr.circle(-55, 75)
tr.rt(85); tr.circle(-40, 110)
tr.end_fill()


#Lanza
tr.color("black","#5A3305")
posicion(-166, -460, 2, "black")
tr.begin_fill()
tr.seth(93.3); tr.fd(740)
tr.seth(185); tr.fd(19)
tr.seth(273.3); tr.fd(737)
tr.goto(-166, -460)
tr.end_fill()


tr.color("black","#970909")
posicion(-208.60,278.77, 2, "black")
tr.begin_fill()
tr.seth(35); tr.circle(18, 295)#(-207.35,307.30)
tr.seth(15); tr.circle(-50, 22)
tr.lt(180); tr.circle(50,22)
tr.seth(230); tr.circle(68, 35)
tr.seth(269); tr.circle(-200, 33)
tr.rt(185); tr.circle(200, 11)
tr.seth(260); tr.circle(-180, 26)
tr.rt(194); tr.circle(130, 17)
tr.seth(252); tr.circle(-180, 10)
tr.rt(190); tr.circle(140, 12)
tr.seth(259); tr.circle(250, 9)
tr.rt(194); tr.circle(-80, 10)
tr.seth(264); tr.circle(100, 20)
tr.rt(192); tr.circle(-120, 21)
tr.seth(98); tr.circle(-80, 23)
tr.lt(185); tr.circle(80, 25)
tr.seth(262); tr.circle(75, 30)
tr.rt(189); tr.circle(-75, 22)
tr.seth(95); tr.circle(-30, 40)
tr.seth(268); tr.circle(-90, 12)
tr.rt(198); tr.circle(40, 40)
tr.seth(275), tr.circle(-200, 8)
tr.rt(195); tr.circle(160, 18)
tr.seth(280); tr.circle(-200, 17)
tr.rt(193); tr.circle(200, 20)
tr.seth(96); tr.circle(-80, 27)
tr.seth(270); tr.circle(220, 29)
tr.rt(195); tr.circle(-220, 15)
tr.seth(270); tr.circle(80, 29)
tr.rt(193); tr.circle(-130, 18)
tr.seth(293); tr.circle(75, 18)
tr.rt(183); tr.circle(-75, 18)
tr.seth(100); tr.fd(20)
tr.seth(290); tr.circle(100, 24)
tr.rt(195); tr.circle(-200, 27)
tr.seth(89); tr.circle(140, 27)
tr.goto(-208.60,278.77)
tr.end_fill()


tr.color("black","silver")
posicion(-207.35,307.30, 2, "black")
tr.begin_fill()
tr.seth(140); tr.circle(18, 100)
tr.seth(60); tr.fd(14)
tr.seth(40); tr.circle(-14, 70)#70
tr.goto(-207.35, 307.30)
tr.end_fill()

posicion(-227.51,314.64, 2, "black")
tr.begin_fill()
tr.seth(145); tr.circle(-13, 280)#280
tr.seth(140); tr.circle(14, 70)
tr.end_fill()

posicion(-228.41,335.25, 3 ,"black")
tr.begin_fill()
tr.seth(98); tr.fd(7)
tr.seth(50); tr.fd(12)
tr.seth(310); tr.fd(12)
tr.lt(180); tr.fd(12)
tr.seth(92); tr.fd(95)
tr.rt(180); tr.fd(95)
tr.seth(220); tr.fd(13)
tr.seth(135); tr.fd(15)
tr.seth(80); tr.fd(100)
tr.seth(282); tr.fd(103)
tr.seth(220); tr.fd(15)
tr.seth(278); tr.fd(7)
tr.seth(145); tr.circle(13, 50)
tr.end_fill()



#Mano
tr.color("black","#E79D57")
posicion(-194.54,-294.93, 2, "black")
tr.begin_fill()
tr.seth(150); tr.fd(9)
tr.seth(204); tr.fd(18)
tr.seth(204); tr.circle(4, 100)
tr.seth(300); tr.circle(-10, 75)
tr.seth(230); tr.circle(9, 100)
tr.seth(310); tr.circle(-9, 75)
tr.seth(235); tr.circle(5, 90)
tr.seth(320); tr.circle(-8, 70)
tr.seth(258); tr.circle(4, 80)
tr.seth(8); tr.circle(-5, 115)
tr.seth(307); tr.circle(12, 90)
tr.seth(2); tr.circle(40, 40); tr.pensize(3)
tr.seth(25); tr.circle(6, 120)
tr.seth(205); tr.circle(-65, 35)
tr.lt(183); tr.circle(65, 32)
tr.seth(21); tr.circle(9, 120)
tr.seth(206); tr.circle(-50, 50)
tr.lt(182); tr.circle(50, 50)
tr.seth(60); tr.circle(12, 80)
tr.seth(190); tr.circle(-50, 30)
tr.seth(240); tr.circle(-7, 140)
tr.rt(180); tr.circle(7, 140)
tr.seth(344); tr.circle(50, 30)
tr.seth(316); tr.circle(-12, 80)
tr.seth(30); tr.circle(17, 85)#(-158.64,-310.63)
tr.seth(147); tr.circle(80, 25)
tr.goto(-194.54, -294.93)
tr.end_fill()


posicion(-160,-311, 2, "black")
tr.begin_fill()
tr.seth(81); tr.circle(80, 13)
tr.seth(81); tr.circle(10, 140)
tr.seth(273.3); tr.fd(4)
tr.seth(0); tr.circle(-2, 160)
tr.seth(245); tr.circle(40, 22)
tr.seth(260); tr.circle(10, 175)
tr.end_fill()

estampas(-168,-307, 0.6, 0.4 ,130, "square","#E2DADA", "#E5AC86")


tr.up()
tr.done()