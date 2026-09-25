from pathlib import Path
from numpy import array

# Automatically gets the absolute path of the directory containing this script
folder_path = str(Path(__file__).resolve().parent)


def saisir() -> int:
    N = int(input("Saisir N= "))
    while not 2 <= N <= 30:
        N = int(input("Saisir N= "))
    return N

def verifier(ch: str) -> bool:
    p = ch.find(" ")
    p1 = ch[ : p]
    p2 = ch[p+1 : ]
    test1 = True
    i = 0
    while test1 and i < len(p1):
        if "A" <= p1[i].upper() <= "Z":
            i += 1
        else:
            test1 = False
    nbr = 0
    i = 0
    test2 = True
    while test2 and i < len(p2):
        if p2[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            i += 1
        elif p2[i] == ".":
            nbr += 1
            i += 1
        else:
            test2 = False
    return test1 and test2 and nbr <= 1
    
            
def remplir(T, N: int):
    F = open(folder_path + "/Eleve.txt", "w") 
    
    for i in range(N):
        T[i] = dict()
        ch = input("ch" + str(i+1) + "= ")
        while not(ch.find(" ") != -1 and ch.find("  ") == -1 and verifier(ch)):
            ch = input("ch" + str(i+1) + "= ")
        F.write(ch + "\n")
        
        p = ch.find(" ")
        p1 = ch[ : p]
        p2 = ch[p + 1 : ]
        T[i]["nom"] = p1
        T[i]["moy"] = float(p2)
        
    F.close()
        
def afficher(T, N: int):
    Fr = open(folder_path + "/Resultat.txt", "w") 
    Ne = int(input("Saisir Nombre de élèves participant à la compétence: "))
    while not ( 0 <= Ne < N ):
        Ne = int(input("Saisir Nombre de élèves participant à la compétence: "))
        
    # Trier le table d’enregistrement
    test = True
    while test:
        test = False
        for i in range(N - 1):
            if T[i]["moy"] < T[i+1]["moy"]:
                aux = T[i]
                T[i] = T[i + 1]
                T[i + 1] = aux
                test = True
    
    # Afficher Les étudiants participants 
    for i in range(Ne):
        ch = T[i]["nom"] + "#" + str((T[i]["moy"]))
        print(ch)
        Fr.write(ch + "\n")
    
    # Fermer le fichier
    Fr.close()
    

# Programme Principale

Enrg = dict(
    nom = str,
    moy = float
)

N = saisir()

T = array([Enrg] * N)

remplir(T, N)

afficher(T, N)