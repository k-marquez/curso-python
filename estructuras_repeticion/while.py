"""
Curso Básico de Python 2024

Caso de estudio: Demostración de la sintaxis del while.

Autor: Kevin Márquez
marquezberriosk@gmail.com
"""

myVar = 0

while myVar < 10:
    print(myVar)
    myVar += 2

"""
Los paréntesis son propios del anidamiento de la operación más que parte de la
sintaxis del while
"""
while (myVar > 0):
    print(myVar)
    myVar -= 2
    break # Salir del ciclo inmediatamente