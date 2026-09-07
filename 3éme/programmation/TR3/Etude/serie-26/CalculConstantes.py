from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox


def Play():
    # déterminer la valeur de epsilon
    epsilon = windows.comboBox.currentText()
    # déterminer la valeur de x
    x = windows.lineEdit.text()
    # déterminer les valeurs de les constantes
    exp = windows.radio_expo.isChecked()
    s = windows.radio_s.isChecked()
    cos = windows.radio_cos.isChecked()

    if x == '':
        QMessageBox.critical(windows, 'Erreur', 'Veuillez saisir x !')
    elif not (exp or s or cos):
        QMessageBox.critical(windows, 'Erreur', 'Veuillez choisir le nom de la constante à calculer !')
    elif epsilon == "Choisir la précision":
        QMessageBox.critical(windows, 'Erreur', 'Veuillez choisir la valeur de epsilon !')
    else:
        x = float(x)
        epsilon = float(epsilon)
        if exp:
            QMessageBox.information(windows, 'Validation', 'Valeur de Exponentielle calculée')
            windows.resultLabel.setText(f'E({x}) = {Const_Exp(x, epsilon)}')
        elif s:
            QMessageBox.information(windows, 'Validation', 'Valeur de S calculée')
            windows.resultLabel.setText(f'S({x}) = {Const_S(x, epsilon)}')
        else:
            QMessageBox.information(windows, 'Validation', 'Valeur de Cosinus calculée')
            windows.resultLabel.setText(f'Cos({x}) = {Const_Cos(x, epsilon)}')


def fact(x):
    f = 1
    for i in range(2, x + 1):
        f *= i
    return f


def puissance(a, b):
    p = 1
    for i in range(b):
        p *= a
    return p


def Const_Exp(x, epsilon):
    e = 1 + x
    ep = 0
    i = 1
    while not(abs(e - ep) <= epsilon):
        i += 1
        ep = e
        e += puissance(x, i) / fact(i)
    return str(e)


def Const_S(x, epsilon):
    e = 1
    ep = 0
    i = 0
    while not(abs(e - ep) <= epsilon):
        i += 1
        ep = e
        if i % 2 == 0:
            e += 1 / puissance(x, i)
        else:
            e -= 1 / puissance(x, i)
    return str(e)


def Const_Cos(x, epsilon):
    e = 1
    ep = 0
    i = 0
    s = 1
    while not(abs(e - ep) <= epsilon):
        s = -s
        i += 2
        ep = e
        e += s * (puissance(x, i) / fact(i))
    return str(e)


def Effacer():
    windows.lineEdit.clear()
    windows.resultLabel.clear()


app = QApplication([])
windows = loadUi("C:/lycee/TR3/Programation/Etude/serie-26/InterfaceConstante.ui")
windows.show()
windows.pushButton.clicked.connect(Play)
windows.pushButton_2.clicked.connect(Effacer)

app.exec_()
