from numpy import array

def saisir_cases():
    n = int(input("Saisir le nombre de cases: "))
    while not 5 <= n <= 100:
        n = int(input("Saisir le nombre de cases: "))
    return n

def remplir_TC(t, n:int):
    for i in range(n):
        t[i] = input("TC[" + str(i + 1) + "]= ")
        while not (t[i].find("-") != -1 and len(t[i][t[i].find("-") + 1 : ]) >= 4 and est_alpha(t[i][ : t[i].find("-")]) and t[i][t[i].find("-") + 1 : ].isdecimal() and check_matricules(t, t[i][t[i].find("-") + 1 : ], i)):
            t[i] = input("TC[" + str(i + 1) + "]= ")

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

def remplir_TN(t, n:int):
    for i in range(n):
        t[i] = float(input("TN[" + str(i + 1) + "]= "))
        while not (0 <= t[i] <= 20):
            t[i] = float(input("TN[" + str(i + 1) + "]= "))

N = saisir_cases()
TC = array([str] * N)
TN = array([float] * N)
TC = remplir_TC(TC, N)
TN = remplir_TN(TN, N)
