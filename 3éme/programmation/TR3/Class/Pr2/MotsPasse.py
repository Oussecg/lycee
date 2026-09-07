from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox
from numpy import array


def Play():
    ch = windows.sumNomInput.text()
    nom = windows.nomInput.text()
    if ch == "":
        QMessageBox.critical(windows, "Erreur !", "Veuillez saisir les noms !")
    elif nom == "":
        QMessageBox.critical(windows, "Erreur !", "Aucun nom saisi !")
    elif not (est_alpha(ch)):
        QMessageBox.critical(windows, "Erreur !", "Veuillez saisir les noms en majuscule !")
    elif ch.find(nom) == -1:
        QMessageBox.critical(windows, "Erreur !", "Nom incorrect !")
    elif ch.find("##") != -1:
        QMessageBox.critical(windows, "Erreur !", "Entre 2 noms un seul # est permis !")
    else:
        QMessageBox.information(windows, "Résultat !", Trouver(ch, nom))


def est_alpha(ch):
    ch1 = ""
    for i in range(len(ch)):
        if ch[i] != "#":
            ch1 += ch[i]
    test = True
    i = 0
    while test and i < len(ch1):
        if "A" <= ch1[i] <= "Z":
            i += 1
        else:
            test = False
    return test


def Trouver(ch, nom):
    nbr = nombre_mots(ch)
    T = array([Profile] * nbr)
    ch1 = ch
    for i in range(nbr):
        T[i] = dict()
        if ch1.find("#") != -1:
            T[i]['username'] = ch1[: ch1.find("#")]
            ch1 = ch1[ch1.find("#") + 1:]
        else:
            T[i]['username'] = ch1
            ch1 = ""
    for i in range(nbr):
        k = nombre_occurrence(T[i]['username'])
        ch1 = ""
        for j in range(len(T[i]['username'])):
            if ord(T[i]['username'][j]) + k <= 90:
                ch1 += chr(ord(T[i]['username'][j]) + k)
            else:
                f = (ord(T[i]['username'][j]) + k) - 90
                ch1 += chr(f + 65)
        T[i]['password'] = ch1
    i = 0
    while nom != T[i]["username"]:
        i += 1
    return f"{T[i]['username']} admet un mot de passe de {T[i]['password']}"


def nombre_mots(ch):
    nbr = 1
    for i in range(len(ch)):
        if ch[i] == "#":
            nbr += 1
    return nbr


def nombre_occurrence(ch):
    nbr = 0
    c = ch[0]
    for i in range(len(ch)):
        if ch[i] == c:
            nbr += 1
    return nbr


def effacer_click():
    windows.sumNomInput.clear()
    windows.nomInput.clear()


Profile = dict(
    username=str,
    password=str
)
app = QApplication([])
windows = loadUi("D:/lycee/TR3/Programation/Class/Pr2/InterfaceMotsPasse.ui")
windows.show()
windows.generer.clicked.connect(Play)
windows.effacer.clicked.connect(effacer_click)

app.exec_()
