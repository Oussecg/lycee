from numpy import array
from random import randint
from pathlib import Path

def saisir(ch: str, x1: int, x2: int) -> int:
    N = int(input(ch + "= "))
    while not x1 <= N <= x2:
        N = int(input(ch + "= "))
    return N

def remplir(M, p: int, q: int):
    Ft = open(folder_path + "/MaxMatrice.txt", "w")
    Ft.write("Avant le Triage \n")
    for i in range(p):
        for j in range(q):
            M[i, j] = randint(10, 99)
            Ft.write(f"{M[i, j]}, ")
        Ft.write("\n")
    Ft.write("\n")
        
    
def Afficher(M, p: int, q: int):
    for j in range(q):
        test = True
        while test:
            test = False
            for i in range(p - 1):
                if M[i, j] > M[i+1, j]:
                    aux = M[i, j]
                    M[i, j] = M[i+1, j]
                    M[i+1, j] = aux
                    test = False
    Ft = open(folder_path + "/MaxMatrice.txt", "a")
    Ft.write("Après le triage \n")
    Mt = 0
    for i in range(p):
        for j in range(q):
            Ft.write(f"{M[i, j]}, ")
        Ft.write("\n")
    Ft.write("\n")
    
    for j in range(q):
        Mc = 0
        for i in range(p):
            if M[i, j] > Mt:
                Mt = M[i, j]
            if M[i, j] > Mc:
                Mc = M[i, j]
        Ft.write(f"Maximum de la colonne {j+1} = {Mc} \n")
    Ft.write(f"Maximum de la matrice = {Mt}")
    Ft.close()
    
                
                    
        
folder_path = str(Path(__file__).resolve().parent)
p = saisir("Ligne", 3, 8)
q = saisir("Colonne", 3, 10)
M = array([[int]*q]*p)
remplir(M, p, q)
print(M)
Afficher(M, p, q)