from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox
from numpy import array


def Play():
    ch = windows.lineEdit.text()
    if ch == "":
        QMessageBox.critical(windows, 'Erreur de saisie !', 'Aucune chaine saisie !')
    elif est_minus(ch) == False:
        QMessageBox.critical(windows, 'Erreur de saisie !', 'Veuillez saisir une chaine en minuscule !')
    else:
        windows.resultLabel.setText(crypter(ch))


def crypter(ch):
    while ch.find("  ") != -1:
        m1 = ch[: ch.find("  ")]
        m2 = ch[ch.find("  ") + 1:]
        ch = m1 + m2
    nbr = 1
    for i in range(len(ch)):
        if ch[i] == " ":
            nbr += 1
    Cryptation = dict(
        Nom=str,
        Pass=str
    )
    T = array([Cryptation] * nbr)
    ch1 = ch
    for i in range(nbr):
        T[i] = dict()
        if ch1.find(" ") != -1:
            T[i]['Nom'] = ch1[: ch1.find(" ")]
            ch1 = ch1[ch1.find(" ") + 1:]
        else:
            T[i]['Nom'] = ch1
            ch1 = ""
        cc = ""
        # Chercher si l'ordre est pair ?
        if (i + 1) % 2 == 0:
            # Cryptage du mot dans l'ordre pair
            for j in range(len(T[i]['Nom'])):
                cc = T[i]['Nom'][j] + cc
        else:
            # Cryptage du mot dans l'ordre impair
            for j in range(len(T[i]['Nom'])):
                cc += chr(ord('z') - (ord(T[i]['Nom'][j]) - ord('a')))
        T[i]['Pass'] = cc
    ch1 = ""
    for i in range(nbr):
        ch1 += T[i]['Pass']
        ch1 += " "
    return ch1


def est_minus(ch):
    test = True
    i = 0
    while test and i < len(ch):
        if 'a' <= ch[i] <= 'z' or ch[i] == " ":
            i += 1
        else:
            test = False
    return test


app = QApplication([])
windows = loadUi("D:/lycee/TR3/Programation/Class/Pr3/InterfaceCryptage.ui")
windows.show()
windows.pushButton.clicked.connect(Play)

app.exec_()
