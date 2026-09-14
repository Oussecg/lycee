from numpy import array

n = 6
T = array([int]*n)
for i in range(n):
    T[i] = int(input(f"T[{i+1}]= "))
    while T[i] <= 0 :
        T[i] = int(input(f"T[{i+1}]= "))
for i in range(0, n-1):
    pmax = i
    for j in range(i+1, n):
        if T[j] > T[pmax]:
            pmax = j
    if i != pmax:
        aux = T[i]
        T[i] = T[pmax]
        T[pmax] = aux
print(T)