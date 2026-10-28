from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidgetItem
from random import randint
from numpy import array


def valide():
    global N, M, test
    
    test = False
    N = F.pushN.text()
    if N == "":
        QMessageBox.critical(F, "Erreur 1", "Taper une valuer")
    elif not N.isdecimal():
        QMessageBox.critical(F, "Erreur 2", "Taper une entier")
    elif not 5 <= int(N) <= 12:
        QMessageBox.critical(F, "Erreur 3", "Taper un entier compris entre 5 et 12")
    else:
        test = True
        N = int(N)
        M = array([[int]*N]*N)
        for L in range(N-1):
            s = 0
            for C in range(N-L):
                if L == 0:
                    M[L, C] = randint(0, 9)
                elif L > 0 and C > 0:
                    M[L, C] = M[L, C-1] - M[L - 1, C-1]
                s += M[L, C]
            M[L+1, 0] = s
        
        for L in range(N):
            F.tableR.insertRow(L)
            F.tableR.setColumnCount(N)
            for C in range(N):
                x = str(M[L, C])
                if x.isdecimal():
                    F.tableR.setItem(L, C, QTableWidgetItem(x))

def qui_click():
    pass


def ann_click():
    pass
        


def aff_click():
    # (0, 0)
    # (0, 1), (1, 0)
    # (0, 2), (1, 1), (2, 0)
    # (0, 3), (1, 2), (2, 1), (3, 0)
    # (0, 4), (1, 3), (2, 2), (3, 1), (4, 0)    
    if test:
        for i in range(N):
            ch = ""
            for j in range(i+1):
                ch += str(M[j, i-j]) + " "
            F.listR.addItem(ch)

app = QApplication([])
F = loadUi("C:/lycee/Bac/Programmation/Etude/Tp2/diagonal.ui")
F.show()
F.remp.clicked.connect(valide)
F.qui.clicked.connect(qui_click)
F.ann.clicked.connect(ann_click)
F.aff.clicked.connect(aff_click)

app.exec_()
