from math import sqrt

for N in range(100, 1000):

    ch = str(N)
    p1 = int(ch[0])
    p2 = int(ch[1])
    p3 = int(ch[2])

    s = p1 + p3
    if sqrt(p2) == s:
        print(N, end=" ")
