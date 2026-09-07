def saisir_chaine():
    ch = input("Saisir une chaine: ")
    while len(ch) > 15 or est_alpha(ch) == False:
        ch = input("Retaper une chaine: ")
    return ch

def saisir_caractere():
    c = input("Saisir un caractére: ")
    while not(len(c) == 1 and "A" <= c.upper() <= "Z"):
        c = input("Retaper un caractére: ")
    return c

def est_alpha(ch):
    i = 0
    test = True
    while i < len(ch) and test == True:
        if "A" <= ch[i].upper() <= "Z":
            i += 1
        else:
            test = False
    return test

def num_acurrence(c, ch):
    n = 0
    for i in range(len(ch)):
        if c.upper() == ch[i].upper():
            n += 1
    return n
    
ch = saisir_chaine()
c = saisir_caractere()
print("Le nombre d'accurence de", c, "dans", ch, "=", num_acurrence(c, ch))

