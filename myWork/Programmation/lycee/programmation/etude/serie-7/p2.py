from numpy import array

def saisir():
  x = int(input("N: "))
  while not(4 <= x <= 20):
    x = int(input("N: "))
  return x

def remplir(m, n):
  for i in range(n):
    for j in range(n):
      m[i, j] = int(input("m[" + str(i+1) + ", " + str(j+1) + "]= "))
      while not(0 <= m[i, j] <= 9):
        m[i, j] = int(input("m[" + str(i+1) + ", " + str(j+1) + "]= "))

def afficher(m, n):
  s1 = 0
  s2 = 0
  m1 = 0
  m2 = 0
  for i in range(n):
    for j in range(n):
      if i == j:
        s1 += m[i, j]
        if m[i, j] > m1:
          m1 = m[i, j]
      if i == (n-1) - j:
        s2 += m[i, n-j-1]
        if m[i, n-j-1] > m2:
          m2 = m[i, n-j-1]
  print("Le maximum de la première diagonale est =", m1)
  print("Le maximum de la dixième diagonale est =", m2)
  print("La somme de la première diagonale est =", s1)
  print("La somme de la dixième diagonale est =", s2)
  if s1 == s2 and m1 == m2:
    print("M est extra")
  else:
    print("M n'est pas extra")

N = saisir()
M = array([[int]*N]*N)
remplir(M, N)
afficher(M, N)


