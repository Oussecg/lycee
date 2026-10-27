from pathlib import Path
from numpy import array
from pickle import dump, load

# Automatically gets the absolute path of the directory containing this script
folder_path = str(Path(__file__).resolve().parent)
    
def saisir() -> int:
    N = int(input("N= "))
    while not 3 <= N <= 100:
        N = int(input("N= "))
    return N

def est_alpha(ch: str) -> bool:
    test = True
    i = 0
    while test and i < len(ch):
        if "A" <= ch[i].upper() <= "Z":
            i += 1
        else:
            test = False
    return test

def remplir(N: int):
    F = open(folder_path + "/ouvrier.dat", "wb")
    for i in range(N):
        nm = input(f"Nom({i})= ")
        while not (0 < len(nm) <= 10 and est_alpha(nm)):
            nm = input(f"Nom{i}= ")
        Ouv["nm"] = nm
        
        nb = int(input(f"Nbr_Enfant({i})= "))        
        while not nb >= 0:
            nb = int(input(f"Nbr_Enfant({i})= ")) 
        Ouv["nb_enf"] = nb
        
        anc = int(input(f"Ancienneté({i})= "))
        while not anc > 0:
            anc = int(input(f"Ancienneté({i})= "))
        Ouv["anc"] = anc
            
        sal = float(input(f"Salaire({i})= "))
        while not sal > 450:
            sal = float(input(f"Salaire({i})= "))
        Ouv["sal"] = sal
        
        dump(Ouv, F)
    F.close()
        
def afficher(N: int):
    F = open(folder_path + "/ouvrier.dat", "rb")
    for i in range(N):
        e = load(F)
        print(f"N°= {i}," ,e["nm"], e["nb_enf"], e["anc"], e["sal"])
    F.close()
    
def Aff_Ouv(N: int):
    F = open(folder_path + "/ouvrier.dat", "rb")
    p = int(input("P= "))
    while not (0 <= p < N):
        p = int(input("P= "))
    for i in range(N):
        if i == p:
            e = load(F)
            print(f"N°= {i},", e["nm"], e["nb_enf"], e["anc"], e["sal"])
    F.close()
                        
def Supp_Ouv(N: int):
    F = open(folder_path + "/ouvrier.dat", "rb")
    T = array([Ouv] * (N - 1))
    p = int(input("P(indice qui va tu supprimer)= "))
    while not (0 <= p < N):
        p = int(input("P(indice qui va tu supprimer)= "))
        
    for i in range(N-1):
       if i != p :
           e = load(F)
           T[i] = e
           
    F = open(folder_path + "/ouvrier.dat", "wb")
    for i in range(N-1):
        dump(T[i], F)
    F.close()
    
Ouv = dict(
    nm= str,
    nb_enf= int,
    anc= int,
    sal= float
)

N = saisir()
remplir(N)
Aff_Ouv(N)
afficher(N)
Supp_Ouv(N)
afficher(N)