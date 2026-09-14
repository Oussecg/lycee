from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def pushButton_click():
    A = int(windows.lineEdit.text())
    B = int(windows.lineEdit_2.text())
    windows.label_5.setText(f"{A} + {B} = {A+B}")

def pushButton_2_click():
    app.exit()

app = QApplication([])
windows = loadUi ("C:/Users/ousse/Documents/lycee/programmation/lycee/designer/tp1.ui")
windows.show()
windows.pushButton.clicked.connect ( pushButton_click )
windows.pushButton_2.clicked.connect ( pushButton_2_click )

app.exec_()

