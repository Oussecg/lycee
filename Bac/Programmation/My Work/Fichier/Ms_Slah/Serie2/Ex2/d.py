from pathlib import Path

# Automatically gets the absolute path of the directory containing this script
folder_path = str(Path(__file__).resolve().parent)

F = open(folder_path + "/nbr.txt", "r")
nb = 0
ch = F.readline()
while ch != "":
    nb += 1
    ch = F.readline()
F.close()

p = int(input("P= "))
while not 1 <= p <= nb:
    p = int(input("P= "))
    
F = open(folder_path + "/nbr.txt", "r")
i = 0
ch = F.readline()
ch1 = ""
while ch != "" and i != p:
    i += 1
    ch1 += ch
    ch = F.readline()
F.close()

F = open(folder_path + "/nbr.txt", "w")
F.write(ch1)