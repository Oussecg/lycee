from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox

def pushButton_click():
    N = int(windows.intInput.text())
    if N < 20 or str(N).isdecimal() == False or str(N) == "":
        QMessageBox.critical(windows, "Error", "Saisir un nombre positif")
    else:
        if windows.comboBox.currentText() == "Nombre Fort ?":
            playFort(N)
        else:
            playNarc(N)

def est_premier(N):
    test = True
    i = 2
    while test and i < (N // 2) + 1:
        if N % i == 0 :
            test = False
        else:
            i += 1
    return test

def puissance(a, b):
    p = 1
    for i in range(b):
        p *= a
    return p

def playFort(N):
    ch = str(N)
    s = 0
    l = len(ch)
    m = ""
    for i in range(l):
        s += sommeFacteurs(int(ch[i]))
    if s == N:
        m = " est un nombre fort"
    else:
        m = " n'est pas un nombre fort"
    windows.resultLabel.setText(ch + m)


def sommeFacteurs(N):
    s = 1
    for i in range(1, N + 1):
        s *= i
    return s


def playNarc(N):
    ch = str(N)
    s = 0
    m = ""
    for i in range(len(ch)):
        s += puissance(int(ch[i]), len(ch))
    if s == N:
        m = " est un nombre Narcissique"
    else:
        m = " n'est pas un nombre Narcissique"
    windows.resultLabel.setText(ch + m)
def pushButton_2_click():
    windows.intInput.clear()
    windows.resultLabel.clear()

app = QApplication([])
windows = loadUi ("C:/Users/ousse/Documents/lycee/programmation/etude/serie-14/ex1.ui")
windows.show()
windows.pushButton.clicked.connect ( pushButton_click )
windows.pushButton_2.clicked.connect ( pushButton_2_click )

app.exec_()