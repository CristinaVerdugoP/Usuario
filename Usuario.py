class Usuario:

    Nombre_banco = "Banco Pitius"

    def __init__(self, nombre, balance):
        self.nombre = nombre
        self.balance = balance

    def hacer_deposito(self, deposito):
        self.balance += deposito

    def hacer_retiro(self, retiro):
        self.balance -= retiro
        return self

    def mostrar_balance(self):
        print("Balance actual para", self.nombre,"sera:", self.balance)
        return self

    def transferencia(self, nombre, monto):
        print("Antes de la transferencia el balance es:",self.balance)
        self.hacer_retiro(monto)
        nombre.hacer_deposito(monto)
        print("Despues de la transferencia el balance es:",self.balance)
    
#Creacion de los 3 objetos
Usuario1 = Usuario("Rodolfo",300)
Usuario2 = Usuario("Felipe", 700)
Usuario3 = Usuario("Gerardo", 500)

#Para el objeto Usuario 1:
print("\nPara usuario1")
Usuario1.hacer_deposito(200)
Usuario1.hacer_deposito(100)
Usuario1.hacer_retiro(50)
Usuario1.transferencia(Usuario3,100)
Usuario1.mostrar_balance()

#Para el objeto Usuario 1:
print("\nPara usuario2")
Usuario2.hacer_deposito(300)
Usuario2.hacer_deposito(200)
Usuario2.hacer_retiro(10)
Usuario2.hacer_retiro(400)
Usuario2.mostrar_balance()

#Para el objeto Usuario 1:
print("\nPara usuario3")
Usuario3.hacer_deposito(500)
Usuario3.hacer_retiro(50)
Usuario3.hacer_retiro(110)
Usuario3.hacer_retiro(30)
Usuario3.mostrar_balance()

