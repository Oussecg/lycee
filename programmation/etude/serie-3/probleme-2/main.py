from numpy import array

def saisir(x, y, m):
    n = int(input(m))
    while not( x <= n <= y ):
        n = int(input(m))
    return n

def remplir(m, c, l):
    for i in range(l):
        for j in range(c):
            m[i, j] = float(input(f"M[{i+1}, {j+1}]= "))
            while not (0 <= m[i, j] <= 20):
                m[i, j] = float(input(f"M[{i+1}, {j+1}]= "))

def afficher(m, c, l):
    for i in range(l):
        mm = 0
        for j in range(c):
            if m[i, j] > mm:
                mm = m[i, j]
        print("Classe" + str(i+1) + ":", end=" ")
        for j in range(c):
            if mm == m[i, j]:
                print(j+1, end="-")
        print()
                
n = saisir(2, 10, "Nombre de classes ? ")
m = saisir(4, 20, "Nombre d'éléves par classe ? ")
M = array([[float] * m] * n)
remplir(M, m, n)
afficher(M, m, n)
            
            
            
            