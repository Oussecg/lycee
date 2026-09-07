from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from numpy import array


def Play():
    input = windows.lineEdit.text()
    msg = ""
    if input == "":
        msg = "Veuillez introduire une phrase"
    elif len(input) > 50:
        msg = "La chaine doit être inférieur à 50"
    elif not("A" <= input[0].upper() <= "Z"):
        msg = "La chaine doit se début par une lettre"
    elif input.find("  ") != -1:
        msg = "Entre 2 mots un seul espace est autorisé"
    elif input[len(input) - 1] != ".":
        msg = "La chaine doit se terminer par un point"
    else:
        msg = Trier(input)
    windows.resultLabel.setText(msg)


def Trier(ch):
    nbr = 1
    ch1 = ch
    while ch1 != "" and ch1.find(" ") != -1:
        ch1 = ch1[ch1.find(" ") + 1:]
        nbr += 1
    ch1 = ch
    T = array([str] * nbr)
    for i in range(nbr):
        if ch1.find(" ") != -1:
            T[i] = ch1[: ch1.find(" ")]
            ch1 = ch1[ch1.find(" ") + 1:]
        else:
            ch1 = ch1[: len(ch1) - 1]
            T[i] = ch1
    print(T)
    test = True
    while test:
        test = False
        for i in range(nbr - 1):
            if len(T[i]) > len(T[i + 1]):
                aux = T[i]
                T[i] = T[i + 1]
                T[i + 1] = aux
                test = True
    print(T)
    r = ""
    for i in range(nbr):
        r += ""
        r += T[i]
    return r


app = QApplication([])
windows = loadUi("D:/lycee/Programation/TR3/CLASS/Pr1/InterfaceTriage.ui")
windows.show()
windows.pushButton.clicked.connect(Play)

app.exec_()
