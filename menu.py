import tkinter as tk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Simple")

# Variable para mostrar la operación
operacion = ""

# Función para actualizar la pantalla
def presionar(valor):
    global operacion
    operacion += str(valor)
    entrada.set(operacion)

# Función para calcular el resultado
def calcular():
    global operacion
    try:
        resultado = str(eval(operacion))
        entrada.set(resultado)
        operacion = resultado  # permite continuar operando
    except:
        entrada.set("Error")
        operacion = ""

# Función para limpiar la pantalla
def limpiar():
    global operacion
    operacion = ""
    entrada.set("")

# Pantalla donde se muestra la operación
entrada = tk.StringVar()
pantalla = tk.Entry(ventana, textvariable=entrada, font=("Arial", 18), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
pantalla.grid(row=0, column=0, columnspan=4)

# Botones
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('/', 4, 3),
    ('Borrar', 5, 0)
]

for (texto, fila, columna) in botones:
    if texto == "=":
        b = tk.Button(ventana, text=texto, padx=20, pady=20, font=("Arial", 12), command=calcular)
    elif texto == "Borrar":
        b = tk.Button(ventana, text=texto, padx=100, pady=20, font=("Arial", 12), command=limpiar)
        b.grid(row=fila, column=columna, columnspan=4)
        continue
    else:
        b = tk.Button(ventana, text=texto, padx=20, pady=20, font=("Arial", 12), command=lambda t=texto: presionar(t))
    b.grid(row=fila, column=columna)

ventana.mainloop()
