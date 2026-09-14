def pgcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

print(pgcd(24, 6))