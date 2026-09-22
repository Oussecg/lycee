from pickle import dump, load
from numpy import array

message = open("message.txt", "r")
validate = open("validate.dat", "wb")


Enregistrement = dict(
    code = str,
    nbr = int
)

T = array([Enregistrement] * 100)

length = 0
k = 0  
for ligne in message:
    ch = ligne.strip()
    c = "1"
    cp = ""
    i = 0
    while (ch.find(c) != -1):
        cp = c
        c += "1"
        i += 1
    if i >= 3:
        length += 1
        T[k] = dict(
            code = cp,
            nbr = i
        )
        T[k]["code"] = ch
        T[k]["nbr"] = i
        dump(T[k], validate)
        k += 1
    
message.close()
validate.close()

test = True
while test:
    test = False
    for i in range(length-1):
        if T[i]["nbr"] < T[i+1]["nbr"]:
            aux = T[i]
            T[i] = T[i+1]
            T[i+1] = aux
            test = True
            
print("Les Messages valides classés sont: ")
for i in range(length):
    print(T[i]["code"])
        
        