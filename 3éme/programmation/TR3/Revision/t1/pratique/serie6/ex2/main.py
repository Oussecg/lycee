from numpy import array
from random import randint

def saisir(x, y, ch):
    n = int(input(ch))
    while not( x <= n <= y ):
        n = int(input(ch))
    return n

def remplir(t, x, y):
    for i in range(x):
        for j in range(y):
            t[i, j] = chr(randint(65, 90))

def afficherM(t, x, y):
    print("Matrice M:")
    for i in range(x):
        for j in range(y):
            print(t[i, j], end="  ")
        print()

def afficher(t, x, y):
  print("La chaîne obtenue est:")
  for i in range(y):
    ch = ""
    for j in range(x):
      ch += t[j, i]
    print(ch, end=" ")

n = saisir(3, 15, "n: ")
m = saisir(3, 15, "m: ")
M = array([[str] * m] * n)
remplir(M, n, m)
afficherM(M, n, m)
afficher(M, n, m)
