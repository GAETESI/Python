# declarar una clase y darle el nombre Usuario
class Usuario:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0
        
    def hacer_retiro (self, amount):
        self.balance_cuenta -= amount
        
    def hacer_deposito (self, amount):
        self.balance_cuenta += amount
            
    def balance_usuario(self):
        print(f"User: {self.name}, Balance: {self.balance_cuenta}")

    
    def transfer_dinero(self,other_user, amount):
         if self.balance_cuenta >= amount:
             self.balance_cuenta -= amount
             other_user.balance_cuenta += amount
             print(f"Transferencia exitosa. {self.name} ha transferido {amount} a {other_user.name}")
             print(f"User: {self.name}, Balance: {self.balance_cuenta} - User: {other_user.name}, Balance: {other_user.balance_cuenta}")
         else:
             print("Saldo insuficiente para realizar la transferencia")
             

Oscar = Usuario( "Oscar Lizama", "oscar.lizama@gmail.com" )
Juan = Usuario( "Juan Perez", "juan.perez@gmail.com" )
Lorena = Usuario( "Lorena Gonzales", "l.gonzales@gmail.com" )

Oscar.hacer_deposito(200)
Oscar.hacer_deposito(150)
Oscar.hacer_deposito(400)
Oscar.hacer_retiro(200)
Oscar.balance_usuario()

Juan.hacer_deposito(800)
Juan.hacer_deposito(700)
Juan.hacer_retiro(100)
Juan.hacer_retiro(500)
Juan.balance_usuario()

Lorena.hacer_deposito(1000)
Lorena.hacer_retiro(200)
Lorena.hacer_retiro(50)
Lorena.hacer_retiro(250)
Lorena.balance_usuario()

Oscar.transfer_dinero(Lorena, 100)