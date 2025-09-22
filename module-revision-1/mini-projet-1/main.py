def saisir():
    x = int(input("Saisir un entier: "))
    while not 10 <= x <= 99:
        x = int(input("Saisir un entier: "))
    return x

def revers(x):
    a = x % 10
    b = x // 10
    print(f"Invers: {a*10+b}")
    return a * 10 + b

def afficher(x):
    a = x % 10
    b = x // 10
    ab = a + b
    c = ab % 10
    d = ab // 10
    s = ab % 10 + ab // 10
    r = str(d) + str(s) + str(c)
    return int(r)

x = saisir()
inv = revers(x)
print(f"{x} + {inv} = {afficher(inv)}")
