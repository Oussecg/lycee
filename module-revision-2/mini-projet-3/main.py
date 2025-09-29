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

ch = saisir_texte()
print(supprimer_espace(ch))
