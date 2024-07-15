a = 10
b = 15
myName = 'Mi nombre es '
name = 'Juan'
myList = [1, 2]
myList2 = [3, 4]

print(a + b) # Suma
print(myName + name) # Concatenación
#print(a + name) # Error, no se pueden sumar/concatenar str con int
print(myList + myList2) # Creación de una nueva lista con los elementos de myList2 añadidos a myList

a *= b
print(a)

print('a' == 'b')
print(name is 'Juan')
print(name is 'Juan' and 2 in myList)