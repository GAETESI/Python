class CuentaBancaria:
    cuentas_activas = []
    
    def __init__(self, balance, tasa_interes ): 
        self.balance = balance
        self.tasa_interes = tasa_interes
        self.cuentas_activas.append(self)
        
        
    def imprimeBalance (self):
        print("Balance actual:",  self.balance)
       
    
    def hacer_retiro (self, amount):
        self.balance -= amount
        return self
        
    def hacer_deposito (self, amount):
        self.balance += amount
        return self
    
    def generar_interés(self):
        if self.balance > 0:
            interes_generado = self.balance * self.tasa_interes
            self.balance += interes_generado
            return self
            
    @classmethod
    def ImprimirCuentas(cls):
        for cuenta in cls.cuentas_activas:
            print("Balance:", cuenta.balance)
            print("Tasa de Interés:", cuenta.tasa_interes)
            print("-----------")

        
Cuenta1= CuentaBancaria(0, 0.05)
Cuenta2= CuentaBancaria(0, 0.05)

Cuenta1.hacer_deposito(200).hacer_deposito(500).hacer_deposito(400).hacer_retiro(200).generar_interés().imprimeBalance()
Cuenta2.hacer_deposito(800).hacer_deposito(1000).hacer_retiro(200).hacer_retiro(200).hacer_retiro(150).hacer_retiro(100).generar_interés().imprimeBalance()



CuentaBancaria.ImprimirCuentas()
