from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox
from numpy import array

def appliquerButton_click():
    if windows.inputDataA.text().isdecimal() == False and int(windows.inputDataA) < 0:
        QMessageBox.critical(windows, "verification", "veuillez saisir deux entiers ")
    elif windows.inputDataB.text().isdecimal() == False and int(windows.inputDataB.text()) < 0:
        QMessageBox.critical(windows, "verification", "veuillez saisir deux entiers ")
    else :
        if windows.checkBox1.isChecked():
            a = int(windows.inputDataA.text())
            b = int(windows.inputDataB.text())
            windows.resultLabel.setText(str(produit1(a,b)))
        elif windows.checkBox2.isChecked():
            a = int(windows.inputDataA.text())
            b = int(windows.inputDataB.text())
            windows.resultLabel.setText(str(produit2(a,b)))


def produit1(a, b):
    s = 0
    for i in range(b):
        s += a
    return s

def produit2(a, b):
    N = Nombre_division(a)
    T1 = array([int] * N)
    T2 = array([int] * N)
    T1[0] = a
    T2[0] = b
    i = 0
    while T1[i] != 1:
        T1[i + 1] = T1[i] // 2
        T2[i + 1] = T2[i] * 2
        i += 1
    s = sommeTableau(T1, T2, N)
    print(T1)
    print(T2)
    return str(a) + " * " + str(b) + " = " + str(s)

def Nombre_division(a):
    n = 1
    while (a != 1):
        a = a // 2
        n += 1
    return n

def sommeTableau(T1, T2, N):
    s = 0
    for i in range(N):
        if T1[i] % 2 == 1 :
            s += T2[i]
    return s

def arreterButton_click():
    windows.close()

app = QApplication([])
windows = loadUi ("C:/Users/ousse/Documents/lycee/programmation/lycee/designer/project4.ui")
windows.show()
windows.appliquerButton.clicked.connect ( appliquerButton_click )
windows.arreterButton.clicked.connect ( arreterButton_click )

app.exec_()