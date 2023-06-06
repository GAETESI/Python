# 1. TAREA: imprime "Hola, mundo"
print("Hola, mundo")
# 2a 
name = "Silvana"
print("Hola,", name)	# con una coma
# 2b 
print("Hola, "+ name)	# con un +
# 3a. 
num = 24
print("Hola,", (num))	
# 3B
#print("Hola, "+ (num))#Da error, se corrige en la linea 13
print("Hola, "+ str(num))
fave_food1 = "sushi"
fave_food2 = "pizza"
#4a
print("Amo comer {} y {}".format(fave_food1,fave_food2)) # con .format()
#4b
print(f"Amo comer {fave_food1} y {fave_food2}") # con una cadena f