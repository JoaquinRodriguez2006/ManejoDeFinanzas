print("Bienvenido al sistema de finanzas")
print("...............................................................")
salario = str(input("Ingrese su salario: $"))
class finanzas():
    def __init__(self,salario):
        self.salario = salario
    
    def add_salary(self,s):
        self.s = salario
        print("Su salario ingresado es de: $",s)
    
    def add_expenses(self,list_of_expenses):
        self.list_of_expenses = list_of_expenses
        list_of_expenses = []
        op = int(input())
        while op != 2:
            if op != 2:
                ex = int(input("Ingrese un gasto: $"))
            op = int(input())
            list_of_expenses.append(ex)
            print(list_of_expenses)
        op = int(input())

    def addup_expenses(self,list_of_expenses):
        self.list_of_expenses = list_of_expenses
        addup = sum(list_of_expenses)
    
    def alert(self,addup,salario):
        if addup >= salario:
            rest = addup-salario
            print("ATENCION! Tus gastos acaban de superar tu sueldo por $",rest)
    
    def errores(self):
        print("falta agregar")
        
f = finanzas(salario)
f.add_salary(salario)
f.add_expenses()
f.addup_expenses()
f.alert()