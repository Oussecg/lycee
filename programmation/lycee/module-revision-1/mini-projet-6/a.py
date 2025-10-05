from random import randint

x = randint(0, 9)
u = int(input("Saisir un chiffre pour decouvrir le nombre secrée: "))
while not (0 <= x <= 10):
    u = int(input("Retaper un chiffre pour decouvrir le nombre secrée: "))
if x == u:
    print("bravo c'est gagnè")
else:
    print("désolé c'est perdu")
    print("le nombre secret est", x)