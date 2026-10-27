from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidgetItem
from pickle import load, dump
from numpy import array


def est_alphaNum(ch):
    test = True
    i = 0
    while test and i < len(ch):
        if "A" <= ch[i].upper() <= "Z" or "0" <= ch[i] <= "9":
            i += 1
        else:
            test = False
    return test


def Genre(gM, gF):
    rep = ""
    if gM:
        rep = "Masculin"
    elif gF:
        rep = "Féminin"
    return rep


def Etat(ett):
    rep = "Non Inscrit"
    if ett:
        rep = "Inscrit"
    return rep


def Cc(x):
    ch = str(x)
    while len(ch) != 1:
        s = 0
        for i in range(len(ch)):
            s += int(ch[i])
        ch = str(s)
    return ch


def ajouter_click():
    Id = F.Id.text()
    tel = F.Tel.text()
    gM = F.rM.isChecked()
    gF = F.rF.isChecked()
    vll = F.vll.currentText()
    ett = F.ett.isChecked()

    if Id == "" or tel == "" or (gM == False and gF == False):
        QMessageBox.critical(F, "Erreur", "Veuillez saisir toutes les informations")
    elif not (est_alphaNum(Id) and len(Id) < 10):
        QMessageBox.critical(F, "Erreur", "Identifiant invalide")
    elif not (len(tel) == 8 and tel.isdecimal):
        QMessageBox.critical(F, "Erreur", "N°Teléphone invalide")
    else:
        Fb = open("Clients.dat", "ab")

        Enr = {}
        Enr["Identifiant"] = Id
        Enr["NTel"] = tel
        Enr["Ville"] = vll
        Enr["Genre"] = Genre(gM, gF)
        Enr["Etat"] = Etat(ett)

        dump(Enr, Fb)
        Fb.close()


def afficherCl_click():
    Fb = open("Clients.dat", "rb")
    test = True
    i = 0
    while test:
        try:
            Enr = load(Fb)
            F.tW.insertRow(i)
            F.tW.setItem(i, 0, QTableWidgetItem(Enr["Identifiant"]))
            F.tW.setItem(i, 1, QTableWidgetItem(Enr["NTel"]))
            F.tW.setItem(i, 2, QTableWidgetItem(Enr["Genre"]))
            F.tW.setItem(i, 3, QTableWidgetItem(Enr["Ville"]))
            F.tW.setItem(i, 4, QTableWidgetItem(Enr["Etat"]))
            i += 1
        except:
            test = False
    Fb.close()


def afficherCh_click():
    Fb = open("Clients.dat", "rb")
    Ft = open("Chance.txt", "w")
    test = True
    while test:
        try:
            Enr = load(Fb)
            x = Cc(Enr["NTel"])
            F.listC.addItem(x)
            Ft.write(x + "\n")
        except:
            test = False
    Fb.close()
    Ft.close()


def afficherG_click():
    Fb = open("Clients.dat", "rb")
    test = True
    N = 0
    while test:
        try:
            Enr = load(Fb)
            N += 1
        except:
            test = False
    Fb.close()

    Fb = open("Clients.dat", "rb")
    T = array([{}] * N)
    for i in range(N):
        Enr = load(Fb)
        T[i] = Enr
    Fb.close()

    Fb = open("Clients.dat", "rb")
    test = True
    while test:
        test = False
        for i in range(N - 1):
            if Cc(T[i]["NTel"]) < Cc(T[i + 1]["NTel"]):
                aux = T[i]
                T[i] = T[i + 1]
                T[i + 1] = aux
                test = True
    Fb.close()

    Fb = open("Clients.dat", "wb")
    Ft = open("Chance.txt", "w")
    for i in range(N):
        F.listG.addItem(T[i]["Identifiant"])
        dump(T[i], Fb)
        Ft.write(str(Cc(T[i]["NTel"])) + "\n")
    Fb.close()
    Ft.close()


app = QApplication([])
F = loadUi("C:/lycee/Bac/Programmation/Etude/Tp1/Interface_Prototype.ui")
F.show()
F.ajouter.clicked.connect(ajouter_click)
F.afficherCl.clicked.connect(afficherCl_click)
F.afficherCh.clicked.connect(afficherCh_click)
F.afficherG.clicked.connect(afficherG_click)

app.exec_()
