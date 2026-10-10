import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import turtle
import threading


a1, a2 = 830, 820
screen = turtle.Screen()
screen.setup(a1, a2)
screen.title("Vista previa")

pen = turtle.Turtle()
pen.speed(0)
screen.tracer(0)

def render(event=None):
    codigo = editor.get("1.0", tk.END)

    pen.clear()
    pen.penup()
    pen.home()
    pen.pendown()

    entorno = {
        "t": pen,
        "tr": pen,
        "turtle": pen,
    }

    try:
        exec(codigo, entorno)
    except Exception:
        pass

    screen.update()

def programar_actualizacion(event=None):
    global temporizador
    if temporizador:
        root.after_cancel(temporizador)
    temporizador = root.after(300, render)

# Ventana del editor
root = tk.Tk()
root.title("Editor Turtle Live")

editor = ScrolledText(root, width=70, height=35, font=("Consolas", 11))
editor.pack(fill="both", expand=True)

editor.insert("1.0", """# Usa la variable t para dibujar

def posicion(x,y, p, c=str("black")):
    tr.penup()
    tr.goto(x,y)
    tr.pendown()
    tr.pensize(p)
    tr.pencolor(c)
    
def cuadricula(ep=20, ct=40, lg=600, gs=2, cl="black"):
    tr.pencolor(cl)
    tr.pensize(gs)
    tr.penup()
    tr.goto(0, 0)
    tr.dot(10, "black")
    for i in range(-ct, ct + 1):
        x = i * ep
        tr.penup()
        tr.goto(x, -lg)
        tr.pendown()
        tr.goto(x, lg)
    for i in range(-ct, ct + 1):
        y = i * ep
        tr.penup()
        tr.goto(-lg, y)
        tr.pendown()
        tr.goto(lg, y)
        
def penseth(s, p):
    tr.seth(s)
    tr.pensize(p)
    
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

tr.pen(shown=False)

""")

temporizador = None
editor.bind("<KeyRelease>", programar_actualizacion)

render()

threading.Thread(target=turtle.mainloop, daemon=True).start()
root.mainloop()
