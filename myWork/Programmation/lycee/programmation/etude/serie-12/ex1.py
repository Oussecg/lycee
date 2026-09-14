from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def sommeDiviseur(x:int):
  s = 0
  for i in range(1, x):
    if x % i == 0:
      s += i
  return s

def executeButton():
    N = int(windows.entierInput.text())
    m = ""
    if N < 10:
      m = f"{N} n'est pas un nombre >= 10"
    else:
      s = sommeDiviseur(N)
      if s == N:
        m = f"{N} est un nombre parfait"
      elif s < N:
        m = f"{N} est un nombre abondant"
      else:
        m = f"{N} est un nombre déficient"
    windows.result.setText(m)

def quitButton():
    windows.close()

app = QApplication([])
windows = loadUi("ex1.ui")
windows.show()
windows.executeButton.clicked.connect(executeButton)
windows.quitButton.clicked.connect(quitButton)

app.exec_()
