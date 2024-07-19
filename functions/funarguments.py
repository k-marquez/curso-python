"""
Curso Básico de Python 

Case study: Function arguments.

Author: Kevin Márquez
marquezberriosk@gmail.com
"""

# Function with 3 positional arguments
def sum(x, y, z):
    return x + y + z

# Called with order
print(f'1 + 2 + 3 = {sum(1,2,3)}') # 6

#sum() # Error, missing all arguments
#sum(1) # Error, missing 2 arguments
#sum(1, 2) # Error, missing 1 argument

# Called by name
print(f'2 + 3 + 1 = {sum(z = 1, x = 2, y = 3)}')


# Default arguments
def sumDefVal(x, y = 2, z = 3):
    return x + y + z

# Call with 0 arg is an error, sumDefVal always expects 1 positional argument
print(f'Call with only 1 arg: {sumDefVal(1)}')
print(f'Call with only 2 arg: {sumDefVal(1, 5)}')
print(f'Call with 3 arg: {sumDefVal(1, 9, 10)}')

# Calling by name and not passing x will fail unless the first argument is positional
print(f'Call by name with only 1 arg: {sumDefVal(x = 1)}')

print(f'Call by name with only 2 arg: {sumDefVal(z = 1, x = 5)}')

print(f'Call by name and 1 positional arg: {sumDefVal(1, y = 1)}')

print(f'Call by name with 3 arg: {sumDefVal(y = 1, z = 9, x = 10)}')


# Arbitrary arguments and keyword arguments
# args is a tuple, kwargs is a dictionary
def printArgs(*args, **kwargs):
    print('Arbitrary arguments')
    for arg in args:
        print(arg)

    print('Keyword arguments')
    for keyword, arg in kwargs.items():
        print(f'{keyword} -> {arg}')

print()
printArgs()

print()
someVal = {1, 3}
printArgs(1, True, [], someVal)

print()
printArgs(kw1 = 1, kw2 = True, kw3 = [], kw4 = someVal)

print()
printArgs(1, 2, x = 19, w = 0)

#printArgs(1, x = 19, 2, w = 0) # Error, all of arbitrary arguments must be pass first 