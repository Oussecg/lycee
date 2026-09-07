from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox

def pushButton_click():
    if windows.dataInput.text() == "" :
      QMessageBox.critical(windows, "Error", "Saisir un nombre !")
    elif windows.dataInput.text().isdecimal() == False :
      print(windows.dataInput.text().isdecimal())
      QMessageBox.critical(windows, "Error", "Tu saisie une chaine, saisie un nombre !")
    else:
      N = int(windows.dataInput.text())
      if windows.comboBox.currentText() == "Super pair plus ?":
        if superPair(N):
          windows.resultat.setText(f"N = {N} est un entier super-pair-plus")
        else:
          windows.resultat.setText(f"N = {N} n'est pas un entier super-pair-plus")
      elif windows.comboBox.currentText() == "Parfait ?":
        if est_parfait(N):
          windows.resultat.setText(f"N = {N} est un entier parfait")
        else:
          windows.resultat.setText(f"N = {N} n'est pas un entier parfait")
      else:
        if est_premier(N):
          windows.resultat.setText(f"N = {N} est un entier premier")
        else:
          windows.resultat.setText(f"N = {N} n'est pas un entier premier")

def superPair(N: int):
  ch = str(N)
  test = True
  i = 0
  while test and i < len(ch):
    if int(ch[i]) % 2 == 0:
      i += 1
    else:
      test = False
  return N % 2 == 0 and test and diviseurPair(N)

def diviseurPair(N:int):
  test = True
  i = 2
  while test and i < N:
    if N % i == 0 :
      if i % 2 == 1 :
        test = False
    i += 1
  return test

def est_parfait(N:int):
  s = 0
  for i in range(1, (N // 2) + 1):
    if N % i == 0:
      s += i
  return s == N

def est_premier(N: int):
  test = True
  i = 2
  while test and i < N:
    if N % i == 0 :
      test = False
    else:
      i += 1
  return test

app = QApplication([])
windows = loadUi ("C:/Users/ousse/Documents/lycee/programmation/lycee/designer/InterfaceNombre.ui")
windows.show()
windows.pushButton.clicked.connect ( pushButton_click )

app.exec_()
