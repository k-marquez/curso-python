"""
Curso Básico de Python 

Case study: Examples of sequential structures.

Author: Kevin Márquez
marquezberriosk@gmail.com
"""

# List example
fruits = ["Apple", "Lemon", "Banana"]

print(fruits[1]) # Lemon
fruits[2] = "Orange" # Change an element
print(fruits[1:3]) # Lemon, Orange
print(len(fruits)) # 3
 
vegetables = ["Tomato", "Carrot"]
food = fruits + vegetables

print(food) # Apple, Lemon, Orange, Tomato...
print(food[1:4:2]) # Lemon, Tomato
print(food[::-1]) # Carrot, Tomato...


food.append("Potato") # Add one element at the end
food.insert(4, "Onion") # Insert in specific index
print(food)
food.extend(["Peach", "Cherry", "Pear"]) # Add n elements at the end, argument is an iterable
print(food)
food.remove("Onion") # Removes the first occurrence
food.pop(1) # Removes element in specific index, by default erase the last one
print(food)
food.clear()
print(food)

textToList = list("Hello world!") # Constructor receive an iterable object
print(textToList)

# String example
text = 'These is a line of text'
print(text[1]) # h
#text[2] = "H" # Error, strings are immutable
print(text[1:3]) # he
print(len(text)) # 23
 
appendText = ' and just little more'
newText = text + appendText

print(newText) # These is a line of text and just little more
print(newText[1:4:2]) # hs
print(newText[::-1]) # erom elttil tsuj dna txet fo enil a si esehT

toText = str(186463)
print(toText)

# Tuple example
animals = ("Cat", "Dog", "Bird", "Mouse")

print(animals[0]) # Cat
#animals[2] = "Bear" # Error, tupples are immutable
print(animals[0:3]) # Cat, Dog, Bird
print(len(animals)) # 4
 
moreAnimals = tuple(["Horse", "Lion"]) # Constructor receive an iterable object
zoo = animals + moreAnimals

print(zoo) # Cat, Dog, Bird, Mouse, Horse...
print(zoo[1:4:2]) # Dog, Mouse
print(zoo[::-1]) # Lion, Horse, Mouse... 