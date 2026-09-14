from numpy import array

class Player:
  def __init__(self, name):
    self.name: str = name
    self.symbol: str = self.check_symbol()
    self.rating: int = 0

  def check_symbol(self):
    symbol = ""
    if self.name == "Messi":
      symbol = "M"
    elif self.name == "Neymar":
      symbol = "N"
    else:
      symbol = "B"
    return symbol

def saisir():
  n = int(input("Saisir le nombre de participant: "))
  while not (2 <= n <= 100):
    n = int(input("Saisir le nombre de participant: "))
  return n

def remplir(n:int):
  for i in range(n):
    t1[i] = input(f"T1[{i + 1}]= ")
    t2[i] = input(f"T2[{i + 1}]= ").upper()
    while not (t2[i] in ["M", "B", "N"]) or not (len(t1[i]) == 8 and t1[i].isdecimal() and unique(t1[i], i)):
      t1[i] = input(f"T1[{i + 1}]= ")
      t2[i] = input(f"T2[{i + 1}]= ").upper()

def unique(t, p: int) -> bool:
  i = 0
  test = True
  while i < p and test:
    if t[i] == t[p] :
      test = False
    else:
      i += 1
  return test

def afficher_résultat(t1, t2, n:int):
  for i in range(n):
    if t2[i] == messi.symbol:
      messi.rating += 1
    elif t2[i] == neymar.symbol:
      neymar.rating += 1
    elif t2[i] == mbappe.symbol:
      mbappe.rating += 1


  if messi.rating > mbappe.rating and messi.rating > neymar.rating:
    best_player_symbol = messi.symbol
    best_player = messi.name
  elif neymar.rating > mbappe.rating and neymar.rating > messi.rating:
    best_player_symbol = neymar.symbol
    best_player = neymar.name
  else:
    best_player_symbol = mbappe.symbol
    best_player = mbappe.name
  print(f"Le joueur le plus populaire est {best_player}")
  print(f"Les numéros des téléspectateurs qui ont choisit {best_player} sont", end=" ")
  for i in range(n):
    if t2[i] == best_player_symbol:
      print(t1[i], end=" ")

messi = Player("Messi")
mbappe = Player("Mbappe")
neymar = Player("Neymar")
N = saisir()
t2 = array([str] * N)
t1= array([str] * N)
remplir(N)
afficher_résultat(t1, t2, N)
