F = open("FTexte.txt", "r")
ch = F.readline()
while not (ch == ""):
    ch = ch[ : len(ch)-1]
    print(ch)
    ch = F.readline()
F.close()