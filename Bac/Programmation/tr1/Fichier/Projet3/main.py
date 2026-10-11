from pathlib import Path
from numpy import array
from random import randint
from time import sleep

def saisir(a: int, b: int, ch: str) -> int:
    x = int(input(ch + "= "))
    while not a <= x <= b: 
        x = int(input(ch + "= "))
    return x

def remplir(M, n: int, m: int):
    F = open(folder_path + "/PointsAigus.txt", "w")
    for i in range(n):
        for j in range(m):
            M[i, j] = randint(1, 9)
            print(str(M[i, j]), end=", ")
            F.write(str(M[i, j]) + ", ")
        print("\n")
        F.write("\n")
    F.close()
    sleep(3)
            
def afficher(M, n: int, m: int):
    F = open(folder_path + "/PointsAigus.txt", "a")
    nb = 0
    for i in range(n):
        for j in range(m):
            mx = Max_Ligne(M, i, m)
            mn = Min_Colonne(M, n, j)
            if M[i, j] == mx and M[i, j] == mn:
                F.write(f"M[{i}, {j}]= {M[i, j]} est un point-aigus \n")
                nb += 1
    if nb == 0:
        F.write("Aucun point-aigus trouvé")  
    F.close()

def Max_Ligne(M, i: int, m: int) -> int:
    mx = M[i, 0]
    for j in range(1, m):
        if M[i, j] > mx:
            mx = M[i, j]
    return mx

def Min_Colonne(M, n: int, j: int) -> int:
    mn = M[0, j]
    for i in range(1, n):
        if M[i, j] < mn:
            mn = M[i, j]
    return mn

folder_path = str(Path(__file__).resolve().parent)

m = saisir(2, 10, "M")
n = saisir(2, m, "N")
M = array([[int]*m]*n)
remplir(M, n, m)
afficher(M, n, m)