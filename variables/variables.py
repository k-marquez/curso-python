"""
Curso Básico de Python 2024

Case study: Variables and data types.

Author: Kevin Márquez
marquezberriosk@gmail.com
"""

number = 1 # type int
withoutVal = None # without type/value
text = "Some text" # type str
customList = [1, 3, 4, 'dog', ['1', '2', True], None, {'key': 'value'}] # type list
myTuple = ("hello", 1 , customList) # type tuple
myDict = {"name": "Juan", "age": 18} # type dictionary

print(type(number))
print(type(withoutVal))
print(type(text))
print(customList)
print(myTuple)
print(myDict)

print(isinstance(number, int))
print(isinstance(number, str))