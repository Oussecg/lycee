from numpy import array

def saisir(x:int, y:int, m:str):
  n = int(input(f"Nombre de {m} ? "))
  while not (x <= n <= y):
    n = int(input(f"Nombre de {m} ? "))
  return n

def remplir(m, l, c):
    for i in range(l):
        for j in range(c):
            m[i, j] = int(input(f"M[{i+1}, {j+1}]= "))
            while not (1 <= m[i, j] <= 9):
                m[i, j] = int(input(f"M[{i+1}, {j+1}]= "))
    print(m)

def afficher(m, l, c):
    mx = maxx(m, l, c)
    print("Dans ce cas, le programme affiche:", end=" ")
    for i in range(c):
        cmm = 0
        for j in range(l):
            if m[j, i] % 2 == 0:
                cmm += 1
        if cmm == mx:
            print(f"Colonne {i+1}", end=" ")

def maxx(m, l, c) -> int:
    mm = 0
    for i in range(c):
        cmm = 0
        for j in range(l):
            if m[j, i] % 2 == 0:
                cmm += 1
        if cmm > mm:
            mm = cmm
    return mm
              
L = saisir(3, 10, "L")
C = saisir(4, 15, "C")
M = array([[int] * C] * L)
remplir(M, L, C)
afficher(M, L, C)
