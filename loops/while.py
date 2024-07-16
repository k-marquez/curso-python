"""
Curso Básico de Python 2024

Caso de estudio: Demostración de la sintaxis del while.

Autor: Kevin Márquez
marquezberriosk@gmail.com
"""

number = 0

while number < 10:
    print(number)
    number += 2

"""
Los paréntesis son propios del anidamiento de la operación más que parte de la
sintaxis del while
"""
while (number > 0):
    print(number)
    number -= 2
    break # Salir del ciclo inmediatamente