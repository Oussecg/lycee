def saisir():
    ch = input("Ch= ")
    return ch

def est_formule(ch: str):
    if (ch.find("+") != -1):
        return True
    return False

def calculer(ch: str):
    equation_list = []
    r = 0
    i = 0
    while i < len(ch):
        if ch[i] in math_operations:
            print(ch[:i], ch[i], ch[i + 1: ])
            equation_list.append(int(ch[:i]))
            equation_list.append(ch[i])
            if check_math(ch[i + 1: ]):
                equation_list.append(ch[i])
            else:
                ch = ch[i + 1: ]
            i = 0
            print(equation_list)
        i += 1
    return r

def check_math(ch):
    for c in ch:
        if c in math_operations:
            return False
    return True
math_operations = ["*", "+", "/", "-"]
ch = saisir()
calculer(ch)
