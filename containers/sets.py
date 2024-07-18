"""
Curso Básico de Python 

Case study: Examples of sets.

Author: Kevin Márquez
marquezberriosk@gmail.com
"""

fruits = {"Apple", "Lemon", "Cherry"}
print(fruits)
print("Peach" in fruits)

fruits.add("Pear") # Add one element
print(fruits)
fruits.add(15)
print(fruits)

fruits.update(["Mango", "Banana", "Pineaple"]) # Add n elements, receive an iterable
fruits.update({1111, 5, 10})
print(fruits)

fruits.remove(1111) # Be careful, in case not exist the element raise an exception
print(fruits)
fruits.discard(5) # In case not exist the element not raise an exception
print(fruits)
print(fruits.pop()) # Remove the first one
print(fruits)
fruits.clear()
print(fruits)

X = {1, 2, 3}
Y = {6, 1, 3}
print(X.difference(Y))
print(Y.difference(X))
print(X - Y)
print(X.intersection(Y))
print(Y.intersection(X))
print(X & Y)
print(X.union(Y))
print(Y.union(X))
print(X | Y)
