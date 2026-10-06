from pathlib import Path

# Automatically gets the absolute path of the directory containing this script
folder_path = str(Path(__file__).resolve().parent)

def saisir() -> int:
    N = int(input("N= "))
    while 2 <= N <= 20 :
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
    
    
def remplir(N):
    F = open(folder_path + "/operations.txt", "w")
    
    for _ in range(N):
        ch = input("Ch= ")
        while est_operation(ch):
            ch = input("Ch= ")
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
            
            # Partie 1 : ( Calculer le résultat de * )
            x1 = int(e["ch1"])
            x2 = int(e["ch2"])
            r = x1 * x2
            
            # Partie 2: ( Effacer le opération de * )
            ch1 = ch[ : e["i1"]]
            ch2 = ch[e["i2"] : ]
            
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
    nb = ""
    nbr = 0
    s = 0
    i = 0
    while i < len(ch):
        if ch[i] in ["+", "-"]:
            nbr += 1
            if nbr == 1:
                s += int(nb)
            else:
                test = True
                j = i+1
                nb1 = ""
                while test and j < len(ch):
                    if ch[j] in ["+", "-"]:
                        i = j
                        test = False
                    else:
                        nb1 += ch[j]
                        j += 1
                print(f"nb1= {nb1}, i= {i}, j= {j}")
                x = int(nb1)
                if ch[i] == "+":
                    s += x
                else:
                    s -= x
        else:
            nb += ch[i]
        i += 1
    ch += "=" + str(s)
    print(ch)
    return ch


def afficher(N):
    F = open(folder_path + "/operations.txt", "r")
    Fr = open(folder_path + "/calculer.txt", "w")
    for _ in range(N):
        ch = F.readline()
        Fr.write(calculer(ch) + "\n")
    F.close()
    Fr.close()
    
    
        
# calculer("12+12*13-15/3+5-2/5")