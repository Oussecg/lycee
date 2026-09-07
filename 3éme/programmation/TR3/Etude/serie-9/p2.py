from numpy import array
from random import randint

def saisir():
  n = int(input("Saisir N= "))
  while not (6 <= n <= 99 and n % 3 == 0):
    n = int(input("Saisir N= "))
  return n

def remplir(t, n):
  for i in range(n):
    t[i] = input(f"T[{i+1}]= ")
    while not (len(t[i]) >= 4 and est_alpha(t[i]) and distinct(t, i)):
      t[i] = input(f"T[{i+1}]= ")

def est_alpha(ch):
  test = True
  i = 0
  while test and i < len(ch):
    if "A" <= ch[i] <= "Z":
      i += 1
    else:
      test = False
  return test

def distinct(t, n):
  test = True
  i = 0
  while test and i < n:
    if t[n] == t[i]:
      test = False
    else:
      i += 1
  return test

def trier(t, n, p):
  b = True
  while b or n > 1:
    for i in range(n-1):
      ord1 = ord(t[i][p])
      ord2 = ord(t[i+1][p])
      s1 = ord1 % 10 + ord1 // 10
      s2 = ord2 % 10 + ord2 // 10
      if s1 < s2:
        aux =  t[i]
        t[i] = t[i+1]
        t[i+1] = aux
        b = False
    n -= 1

def afficher(t, nb, p):
  print(f"Si P = {p}, les clients gagnants sont:",end=" ")
  for i in range(nb):
    print(t[i], end=" ")

N = saisir()
nb = N // 3
p = randint(0, 3)
T = array([str]*N)
remplir(T, N)
trier(T, N, p)
afficher(T, nb, p)
