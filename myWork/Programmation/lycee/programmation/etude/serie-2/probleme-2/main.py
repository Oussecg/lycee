from numpy import array

def saisir_cases():
    n = int(input("Saisir le nombre de cases: "))
    while not 2 <= n <= 100:
        n = int(input("Saisir le nombre de cases: "))
    return n

def remplir_TAB(t1, t2, n:int):
    for i in range(n):
        # IMPORTANT: Remplir tableau 1
        t1[i] = input("TC[" + str(i + 1) + "]= ")
        while not (t1[i].find("-") != -1 and len(t1[i][t1[i].find("-") + 1 : ]) >= 4 and est_alpha(t1[i][ : t1[i].find("-")]) and t1[i][t1[i].find("-") + 1 : ].isdecimal() and check_matricules(t1, t1[i][t1[i].find("-") + 1 : ], i)):
            t1[i] = input("TC[" + str(i + 1) + "]= ")

        # IMPORTANT: Remplir tableau 2
        t2[i] = float(input("TN[" + str(i + 1) + "]= "))
        while not (0 <= t2[i] <= 20):
            t2[i] = float(input("TN[" + str(i + 1) + "]= "))


def est_alpha(ch: str) -> bool:
    test = True
    i = 0
    while i < len(ch) and test == True:
        if "A" <= ch[i] <= "Z":
            i += 1
        else:
            test = False
    return test

def check_matricules(t, ch: str, n: int):
    test = True
    i = 0
    while i < n and test == True:
        if t[i][t[i].find("-") + 1 : ] == ch:
            test = False
        else:
            i += 1
    return test

def cherche_réussite(t, n:int):
    nb = 0
    for i in range(n):
        if t[i] >= 10:
            nb += 1
    r = round(nb / n * 100)
    print(f"Taux de réussite = {r} %")
    return round(nb / n * 100)

def afficher_gouvernement(t1, t2, n:int):
    max_note = max(t2)
    print("Gouvernorat(s) ayant la meilleure note:", end=" ")
    for i in range(n):
        if t2[i] >= max_note:
            print(t1[i][ : t1[i].find("-")], end=" ")
    print("")

def chercher_matricule(t1, t2, n:int):
    m = int(input("Donner la matricule du participant: "))
    while not(m >= 1000):
        m = int(input("Donner la matricule du participant: "))
    i = 0
    test = True
    while i < n and test:
        mt = int(t1[i][ t1[i].find("-") + 1 : ])
        if mt == m:
            test = False
        else:
            i += 1
    if not test:
        print(f"La note de participant {m} est: {t2[i]}")
    else:
        print("Matricule introuvable")


N = saisir_cases()
TC = array([str] * N)
TN = array([float] * N)
remplir_TAB(TC, TN ,N)
print("")
print(f"TC = {TC} and TN = {TN}")
TRN = cherche_réussite(TN, N)
afficher_gouvernement(TC, TN, N)
chercher_matricule(TC, TN, N)
