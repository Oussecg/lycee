from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def poidsChaine(ch:str):
  s = 0
  for i in range(len(ch)):
    if ch[i].upper() in ["A", "E", "Y", "U", "O", "I"]:
      s += (ord(ch[i].upper()) - 64) * i
  return s

def executeButton():
    ch = windows.chaineInput.text()
    p = ""
    if ch == "":
      p = "Aucune chaine saisie !"
    elif not est_alpha(ch):
      p = "Chaine non valable"
    else:
      p = f"Le poids du mot {ch} = {poidsChaine(ch)}"
    windows.result.setText(p)

def est_alpha(ch:str):
  test = True
  i = 0
  while test and i < len(ch):
    if "A" <= ch[i].upper() <= "Z":
      i += 1
    else:
      test = False
  return test

def restartButton():
  windows.result.setText("")
  windows.chaineInput.setText("")

def quitButton():
    windows.close()

app = QApplication([])
windows = loadUi("programmation\etude\serie-12\ex2.ui")
windows.show()
windows.executeButton.clicked.connect(executeButton)
windows.quitButton.clicked.connect(quitButton)
windows.optionButton.clicked.connect(restartButton)
app.exec_()

