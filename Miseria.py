import turtle as tr

#Circulo Base
tr.speed(0)
tr.bgcolor("#64cede")
tr.penup()
tr.goto(0,-250)
tr.pendown()
tr.pensize(10)
tr.color("#000005","#30EC37")#000005 #30EC37
tr.begin_fill()
for i in range(1):
    tr.circle(-3400,None,25) 
tr.end_fill()

#Flores pasto
tr.pen(fillcolor="#BCCE18")
tr.shape("turtle")
tr.pensize(1)
tr.penup()
tr.goto(-500, -335)
tr.pendown()
tr.setheading(7)
for i in range(10):
    tr.penup()
    tr.forward(50)
    tr.pendown()
    for _ in range(4):
        tr.left(90)
        tr.stamp()
        
tr.penup()
tr.goto(-0, -275)
tr.pendown()
tr.setheading(353)
for i in range(10):
    tr.penup()
    tr.forward(50)
    tr.pendown()
    for _ in range(4):
        tr.left(90)
        tr.stamp()

tr.pen(fillcolor="#07271f")
tr.shape("classic")
tr.penup()
tr.goto(-525, - 358)
tr.pendown()
tr.tilt(270)
tr.resizemode("user")
tr.shapesize(stretch_len=1, stretch_wid=2)
tr.setheading(7)
for i in range(11):
    tr.stamp()
    tr.penup()
    tr.forward(50)
    tr.pendown()
    
tr.penup()
tr.goto(20, -298)
tr.pendown()
tr.setheading(353)
for i in range(11):
    tr.stamp()
    tr.penup()
    tr.forward(50)
    tr.pendown()

tr.pen(fillcolor="#4a4069")
tr.shape("square") 
tr.resizemode("auto")
tr.penup()
tr.goto(-500, -370)
tr.pendown()
tr.setheading(7)
for i in range(10):
    tr.penup()
    tr.forward(50)
    tr.pendown()
    for _ in range(3):
        tr.left(120)
        tr.stamp()

tr.penup()
tr.goto(0, -310)
tr.pendown()
tr.setheading(353)
for i in range(10):
    tr.penup()
    tr.forward(50)
    tr.pendown()
    for _ in range(3):
        tr.left(120)
        tr.stamp()

tr.pen(fillcolor="#173312")
tr.shape("classic")
tr.penup()
tr.goto(-525, - 400)
tr.pendown()
tr.resizemode("user")
tr.shapesize(stretch_len=3, stretch_wid=1)
tr.setheading(7)
for i in range(11):
    tr.stamp()
    tr.penup()
    tr.forward(50)
    tr.pendown()

tr.penup()
tr.goto(20, - 338)
tr.pendown()
tr.setheading(353)
for i in range(11):
    tr.stamp()
    tr.penup()
    tr.forward(50)
    tr.pendown()

tr.pen(fillcolor="#a0724c")
tr.shape("turtle")
tr.resizemode("auto")
tr.pensize(1)
tr.penup()
tr.goto(-500, -405)
tr.pendown()
tr.setheading(7)
for i in range(10):
    tr.penup()
    tr.forward(50)
    tr.pendown()
    for _ in range(4):
        tr.left(90)
        tr.stamp()
    
tr.penup()
tr.goto(-0, -345)
tr.pendown()
tr.setheading(353)
for i in range(10):
    tr.penup()
    tr.forward(50)
    tr.pendown()
    for _ in range(4):
        tr.left(90)
        tr.stamp()

tr.pen(fillcolor = "#131B03")
tr.shape("classic")
tr.penup()
tr.goto(-525, - 430)
tr.pendown()
tr.tilt(00)
tr.resizemode("user")
tr.shapesize(stretch_len=1, stretch_wid=2)
tr.setheading(7)
for i in range(11):
    tr.stamp()
    tr.penup()
    tr.forward(50)
    tr.pendown()
    
tr.penup()
tr.goto(20, -370)
tr.pendown()
tr.setheading(353)
for i in range(11):
    tr.stamp()
    tr.penup()
    tr.forward(50)
    tr.pendown()

tr.pen(fillcolor = "#ca545e")
tr.shape("square") 
tr.resizemode("auto")
tr.penup()
tr.goto(-500, -440)
tr.pendown()
tr.setheading(7)
for i in range(10):
    tr.penup()
    tr.forward(50)
    tr.pendown
    for _ in range(3):
        tr.left(120)
        tr.stamp()

tr.penup()
tr.goto(0, -380)
tr.pendown()
tr.setheading(353)
for i in range(10):
    tr.penup()
    tr.forward(50)
    tr.pendown()
    for _ in range(3):
        tr.left(120)
        tr.stamp()
    
#Circulos pasto   
tr.pen(fillcolor="#4D179A") 
tr.pensize(1)
tr.shape("circle")
tr.shapesize(1)
tr.pen(resizemode="user")
tr.penup()
tr.goto(-480, -310)
tr.pendown()
tr.setheading(7)
for i in range(12):
    tr.forward(20)
    tr.left(90)
    tr.forward(18)
    tr.left(180)
    tr.stamp()
    tr.forward(18)
    tr.left(90)
    tr.forward(20)
    
tr.penup()
tr.goto(0, -250)
tr.pendown()
tr.setheading(353)
for i in range(12):
    tr.forward(20)
    tr.left(90)
    tr.forward(18)
    tr.left(180)
    tr.stamp()
    tr.forward(18)
    tr.left(90)
    tr.forward(20)
    
tr.pen(fillcolor="#59168B")
tr.shapesize(1)
tr.pen(resizemode="user")
tr.penup()
tr.goto(-500, -310)
tr.pendown()
tr.setheading(7)
for i in range(12):
    tr.forward(20)
    tr.left(90)
    tr.forward(32)
    tr.left(180)
    tr.stamp()
    tr.forward(32)
    tr.left(90)
    tr.forward(20)

tr.shapesize(1)
tr.pen(resizemode="user")
tr.penup()
tr.goto(20, -250)
tr.pendown()
tr.setheading(352.5)
for i in range(12):
    tr.forward(20)
    tr.left(90)
    tr.forward(32)
    tr.left(180)
    tr.stamp()
    tr.forward(32)
    tr.left(90)
    tr.forward(20)
    

#Flores conectadas

tr.pen(fillcolor="#636363")
tr.shape("classic")
tr.tilt(90)
tr.pen(resizemode="noresize")
tr.pensize(1)
tr.penup()
tr.goto(-400, -300)
tr.pendown()
for i in range(10):
    tr.stamp()
    tr.setheading(90)
    tr.fd(15)
tr.pensize(1.5)
tr.color("#31C950","#FF10F0")
for i in range(20):
    tr.goto(-400, -150)
    tr.begin_fill()
    tr.fd(50)
    tr.lt(20)
    tr.fd(25)
    tr.end_fill()

tr.pen(fillcolor="#636363")
tr.pensize(1)
tr.penup()
tr.goto(-275,-280)
tr.pendown()
for i in range(15):
    tr.stamp()
    tr.setheading(90)
    tr.fd(15)
tr.pensize(1.5)
tr.color("#C71D36","#39FF14")
for i in range(20):
    tr.goto(-275, -60)
    tr.begin_fill()
    tr.fd(50)
    tr.lt(20)
    tr.fd(25)
    tr.end_fill()
    
tr.pen(fillcolor="#636363")
tr.pensize(1)
tr.penup()
tr.goto(-140,-265)
tr.pendown()
for i in range(10):
    tr.stamp()
    tr.setheading(90)
    tr.fd(15)
tr.color("#8207DB", "#FFF01F")
tr.pensize(1.5)
for i in range(20):
    tr.goto(-140, -115)
    tr.begin_fill()
    tr.fd(50)
    tr.lt(20)
    tr.fd(25)
    tr.end_fill()
    
tr.pen(fillcolor="#636363")
tr.pensize(1)
tr.penup()
tr.goto(140,-265)
tr.pendown()
for i in range(10):
    tr.stamp()
    tr.setheading(90)
    tr.fd(15)
tr.pensize(1.5)
tr.color("#BB4D1A", "#0FF0FC")
for i in range(20):
    tr.goto(140, -115)
    tr.begin_fill()
    tr.fd(50)
    tr.lt(20)
    tr.fd(25)
    tr.end_fill()

tr.pen(fillcolor="#636363")
tr.pensize(1)
tr.penup()
tr.goto(275,-280)
tr.pendown()
for i in range(15):
    tr.stamp()
    tr.setheading(90)
    tr.fd(15)
tr.pensize(1.5)
tr.color("#1447E6","#FF5E00")
for i in range(20):
    tr.goto(275, -55)
    tr.begin_fill()
    tr.fd(50)
    tr.lt(20)
    tr.fd(25)
    tr.end_fill()

tr.pen(fillcolor="#636363")
tr.pensize(1)
tr.penup()
tr.goto(400, -300)
tr.pendown()
for i in range(10):
    tr.stamp()
    tr.setheading(90)
    tr.fd(15)
tr.pensize(1.5)
tr.color("#FFDF20","#BC13FE")
for i in range(20):
    tr.goto(400, -150)
    tr.begin_fill()
    tr.fd(50)
    tr.lt(20)
    tr.fd(25)
    tr.end_fill()

#Flores esparcidas
tr.pensize(1)
tr.penup()
tr.goto(-150, 45)
tr.pendown()
petalos = 30
giro = 360 / petalos
angulo = 60
tr.color("#ffc30b","#800080")
for i in range(petalos):
    tr.begin_fill()
    tr.circle(75, angulo)
    tr.left(180 - angulo)
    tr.circle(75,angulo)
    tr.end_fill()
    tr.left(180 - angulo + giro)
    tr.dot(15,"#F0F8FF")

tr.penup()
tr.goto(150, 45)
tr.pendown()
for i in range(petalos):
    tr.begin_fill()
    tr.circle(75, angulo)
    tr.left(180 - angulo)
    tr.circle(75,angulo)
    tr.end_fill()
    tr.left(180 - angulo + giro)
    tr.dot(15,"#F0F8FF")


tr.penup()
tr.goto(-410, 150)
tr.pendown()
tr.color("#808080","#FFFFFF")
for i in range(petalos):
    tr.begin_fill()
    tr.circle(75, angulo)
    tr.left(180 - angulo)
    tr.circle(75,angulo)
    tr.end_fill()
    tr.left(180 - angulo + giro)
    tr.dot(15,"#FFC0CB")
    
tr.penup()
tr.goto(410, 150)
tr.pendown()
for i in range(petalos):
    tr.begin_fill()
    tr.circle(75, angulo)
    tr.left(180 - angulo)
    tr.circle(75,angulo)
    tr.end_fill()
    tr.left(180 - angulo + giro)
    tr.dot(15,"#ffc0cb")

petalos = 35
tr.penup()
tr.goto(275, 287)
tr.pendown()
tr.color("#FFFFFF","#40E0D0")
for i in range(petalos):
    tr.begin_fill()
    tr.circle(60, angulo)
    tr.left(180 - angulo)
    tr.circle(55,angulo)
    tr.end_fill()
    tr.left(180 - angulo + giro)
    tr.dot(10,"#FFC0CB")

tr.penup()
tr.goto(-275, 295)
tr.pendown()
for i in range(petalos):
    tr.begin_fill()
    tr.circle(60, angulo)
    tr.left(180 - angulo)
    tr.circle(55,angulo)
    tr.end_fill()
    tr.left(180 - angulo + giro)
    tr.dot(10,"#FFC0CB")


pentalos = 25
tr.penup()
tr.goto(-425,0)
tr.pendown()
tr.pen(shown=False)
tr.color("#b87333","#fdd0a9")
for i in range(petalos):
    tr.begin_fill()
    tr.circle(petalos, angulo)
    tr.left(180 - angulo)
    tr.circle(petalos,angulo)
    tr.left(180 - angulo + giro)
    tr.end_fill()
    tr.dot(10,"#FAF0E6")

tr.penup()
tr.goto(425,0)
tr.pendown()
tr.pen(shown=False)
for i in range(petalos):
    tr.begin_fill()
    tr.circle(petalos, angulo)
    tr.left(180 - angulo)
    tr.circle(petalos,angulo)
    tr.end_fill()
    tr.left(180 - angulo + giro)
    tr.dot(10,"#FAF0E6")

petalos = 8
giro = 360 / petalos
angulo = 60
tr.penup()
tr.goto(300,70)
tr.pendown()
tr.pen(shown=False)
tr.color("#c19a6b","#000000")
for i in range(petalos):
    tr.begin_fill()
    tr.circle(30, angulo)
    tr.left(180 - angulo)
    tr.circle(30,angulo)
    tr.end_fill()
    tr.left(180 - angulo + giro)
    tr.dot(10,"#ffecb3")

tr.penup()
tr.goto(-300,70)
tr.pendown()
tr.pen(shown=False)
for i in range(petalos):
    tr.begin_fill()
    tr.circle(30, angulo)
    tr.left(180 - angulo)
    tr.circle(30,angulo)
    tr.end_fill()
    tr.left(180 - angulo + giro)
    tr.dot(10,"#ffecb3")

petalos = 16

tr.penup()
tr.goto(-400, 325)
tr.pendown()
petalos = 16
giro = 360 / petalos
angulo = 60
tr.color("#99004C","#FF8C00")
for i in range(petalos):
    tr.begin_fill()
    tr.circle(30, angulo)
    tr.left(180 - angulo)
    tr.circle(30,angulo)
    tr.end_fill()
    tr.left(180 - giro + angulo)
    tr.dot(12, "#FFFFFF")

tr.penup()
tr.goto(400, 325)
tr.pendown()
petalos = 16
giro = 360 / petalos
angulo = 60
for i in range(petalos):
    tr.begin_fill()
    tr.circle(30, angulo)
    tr.left(180 - angulo)
    tr.circle(30,angulo)
    tr.end_fill()
    tr.left(180 - giro + angulo)
    tr.dot(12,"#FFFFFF")

petalos = 24
largo = 40
angulo_pico = 20 
tr.penup()
tr.goto(-235,160)
tr.pendown()
tr.color("#000000","#c0c0c0")
for i in range(petalos):
    tr.begin_fill()
    tr.forward(largo)
    tr.left(180 - angulo_pico)
    tr.forward(largo)
    tr.left(angulo_pico)
    tr.left(360 / petalos)
    tr.end_fill()
tr.penup()
tr.goto(-230,156)
tr.pendown()
tr.dot(15,"#faf9f7")
    
tr.penup()
tr.goto(235, 160)
tr.pendown()
for i in range(petalos):
    tr.begin_fill()
    tr.forward(largo)
    tr.left(180 - angulo_pico)
    tr.forward(largo)
    tr.left(angulo_pico)
    tr.left(360 / petalos)
    tr.end_fill()
tr.penup()
tr.goto(242,156)
tr.pendown()
tr.dot(15,"#faf9f7")


#Tallo Flor y medio circulo del espiral
tr.color("#1D293D","#022F2E")
tr.pensize(2)
tr.penup()
tr.goto(0,-250)
tr.pendown()
for i in range(4):
    tr.setheading(52.5)
    tr.circle(50,55)
    for i in range(1):
         tr.begin_fill()
         tr.circle(75, 60)
         tr.left(120)
         tr.circle(75,60)
         tr.end_fill()
    tr.setheading(108)
    tr.left(380)
    tr.circle(-50,55)
    for i in range(1):
         tr.begin_fill()
         tr.setheading(0.5)
         tr.circle(75, 60)
         tr.left(120)
         tr.circle(75,60)
         tr.end_fill()
    tr.setheading(90)
tr.setheading(0)

    
tr.speed(0)
tr.penup()
tr.home
tr.sety(115)
tr.pendown()
rad = 145

tr.pen(fillcolor="#ff0634")
tr.speed(4)
tr.penup()
tr.goto(0, -200)
tr.goto(0, 115)
tr.pendown()
tr.circle(rad , 90, 3)
tr.penup()
tr.goto(0, 115)
tr.pendown()
tr.left(270)
tr.circle(rad, -90, 3)

#Espiral infinito
tr.shape("classic")
radio = 1
vueltas = 65
tr.pensize(1)
tr.speed(99)
tr.color("#EDF100","#ffffff")
try:
    while True:
       tr.penup()
       tr.goto(0,250)
       tr.pendown()
       tr.dot(10,"black")
       
       tr.begin_fill()
       for i in range(vueltas):
           tr.circle(radio, 55)
           tr.stamp()
           radio = radio + 2
       radio = 0
    
       for i in range(vueltas * 2):
            tr.undo()
    
       for i in range(vueltas):
            tr.circle(-radio, 55)
            tr.stamp()
            radio = radio + 2
       radio = 0
       
       for i in range(vueltas * 2):
            tr.undo()
       tr.end_fill()
except Exception:
    print("Programa interrumpido")
    