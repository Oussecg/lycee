from numpy import array
from pickle import dump, load
from random import randint
from pathlib import Path
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *


def Quitter_click():
    F.close()


def Aff_click():
    Ft = open(folder_path + "/Nombres.txt", "r")
    ch = Ft.read()
    F.Nbr.addItem(ch)


def nbr_element() -> int:
    Ft = open(folder_path + "/Nombres.txt", "r")
    nbr = -1
    ch = Ft.readline()
    while not ch == "":
        nbr += 1
        ch = Ft.readline()
    Ft.close()
    return nbr


def Ver_click():
    clearTable()
    Nbr = nbr_element()
    generer(Nbr)

    Fb = open(folder_path + "/Nombres.dat", "rb")
    for i in range(Nbr):
        En = load(Fb)

        F.Tw.insertRow(i)
        F.Tw.setItem(i, 0, QTableWidgetItem(str(En["Nbr"])))
        F.Tw.setItem(i, 1, QTableWidgetItem(En["Msg"]))

def clearTable():
    F.Tw.clear()
    F.Tw.setRowCount(0)
    
def generer(Nbr):
    Ft = open(folder_path + "/Nombres.txt", "r")
    Fb = open(folder_path + "/Nombres.dat", "wb")

    nb = 0
    msg = ""
    for i in range(Nbr):
        En = {}
        ch = Ft.readline()
        ch = ch[: len(ch) - 1]
        En["Nbr"] = int(ch)

        if F.cB.currentText() == "Polydivisible":
            x = est_Poly(ch)
            En["Msg"] = x
            msg = "Polydivisble(s)"
            if x == "est polynôme":
                nb += 1
        else:
            x = est_Nar(ch)
            En["Msg"] = x
            msg = "Narcissique(s)"
            if x == "est narcissique":
                nb += 1
        dump(En, Fb)

    QMessageBox.information(F, "Nbr", f"{nb} Nombre(s) {msg} trouvé(s)")

    Ft.close()
    Fb.close()


def est_Poly(ch: str) -> str:
    test = True
    i = 2
    while test == True and i < len(ch):
        if int(ch[: i]) % i == 0:
            i += 1
        else:
            test = False
    Rep = "est polynôme"
    if not test:
        Rep = "n'est pas polynôme"
    return Rep


def est_Nar(ch: str) -> str:
    k = len(ch)
    s = 0
    for i in range(k):
        s += puiss(int(ch[i]), k)
    Rep = "n'est pas narcissique"
    if s == int(ch):
        Rep = "est narcissique"
    return Rep


def puiss(x1, x2):
    s = 1
    for i in range(x2):
        s = s * x1
    return s


app = QApplication([])
F = loadUi("C:/lycee/Bac/Programmation/tr1/Fichier/Projet6/Interface_Matrice.ui")
F.show()
F.Quitter.clicked.connect(Quitter_click)
F.Aff.clicked.connect(Aff_click)
F.Ver.clicked.connect(Ver_click)
folder_path = str(Path(__file__).resolve().parent)

app.exec_()
