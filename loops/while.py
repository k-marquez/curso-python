"""
Curso Básico de Python 2024

Case study: Syntax example of while loop.

Author: Kevin Márquez
marquezberriosk@gmail.com
"""

number = 0

while number < 10:
    print(number)
    number += 2

"""
The parentheses are typical of the nesting of the operation rather than
part of the while syntax
"""
while (number > 0):
    print(number)
    number -= 2
    break # Loop exit