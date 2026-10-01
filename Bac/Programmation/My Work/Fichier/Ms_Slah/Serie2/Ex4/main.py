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
    
def chercher(ch:str, dir:str) -> str:
    p1 = ch.find("+") 
    p2 = ch.find("-") 
    if p1 != -1:
        if dir == "r":
            ch = ch[p1+1 : ]
        else:
            ch = ch[ : p1]
    elif p2 != -1:
        if dir == "r":
            ch = ch[p2+1 : ]
        else:
            ch = ch[ : p2]
    # We have to return both Numbers on form of string and the position of the + or - to fully remove them from the operation
    return ch
    
def calculer(ch: str) -> str:
    # étape 1 : Identification de * et /
    while ch.find("*") != -1 or ch.find("/") != -1:
        p1 = ch.find("*")
        if p1 != -1:
            # Fix this, We have to remove the * operation and add the result of it in the back of the string
            ch1 = ch[ : p1]
            x1 = int(chercher(ch1, "r"))
            ch2 = ch[p1 + 1 : ]
            x2 = int(chercher(ch2, "l"))
            # ch +
        p2 = ch.find("/")

def afficher(N):
    F = open(folder_path + "/operations.txt", "r")
    Fr = open(folder_path + "/calculer.txt", "w")
    for _ in range(N):
        ch = F.readline()
        Fr.write(calculer(ch) + "\n")