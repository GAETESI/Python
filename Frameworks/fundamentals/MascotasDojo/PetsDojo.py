       
class Mascota:
    total_obesos = []
    def __init__(self, name, tipo, golosinas, salud, energia):
        self.name= name
        self.tipo= tipo
        self.golosinas= golosinas
        self.salud= salud
        self.energia= energia
        self.total_obesos.append(self)
        
    def dormir(self):
        self.energia += 25
        return self
        
    def comer(self):
        self.energia +=5
        self.salud += 10
        return self
        
    def jugar(self):
        self.salud += 5
        self.energia -=10
        print(f"Salud:{self.salud} - Salud:{self.energia}")
        return self
        
    def ruido(self):
        self.salud += 10
        return self
            
class Gato( Mascota ):
    def __init__(self, name, tipo, golosinas, salud, energia, sonido):
        super().__init__(name, tipo, golosinas, salud, energia)
        self.sonido = sonido
            
Michi = Gato ("Michi", "Felino", "Churu", 10, 15, "Miauh")

Michi.jugar()

