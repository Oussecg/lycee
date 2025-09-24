from math import sqrt

def saisir():
    x = int(input("Saisir un entier: "))
    while not (0 < x):
        x = int(input("Retaper un entier: "))
    return x

def somme_racine(x1, x2):
    return sqrt(x1) + sqrt(x2)

def puissance(x1, x2):
    r = 1
    for _ in range(x2):
        r = r * x1
    return r

a = saisir()
b = saisir()

R1 = somme_racine(a, b)
R2 = puissance(a, b) + puissance(b, a)

print("R1 =", R1)
print("R2 =", R2)
