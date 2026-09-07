from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox
from math import sqrt


def pushButton_click():
    N = int(windows.lineEdit.text())
    if N <= 0:
        QMessageBox.critical(windows, "Erreur de saisie", "Veuillez saisir un entier strictement supérieur à 0")
    else:
        if windows.comboBox.currentText() == "Methode 1":
            windows.resultLabel.setText(str(Methode1(N)))
        elif windows.comboBox.currentText() == "Methode 2":
            windows.resultLabel.setText(str(Methode2(N)))
        else:
            windows.resultLabel.setText(str(Methode3(N)))
            print('M3')


def Methode1(N):
    s = 1
    for i in range(2, N + 1):
        s += 1 / (i * i)
    return (sqrt(6 * s))


def Methode2(N):
    epsolon = 1 / N
    s = 1
    s1 = 0
    i = 1
    while not(abs(s - s1) <= epsolon):
        i += 1
        s1 = s
        s += 1 / (i * i)
    return sqrt(6 * s)


def Methode3(N):
    epsolon = 1 / N
    i = 1
    x = 2
    y = 1
    p = 1
    pp = 0
    while not(abs(p - pp) <= epsolon):
        print(i, f'{x}/{y}')
        if i % 2 == 0:
            x += 2

        else:
            y += 2
        pp = p
        p *= x / y
        i += 1
    return p


app = QApplication([])
windows = loadUi("D:/lycee/TR3/Programation/Class/Approximation/InterfaceApproximation.ui")
windows.show()
windows.pushButton.clicked.connect(pushButton_click)

app.exec_()
