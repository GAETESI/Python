#Actualizar valores en diccionarios y listas
x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1.1
x[1][0] = 15
print(x)

#1.2
estudiantes[0]["last_name"]= "Bryant"
print(estudiantes)

#1.3
directorio_deportes["fútbol"][0] = "Andrés"
print(directorio_deportes)

#1.4
z[0]['y'] = '30'
print(z)

#2
estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(estudiantes):
    for i in range(len(estudiantes)):
        for key, value in estudiantes[i] .items():
            print(f"{key} - {value}")
            print("")
            
iterateDictionary(estudiantes)
      
#3
estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictionary2(key_name, lista_estudiantes):
    for estudiante in (lista_estudiantes):
        if key_name in estudiante.keys():
            print(estudiante[key_name])
        else: 
         print("valor no existe")
            
iterateDictionary2('first_name', estudiantes)

#4
dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dicts):
    for key, values in some_dicts.items():
        print(f"{key}: {len(values)}")
        for valor in values:
            print (valor)
        
printInfo(dojo)

