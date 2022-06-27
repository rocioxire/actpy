#Crea una función que sume los enteros de un arreglo de hasta 1000 números enteros.

import random

x = input("Tamaño de la lista (entre 1 y 1000 elementos): ")
x = int(x)

numeros = []

i = 0
while i < x:
  numeros.append(random.randint(0,100))
  i += 1

print(numeros)

def SumaEnteros(y):
    s = 0
    j = 0
    while j < len(y):
        s = s + y[j]
        j += 1
    print(s)

SumaEnteros(numeros)
