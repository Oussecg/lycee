from pathlib import Path

# Automatically gets the absolute path of the directory containing this script
folder_path = str(Path(__file__).resolve().parent)

Ft = open(folder_path + "/noms.txt", "r")

ch: str = Ft.read()
Ft.close()

nb = 0
for i in range(len(ch)):
    if ch[i].upper() in ["A", "E", "Y", "U", "I", "O"]:
        nb += 1
print("Nombre de Voyelle dans le fichier noms.txt est égale à " + str(nb))