from numpy import array

def saisir():
    n = int(input("Saisir nombre d'èléves: "))
    while not (5 <= n <= 30):
        n = int(input("Saisir nombre d'èléves: "))
    return n

def remplir1(t, n):
    for i in range(n):
        ch = input("Nom = ")
        while not "A" <= ch[0] <= "Z":
            ch = input("Nom = ")
        
        x = int(input("X = "))
        y = int(input("Y = "))
        while not(10 <= x <= 9999 and 10 <= y <= 9999):
            x = int(input("X = "))
            y = int(input("Y = "))
            
        t[i] = ch + "@" + str(x) + "+" + str(y)
        
def remplir2(t, n):
    for i in range(n):
        t[i] = int(input("T2[" + str(i + 1) + "]= "))
        while not( t[i] > 0 ):
            t[i] = int(input("T2[" + str(i + 1) + "]= "))
            
N = saisir()
T1 = array([str] * N)
T2 = array([int] * N)
remplir1(T1, N)
remplir2(T2, N)