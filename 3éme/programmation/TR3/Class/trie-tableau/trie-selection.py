from numpy import array

def saisir():
  x = int(input("Saisir N: "))
  while not (6 <= x <= 99):
    x = int(input("Saisir N: "))
  return x

def remplir1(T, N):
  for i in range(N):
    T[i] = input(f"T[{i+1}]= ")
    while not (est_alpha(T[i]) and distant(T, i)) :
      T[i] = input(f"T[{i+1}]= ")

def remplir2(T, N):
  for i in range(N):
    T[i] = int(input(f"T[{i+1}]= "))
    while not (len(str(T[i])) == 4) :
      T[i] = int(input(f"T[{i+1}]= "))

def est_alpha(ch):
  test = True
  i = 0
  while test and i < len(ch):
    if "A" <= ch[i].upper() <= "Z":
      i += 1
    else:
      test = False
  return test

def distant(T, N):
  test = True
  i = 0
  while test and i < N:
    if T[i] == T[N]:
      test = False
    else:
      i += 1
  return test

def trier(T1, T2, N):
  for i in range(N):
    pMax = max_tab(T2, N, i)
    if pMax != i:
      aux1 = T1[i]
      aux2 = T2[i]
      T1[i] = T1[pMax]
      T2[i] = T2[pMax]
      T1[pMax] = aux1
      T2[pMax] = aux2

def max_tab(T, N, j):
  nMax = j
  for i in range(j+1, N):
    if T[i] > T[nMax]:
      nMax = i
  return nMax

def afficher(T1, T2, N):
  Np = int(input("Saisir Np: "))
  while not (N % Np == 0):
    Np = int(input("Saisir Np: "))
  print("Les jeunes acceptés sont:")
  for i in range(Np):
    print(f"{T1[i]}#{2025-T2[i]}ans")

N = saisir()
T1 = array([str]*N)
T2 = array([int]*N)
remplir1(T1, N)
remplir2(T2, N)
trier(T1, T2, N)
print(T2)
afficher(T1, T2, N)
