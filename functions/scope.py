"""
Curso Básico de Python 

Case study: Basic knowledge of the scope of a variable.

Author: Kevin Márquez
marquezberriosk@gmail.com
"""

# Definition of global variables
x = 7
point = (1, 2)

# Use local var
def addFive(operand):
    x = 5
    print(operand + x) # 7 + 5

# Use global var
def addFiveGlobal(operand):
    print(operand + x) # 7 + 7

addFive(x)
addFiveGlobal(x)

# Change a global var
def changeX():
    global x

    x = 15

print(x)
changeX()
print(x)

# ¿Local o global?
def useX():
    x = 9999

    print(x) # Python will always use the local variable over the global one

useX()