from numpy import array
from pickle import dump, load

El = dict(
    N= str,
    M= float
)

def remplir():
    nb = 0
    El["N"] = input(f"Nom{nb+1}= ")  
    while not est_alpha(El["N"]):
        El["N"] = input(f"Nom{nb+1}= ")  
        
def est_alpha(ch: str) -> bool:
    