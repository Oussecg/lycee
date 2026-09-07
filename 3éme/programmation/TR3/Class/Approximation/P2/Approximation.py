from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox


def Play():
    epsilon = float(windows.selectBox.currentText())
    if windows.Ex_radio.isChecked():
        windows.resultLabel.setText(exponontiel(epsilon))
    else:
        windows.resultLabel.setText()


app = QApplication([])
windows = loadUi("C:/lycee/TR3/Programation/Class/Approximation/P2/Interface_Approximation.ui")
windows.show()
windows.pushButton.clicked.connect(Play)

app.exec_()
