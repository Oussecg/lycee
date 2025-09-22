from math import sqrt

N = 100
nb = 0
while nb < 6:  
    N += 1
    ch = str(N)
    p1 = int(ch[0])
    p2 = int(ch[1])
    p3 = int(ch[2])

    s = p1 + p3
    if sqrt(p2) == s:
        print(N, end=" ")
        nb += 1

