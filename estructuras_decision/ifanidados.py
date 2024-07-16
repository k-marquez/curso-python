"""
Curso Básico de Python 2024

Caso de estudio: Sintaxis anidada de if / elif / else y str formateados.

Autor: Kevin Márquez
marquezberriosk@gmail.com
"""

numbersList = []

if len(numbersList) == 0:
    numbersList = [1]

print(numbersList)

if len(numbersList): # Entra porque len(numbersList) != 0 = True
    numbersList = [1, 3, 4]
    number = 11
    if number in numbersList:
        print('There is a ' + str(number) + ' on the list.')
    else:
        print(f'There is no a {number} on the list.') # Conocido como formatted string literal

print(numbersList)
