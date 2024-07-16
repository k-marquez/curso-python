"""
Curso Básico de Python 2024

Caso de estudio: Demostración de la sintaxis del for.

Autor: Kevin Márquez
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
    print(f'El estudiante {classroom[id]} obtuvo una nota de {evaluation["evaluationResult"]} puntos.')

for key, value in classroom.items():
    print(f'El estudiante {value} tiene asociado el id {key}.')

for key in classroom.keys():
    print(key)

for value in classroom.values():
    print(value)

for i in range(5):
    print(i)

for i = 0, i