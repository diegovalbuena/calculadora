from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def init_window():
    window = Tk()
    window.title("mi primera aplicacion")
    window.geometry('300x250')

    pestaña = ttk.Notebook(window)
    pestaña.pack(fill= 'both', expand= 'yes')

    calculadora = ttk.Frame(pestaña)
    pestaña.add(calculadora, text= 'calculadora')

    historial = ttk.Frame(pestaña)
    pestaña.add(historial, text= 'historial')

    label = Label(calculadora, text= "calculadora", font=('Arial bold', 15))
    label.grid(column = 0, row = 0)

    label_entrada1 = Label(calculadora, text="ingrese primer numero:", font=('Arial bold', 10))
    label_entrada1.grid(column=0, row=1)

    label_entrada2 = Label(calculadora, text="ingrese segundo numero:", font=('Arial bold', 10))
    label_entrada2.grid(column=0, row=2)

    entrada1 = Entry(calculadora, width=10)
    entrada2 = Entry(calculadora, width=10)

    entrada1.focus()
    entrada1.focus()

    entrada2.grid(column = 1, row = 2)
    entrada1.grid(column=1, row=1)

    label_operador = Label(calculadora, text = 'Escoja un operador', font=('Arial bold', 10))
    label_operador.grid(column = 0, row = 3)

    combo_operadores = ttk.Combobox(calculadora)
    combo_operadores ['values'] = ('+', '-', '*','/', '**')
    combo_operadores.current(0)
    combo_operadores.grid(column=1, row=3)

    label_resultado = Label(calculadora, text = 'Resultado', font=('Arial bold', 15))
    label_resultado.grid(column = 0, row = 5,)

    historial_res = Listbox(historial, width= 18, height= 8, font= ('Arial', 15))
    historial_res.grid(column= 1, row= 0)

    limpiar_historial = Button(historial,
                               text= 'borrar historial',
                               bg= 'blue',
                               fg= 'white',
                               command= lambda: limpiar(historial_res))
    limpiar_historial.grid(column= 3, row= 0)

    boton = Button(calculadora,
                    command = lambda: click_calcular(
                          label_resultado,
                          entrada1.get(),
                          entrada2.get(),
                          combo_operadores.get(),
                          historial_res),
                    text='Calcular',
                    bg= "purple",
                    fg= "white")
    boton.grid(column= 1, row= 4)

    window.mainloop()

def limpiar(historial_res):
    valor = messagebox.askokcancel("limpiar", "¿Desea borrar historial?",)
    if valor == True:
        historial_res.delete(0, END)

def historial(res, num1, num2, operador, historial_res):
    ingresos = str(num1) + ' ' + operador + ' ' + str(num2)
    resultado = ' ' + '=' + ' ' + str(res)
    cadena = ingresos + resultado
    historial_res.insert(END, cadena)

def calculadora(num1, num2, operador):
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        resultado = num1 / num2
    else:
        resultado = num1 ** num2
    return resultado

def click_calcular(label, num1, num2, operador, historial_res):
    valor1 = float(num1)
    valor2 = float(num2)
    res = calculadora(valor1, valor2, operador)
    label.configure(text= 'resultado: ' + str(res))
    historial(res, num1, num2, operador, historial_res)

def main():
    init_window()

main()