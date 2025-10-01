from numpy import array

def nombre_eleve():
    x = int(input("Donner le nombre d'élèves: "))
    while not (3 < x <= 25):
        x = int(input("Donner le nombre d'élèves: "))
    return x

def remplir_tableau(t, N):
    for i in range(N):
        t[i] = float(input("Moyenne de l'élève " + str(i + 1) + " : "))
        while not (0 <= t[i] <= 20):
            t[i] = float(input("Moyenne de l'élève " + str(i + 1) + " : "))

def moyen_generale(t, n):
    mg = 0
    for i in range(n):
        mg += t[i]
    mg = round(mg/n, 2)
    return mg
        
N = nombre_eleve()
t = array([float] * N)
remplir_tableau(t, N)
Mg = moyen_generale(t, N)
# Ne = nombre_superieur(t, N, Mg)
# My = max_moyen(t, N)
print("Le moyen generale est:", Mg)