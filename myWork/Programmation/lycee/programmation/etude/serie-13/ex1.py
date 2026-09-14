from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox

def pushButton_click():
    ch = str(windows.inputN.text())

    if ch.isdecimal() == False :
        QMessageBox.critical(windows, "Attention !", ch + " n'est pas un nombre")
    elif int(ch) < 10:
        QMessageBox.critical(windows, "Attention !", "Veuillez saisir un entier >= 10")
    else:
        play(ch)

def play(ch: str):
    r:str = ""
    if windows.comboBox.currentText() == "Nombre Magnifique ?":
        if est_magnifique(ch):
            r = ch + " est un nombre magnifique"
        else:
            r = ch + " n'est pas un nombre magnifique"

    elif windows.comboBox.currentText() == "Nombre Puissant ?":
        if est_puissant(ch):
            r = ch + " est un nombre puissant"
        else:
            r = ch + " n'est pas un nombre puissant"
    elif windows.comboBox.currentText() == "Nombre Extra ?":
        if est_extra(ch):
            r = ch + " est un nombre extra"
        else:
            r = ch + " n'est pas un nombre extra"
    windows.resultat.setText(r)

def est_magnifique(ch: str):
    N1 = int(ch)
    N2 = int(mirroir(ch))
    print(N1, N2)
    return (est_premier(N1) and est_premier(N2))

def mirroir(ch:str):
    ch1 = ""
    for i in range(len(ch)):
        ch1 = ch[i] + ch1
    return ch1

def est_premier(N:int):
    test = True
    i = 2
    while test and i<(N//2+1):
        if N % i != 0 :
            i += 1
        else:
            test = False
    return test

def est_puissant(ch: str):
    s1 = 0
    s2 = 0
    for i in range(len(ch)):
        if i % 2 == 0:
            s1 += puiss(int(ch[i]), i)
        else:
            s2 += puiss(int(ch[i]), i)
    return s1 == s2

def puiss(x1, x2):
    p = 1
    for i in range(x2):
        p *= x1
    return p

def est_extra(ch: str):
    N = int(ch)
    test = True
    i = 0
    while test and i < len(ch) :
        if N % int(ch[i]) == 0 :
            i += 1
        else :
            test = False
    return test


def pushButton_2_click():
    windows.inputN.clear()
    windows.resultat.clear()

app = QApplication([])
windows = loadUi ("C:/Users/ousse/Documents/lycee/programmation/etude/serie-13/ex1.ui")
windows.show()
windows.pushButton.clicked.connect ( pushButton_click )
windows.pushButton_2.clicked.connect ( pushButton_2_click )

app.exec_()