from pathlib import Path

# Automatically gets the absolute path of the directory containing this script
folder_path = str(Path(__file__).resolve().parent)

def saisir() -> int:
    N = int(input("N= "))
    while not 1 <= N <= 20 :
        N = int(input("N= "))
    return N

def est_operation(ch: str) -> bool:
    test = True
    i = 0
    while test and i < len(ch):
        if ch[i] in {"1", "2", "3", "4", "5", "6", "7", "8", "9"} or ch[i] in {"+", "-", "*", "/"}:
            i += 1
        else:
            test = False
    return test 
    
    
def remplir(N: int):
    F = open(folder_path + "/operations.txt", "w")
    
    for i in range(1, N+1):
        ch = input(f"Ch{i}= ")
        while not est_operation(ch):
            ch = input(f"Ch{i}= ")
        F.write(ch + "\n")
    
    F.close()
    
def chercher(ch:str, p1:int) -> dict:
    test = True
    i1 = p1 - 1
    while test and i1 != 0:
        if ch[i1] in ["+", "-"]:
            test = False
        else:
            i1 -= 1
    ch1 = ch[i1+1 : p1]
    
    test = True
    i2 = p1 + 1
    while test and i2 != len(ch):
        if ch[i2] in ["+", "-"]:
            test = False
        else:
            i2 += 1
    ch2 = ch[p1 + 1: i2]
    
    # We have to return both Numbers on form of string and the position of the + or - to fully remove them from the operation
    return dict(ch1= ch1, i1= i1, ch2= ch2, i2= i2, c= ch[i1])
    
def calculer(ch: str) -> str:
    # étape 1 : Identification de * et /
    while ch.find("*") != -1 or ch.find("/") != -1:
        p1 = ch.find("*")
        if p1 != -1:
            e = chercher(ch, p1)
            
            # Il existe trois parties
            
            print("e1", e["ch1"])
            print("e2", e["ch2"])
            # Partie 1 : ( Calculer le résultat de * )
            x1 = int(e["ch1"])
            x2 = int(e["ch2"])
            r = x1 * x2
            
            # Partie 2: ( Effacer le opération de * )
            ch1 = ch[ : e["i1"]]
            ch2 = ch[e["i2"] : ]
            
            print(ch1, ch2)
            # Partie 3: ( Concaténation des trois chaines )
            ch = ch1 + ch2 + e["c"] + str(r)
            
        p2 = ch.find("/")
        if p2 != -1:
            e = chercher(ch, p2)
            
            # Il existe trois parties
            
            # Partie 1 : ( Calculer le résultat de / )
            x1 = int(e["ch1"])
            x2 = int(e["ch2"])
            r = x1 // x2
            
            # Partie 2: ( Effacer le opération de / )
            ch1 = ch[ : e["i1"]]
            ch2 = ch[e["i2"] : ]
            
            # Partie 3: ( Concaténation des trois chaines )
            ch = ch1 + ch2 + e["c"] + str(r)
            
    # Etape 2: La calcule de ch
    test = True
    p = 0
    while test and p < len(ch):
        if ch[p] in ["+", "-"] and p >= 1:
            test = False
        else:
            p += 1
    s = int(ch[ : p])
    i = 0
    for i in range(p, len(ch)):
        if ch[i] in ["+", "-"]:
            test = True
            j = i + 1
            while test and j < len(ch):
                if ch[j] in ["+", "-"]:
                    test = False
                else:
                    j += 1
            if ch[i] == "+":
                s += int(ch[i+1: j])
            else:
                s -= int(ch[i+1: j])
            i = j         
    ch += "=" + str(s)
    return ch

def remove_newline(s: str) -> str:
    return s.rstrip("\n")

def afficher(N: int):
    F = open(folder_path + "/operations.txt", "r")
    Fr = open(folder_path + "/calculer.txt", "w")
    for _ in range(N):
        ch = F.readline()
        ch = remove_newline(ch)
        Fr.write(calculer(ch) + "\n")
    F.close()
    Fr.close()
    
    
        
N = saisir()
remplir(N)
afficher(N)