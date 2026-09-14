from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox

def play():
    ch = windows.lineEdit.text()
    if ch.isdecimal() == False:
        QMessageBox.critical(windows, "Désolé !", ch + "!Veuillez saisir un nombre !")
    elif int(ch) % 2 == 0 or int(ch) < 100:
        QMessageBox.critical(windows, "Désolé !", "Saisir un nombre impairs de 3 chiffres au moins!")
    else:
        m = ""
        if windows.comboBox.currentText() == "Premier Palindrome ?":
            if est_palindrome(ch):
                m = ch + " est un premier palindrome"
            else:
                m = ch + " n'est pas un premier palindrome"
        else:
            if est_harshad(ch):
                m = ch + " est harshad premier"
            else:
                m = ch + " n'est pas harshad premier"
        windows.resultLabel.setText(m)

def est_premier(ch):
    N = int(ch)
    test = True
    i = 2
    while test and i < N :
        if N % i == 0 :
            test = False
        else:
            i += 1
    return N

def est_symetrie(ch):
    ch1 = ""
    for i in range(len(ch)):
        ch1 = ch[i] + ch1
    return ch1 == ch
        
def est_palindrome(ch):
    s = 0
    N = int(ch)
    for i in range(1, (N%2)+1):
        if N % i == 0 :
            s += i
    return est_premier(s) and est_symetrie(ch)
            
def est_harshad(ch):
    N = int(ch)
    s = 0
    for i in range(len(ch)):
        s += int(ch[i])
    return N % s == 0 and est_premier(s)

def pushButton_2_click():
    windows.lineEdit.clear()
    windows.resultLabel.clear()

app = QApplication([])
windows = loadUi ("C:/Users/ousse/Documents/lycee/programmation/etude/serie-16/InterfaceArithmétique.ui")
windows.show()
windows.pushButton.clicked.connect ( play )
windows.pushButton_2.clicked.connect ( pushButton_2_click )

app.exec_()