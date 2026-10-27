from pathlib import Path

def saisir(a: int, b:int) -> int:
    x = int(input("N= "))
    while not a <= x <= b:
        x = int(input("N= "))
    return x

def remplir(N: int):
    F = open(folder_path + "/Nombres.txt", "w")
    
    for i in range(N):
        x = int(input(f"N{i+1}= "))
        while x <= 0:
            x = int(input(f"N{i+1}= "))
        F.write(str(x) + "\n")
    
    F.close()

folder_path = str(Path(__file__).resolve().parent)
N = saisir(2, 9)
remplir(N)