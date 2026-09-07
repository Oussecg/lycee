from numpy import array
from random import randint

def saisir(ch):
  n = int(input(ch))
  while not (3 <= n <= 8):
    n = int(input(ch))
  return n

def remplir(m, l, c):
  for i in range(l):
    for j in range(c):
      m[i, j] = randint(10, 99)

def afficher_matrice(m, l, c):
  print("La matrice M:")
  for i in range(l):
    for j in range(c):
      print(m[i, j], end=" ")
    print()

def afficher(m, l, c):
  t = array([int]*(l*c))
  k = 0
  for i in range(l):
    for j in range(c):
      t[k] = m[i, j]
      k += 1
  test = False
  while not (test or k == 1):
    test = True
    for z in range(k-1):
      if t[z] > t[z+1]:
        aux = t[z]
        t[z] = t[z+1]
        t[z+1] = aux
        test = False
    k -= 1
  k = 0
  print()
  for i in range(l):
    for j in range(c):
      m[i, j] = t[k]
      k += 1
  afficher_matrice(m, l, c)

L = saisir("Donner L: ")
C = saisir("Donner C: ")
M = array([[int]*C]*L)
remplir(M, L, C)
afficher_matrice(M, L, C)
afficher(M, L, C)
print(f"Max= {M[L-1, C-1]}")
