def saisir_texte():
    ch = input("Saisir un texte: ")
    while not "A" <= ch[0].upper() <= "Z":
        ch = input("Retaper un texte: ")
    return ch

def supprimer_espace(ch: str):
    if (ch.find(" ") != -1):
        ch1 = ""
        i = 0
        while i < len(ch):
            if not(ch[i - 1] == " " and ch[i] == " "):
                ch1 += ch[i]
            i += 1
    else:
        ch1 = ch
    return ch1

def calculer_montant(ch: str):
    nb = 0
    for c in ch:
        if c == " ":
            nb += 1
    return nb * 0.75

ch = saisir_texte()
ch = supprimer_espace(ch)
ct = calculer_montant(ch)
print(f"Le coût de {ch} est {ct}")
