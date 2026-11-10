from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMessageBox
from pickle import dump, load


def ajout():
    pN = F.pN.text()
    pC = F.pC.text()
    pT = F.pT.currentText()
    if pN == "" or pC == "":
        QMessageBox.critical(F, "Erreur", "Veuillez saisir toutes les informations")
    elif not ("A" <= pN[0] <= "Z" and len(pN) <= 10 and est_alpha(pN)):
        QMessageBox.critical(F, "Erreur", "Nom du produit invalide")
    elif not (len(pC) == 13 and pC.isdecimal()):
        QMessageBox.critical(F, "Erreur", "Code-Barres invalide")
    elif pT == "":
        QMessageBox.critical(F, "Erreur", "Choisir le type du produit")
    else:
        Fb = open("cosmo.dat", "ab")
        Prod = dict(
            pN=pN,
            pC=pC,
            pT=pT
        )
        dump(Prod, Fb)
        Fb.close()
        affiche()
        QMessageBox.information(F, "Confirmation", "Produit est enregistré avec succés")


def est_alpha(ch):
    test = True
    i = 0
    while test and i < len(ch):
        if "A" <= ch[i].upper() <= "Z":
            i = i + 1
        else:
            test = False
    return test


def affiche():
    F.tW.setRowCount(0)
    Fb = open("cosmo.dat", "rb")
    i = 0
    test = True
    while test:
        try:
            Prod = load(Fb)
            F.tW.insertRow(i)
            F.tW.setItem(i, 0, QTableWidgetItem(Prod["pN"]))
            F.tW.setItem(i, 1, QTableWidgetItem(Prod["pC"]))
            F.tW.setItem(i, 2, QTableWidgetItem(Prod["pT"]))
            i = i + 1
        except:
            test = False
    Fb.close()


def recommance():
    F.pN.clear()
    F.pC.clear()


def quitter():
    F.close()


def verifier():
    Fb = open("cosmo.dat", "rb")
    F.lW.clear()
    F.lW.addItem("Liste des produits authentiques:")
    i = 0
    test = True
    while test:
        try:
            Prod = load(Fb)
            pN = Prod["pN"]
            pC = Prod["pC"]
            pT = Prod["pT"]
            if est_barre(pC):
                F.lW.addItem(pN + "--" + pT)
            i = i + 1
        except:
            test = False
    Fb.close()


def est_barre(x):
    ch = str(x)
    s1 = 0
    s2 = 0
    for i in range(len(ch)):
        if i != len(ch) - 1:
            if i % 2 == 0:
                s2 = s2 + int(ch[i])
            else:
                s1 = s1 + int(ch[i])
    s1 = s1 * 3
    ch1 = str(s1 + s2)
    n = 10 - int(ch1[1:2])
    return ch[len(ch) - 1] == str(n)


app = QApplication([])
F = loadUi("C:/lycee/Bac/Programmation/Etude/Dc/D1/produit.ui")
F.show()
F.aJ.clicked.connect(ajout)
F.aF.clicked.connect(affiche)
F.rE.clicked.connect(recommance)
F.qI.clicked.connect(quitter)
F.vE.clicked.connect(verifier)

app.exec_()
