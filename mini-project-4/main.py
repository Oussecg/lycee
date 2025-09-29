def saisir():
    ch = input("Ch= ")
    while not est_formule(ch):
        ch = input("Ch= ")
    return ch

def est_formule(ch: str):
    if (ch.find("+") != -1):
        return True
    return False

def calculer(ch: str):
    math_operations = ["*", "+", "/", "-"]
    r = 0
    i = 0
    while i < len(ch):
        if ch[i] in math_operations:
            if ch[i] == "+":
                r += int(ch[: i])
                ch = ch[i + 1: ]
                i = 0
        elif (ch[i] in math_operations) == False and i + 1 == len(ch) :
            r += int(ch)
        print(f"Ch = {ch} and ch[{i}] = {ch[i]} and r = {r}")
        i += 1
    return r

ch = saisir()
calculer(ch)
