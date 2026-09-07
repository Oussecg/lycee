from numpy import array

def saisir():
    x = int(input("N= "))
    while not (5 <= x <= 100):
        x = int(input("N= "))
    return x

def remplir(m, x):
    for l in range(x):
        for c in range(x):
            m[l, c] = input("M[" + str(l+1) + ", " + str(c+1) + "]= ")
            while not ("A" <= m[l, c] <= "Z"):
                m[l, c] = input("M[" + str(l+1) + ", " + str(c+1) + "]= ")

def afficher_matrice(m, x):
    print("La matrice suivante: ")
    for l in range(x):
        for c in range(x):
            print(m[l, c], end=" ")
        print()
        
def afficher(m, x):
    test = True
    l = 0
    while l < x and test:
        c = 0
        while c < x and test:
            if l == c or x - c - 1 == l:
                if m[l, c] in ["A", "E", "Y", "U", "I", "O"]:
                    c += 1
                else:
                    test = False
            else:
                if m[l, c] in ["A", "E", "Y", "U", "I", "O"]:
                    test = False
                else:
                    c += 1
        l += 1
    if test:
        print("est extraordinaire")
    else:
        print("n'est pas extraordinaire")

N = saisir()
M = array([[str]*N]*N)
remplir(M, N)
afficher_matrice(M, N)
afficher(M, N)