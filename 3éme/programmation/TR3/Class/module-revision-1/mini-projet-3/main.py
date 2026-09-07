from math import sqrt

N = int(input("Saisir un entier: "))
while not(100 <= N <= 999):
    N = int(input("Retaper un entier: "))

ch = str(N)
p1 = int(ch[0])
p2 = int(ch[1])
p3 = int(ch[2])

s = p1 + p3
if sqrt(p2) == s:
    print(N, "est extra_racine")
else:
    print(N, "n'est pas extra_racine")