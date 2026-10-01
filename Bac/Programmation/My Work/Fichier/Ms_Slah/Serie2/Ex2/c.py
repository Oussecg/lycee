from pathlib import Path

# Automatically gets the absolute path of the directory containing this script
folder_path = str(Path(__file__).resolve().parent)

F = open(folder_path + "/nbr.txt", "r")
s = 0
ch = F.readline()
while ch != "":
    s += int(ch)
    ch = F.readline()
F.close()

F = open(folder_path + "/nbr.txt", "a")
F.write(f"Somme= {s} \n")