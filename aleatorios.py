import random
aleatorioentero = random.randint(5,245000)
print(aleatorioentero)

aleatorioflotante = random.uniform(0.0,5)
print(aleatorioflotante)

#del modulo random solo importar esas 2 funciones:
from random import randint, uniform
aleatorioentero = randint(5,245000)
print(aleatorioentero)
'''
aleatorioflotante = uniform(0.0,5)
print(aleatorioflotante)
# Crear una lista de 100 numeros aleatorios:
#1. Crear una lista vacía
edades = []
#2. Generar un numero aleatorio
edad = randint(0,110)
#3. Agregamos el umero a la llista
edades.append(edad)
print(edades)
'''
"""
#4. Generar 100 numeros aleatorios y agregarlos a la lista
for i in range(100):
    edad = randint(0,110)
    edades.append(edad)
print(edades)
list2 = [18, 23, 88, 109, 68, 45, 77, 41, 108, 29, 67, 66, 20, 4, 97, 5, 43, 88, 102, 14, 60, 95, 28, 83, 100, 87, 29, 99, 49, 91, 33, 79, 50, 96, 17, 18, 105, 96, 1, 110, 3, 52, 4, 108, 51, 60, 42, 94, 98, 24, 53, 41, 36, 50, 6, 22, 85, 93, 19, 59, 5, 60, 34, 35, 101, 55, 81, 97, 45, 95, 8, 68, 41, 37, 98, 71, 72, 65, 75, 91, 6, 82, 55, 2, 2, 66, 104, 35, 31, 70, 108, 30, 30, 65, 13, 73, 24, 5, 7, 74, 58]
v= len(list2)
print (v)
"""
"""
cont = 0
while cont < 100:
    edad = randint(0,110)
    edades.append(edad)
    cont += 1
print(edades)
"""
notas =[]
for i in range(20):
    print(i)
    nota = uniform(0,5)
    notas.append(nota)
    print(f"Nota = {notas[i]:0.2f}")

