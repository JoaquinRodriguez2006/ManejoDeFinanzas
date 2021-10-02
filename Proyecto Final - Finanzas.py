print("Bienvenido al sistema de finanzas")
print("...............................................................")
salario = str(input("Ingrese su salario: $"))
class finanzas():
    def __init__(self,salario):
        self.salario = salario
    
    def add_salary(self,s):
        self.s = salario
        print("Su salario ingresado es de: $",s)
    
    def add_expenses_and_addup(self):
        list_of_expenses = []
        op = int(input())
        while op != 2:
            if op != 2:
                ex = int(input("Ingrese un gasto: $"))
            op = int(input())
            list_of_expenses.append(ex)
            print(list_of_expenses)
        op = int(input())
        if op==2:
            self.list_of_expenses = list_of_expenses
            addup = sum(list_of_expenses)
            print(addup)
        if int(addup) >= int(salario):
            rest = int(addup)-int(salario)
            print("ATENCION! Tus gastos acaban de superar tu sueldo por $",rest)
        
f = finanzas(salario)
f.add_salary(salario)
f.add_expenses_and_addup()