from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox
from numpy import array


def Play():
    ch = windows.lineEdit.text()
    if ch == "":
        QMessageBox.critical(windows, "Attention", "Veuillez saisir une chaine !")
    elif ch.find("  ") != -1:
        QMessageBox.critical(windows, "Attention", "Entre 2 mots un seul espace est autorisé !")
    elif not(est_alpha(ch)):
        QMessageBox.critical(windows, "Attention", "Veuillez saisir une chaine en majuscule !")
    else:
        if windows.comboBox.currentText() == "Methode 1":
            m = 'm1'
        elif windows.comboBox.currentText() == "Methode 2":
            m = 'm2'
        else:
            m = 'm3'
        windows.resultLabel.setText(crypter(ch, m))
        QMessageBox.information(windows, "Validation", "Cryptage effectué avec la méthode (" + m + ")")


def est_alpha(ch):
    test = True
    i = 0
    while test and i < len(ch):
        if ch[i] != " ":
            if "A" <= ch[i] <= "Z":
                i += 1
            else:
                test = False
        else:
            i += 1
    return test


def crypter(ch, M):
    nbr = 1
    for i in range(len(ch)):
        if ch[i] == " ":
            nbr += 1
    Cryptage = dict(
        Mot=str,
        M1=str,
        M2=str,
        M3=str
    )
    T = array([Cryptage] * nbr)
    ch1 = ch

    for i in range(nbr):
        T[i] = dict()
        if ch1.find(" ") != -1:
            T[i]['Mot'] = ch1[: ch1.find(" ")]
            ch1 = ch1[ch1.find(" ") + 1:]
        else:
            T[i]['Mot'] = ch1
            ch1 = ""
        T[i]['M1'] = cryptage1(T[i]['Mot'], nbr)
        T[i]['M2'] = cryptage2(T[i]['Mot'])
        T[i]['M3'] = cryptage3(T[i]['Mot'])
    resultat = ""
    for i in range(nbr):
        resultat += " "
        if M == "m1":
            resultat += T[i]['M1']
        elif M == "m2":
            resultat += T[i]['M2']
        else:
            resultat += T[i]['M3']
    return resultat

def cryptage1(ch, nbr):
    ch1 = ""
    for i in range(len(ch)):
        if ord(ch[i]) + nbr <= 90:
            ch1 += chr(ord(ch[i]) + nbr)
        else:
            ch1 += chr(ord(ch[i]) + nbr - 26)
    return ch1


def cryptage2(ch):
    nbr = 0
    for i in range(len(ch)):
        if ch[i] in ["A", "E", "Y", "U", "I", "O"]:
            nbr += 1
    ch1 = ""
    for i in range(len(ch)):
        if ord(ch[i]) + nbr <= 90:
            ch1 += chr(ord(ch[i]) + nbr)
        else:
            ch1 += chr(ord(ch[i]) + nbr - 26)
    return ch1


def cryptage3(ch):
    ch1 = ""
    for i in range(len(ch)):
        ch1 = ch[i] + ch1
    return ch1


def Effacer():
    windows.lineEdit.clear()
    windows.resultLabel.clear()


app = QApplication([])
windows = loadUi("D:/lycee/TR3/Programation/Etude/serie-23/InterfaceCryptage.ui")
windows.show()
windows.crypterButton.clicked.connect(Play)
windows.reinstallerButton.clicked.connect(Effacer)

app.exec_()
