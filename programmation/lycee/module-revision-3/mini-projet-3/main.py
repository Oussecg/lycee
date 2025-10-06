from numpy import array

def saisir_cases():
    x = int(input("Saisir le nombre de cases: "))
    while not 5 <= x <= 30 :
        x = int(input("Saisir le nombre de cases: "))
    return x

def remplir_tableau(t, n):
    for i in range(n - 1):
        t[i] = int(input("T["+str(i)+"]= "))
        while not (t[i] > 0):
            t[i] = int(input("T["+str(i)+"]= "))
    
def saisir_entier():
    x = int(input("Saisir un entier: "))
    while x < 0:
        x = int(input("Saisir un entier: "))
    return x

def saisir_position(n):
    x = int(input("Saisir le position: "))
    while not ( 0 <= x <= n-2):
        x = int(input("Saisir un entier: "))
    return x

def insertion_entier(t, n, p, e):
    x = t[p]
    t[p] = e
    for i in range(p+1, n):
        c = t[i]
        t[i] = x
        x = c
        
N = saisir_cases()
T = array([int] * N)
remplir_tableau(T, N)
E = saisir_entier()
p = saisir_position(N)
insertion_entier(T, N, p, E)
print(T)