from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox
from numpy import array


def crypterButt_click():
    mc = F.pushCl.text()
    ch = F.pushCrypt.text()
    if not (3 <= len(mc) <= 10 and est_cle(mc)):
        QMessageBox.critical(
            F, "Erreur", "Le mot de clé doit être formé uniquement de L lettres majuscules sans doublons et ne contient pas la lettre W avec 3 <= L <= 10")
    elif not verif(ch):
        QMessageBox.critical(F, "Erreur", "Le mot à crypter doit être formé uniquement de lettres majuscules")
    else:
        M = array([[''] * 5] * 5)
        i = 0
        j = 0
        N = 0
        while N < len(mc):
            if j > 4:
                j = 0
                i += 1
            M[i, j] = mc[N]
            N += 1
            j += 1

        ch1 = ""
        for k in range(65, 91):
            c = chr(k)
            if mc.find(c) == -1 and c != "W":
                ch1 += c

        ch1 = mc + ch1
        K = 0
        pV = ""
        for i in range(5):
            for j in range(5):
                M[i, j] = ch1[K]
                K += 1

        Ft = open("Mess_Crypte.txt", "w")
        ch2 = ""
        for k in range(len(ch)):
            for i in range(5):
                for j in range(5):
                    if M[i, j] == ch[k]:
                        ch2 += str(i + 1) + str(j + 1)
                    elif ch[k] == "W" and M[i, j] == "V":
                        ch2 += str(i + 1) + str(j + 1)
            if ch[k] == " ":
                ch2 += " "

        print(ch2)
        F.resultat.setText(ch2)
        Ft.write(ch2)


def est_cle(ch):
    test = True
    i = 0
    while test and i < len(ch):
        if "A" <= ch[i] <= "Z" and ch[i] != "W" and est_distinct(ch, i):
            i += 1
        else:
            test = False
    return test


def est_distinct(ch, i):
    test = True
    j = i - 1
    while test and j >= 0:
        if ch[i] == ch[j]:
            test = False
        else:
            j -= 1
    return test


def verif(ch):
    test = True
    i = 0
    while test and i < len(ch):
        if "A" <= ch[i] <= "Z" or ch[i] == " ":
            i += 1
        else:
            test = False
    return test


app = QApplication([])
F = loadUi("C:/lycee/Bac/Programmation/Etude/SdE/SdE5/Ex3/Interface.ui")
F.show()
F.crypterButt.clicked.connect(crypterButt_click)

app.exec_()
