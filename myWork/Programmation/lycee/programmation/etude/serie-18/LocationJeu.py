from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox
from numpy import array

def pushButton_click():
    ch = windows.lineEdit.text()
    if ch.find("##") != -1 or ch[0] == "#" or ch[len(ch) - 1] == "#" or verifier1(ch):
        QMessageBox.critical(windows, "Invalide !", "Chaine non conforme")
    elif verifier2(ch) < 5:
        QMessageBox.critical(windows, "Invalide !", "Le nombre de participants doit etre 5 au moins")
    else:
        N = verifier2(ch)
        T = array([int] * N)
        ch1 = ch
        for i in range(N):
            if i == N:
                T[i] = Poid(ch1)
            else:
                T[i] = Poid(ch1[ : ch1.find("#")])
                ch1 = ch1[ch1.find("#") + 1 : ]
        
    
def verifier1(ch):
    ch1 = ch
    test = True
    while test and ch1 != "":
        if ch1.find("#") == -1 :
            test = est_majus(ch1)
            ch1 = ""
        elif est_majus(ch1[ : ch1.find("#")]):
            ch1 = ch1[ch1.find("#")+1 : ]
        else:
            test = False
    return test == False 

def est_majus(ch):
    test = True
    i = 0
    while test and i < len(ch) :
        if "A" <= ch[i] <= "Z" :
            i += 1
        else:
            test = False
    return test

def verifier2(ch):
    m = 1
    for i in range(len(ch)):
        if ch[i].find("#") != -1 :
            m += 1
    return m

def Poid(ch):
    ch1 = 0
    s = 0
    for i in range(len(ch)):
        if ch[i] in ["A", "E", "Y", "U", "I", "O"]:
            ch1 += ch(ord(ch[i]))
    for i in range(len(ch1)):
        s += int(ch1[i])
    return s

def trier(T, N):
    test = True
    while test:
        test = False
        for i in range(N-1):
            if T[i] < T[i+1]:
                aux = T[i]
                T[i] = T[i+1]
                T[i + 1] = aux
                test = True
    return test

app = QApplication([])
windows = loadUi ("C:/Users/ousse/Documents/lycee/programmation/etude/serie-18/InterfaceJeu.ui")
windows.show()
windows.pushButton.clicked.connect ( pushButton_click )

app.exec_()