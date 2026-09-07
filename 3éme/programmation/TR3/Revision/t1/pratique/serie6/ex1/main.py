from numpy import array
from random import randint

def saisir(x, y, ch):
    n = int(input(ch))
    while not( x <= n <= y ):
        n = int(input(ch))
    return n

def remplir(t, x, y):
    for i in range(x):
        for j in range(y):
            t[i, j] = randint(10, 99)
            
def afficherM(t, x, y):
    print("Matrice M:")
    for i in range(x):
        for j in range(y):
            print(t[i, j], end="  ")
        print()

def afficher(t, x, y):
    print("Ligne(s) trièe(s) :")
    nb = 0
    for i in range(x):
        if est_trie(t, i, y):
            nb += 1
            ch = ""
            print("Ligne" + str(i) + ":", end=" ")
            for j in range(y):
                ch += str(t[i, j]) + "#"
            ch = ch[ : len(ch)-1]
            print(ch)
    if nb > 0:
        print("Nombre de lignes trièes = " + str(nb))
    else:
        print("aucune ligne trièe")
        
def est_trie(t, i, y):
    test = True
    j = 0
    while test and j < y - 1:
        if t[i, j] < t[i, j+1]:
            j += 1
        else:
            test = False
    return test
            
L = saisir(2, 20, "Saisir L? ")
C = saisir(3, 25, "Saisir C? ")
M = array([[int] * C] * L)
remplir(M, L, C)
afficherM(M, L, C)
afficher(M, L, C)
