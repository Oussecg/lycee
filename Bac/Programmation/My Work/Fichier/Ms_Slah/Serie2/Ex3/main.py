from pathlib import Path

# Automatically gets the absolute path of the directory containing this script
folder_path = str(Path(__file__).resolve().parent)

def Max_Anciennete() -> int:   
    F = open(folder_path + "/ouvrier.txt", "r")
    ch = F.readline()
    m = int(ch[ch.find("#")+1 : ])
    while not (ch == ""):
        x = int(ch[ch.find("#")+1 : ])
        ch = F.readline()
        if m < x:
            m = x
    F.close()
    return m

def Afficher():
    F = open(folder_path + "/ouvrier.txt", "r")
    m = Max_Anciennete()
    ch = F.readline()
    while not (ch == ""):
        x = int(ch[ch.find("#")+1 : ])
        if x == m:
            nom = ch[ : ch.find("#")]
            print(nom)
        ch = F.readline()
    F.close()
        
Afficher()