from numpy import array
from random import randint

def saisir(x, y, ch):
  n = int(input(ch))
  while not(x <= n <= y):
    n = int(input(ch))
  return n

def remplir(A, n, m):
  for L in range(n):
    for C in range(m):
      A[L, C] = chr(randint(97, 122))
      print(A[L, C], end=" ")
    print("")

def afficher(A, n, m):
  nb = 0
  print("Les elements Parfaitement_Uniques sont:")
  for L in range(n):
    for C in range(m):
       if verifier(A, L, C, n, m):
         print("A[" + str(L) + "," + str(C) + "]=" + A[L, C])
         nb += 1
  if nb == 0:
    print("aucun element trouvé")

def verifier(A, L, C, n, m):
  nb1 = 0
  nb2 = 0
  for j in range(m):
    if A[L, C] == A[L, j]:
      nb1 += 1

  for i in range(n):
    if A[L, C] == A[i, L]:
      nb2 += 1

  if nb1 <= 1 and nb2 <= 1:
    return True
  return False

n = saisir(3, 10, "n= ")
m = saisir(n+1, 15, "m= ")
A = array([[chr]*m]*n)
remplir(A, n, m)
afficher(A, n, m)
