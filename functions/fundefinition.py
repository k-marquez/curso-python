"""
Curso Básico de Python 

Case study: Function definition syntax.

Author: Kevin Márquez
marquezberriosk@gmail.com
"""

# Definition
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y
    print(x - y) # Never prints

# Function call
sum = add(10, 5)
sub = subtract(10 - 5, 5)

print(sum)
print(sub)

# printMessage('Hello world!') # Error, functions must be defined before calling it

def printMessage(message):
    print(message)

printMessage('Hello world!')