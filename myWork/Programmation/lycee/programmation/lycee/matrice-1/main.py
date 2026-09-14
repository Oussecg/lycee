from numpy import array

def saisir(x):
    n = int(input("N= "))
    while not(2<= n <= x):
        n = int(input("N= "))
    return n

def remplir(m, x, y):
    for i in range(x):
        for j in range(y):
            message = "m["+str(i+1)+","+str(j+1)+"]= "
            m[i,j] = int(input(message, end=" "))
            while not(m[i, j] >= 0):
                m[i,j] = int(input(message, end=" "))

def afficher(m, x, y):
    for i in range(x):
        mm = 0
        for j in range(y):
            if m[i,j] > m[i, mm]:
                mm = j
        print("Clinique n°" + str(j+1) , "l’étage", mm+1, "comporte le plus grand nombre de patients")

Nc = saisir(10)
Ne = saisir(6)
m = array([[int] * Ne] * Nc)
remplir(m, Nc, Ne)
afficher(m, Nc, Ne)
