from pathlib import Path

# Automatically gets the absolute path of the directory containing this script
folder_path = str(Path(__file__).resolve().parent)

Ft = open(folder_path + "/pers.txt", "r")
nb = 0
ch = Ft.readline()
while ch != "":
    nb += 1
    ch = Ft.readline()
print("Nb= " + str(nb))

Ft.close()