from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox

def pushButton_click():
    ch = windows.intInput.text()
    if len(ch) < 3 or ch.isdecimal() == False:
        QMessageBox.critial(windows, "Error", "Veuillez saisir un entier de 3 chiffres au moins")
    else:
        if windows.radioButton.isChecked():
            playRigo(ch)
        elif windows.radioButton_2.isChecked():
            playSuper(ch)
            
def est_premier(N):
    test = True
    i = 0
    while test and i < (N % 2) + 1 :
        if N % i == 0 :
            test = False
        else:
            i += 1
    return test

def playRigo(ch):
    N = int(ch)
def pushButton_2_click():
    pass
def pushButton_3_click():
    windows.close()
    
app = QApplication([])
windows = loadUi ("C:/Users/ousse/Documents/lycee/programmation/etude/serie-14/ex2.ui")
windows.show()
windows.pushButton.clicked.connect ( pushButton_click )
windows.pushButton_2.clicked.connect ( pushButton_2_click )
windows.pushButton_3.clicked.connect ( pushButton_3_click )

app.exec_()