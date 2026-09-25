from pathlib import Path

# Automatically gets the absolute path of the directory containing this script
folder_path = str(Path(__file__).resolve().parent)

Fc = open(folder_path + "/rapport.txt", "w")
ch = input("Ch= ")
while ch[len(ch) - 1] != "." :
    ch = input("Ch= ")
Fc.write(ch + "\n")

Fc.close()