from pickle import load

f = open("entier.dat", "rb")
fin = False
while (not fin):
    try:
        x = load(f)
        print(x)
    except:
        fin = True
f.close()