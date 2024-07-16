"""
Curso Básico de Python 2024

Caso de estudio: Operadores.

Autor: Kevin Márquez
marquezberriosk@gmail.com
"""

x1 = 10
x2 = 15
myNameIs = 'My name is '
name = 'Juan'
numbers = [1, 2]
numbers2 = [3, 4]

print(x1 + x2) # Suma
print(myNameIs + name) # Concatenación
#print(a + name) # Error, no se pueden sumar/concatenar str con int
print(numbers + numbers2) # Creación de una nueva lista con los elementos de numbers2 añadidos a numbers

x1 *= x2
print(x1)

anotherName = 'Juan'
print('a' == 'b')
print(name is anotherName)
anotherName = 'Carlos'
print(name is anotherName and 2 in numbers)