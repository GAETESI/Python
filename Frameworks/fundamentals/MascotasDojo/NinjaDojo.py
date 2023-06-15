from PetsDojo import Mascota

class Ninja:
    def __init__(self, nombre, apellido, premio, mascota, comida_mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.premio = premio
        self.mascota = mascota
        self.comida_mascota = comida_mascota
        
    def caminar(self):
        print(f"{self.mascota.name}")
        self.mascota.jugar()
        return self
        
    def alimentar(self):
       print (f"Alimentando {self.mascota.name} - {self.comida_mascota}!")
       self.mascota.comer()
       return self
        
    def bañar(self):
        print(f"{self.mascota.name} esta limpio y feliz!")
        self.mascota.ruido()
        return self
    
Sishui = Mascota("Sishui", "Hamster", "Drops", 10, 10)
Zawardito = Mascota("Zawardito", "Chinchilla", "Gusanos", 15, 10)

Itachi = Ninja("Itachi", "De la Luz", "Drops", Sishui, "Fruta")

Itachi.alimentar().bañar().caminar()