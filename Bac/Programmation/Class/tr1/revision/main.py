from numpy import array


def saisir():
    x = int(input("N= "))
    while not (2 <= x <= 100):
        x = int(input("N= "))
    return x

def remplir(T, N):
    for i in range (N):
        T[i] = dict()
        T[i]["M"] = input("M[" + str(i) + "]= ")
        while not (len(T[i]["M"]) == 8 and T[i]["M"].isdecimal() and est_distinct(T, i)):
            T[i]["M"] = input("M[" + str(i) + "]= ")
            
        T[i]["S"] = int(input("S[" + str(i) + "]= "))
        while not (20 <= T[i]["S"] <= 120):
            T[i]["S"] = int(input("S[" + str(i) + "]= "))
   
def est_distinct(T, N):
    test = True
    i = 0
    while test and i < N:
        if T[i] == T[N]:
            test = False
        else:
            i += 1
    return test

def trier(T, N):
    test = True
    while test:
        test = False
        for i in range(N-1):
            if T[i]["S"] < T[i + 1]["S"]:
                aux = T[i]
                T[i] = T[i+1]
                T[i+1] = aux
                test = True

def afficher(T, N):
    N = round((N * 25) / 100)
    for i in range(N):
        print(T[i]["M"], T[i]["S"])

Enr = dict(
    M= str,
    S= int
)

N = saisir()

T = array([Enr] * N)

remplir(T, N)
trier(T, N)
afficher(T, N)