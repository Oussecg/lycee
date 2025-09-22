from random import randint

x = randint(0, 9)
gagnant = False
essaie = 4

while not (essaie == 0 or gagnant == True):
    essaie -= 1
    u = int(input("Saisir un chiffre pour decouvrir le nombre secrée: "))
    while not (0 <= x <= 10):
        u = int(input("Retaper un chiffre pour decouvrir le nombre secrée: "))
    if x == u:
        print("bravo c'est gagnè")
        gagnant = True
    else:
        print("n'est pas un bon choix")
        
if not gagnant:
    print("")
    print("désolé tu as perdu")
    print("le nombre secret est", x)
