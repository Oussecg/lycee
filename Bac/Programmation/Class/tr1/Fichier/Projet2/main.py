from pickle import dump, load
from pathlib import Path

# Automatically gets the absolute path of the directory containing this script
folder_path = str(Path(__file__).resolve().parent)

def est_alpha(ch: str) -> bool:
    test = True
    i = 0
    while test and i < len(ch):
        if "A" <= ch[i].upper() <= "Z" or ch[i] == " ":
            i += 1
        else:
            test = False
    return test

def remplir() -> int:
    F = open(folder_path + "/eleves.dat", "wb")
    nb = 0
    test = True
    while test:
        El = {}
        
        # Remplissage de nom
        El["N"] = input(f"Nom{nb+1}= ")  
        while not est_alpha(El["N"]):
            El["N"] = input(f"Nom{nb+1}= ")  
            
        # Remplissage de moyen
        El["M"] = float(input(f"Moy{nb+1}= "))
        while not (0 <= El["M"] <= 20):
            El["M"] = float(input(f"Moy{nb+1}= "))
            
        nb += 1
        dump(El, F)
        
        Rp = input("O/N: ").upper()
        while not (Rp in ["O", "N"]):
            Rp = input("O/N: ").upper()
            
        test = False
        if Rp == "O":
            test = True
    F.close()
    return nb
    
def afficher(N: int):
    F = open(folder_path + "/eleves.dat", "rb")
    for i in range(N):
        El = load(F)
        print(f"{i+1}: {El['N']}, {El['M']}")
    F.close()
    
def calculer(N: int):
    F = open(folder_path + "/eleves.dat", "rb")
    Ft = open(folder_path + "/admis.txt", "w")
    Ft.write("Les admis sont : \n")
    nb = 0
    for _ in range(N):
        El = load(F)
        if El["M"] >= 10:
            Ft.write(f"{El['N']}: {El['M']} \n")
            nb += 1
    Ft.write(f"Nombre d'admis= {nb} \n")
    Ft.close()
    
def chercher(N: int):
    F = open(folder_path + "/eleves.dat", "rb")
    m = 0
    for _ in range(N):
        El = load(F)
        if El["M"] > m:
            m = El["M"] 
    F.close()
    
    F = open(folder_path + "/eleves.dat", "rb")
    Ft = open(folder_path + "/admis.txt", "a")
    Ft.write("\nLe(s) meilleur(s) élèves(s):\n")
    for _ in range(N):
        El = load(F)
        if El["M"] == m:
            Ft.write(f"{El['N']} \n")
    F.close()
    Ft.close()

N = remplir()
afficher(N)
calculer(N)
chercher(N)



        