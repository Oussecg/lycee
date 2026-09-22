from pickle import dump


f = open("entier.dat", "wb")
nb = 0
s = 0
test = True
while test:
    x = int(input("x= "))
    while (not(x >= 0)):
        x = int(input("x= "))
    nb += 1
    s += x
    dump(x, f)
    if nb > 10 or s > 1000:
        test = False
f.close()
            

