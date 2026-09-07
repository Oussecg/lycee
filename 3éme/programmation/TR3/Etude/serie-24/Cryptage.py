from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox
from numpy import array


def Play():
    ch = windows.lineEdit.text()
    if ch == "":
        QMessageBox.critical(windows, "Attention", "Veuillez saisir une chaine !")
    elif est_alpha(ch) == False:
        QMessageBox.critical(windows, "Attention", "Veuillez saisir une chaine en majuscule !")
    elif ch.find("  ") != -1:
        QMessageBox.critical(windows, "Attention", "Entre 2 mots un seul espace est autorisé !")
    else:
        QMessageBox.information(windows, "Validation", Cryptage(ch, windows.comboBox.currentText()))


def est_alpha(ch):
    test = True
    i = 0
    while test and i < len(ch):
        if 'A' <= ch[i] <= 'Z' or ch[i] == " ":
            i += 1
        else:
            test = False
    return test


def Cryptage(ch, meth):
    nbr = 1
    for i in range(len(ch)):
        if ch[i] == " ":
            nbr += 1
    Crypt = dict(
        Mot=str,
        M1=str,
        M2=str
    )
    T = array([Crypt] * nbr)
    ch1 = ch
    for i in range(nbr):
        T[i] = dict()
        if ch1.find(" ") == -1:
            T[i]['Mot'] = ch1
            ch1 = ""
        else:
            T[i]['Mot'] = ch1[: ch1.find(" ")]
            ch1 = ch1[ch1.find(" ") + 1:]
    for i in range(nbr):
        T[i]['M1'] = cryptage1(T[i]['Mot'])
        T[i]['M2'] = cryptage2(T[i]['Mot'])
    msg = ""
    cc = ""
    if meth == "Méthode 1":
        msg = "Cryptage effectué avec la Méthode 1"
        for i in range(nbr):
            cc += T[i]['M1']
            cc += "#"
    else:
        msg = "Cryptage effectué avec la Méthode 2"
        for i in range(nbr):
            cc += T[i]['M2']
            cc += "#"
    cc = cc[: len(cc) - 1]
    windows.resultLabel.setText(cc)


def cryptage1(ch):
    ch1 = ""
    for i in range(len(ch)):
        ch1 = ch[i] + ch1
    cc = ""
    p = 0
    for i in range(len(ch1)):
        if ch1[i] in ['A', 'E', 'Y', 'U', 'I', 'O']:
            p += i
    for i in range(len(ch1)):
        if ord(ch1[i]) + p > 90:
            cc += chr(ord(ch1[i]) + p - 26)
        else:
            cc += chr(ord(ch1[i]) + p)
    return cc


def cryptage2(ch):
    ch1 = ""
    for i in range(len(ch)):
        ch1 = ch[i] + ch1
    cc = ""
    p = 0
    for i in range(len(ch)):
        if ch1[i] in ['A', 'E', 'Y', 'U', 'I', 'O']:
            p += ord(ch1[i]) - 64
    for i in range(len(ch1)):
        if ord(ch1[i]) + p > 90:
            cc += chr(ord(ch1[i]) + p - 26)
        else:
            cc += chr(ord(ch1[i]) + p)
    return cc


def Effacer():
    windows.lineEdit.clear()
    windows.resultLabel.clear()


app = QApplication([])
windows = loadUi("D:/lycee/TR3/Programation/Etude/serie-24/InterfaceCryptage.ui")
windows.show()
windows.pushButton.clicked.connect(Play)
windows.pushButton_2.clicked.connect(Effacer)

app.exec_()
