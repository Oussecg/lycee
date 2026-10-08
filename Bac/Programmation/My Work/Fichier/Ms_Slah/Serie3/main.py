from pickle import dump, load
from pathlib import Path
from numpy import array

def remplir() -> int:
    F = open(fp + "/texte.txt", "w")
    test = True
    nb = 0
    while test:
        nb += 1
        ch = input(f"ch{nb}= ")
        while not verif(ch):
            ch = input(f"ch{nb}= ")
        F.write(ch + "\n")
            
        rep = input("Continue ? Y/N: ").upper()
        while not rep in ["Y", "N"]:
            rep = input("Continue ? Y/N: ").upper()
        if rep == "Y":
            test = True
        else:
            test = False
    F.close()
    return nb
            
def verif(ch: str) -> bool:
    i = 0
    test = True
    while test and i < len(ch):
        if "A" <= ch[i].upper() <= "Z" or ch[i] == " ":
            i += 1
        else:
            test = False
    return test

def Supp_Superflus(ch: str) -> str:
    if ch[0] == " ":
        ch = ch[1 : ]
        
    if ch[len(ch)-1] == " ":
        ch = ch[ : len(ch)-1]
        
    while ch.find("  ") != -1:
        p = ch.find("  ")
        ch1 = ch[ : p]
        ch2 = ch[p+1 : ]
        ch = ch1 + ch2
    return ch

def Nbr_Mots(ch: str) -> int:
    ch = Supp_Superflus(ch)
    nb = 0
    for i in range(len(ch)):
        if ch[i] == " ":
            nb += 1
    return nb

def Totalogramme(ch: str) -> bool:
    test = True
    ch = Supp_Superflus(ch) + " "
    while test and ch.find(" ") != -1:
        p = ch.find(" ")
        a = ch[0].upper()
        b = ch[p-1].upper()
        if a == b:
            ch = ch[p+1: ]
        else:
            test = False
    return test

def Creer(N: int):
    Ft = open(fp + "/texte.txt", "r")
    F = open(fp + "/LigneTotal.dat", "wb")
    
    nb = 0
    for i in range(N):
        ch = Ft.readline()
        ch = ch[ : len(ch)-1]
        if Totalogramme(ch):
            Enr = {}
            Enr["num"] = i+1
            Enr["nb_mots"] = Nbr_Mots(ch)
            nb += 1
            dump(Enr, F)
    Ft.close()
    F.close()
    print(f"Il y'a {nb} chaîne qui est Totalogramme")
    return nb
        
        
def Afficher(N: int, Nb: int):
    F = open(fp + "/LigneTotal.dat", "rb")
    Enr = dict(
        num= int,
        nb_mots= int
    )
    T = array([Enr] * Nb)
    
    # Remplissage
    for i in range(Nb):
        Enr = load(F)
        T[i] = Enr
    F.close()
        
    # Triage
    test = True
    while test:
        test = False
        for i in range(Nb - 1):
            if T[i]["nb_mots"] < T[i+1]["nb_mots"]:
                aux = T[i]
                T[i] = T[i+1]
                T[i+1] = aux
                test = True
    
    # Affichage
    for i in range(Nb):
        Ft = open(fp + "/texte.txt", "r")
        for j in range(1, N+1):
            ch = Ft.readline()
            if T[i]["num"] == j:
                print(f"Pour i= {i+1}, < le chaîne est {ch} >")
        Ft.close()
        

fp = str(Path(__file__).resolve().parent)

N = remplir()
Nb = Creer(N)
Afficher(N, Nb)