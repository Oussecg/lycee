def ppcm(a, b):
    ch = ""
    if b > a :
        aux = b
        b = a
        a = aux
    p = a
    while p % b != 0:
        p = p + a
        ch += str(p) + ","
    return ch[ : len(ch)-1 ]
print(ppcm(24, 111))