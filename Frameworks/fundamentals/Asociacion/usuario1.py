from CuentaBancaria1 import CuentaBancaria

class Usuario:
    def __init__(self, name):
        self.name = name
        self.cuenta = [CuentaBancaria(balance=0, tasa_interes= 0.02)]
        
    def AgregarCuenta (self, balance, tasa_interes):    
        self.cuenta.append(CuentaBancaria(balance=balance, tasa_interes=tasa_interes))
        
    def hacer_retiro (self, amount, numeroDeCuenta):
        self.cuenta[numeroDeCuenta].balance -= amount
        return self
        
    def hacer_deposito (self, amount, numeroDeCuenta):
        self.cuenta[numeroDeCuenta].balance += amount
        return self
            
    def balance_usuario(self, numeroDeCuenta):
        print(f"User: {self.name}, Balance: {self.cuenta[numeroDeCuenta].balance}")
        return self

    
    def transfer_dinero(self,other_user, amount, numeroDeCuenta):
         if self.cuenta[numeroDeCuenta].balance >= amount:
             self.cuenta[numeroDeCuenta].balance -= amount
             other_user.cuenta[numeroDeCuenta].balance += amount
             print(f"Transferencia exitosa. {self.name} ha transferido {amount} a {other_user.name}")
             print(f"User: {self.name}, Balance: {self.cuenta[numeroDeCuenta].balance} - User: {other_user.name}, Balance: {other_user.cuenta[numeroDeCuenta].balance}")
         else:
             print("Saldo insuficiente para realizar la transferencia")
         return self 

Oscar = Usuario( "Oscar Lizama")
#Juan = Usuario( "Juan Perez")
#Lorena = Usuario( "Lorena Gonzales")

Oscar.AgregarCuenta(2000, 0.02)
Oscar.AgregarCuenta(3000, 0.05)
Oscar.AgregarCuenta(1000, 0.06)

Oscar.hacer_deposito(200, 2).hacer_deposito(150, 2).hacer_deposito(400, 2).hacer_retiro(200, 2).balance_usuario(2)
Oscar.hacer_deposito(1200, 0).hacer_deposito(100, 0).hacer_deposito(400, 0).hacer_retiro(800, 0).balance_usuario(0)
"""Juan.hacer_deposito(800).hacer_deposito(700).hacer_retiro(100).hacer_retiro(500).balance_usuario()
Lorena.hacer_deposito(1000).hacer_retiro(200).hacer_retiro(50).hacer_retiro(250).balance_usuario()
Oscar.transfer_dinero(Lorena, 100)"""