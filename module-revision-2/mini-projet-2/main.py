def saisir_chaine():
    ch = input("Saisir une chaine: ")
    while not ("A" <= ch[0] <= "Z" and ch.find(" ") == -1):
        ch = input("Retaper une chaine ne contient pas un espace et debut pas une lettre majuscule: ")
    return ch

def lower(c):
    return chr(ord(c) + 32)
    
def transformation(ch):
    ch1 = ""
    for i in range(len(ch)):
        if "A" <= ch[i] <= "Z":
            ch1 += lower(ch[i])
        elif "a" <= ch[i] <= "z":
            ch1 += ch[i].upper()
    return ch1

ch = saisir_chaine()
print(transformation(ch))