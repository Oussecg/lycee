from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from numpy import array

def Verifier():
    M = windows.dataInputM.text()
    N = windows.dataInputN.text()
    msg = ""
    if M == "" and N == "":
        msg = "Veuillez saisir les deux valeurs de M et N"
    elif M ==  "":
        msg = "Veuillez saisir le valeur de M"
    elif N == "":
        msg = "Veuillez saisir le valeur de N"
    elif int(M) < 0 or int(N) < 0:
        msg = "Veuillez saisir 2 entiers > 0"
    elif not ( M.isdecimal() or N.isdecimal()):
        msg = "Veuillez saisir 2 entiers !"
    else:
        if is_successive(M, N):
            msg = M + " et " + N + " forment une succession parfaite"
        else:
            msg = M + " et " + N + " ne forment pas une succession parfaite"
    windows.resultLabel.setText(msg)

def is_successive(M, N):
    ch = M + N
    T = array([int] * len(ch))
    for i in range(len(ch)):
        T[i] = int(ch[i])
    test = True
    while test:
        test = False
        for i in range(len(ch)):
            if int(T[i]) < int(T[i]):
                aux = T[i]
                T[i] = T[i+1]
                T[i+1] = aux
                test = True
    test = True
    i = 0
    while test and i < len(ch) - 1:
        if T[i+1] - T[i] == 1 :
            i += 1
        else:
            test = False
    return test
    
    

def pushButton_2_click():
    pass

app = QApplication([])
windows = loadUi ("C:/Users/ousse/Documents/lycee/programmation/etude/serie-17/InterfaceSuccession.ui")
windows.show()
windows.pushButton.clicked.connect ( Verifier )
windows.pushButton_2.clicked.connect ( pushButton_2_click )

app.exec_()