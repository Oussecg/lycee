from numpy import array

def saisir():
    n = int(input("Saisir nombre d'èléves: "))
    while not (1 <= n <= 30):
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

def remplir2(t, n, t1):
    for i in range(n):
        print(t1[i][t1[i].find("@") + 1 : ])
        t[i] = int(input("T2[" + str(i + 1) + "]= "))
        while not( t[i] > 0 ):
            t[i] = int(input("T2[" + str(i + 1) + "]= "))

def afficher(t1, t2, n):
    nb = 0
    print("Les èléves ayant la réponse correcte : ", end=" ")
    for i in range(n):
        p1 = t1[i].find("@")
        p2 = t1[i].find("+")
        ch = t1[i][ : p1]
        x1 = int(t1[i][p1 + 1 : p2])
        x2 = int(t1[i][p2+1 : ])
        if x1 + x2 == t2[i]:
            nb += 1
            print(ch, end="  ")
    print("")
    print("Pourcentage = " + str(round(nb / n * 100)) + "%")


N = saisir()
T1 = array([str] * N)
T2 = array([int] * N)
remplir1(T1, N)
remplir2(T2, N, T1)
afficher(T1, T2, N)
