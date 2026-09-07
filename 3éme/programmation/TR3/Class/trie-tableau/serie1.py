from numpy import array

def saisir():
    x = int(input("Donner N: "))
    while not(2 <= x <= 100):
        x = int(input("Donner N: "))
    return x

def remplir1(t, n):
    for i in range(n):
        t[i] = input("M["+str(i+1)+"]= ")
        while not(len(t[i]) == 8 and t[i].isdecimal()):
            t[i] = input("M["+str(i+1)+"]= ")

def remplir2(t, n):
    for i in range(n):
        t[i] = int(input("S["+str(i+1)+"]= "))
        while not(20 <= t[i] <= 120):
            t[i] = int(input("S["+str(i+1)+"]= "))

def trier(t1, t2, n):
  for j in range(n, 0, -1):
      for i in range(j-1):
          if t2[i] > t2[i+1]:
              # p = t1[i]
              # t1[i] = t1[i+1]
              # t1[i+1] = p
              p = t2[i]
              t2[i] = t2[i+1]
              t2[i+1] = p
          print(t2)
  print(t2)

N = saisir()
M = array([str]*N)
S = array([int]*N)
# remplir1(M, N)
remplir2(S, N)
trier(M, S, N)
