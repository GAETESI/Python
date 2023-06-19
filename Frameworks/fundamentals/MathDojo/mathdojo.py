class MathDojo:
    
    def __init__(self):
        self.resultado = 0

    def add(self, *args):
        for num in args:
            self.resultado += num
        return self

    def subtract(self, *args):
        for num in args:
            self.resultado -= num
        return self
    
md = MathDojo()
# para probar:
x = md.add(2).add(2,5,1).subtract(3,2).resultado
print(x)

i = md.add(4).add(4,5,1).subtract(3,2).resultado
print(i)

p = md.add(7).add(7,5,1).subtract(3,2).resultado
print(p)# debería imprimir 5
# ejecuta cada uno de los métodos unas cuantas veces más y verifica el resultado

z = md.subtract(2).subtract(2,5,1).add(3,2).resultado
print(z)

