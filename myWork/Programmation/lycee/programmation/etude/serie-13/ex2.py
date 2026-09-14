from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox

def pushButton_click():
    ch = str(windows.inputN.text())

    if ch == "" :
        QMessageBox.critical(windows, "Attention !", ch + " Aucune nombre saisie !")
    elif int(ch) < 100:
        QMessageBox.critical(windows, "Attention !", "Veuillez saisir un entier >= 100")
    else:
        play(ch)

def play(ch: str):
    test = True
    i = 2
    while test and  i < len(ch):
        if int(ch[ : i]) % i == 0:
            i += 1
        else:
            test = False
            windows.resultat.setText(ch + " est un nombre non polynome")
    if test:
        windows.resultat.setText(ch + " est un nombre polynome")


def pushButton_2_click():
    windows.inputN.clear()
    windows.resultat.clear()

def pushButton_3_click():
    windows.close()

app = QApplication([])
windows = loadUi ("C:/Users/ousse/Documents/lycee/programmation/etude/serie-13/ex2.ui")
windows.show()
windows.pushButton.clicked.connect ( pushButton_click )
windows.pushButton_2.clicked.connect ( pushButton_2_click )
windows.pushButton_3.clicked.connect ( pushButton_3_click )

app.exec_()