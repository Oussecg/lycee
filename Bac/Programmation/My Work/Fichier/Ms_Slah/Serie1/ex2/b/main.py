from pathlib import Path
from numpy import array
from random import randint

# Automatically gets the absolute path of the directory containing this script
folder_path = str(Path(__file__).resolve().parent)

def saisir() -> int:
    N = int(input("N= "))
    while not (0 < N <= 26):
        N = int(input("N= "))
    return N

def Creer() -> str:
    ch = ""
    for _ in range(4):
        ch += chr(randint(65, 90))
    return ch

def est_distinct(T, ch:str, i:int) -> bool:
    j = 0
    test = True
    while j < i and test:
        if T[j] == ch:
            test = False
        else:
            j += 1
    return test
    
def remplir(N):
    Fc = open(folder_path + "/alpha.txt", "w")
    T = array([str] * N)
    for i in range(N):
        ch = Creer()
        while not est_distinct(T, ch, i):
            ch = Creer()
        T[i] = ch
        Fc.write(ch + "\n")
    Fc.close()

N = saisir()
remplir(N)