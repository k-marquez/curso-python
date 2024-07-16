"""
Curso Básico de Python 2024

Caso de estudio: Sintaxis anidada de if / elif / else y str formateados.

Autor: Kevin Márquez
marquezberriosk@gmail.com
"""

myList = []

if len(myList) == 0:
    myList = [1]

print(myList)

if len(myList): # Entra porque len(myList) != 0 = True
    myList = [1, 3, 4]
    number = 11
    if number in myList:
        print('Hay un ' + str(number) + ' en la lista.')
    else:
        print(f'No hay un {number} en la lista.') # Conocido como formatted string literal

print(myList)
