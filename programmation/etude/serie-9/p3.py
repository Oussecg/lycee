from numpy import array

def saisir(x, y, ch):
  n = int(input(ch))
  while not (x <= n <= y):
    n = int(input(ch))
  return n

def remplir(m, ns, ne):
  for i in range(ns):
    for j in range(ne):
      m[i, j] = input(f"M[{i+1}, {j+1}]= ")
      while not (m[i, j].find("#") != -1 and est_alpha(m[i, j][ 0 : m[i, j].find("#") ]) and  2 <= int(m[i, j][m[i, j].find("#")+1 : ]) <= 35) :
        m[i, j] = input(f"M[{i+1}, {j+1}]= ")

def est_alpha(ch):
  test = True
  i = 0
  while i < len(ch) and test:
    if "A" <= ch[i] <= "Z":
      i += 1
    else:
      test = False
  return test

def trier(m, ns, ne):
  for i in range(ns):
    n = ne
    b = True
    while b or  n - 1 > 0:
      for c in range(n-1):
        ag1 = int(m[i, c][m[i, c].find("#")+1: ])
        ag2 = int(m[i, c+1][m[i, c+1].find("#")+1: ])
        if ag1 < ag2:
          aux = m[i, c]
          m[i, c] = m[i, c+1]
          m[i, c+1] = aux
          b = False
        print(n, i, c, c+1, m[i, c], m[i, c+1], m[i])
      n -= 1

def afficher(m, ns, ne):
  for i in range(ns):
    print(f"Société {i} :", end=" ")
    for j in range(ne):
      print(m[i, j], end=" - ")
    print()

Ns = saisir(3, 10, "Ns= ")
Ne = saisir(4, 15, "Ne= ")
M = array([[str]*Ne]*Ns)
remplir(M, Ns, Ne)
trier(M, Ns, Ne)
afficher(M, Ns, Ne)

