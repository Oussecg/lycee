from numpy import array
from random import randint

def remplir(m, n):
  for i in range(n):
    for j in range(n):
      m[i, j] = randint(1, 20)

def saisir():
  x = int(input("X= "))
  while not (1 <= x <= 20):
    x = int(input("X= "))
  return x

def trouver(m, n, x):
  for i in range(n):
      test = True
      j = 0
      while not (test or j < n):
        if m[i, j] == x:
          test = 
N = randint(5, 15)
M = array([[int]*N])
remplir(M, N)
trouver()
