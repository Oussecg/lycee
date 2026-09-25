from pathlib import Path

# Automatically gets the absolute path of the directory containing this script
folder_path = str(Path(__file__).resolve().parent)

Fch = open(folder_path + "/info.txt", "r")
i = 0
ch = Fch.readline()
while ch != "":
    i += 1
    print(str(i) + ": " + ch)
    ch = Fch.readline()
    
Fch.close()