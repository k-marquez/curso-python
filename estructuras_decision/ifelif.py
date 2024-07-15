myVar = -10

if myVar > 0:
    print('Soy mayor que 0')
elif myVar < 0:
    print('Soy menor que 0')
else:
    print('Soy el 0')

if None:
    print('Soy un print invisible')
elif []:
    print('Soy otro print invisible')
elif [1]:
    print('Soy inevitable')

if myVar < 0 and myVar > -20:
    print('Estoy en el rango de -20 a 0')

# Convertir un número negativo a positivo
mySecondVar = myVar * -1 if myVar < 0 else myVar 
print(mySecondVar)