from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox

def Generer():
    ch = windows.lineEdit.text()
    if ch.isdecimal() == False or int(ch) < 100 :
        if ch.isdecimal() == False :
            QMessageBox.critical(windows, "Attention !", ch + " n'est pas un nombre !")
        else:
            QMessageBox.critical(windows, "Attention !", ch + " Veuillez introduire un entier >= 100")
    else:
        if different_zero(ch) and Distinct(ch) and Divisible(ch):
            windows.resultLabel.setText(ch + " est un nombre auto-divsible")
        else:
            windows.resultLabel.setText(ch + " n'est pas un nombre auto-divisible")

def different_zero(ch):
    test = True
    i = 0
    while test and i < len(ch):
        if int(ch[i]) == 0 :
            test = False
        else:
            i += 1
    return test

def Distinct(ch):
    test = True
    j = 0
    while test and j < len(ch):
        i = j
        while test and i < len(ch) - 1 :
            if ch[j] == ch[i + 1] :
   
windows = loadUi ("C:/Users/ousse/Documents/lycee/programmation/lycee/designer/project5.ui")
windows.show()
windows.verifierButton.clicked.connect ( Generer )
windows.autreButton.clicked.connect ( Supprimer )
windows.fermerButton.clicked.connect ( Quitter )

app.exec_()