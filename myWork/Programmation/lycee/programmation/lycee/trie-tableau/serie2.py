from numpy import array

def saisir(x, y, ch):
  n = int(input(ch))
  while not (x <= n <= y):
    n = int(input(ch))
  return n

def remplir(p,y,x):
  for i in range (y):
    for j in range (x):
      p[i,j]=int(input("donner number : "))
      while not 0<p[i,j]<10:
        p[i,j]=int(input("donner number : "))

def pair(p, x, j):
  j=0
  test=True
  while test==True and j==x:
    if p[x,j]%2==0:
      print("ligne :",x,p[x,j])
      j=j+1
    else:
      test=False
    return test

def affiche(p, y,x):
  m=0
  d=0
  for i in range (y):
    test=True
    while (test==True or d!=x):
      if p[i,d]%2==0:


L = saisir(3,10,"L: ")
C =saisir(4,20,"C: ")
p=array([[int]*C]*L)
remplir(p,L,C)
