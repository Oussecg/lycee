from numpy import array
from random import randint

def nombre_cases() -> int:
    x = int(input("Saisir le nombre de case de tableau: "))
    while not (4 <= x <= 10):
        x = int(input("Retaper le nombre de case de tableau de 4 à 10: "))
    return x

def remplir_tableau(t, n:int):
    for i in range(n):
        t[i] = randint(10, 99)

def inverse_tableau(t, n):
    t1 = array([int] * n)
    for i in range(n):
        t1[i] = t[(n -1) - i]
    return t1

N = nombre_cases()
t = array([int] * N)
remplir_tableau(t, N)
t1 = inverse_tableau(t, N)
print("Tableau 1:", t)
print("Tableau 2:", t1)
