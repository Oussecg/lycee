from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from numpy import array
from random import randint


def Autre_click():
    pass
            
def AvantTri():
    Ft = open("texte.txt", "w")
    L = int(F.L.text())
    C = int(F.C.text())
    M = array([[int]*C]*L)
    ch = ""
    for i in range(L):
        for j in range(C):
            M[i, j] = randint(10, 99)
            ch += str(M[i, j]) + ", "
        ch += "\n"
    Ft.write(ch)
    F.Avt.addItem(ch)

def ApresTri():
    pass

def Quitter_click():
    pass


app = QApplication([])
F = loadUi("C:/lycee/Bac/Programmation/tr1/Fichier/Projet5/Interface_Matrice.ui")
F.show()
F.vT.clicked.connect(AvantTri)
F.pT.clicked.connect(ApresTri)
F.Autre.clicked.connect(Autre_click)
F.Quitter.clicked.connect(Quitter_click)

app.exec_()
