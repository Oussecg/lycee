from numpy import array

def saisir(x, y, ch):
  n = int(input(ch))
  while not (x <= n <= y):
    n = int(input(ch))
  return n

def remplir(p,y,x):
  for i in range (y):
    for j in range (x):
      p[i,j]= int(input("M[" + str(i+1) + ", " + str(j+1) + "]= "))
      while not (0<p[i,j]<10):
        p[i,j]= int(input("M[" + str(i+1) + ", " + str(j+1) + "]= "))

def pair(p, x, j):
  j = 0
  test = True
  while test and j < x:
    if p[x,j] % 2 == 0:
      j += 1
    else:
      test = False
    return test

def afficher_case(p, i, c):
  for j in range(c):
    print(p[i, j], end=" ")

def afficher(p, l, c):
  m=0
  for i in range (l):
    if pair(p, i, c):
      print("Ligne" + str(i), ":", end=" ")
      afficher_case(p, i, c)
      m += 1
  print()
  if m == 0:
    print("aucune ligne n'est trouvée")
  else:
    print("Nombre de lignes = " + str(m))

L = saisir(3,10,"L: ")
C =saisir(4,20,"C: ")
p=array([[int]*C]*L)
remplir(p, L, C)
afficher(p, L, C)
