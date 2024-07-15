myVar = 1 # tipo int
myVar2 = None # sin tipo/valor asociado
anotherVar = "Some text" # tipo str
myList = [1, 3, 4]
myTuple = ("Hola", 1 , myList)
myDict = {"name": "Juan", "age": 18}

print(type(myVar))
print(type(myVar2))
print(type(anotherVar))
print(myList)
print(myTuple)
print(myDict)

print(isinstance(myVar, int))
print(isinstance(myVar, str))