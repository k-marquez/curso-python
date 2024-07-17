"""
Curso Básico de Python 2024

Case study: Conditionals syntax examples.

Author: Kevin Márquez
marquezberriosk@gmail.com
"""

number = -10

if number > 0:
    print('Greater than 0')
elif number < 0:
    print('Less than 0')
else:
    print('Is 0')

if None:
    print('I am invisible')
elif []:
    print('I am invisible again')
elif [1]:
    print('I am inevitable')

if number < 0 and number > -20:
    print('I am in the range (-20 to 0)')

if -20 < number < 0: # Equivalente a number < 0 and number > -20
    print('I am in the range (-20 to 0)')

# Convertir un número negativo a positivo
positiveNumber = number * -1 if number < 0 else number 
print(positiveNumber)