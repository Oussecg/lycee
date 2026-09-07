from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox
from math import*


def Play():
    x = f.comboBox.currentText()
    n = f.lineEdit.text()
    if n == "":
        QMessageBox.critical(f, "erreur", " saisir le valeur de epsilon")
    elif not(0.0000001 <= float(n) <= 0.01):
        QMessageBox.critical(f, "erreur", " saisir le nombre 0.000001<=n<=0.01")
    else:
        if x == "Méthode 1":
            QMessageBox.information(f, "info", "valeur de PI avec Method 1! ")
            f.resultLabel.setText(str(PI_Meth1(n)))
        else:
            QMessageBox.information(f, "info", "valeur de PI avec Method 2! ")
            f.resultLabel.setText(str(PI_Meth2(n)))


def PI_Meth1(n):
    n = float(n)
    i = 0
    k = 1
    p = 1
    pp = 0
    while not abs(p - pp) <= n:
        i = i + 1
        k = k + 2
        pp = p
        p = p + fact(i) / fact_imp(k)
    return p * 2


def fact(x):
    f = 1
    for i in range(2, x + 1):
        f = f * i
    return f


def fact_imp(x):
    f = 1
    for i in range(1, x + 1, 2):
        f = f * i
    return f


def PI_Meth2(n):
    n = float(n)
    i = 0
    k = 1
    p = 1
    pp = 0
    s = 1
    while not (abs(p - pp) <= n):
        s = -s
        i = i + 1
        k += 2
        pp = p
        p += s * (i / (k * (some(3, i))))
    return sqrt(12) * p


def some(x, i):
    s = 1
    for j in range(1, i + 1):
        s = s * x
    return s


def Supprrimer():
    pass


app = QApplication([])
f = loadUi("C:/lycee/TR3/Programation/Class/Pr4/InterfaceCalcul.ui")
f.show()
f.pushButton.clicked.connect(Play)
f.pushButton_2.clicked.connect(Supprrimer)

app.exec_()
