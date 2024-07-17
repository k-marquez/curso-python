"""
Curso Básico de Python 2024

Case study: Operators.

Author: Kevin Márquez
marquezberriosk@gmail.com
"""

x1 = 10
x2 = 15
myNameIs = 'My name is '
name = 'Juan'
numbers = [1, 2]
numbers2 = [3, 4]

print(x1 + x2) # Suma
print(myNameIs + name) # concatenation
#print(x1 + name) # Error, cannot add/concatenate str with ints
print(numbers + numbers2) # New list with elements of numbers2 joined to numbers

x1 *= x2
print(x1)

anotherName = 'Juan'
print('a' == 'b')
print(name is anotherName)
anotherName = 'Carlos'
print(name is anotherName and 2 in numbers)