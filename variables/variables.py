"""
Curso Básico de Python 2024

Caso de estudio: Variables y tipos de datos.

Autor: Kevin Márquez
marquezberriosk@gmail.com
"""

number = 1 # tipo int
withoutVal = None # sin tipo/valor asociado
text = "Some text" # tipo str
customList = [1, 3, 4, 'dog', ['1', '2', True], None, {'key': 'value'}] # tipo list
myTuple = ("hello", 1 , customList) # tipo tuple
myDict = {"name": "Juan", "age": 18} # tipo dictionary

print(type(number))
print(type(withoutVal))
print(type(text))
print(customList)
print(myTuple)
print(myDict)

print(isinstance(number, int))
print(isinstance(number, str))