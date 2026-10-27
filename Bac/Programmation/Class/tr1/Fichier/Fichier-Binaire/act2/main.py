from pickle import dump, load
from pathlib import Path

# Automatically gets the absolute path of the directory containing this script
folder_path = str(Path(__file__).resolve().parent)

def Write_Eleve():
    N = int(input("Saisir le nombre de élèves: "))
    while not (2 <= N <= 30):
        N = int(input("Saisir le nombre de élèves: "))
        
    F = open(folder_path + "/fichier.dat", "wb")
    for i in range(N):
        Moy = float(input(f"Moy{i+1}= "))
        while not (0 <= Moy <= 20):
            Moy = float(input(f"Moy{i+1}= "))
        dump(Moy, F)
    F.close()
    
def Add_Eleve(N: int):
    i = N
    test1 = True
    F = open(folder_path + "/fichier.dat", "ab")
    while test1:
        i += 1
        Moy = float(input(f"Moy{i}= "))
        while not (0 <= Moy <= 20):
            Moy = float(input(f"Moy{i}= "))
        dump(Moy, F)
        
        R1 = input("Do You want to add another value ? Y/N: ")
        while not(R1.upper() in {"Y", "N"}):
            R1 = input("Do You want to add another value ? Y/N: ")
        R1 = R1.upper()
        
        if R1 == "N":
            test1 = False
            print()
    F.close()
    
def Afficher_Eleve(N):
    F = open(folder_path + "/fichier.dat", "rb")
    for i in range(N):
        Moy = load(F)
        print(f"i= {i+1}, Moy= {Moy}")
    F.close()
    
def Calculer_Length() -> int:
    F = open(folder_path + "/fichier.dat", "rb")
    nb = 0
    test = True
    while test:
        try:
            x = load(F)
            nb += 1
        except:
            test = False
    return nb

def Calculer_Somme(N) -> float:
    F = open(folder_path + "/fichier.dat", "rb")
    S = 0
    for i in range(N):
        Moy = load(F)
        S += Moy
    print(f"Moyen Générale: {S / N}")
    

test = True
while test:
    ch = input("W: Write / A: Add / R: Read / Mg: Moyen Générale :   ")
    while not ch.upper() in ["W", "A", "R", "MG"]:
        ch = input("W: Write / A: Add / R: Read / Mg: Moyen Générale :   ")
    ch = ch.upper()

    if ch == "W":
        N = Write_Eleve()
    elif ch == "A":
        N = Calculer_Length()
        N = Add_Eleve(N)
    elif ch == "R":
        N = Calculer_Length()
        Afficher_Eleve(N)
    elif ch == "MG":
        N = Calculer_Length()
        Calculer_Somme(N)
        
    R = input("Do you want to continue ? Y/N: ")
    while not (R.upper() in {"Y", "N"}):
        R = input("Do you want to continue ? Y/N: ")      
    R = R.upper()
    
    if R == "N":
        test = False
        
        
