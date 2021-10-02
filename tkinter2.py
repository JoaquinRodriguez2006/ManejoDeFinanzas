from tkinter import *
def add_expenses():
        list_of_expenses = []
        op = int(input())
        while op != 2:
            if op != 2:
                ex = int(input("Ingrese un gasto: $"))
            op = int(input())
            list_of_expenses.append(ex)
            print(list_of_expenses)
        op = int(input())
        
rama = Tk()

Label(rama, text="Ingrese su sueldo: $").grid(pady=5, row=0, column=0)

Label(rama, text="Ingrese sus gastos: $").grid(pady=5, row=1, column=0)

Entry(rama, width=40).grid(padx=5, row=0, column=1)
Entry(rama, width=40).grid(padx=5, row=1, column=1)

rama.mainloop()

