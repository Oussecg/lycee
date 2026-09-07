from numpy import array

def nombre_élève() -> int:
    x = int(input("Donner le nombre d'élèves: "))
    while not (3 < x <= 25):
        x = int(input("Donner le nombre d'élèves: "))
    return x

def remplir_tableau(t, n: int):
    for i in range(n):
        t[i] = float(input("Moyenne de l'élève " + str(i + 1) + " : "))
        while not (0 <= t[i] <= 20):
            t[i] = float(input("Moyenne de l'élève " + str(i + 1) + " : "))

def moyen_générale(t, n: int) -> float:
    mg = 0
    for i in range(n):
        mg += t[i]
    mg = round(mg/n, 2)
    return mg

def nombre_moyen_générale(t, n: int, mg: int) -> int:
    nb = 0
    for i in range(n):
        if t[i] >= mg:
            nb += 1
    return nb

def max_moyen(t, n: int) -> float:
    m = 0
    for i in range(n):
        if t[i] > m:
            m = t[i]
    return m

N = nombre_élève()
t = array([float] * N)
remplir_tableau(t, N)
Mg = moyen_générale(t, N)
Ne = nombre_moyen_générale(t, N, Mg)
My = max_moyen(t, N)

print("Le moyen générale est:", Mg)
print("Le nombre d’élèves ayant une moyenne supérieure à", Mg, "est:", Ne)
print("La moyenne la plus élevée est:", My)
