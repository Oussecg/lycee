from numpy import *
from random import *

N = 3
M=array([[int]*N]*N)

def Remplir(m,n):
    print("M=")
    for i in range (0,n):
        for j in range (0,n):
            m[i,j]=randint(10,99)
            print(m[i, j], end=" ")
        print()
            
        

def Somme(m,n):
    print("")
    s1=0
    s2=0
    for i in range(0,N):
        s1=s1+m[i,i]
        s2=s2+m[i,n-1-i]
    print(s1, s2)
            
        



Remplir(M, N)
Somme(M,N)