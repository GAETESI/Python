#1
def backcount (count):
    lista = list(range(count, -1, -1))
    return lista

count = 5
resultado = backcount(count)
print(resultado)


#2
def imprimir_y_devolver(lista):
    primerValor = lista [0]
    print (primerValor)
    segundoValor = lista [1]
    return segundoValor

numeros = [1,2]
valor_devuelto = imprimir_y_devolver(numeros)
print("Valor devuelto:", valor_devuelto)
    

#3
def primero_mas_longitud(lista):
    primer_Valor = lista[0]
    longitud = len(lista)
    suma = primer_Valor + longitud
    return suma
    
numeros = [1,2,3,4,5]
resultado = primero_mas_longitud(numeros)
print(resultado)

#4
def valores_mayores_que_el_segundo(newList):       
    for x in (numeros):
       if x > numeros[1]: 
           newList.append(x)     
    if len(newList) < 2:
        return False
    return newList

newList= []
numeros = [5,2,3,2,1,4]
resultado = valores_mayores_que_el_segundo(newList)
print(len(newList), resultado)

newList= []
numeros = [1,1,4,1]
resultado = valores_mayores_que_el_segundo(newList)
print(len(newList), resultado)


#5
def length_and_value(longitud, valor):
    return [valor] * longitud
    
resultado1 = length_and_value(4,7)
print (resultado1)
resultado2 = length_and_value(6,2)
print (resultado2)