from numpy import array

def saisir_nombre():
  n = int(input("Saisir le nombre d’élèves: "))
  while not (1 <= n <= 25):
    n = int(input("Saisir le nombre d’élèves: "))
  return n

def remplir_tableau1(t, n:int):
  for i in range(n):
    t[i] = input(f"TE[{i + 1}]= ")
    while not(check_case(t[i])):
      t[i] = input(f"TE[{i + 1}]= ")
  return t

def check_case(ch: str):
  nom = ch[ : ch.find("#")]
  ch = ch[ch.find("#") + 1 : ]
  my1 = float(ch[ : ch.find("#")])
  my2 = float(ch[ch.find("#")+1 : ])
  if est_alpha(nom) and est_moyenne(my1) and est_moyenne(my2):
    return True
  return False

def est_alpha(ch:str) -> bool:
  test = True
  i = 0
  while i < len(ch) and test:
    if "A" <= ch[i].upper() <= "Z":
      i += 1
    else:
      test = False
    return test

def est_moyenne(x: float) -> bool:
  if 0 <= x <= 20:
    return True
  return False

def remplir_tableau2(t2, t1, n:int):
  for i in range(n):
    ch = t1[i][ t1[i].find("#") + 1 : ]
    print(t1[i], ch)
    my1 = float(ch[ : ch.find("#") ])
    my2 =  float(ch[ ch.find("#") + 1 : ])
    t2[i] = round((my1 + my2 * 2) / 3, 2)
  return t2

def afficher(t1, t2, n: int, ch: str):
  for i in range(n):
    pass
N = saisir_nombre()
TE = remplir_tableau1(array([str] * N), N)
TM = remplir_tableau2(array([float] * N), TE, N)
print(f"TE = {TE}, TM = {TM}")
nom = input("Saisir nom: ")
while not(est_alpha(nom)):
  nom = input("Saisir nom: ")
afficher(TE, TM, N, nom)

# I'm typing something right now ! why the atmosphere dosent work ?



