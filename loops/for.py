"""
Curso Básico de Python 2024

Case study: Syntax example of for loop.

Author: Kevin Márquez
marquezberriosk@gmail.com
"""

classroom = {
    1: 'Carlos',
    2: 'Ramiro',
    3: 'Lewis',
    4: 'José',
    5: 'María'
}

graderResults = [
    {'id': 1, 'evaluationResult': 14},
    {'id': 2, 'evaluationResult': 2},
    {'id': 3, 'evaluationResult': 17},
    {'id': 4, 'evaluationResult': 18},
    {'id': 5, 'evaluationResult': 20}
]

for evaluation in graderResults:
    id = evaluation['id']
    print(f'Student {classroom[id]} obtained a score of {evaluation["evaluationResult"]} points.')
for key, value in classroom.items():
    print(f'Student {value} has the id {key}.')

for key in classroom.keys():
    print(key)

for value in classroom.values():
    print(value)

for i in range(5):
    print(i)