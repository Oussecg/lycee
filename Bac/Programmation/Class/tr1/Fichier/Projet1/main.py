def saisir() -> int:
    N = int(input("Saisir N= "))
    while not N > 0:
        N = int(input("Saisir N= "))
    return N

def remplir(F1, N: int):
    for i in range(N):
        ch = input("Ch" + str(i + 1) + "= ")
        while not (verifier(ch)): 
            ch = input("Ch" + str(i + 1) + "= ")
        F1.write(ch + "\n")
    F1.close()
    
def verifier(ch: str) -> bool:
    test = True
    i = 0
    while test and i < len(ch):
        if ch[i] in ["M", "D", "C", "L", "X", "V", "I"]:
            i += 1
        else:
            test = False
    return test

def valeur(c: str) -> int:
    if c == "M":
        return 1000
    elif c == "D":
        return 500
    elif c == "C":
        return 100
    elif c == "L":
        return 50
    elif c == "X":
        return 10
    elif c == "V":
        return 5
    else:
        return 1
    
def Dc_Romain(ch: str) -> int:
    s = 0
    for i in range(len(ch)-1):
        v = valeur(ch[i])
        vp = valeur(ch[i + 1])
        if v >= vp:
            s += v
        else:
            s -= v
    s += valeur(ch[len(ch) - 1])
    return s

def Creer_Nbr(F2, N: int):
    F1 = open("romains.txt", "r")
    for i in range(N):
        ch = F1.readline()
        ch = ch[ : len(ch)-1]
        ch = ch + " = " + str(Dc_Romain(ch)) + "\n"
        F2.write(ch)
        
    
F1 = open("romains.txt", "w")
F2 = open("nombres.txt", "w")
N = saisir()
remplir(F1, N)
Creer_Nbr(F2, N)
F1.close()
F2.close()