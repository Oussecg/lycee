from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from numpy import array

def Play():
    ch = windows.dataInput.text()
    msg =  ""
    if ch ==  "" and len(ch) < 50 and "A" <= ch[0].upper() <= "Z" :
        msg = "Veuillez introduire un phrase"
    elif ch.find("  ") != -1 :
        msg = "Entre 2 mots un seul espace est autorisé"
    elif ch[len(ch) - 1] != ".":
        msg = "La chaine doit se terminer par un point"
    else:
        msg = Trier(ch)
    windows.resultLabel.setText(msg)
    
def Trier(ch):
    N = 1
    for i in range(len(ch)):
        if ch[i] == " ":
            N += 1
    T = array([str] * N)
    ch1 = ch
    for i in range(N):
        T[i] = ch1[ : ch1.find(" ")]
        ch1 = ch1[ch1.find(" ")+1 : ]
    test = True
    while test:
        test = False
        for i in range(N - 1, 0, -1):
            if len(T[i]) < len(T[i - 1]):
                aux = T[i]
                T[i] = T[i - 1]
                T[i - 1] = aux
                test = True
    r = ""
    for i in range(N):
        r += T[i] + " "
    return r

app = QApplication([])
windows = loadUi ("C:/Users/ousse/Documents/lycee/programmation/etude/serie-17/InterfaceTriage.ui")
windows.show()
windows.pushButton.clicked.connect ( Play )

app.exec_()