from numpy import array

def saisir(x, y, ch):
    n = int(input(ch))
    while not(x <= n <= y):
        n = int(input(ch))
    return n
def Remplir(m,ne,nc):
    for i in range (ne):
        for j in range (nc):
            m[i,j]=float(input("["+str(i)+","+str(j)+"]"))
            while not 0<=m[i,j]<=20:
                 m[i,j]=float(input("["+str(i)+","+str(j)+"]"))
def affiche(m,ne,nc):
    for i in range (ne):
        for j in range (nc):
            print (m[i,j],end="  ")
        print()
    for j in range(nc):
        s=0
        for i in range(ne):
            s=s+m[i,j]
        so=s/ne
        print("moy gen de classe", j+1,"est",so)
    
    

nc = saisir(3, 10, "Nombre de colonne = ")
ne = saisir(4, 30, "Nombre de lignes = ")
m=array([[float]*nc]*ne)
Remplir(m,ne,nc)
affiche(m,ne,nc)