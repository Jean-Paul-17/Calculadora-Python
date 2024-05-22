import tkinter as tk
from tkinter import *

ventana = tk.Tk()
imagen = tk.PhotoImage(file="img_calculadora.png")
ventana.resizable(0, 0)
ventana.title("Calculadora")
ventana.geometry("476x876")

label_img = tk.Label(ventana, image=imagen)
label_img.pack()

# Caja de números

entrada = tk.Entry(ventana)
entrada.place(x=50, y=50, width=350, height=25)

#Función para tomar valores numéricos
def info_boton(valor):
    anterior = entrada.get()
    entrada.delete(0, END)
    entrada.insert(0, str(anterior) + str(valor))
#Funciones aritméticas
def igual():
      global sum1
      sum2 = float(entrada.get())
      entrada.delete(0, END)
      if operacion == "+":
          entrada.insert(0, sum1 + sum2)
      if operacion == "-":
          entrada.insert(0, sum1 - sum2)
      if operacion == "*":
          entrada.insert(0, sum1 * sum2)
      if operacion == "/":
          entrada.insert(0, sum1 / sum2)   

def suma():
    global sum1
    global operacion
    sum1 = float(entrada.get())
    entrada.delete(0, END)
    operacion = "+"

def resta():
    global sum1
    global operacion
    sum1 = float(entrada.get())
    entrada.delete(0, END)
    operacion = "-"

def multi():
    global sum1
    global operacion
    sum1 = float(entrada.get())
    entrada.delete(0, END)
    operacion = "*"

def division():
    global sum1
    global operacion
    sum1 = float(entrada.get())
    entrada.delete(0, END)
    operacion = "/"

# Botones numéricos

num0 = tk.Button(ventana, text="0", command=lambda: info_boton(0))
num0.place(x=25, y=580, width=60, height=40)

num1 = tk.Button(ventana, text="1", command=lambda: info_boton(1))
num1.place(x=115, y=640, width=60, height=40)

num2 = tk.Button(ventana, text="2", command=lambda: info_boton(2))
num2.place(x=205, y=640, width=60, height=40)

num3 = tk.Button(ventana, text="3", command=lambda: info_boton(3))
num3.place(x=290, y=640, width=60, height=40)

num4 = tk.Button(ventana, text="4", command=lambda: info_boton(4))
num4.place(x=115, y=580, width=60, height=40)

num5 = tk.Button(ventana, text="5", command=lambda: info_boton(5))
num5.place(x=205, y=580, width=60, height=40)

num6 = tk.Button(ventana, text="6", command=lambda: info_boton(6))
num6.place(x=290, y=580, width=60, height=40)

num7 = tk.Button(ventana, text="7", command=lambda: info_boton(7))
num7.place(x=115, y=520, width=60, height=40)

num8 = tk.Button(ventana, text="8", command=lambda: info_boton(8))
num8.place(x=205, y=520, width=60, height=40)

num9 = tk.Button(ventana, text="9", command=lambda: info_boton(9))
num9.place(x=290, y=520, width=60, height=40)

# Botones aritméticos
button_suma = tk.Button(ventana, text="+", command=suma)
button_suma.place(x=380, y=640, width=60, height=40)

button_resta = tk.Button(ventana, text="-", command=resta)
button_resta.place(x=380, y=580, width=60, height=40)

button_multi = tk.Button(ventana, text="*", command=multi)
button_multi.place(x=380, y=520, width=60, height=40)

button_division = tk.Button(ventana, text="/", command=division)
button_division.place(x=380, y=460, width=60, height=40)

button_igual = tk.Button(ventana, text="=", command=igual)
button_igual.place(x=25, y=640, width=60, height=40)

ventana.mainloop()