"""
Curso Básico de Python 2024

Case study: Selection sort algorithm.

Author: Kevin Márquez
marquezberriosk@gmail.com
"""

unorderedList = [5,2,6,1,8,12,42,96,4] # List to ordenate

print(f'Before: {unorderedList}')

length = len(unorderedList)
i = 0

# Execute until length - 1
while i < length: 
    less = i # Suppose first one is the lesser
    for j in range(i + 1, length): 
        # Find the lesser of the remainder
        if unorderedList[less] > unorderedList[j]:
            less = j # Save position
    # Swap minor found with position i
    unorderedList[i], unorderedList[less] = unorderedList[less], unorderedList[i]
    i += 1 # Move to next position

print(f'After: {unorderedList}')