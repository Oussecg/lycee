from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox
from numpy import array


def pushButton_click():
    ch = windows.lineEdit.text()
    if ch == "":
      QMessageBox.critical(windows, 'Erreur', 'Vous ')


def pushButton_2_click():
    pass


app = QApplication([])
windows = loadUi("D:/lycee/TR3/Programation/revision/InterfaceCryptage.ui")
windows.show()
windows.pushButton.clicked.connect(pushButton_click)
windows.pushButton_2.clicked.connect(pushButton_2_click)

app.exec_()
