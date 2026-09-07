from numpy import array

def saisir():
  x = int(input("Saisir le nombre de cases et de lignes: "))
  while not (2 <= x <= 6):
    x = int(input("Saisir le nombre de cases et de lignes: "))
  return x

def remplir1(x, n):
  for i in range(n):
    for j in range(n):
      x[i, j] = input(f"X[{i+1}, {j+1}]= ")
      while not("A" <= x[i, j] <= "Z"):
        x[i, j] = input(f"X[{i+1}, {j+1}]= ")
  return x

def remplir2(y, x, n):
  for i in range(n):
    ch1 = ""
    ch2 = ""
    for j in range(n):
      ch1 += x[i, j]
      ch2 += x[j, i]
    y[0, i] = ch1
    y[1, i] = ch2
  return y

def afficherY(y, n):
  for i in range(2):
    for j in range(n):
      print(f"Y[{i+1}, {j+1}]= {y[i, j]}", end=" ")
    print()

def est_alpha(ch):
  test = True
  i = 0
  while i < len(ch) and test:
    if "A" <= ch[i] <= "Z":
      i += 1
    else:
      test = False
  return test


def inverse(ch):
  ch1 = ""
  for i in range(len(ch)):
    ch1 = ch[i] + ch1
  return ch1

def afficher(y, n, M):
  nb = 0
  for i in range(2):
    for j in range(n):
      if y[i, j] == M or inverse(y[i, j]) == M:
        nb += 1
  print(f"Le nombre de récurrence de {M} dans Y est {nb}")

N = saisir()
X = array([[str] * N] * N)
Y = array([[str] * N] * 2)
X = remplir1(X, N)
Y = remplir2(Y, X, N)
afficherY(Y, N)
M = input("M= ")
while not(len(M) == N and est_alpha(M)):
  M = input("M= ")
afficher(Y, N, M)
