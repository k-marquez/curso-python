"""
Curso Básico de Python 

Case study: Examples of dictionaries.

Author: Kevin Márquez
marquezberriosk@gmail.com
"""

# Create dict
inventory = {
    "candy": 10,
    'sugar': 5,
    "chocolate": 3
}

customDict = dict(first = True, second = [])

print(inventory)
print(customDict)

print(len(inventory)) # Number of pairs key:value

# Access elements
print(customDict.get(1)) # If it exists it is returned, otherwise it is None
#print(customDict[1]) # Raises an exception if the element does not exist
print(customDict['first'])

# Modify elements
inventory['candy'] -= 1
inventory.update({'sugar': 20}) # Creates the element if does not exist
print(inventory)

# Add elements
inventory['cookie'] = [1, 14, 53] # Add un element
inventory.update({'lolipop': 15, 'Coke': 20})
print(inventory) 

# Remove element
inventory.pop('cookie')
print(inventory)
#inventory.pop(1) # Exception because element does not exist
customDict.clear()
print(customDict)

# Which is a valid key?
customDict[False] = 1 # Valid key
customDict[0] = 2 # False = 0
print(customDict)
customDict[1] = 1
customDict[True] = 2
print(customDict)
customDict[(1,2)] = 'Yolo' # Valid key
print(customDict)

# Methods
print(inventory.items()) # Result is not accessible by index
print(inventory.keys()) # Result is not accessible by index
print(inventory.values()) # Result is not accessible by index