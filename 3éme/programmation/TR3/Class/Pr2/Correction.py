from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from numpy import *

code = dict(nom=str,
            mp=str)
t = array([code] * 20)
# -----------------------------------------------------------------------


def alpha(ch):
    i = 0
    b = True
    while i < len(ch) and b:
        if "A" <= ch[i] <= "Z" or ch[i] == "#":
            i = i + 1
        else:
            b = False
    return b


def nbr_occ(m):
    c = m[0]
    nb = 0
    for i in range(len(m)):
        if c == m[i]:
            nb = nb + 1
    return nb


def Coder_mot(m):
    k = nbr_occ(m)
    mc = ""
    for i in range(len(m)):
        if ord(m[i]) + k <= ord("Z"):
            mc = mc + chr(ord(m[i]) + k)
        else:
            mc = mc + chr(ord(m[i]) + k - 26)
    return mc


def Play():
    ch = windows.a.text()
    if ch == "":
        QMessageBox.critical(windows, "Erreur !", "Veuillez saisir les noms !")
    elif alpha(ch) == False:
        QMessageBox.critical(windows, "Erreur !", "Veuillez saisir les noms en majuscule !")
    elif ch.find("##") != -1:
        QMessageBox.critical(windows, "Erreur !", "Entre 2 noms un seul # est permis !")
    else:
        nm = windows.d.text()
        if nm == "":
            QMessageBox.critical(windows, "Erreur !", "Aucun nom saisi !")
        else:
            QMessageBox.information(windows, "Résultat", Trouver(ch, nm))


def Trouver(ch, nm):
    ch = ch + "#"
    n = 0
    while ch != "":
        p = ch.find("#")
        m = ch[:p]
        t[n] = dict()
        t[n]["nom"] = m
        t[n]["mp"] = Coder_mot(m)
        ch = ch[p + 1:]
        n = n + 1
    p = 0
    while p < n and t[p]["nom"] != nm:
        p = p + 1
    if p == n:
        return "Nom incorrect !"
    else:
        return "le mot de passe de " + nm + " est " + t[p]["mp"]


def Supprimer():
    windows.a.clear()
    windows.d.clear()


# -----------------------------------------------------------------------
app = QApplication([])
windows = loadUi("InterfaceMotsPasse_Final.ui")
windows.show()
windows.e.clicked.connect(Play)
windows.f.clicked.connect(Supprimer)
app.exec()
