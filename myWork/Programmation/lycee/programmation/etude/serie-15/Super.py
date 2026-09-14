from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def pushButton_click():
    ch = windows.lineEdit.text()
    msg = ""
    if ch == "" :
        m = "Aucun Nombre saisi !"
    elif not ch.isdecimal() :
        m = ch + " n'est pas un nombre !"
    elif int(ch) < 100 :
        m = "Saisir un nombre de 3 chiffres au moins !"
    else :
        if est_super_premier(ch):
            m = ch + " est super premier"
        else:
            m = ch + " n'est pas super premier"
    windows.resultLabel.setText(m)

def est_premier(N):
    test = True
    i = 2
    while test and i < (N//2)+1 :
        if N % i == 0 :
            test = False
        else :
            i += 1
    return test

def est_super_premier(ch):
    test = True
    i = 0
    while test and i != len(ch)-1 :
        if est_premier(int(ch[ : len(ch)-i-1])):
            i+= 1
        else :
            test = False
    return test

app = QApplication([])
windows = loadUi ("C:/Users/ousse/Documents/lycee/programmation/etude/serie-15/Super.ui")
windows.show()
windows.pushButton.clicked.connect ( pushButton_click )

app.exec_()