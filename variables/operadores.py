"""
Curso Básico de Python 2024

Caso de estudio: Operadores.

Autor: Kevin Márquez
marquezberriosk@gmail.com
"""

a = 10
b = 15
myNameIs = 'Mi nombre es '
name = 'Juan'
numbers = [1, 2]
numbers2 = [3, 4]

print(a + b) # Suma
print(myNameIs + name) # Concatenación
#print(a + name) # Error, no se pueden sumar/concatenar str con int
print(numbers + numbers2) # Creación de una nueva lista con los elementos de numbers2 añadidos a numbers

a *= b
print(a)

print('a' == 'b')
print(name is 'Juan')
print(name is 'Juan' and 2 in numbers)