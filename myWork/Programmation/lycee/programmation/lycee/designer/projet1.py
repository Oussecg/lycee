from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox

def pushButton_click():
    if checkInputs():
      A = int(windows.inputA.text())
      B = int(windows.inputB.text())
      if windows.radioPUISSANCE.isChecked():
        windows.resultat.setText(str(puissance(A, B)))
      elif windows.radioPGCD.isChecked():
        windows.resultat.setText(str(pgcd(A, B)))
      elif windows.radioPPCM.isChecked():
        windows.resultat.setText(str(ppcm(A, B)))
      else:
        QMessageBox.critical(windows, "Error", "Please check an option")

def pushButton_2_click():
    windows.inputA.setText("")
    windows.inputB.setText("")
    windows.resultat.setText("")
    windows.radioButton.setChecked(True)

def checkInputs():
  A = windows.inputA.text()
  B = windows.inputB.text()
  if A.isdecimal() and B.isdecimal() and int(A) > 0 and int(B) > 0:
    return True
  else:
    QMessageBox.critical(windows, "Error", "Introduire un entier > 0")
    return False

def puissance(A, B):
  p = 1
  for i in range(B):
    p *= A
  return p

def pgcd(A, B):
  while A != B:
    if A > B:
      A -= B
    elif B > A:
      B -= A
  return A

def ppcm(A, B):
  P = A
  while P % B != 0:
    P += A
  return P

app = QApplication([])
windows = loadUi ("C:/Users/ousse/Documents/lycee/programmation/lycee/designer/project1.ui")
windows.show()
windows.pushButton.clicked.connect ( pushButton_click )
windows.pushButton_2.clicked.connect ( pushButton_2_click )

app.exec_()
