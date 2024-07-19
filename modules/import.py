"""
Curso Básico de Python 

Case study: Example of import a module.

Author: Kevin Márquez
marquezberriosk@gmail.com
"""

from csv import DictReader # Bult-in module
import csv

#print(dir(csv)) # Show content of a module

with open('grades.csv', newline='') as csvfile:
    reader = DictReader(csvfile) # without csv.
    for row in reader:
        print(f'{row["Firstname"]} {row["Lastname"]}')

with open('trees.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
