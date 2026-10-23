from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication


def Quitter_click():
    pass


def Aff_click():
    pass


def Ver_click():
    pass


app = QApplication([])
windows = loadUi("C:/lycee/Bac/Programmation/tr1/Fichier/Projet6/Interface_Matrice.ui")
windows.show()
windows.Quitter.clicked.connect(Quitter_click)
windows.Aff.clicked.connect(Aff_click)
windows.Ver.clicked.connect(Ver_click)

app.exec_()
