from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox

def factButton_click():
    if int(windows.inputData.text()) <= 1:
        QMessageBox.critical(windows, "Attention !", windows.inputData.text() + " : nombre non valable")
    else:
        windows.resultLabel.setText(factPremier(windows.inputData.text()))

def factPremier(ch):
    N = int(ch)
    ch1 = ""
    i = 2
    while N != 1 :
        if N % i == 0:
            N = N // i
            ch1 += str(i) + "*"
        else:
            i += 1
    print(ch1)
    return (ch1[ : len(ch1) - 1])

def arreterButton_click():
    windows.close()

app = QApplication([])
windows = loadUi ("C:/Users/ousse/Documents/lycee/programmation/lycee/designer/project3.ui")
windows.show()
windows.factButton.clicked.connect ( factButton_click )
windows.arreterButton.clicked.connect ( arreterButton_click )

app.exec_()