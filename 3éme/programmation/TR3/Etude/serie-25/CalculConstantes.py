from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox


def Play():
    mth = ""
    p = 0
    if windows.checkBox_K.isChecked():
        p += 1
        mth = 'k'
    if windows.checkBox_S.isChecked():
        p += 1
        mth = 's'
    if windows.checkBox_PI.isChecked():
        mth = 'pi'
        p += 1

    if p != 1:
        if p == 0:
            QMessageBox.critical(windows, "Erreur", "Veuillez choisir le nom de la constante à calculer")
        else:
            QMessageBox.critical(windows, "Erreur", "Veuillez cocher une seule case !")
    else:
        QMessageBox.information(windows, "Validation", "Constante " + mth + " calculée")
        windows.resultLabel.setText(calculConstante(float(windows.comboBox.currentText()), mth))


def calculConstante(epsilon, mth):
    msg = ''
    if mth == 'k':
        msg = 'Constante ' + mth + ' = ' + str(Const_K(epsilon))
    elif mth == 's':
        msg = 'Constante ' + mth + ' = ' + str(Const_S(epsilon))
    else:
        msg = 'Constante ' + mth + ' = ' + str(Const_Pi(epsilon))
    return msg


def Const_K(epsilon):
    p = 1
    pp = 0
    i = 1
    while not(abs(p - pp) <= epsilon):
        i += 2
        pp = p
        p += 1 / fact(i)
    return p


def Const_S(epsilon):
    p = 1
    pp = 0
    i = 1
    while not(abs(p - pp) <= epsilon):
        i += 1
        pp = p
        if i % 2 == 0:
            p -= 1 / i
        else:
            p += 1 / i
    return p


def Const_Pi(epsilon):
    p = 1 / 3
    pp = 0
    i = 1
    j = 3
    while not(abs(p - pp) <= epsilon):
        i += 4
        j += 4
        pp = p
        p += 1 / (i * j)
    return p * 8


def fact(x):
    p = 1
    for i in range(1, x + 1):
        p *= i
    return p


def Effacer():
    windows.resultLabel.clear()


app = QApplication([])
windows = loadUi("D:/lycee/TR3/Programation/Etude/serie-25/InterfaceConstantes.ui")
windows.show()
windows.pushButton.clicked.connect(Play)
windows.pushButton_2.clicked.connect(Effacer)

app.exec_()
