import entitties
from owner import Owner
from pet import Pet
import time

OL = []
PL = []

# crea la lista di tutti i proprietari esistenti
def owner_list():
    for name in dir(entitties):
        quack = getattr(entitties, name)
        if isinstance(quack, Owner):
            OL.append(quack)

# crea la lista di tutti gli animali esistenti
def pets_list():
    for name in dir(entitties):
        noot = getattr(entitties, name)
        if isinstance(noot, Pet):
            PL.append(noot)

# stampa la lista degli animali
def POL():
    print("the list of pets:\n")
    x = 0
    while x != len(PL):
        print(f"{x +1}. ", end="")
        print(PL[x])
        x += 1

# stampa la lista dei proprietari
def PPL():
    x = 0
    print("the list of owner:\n")
    while x != len(OL):
        print(f"{x +1}. ", end="")
        print(OL[x])
        x +=1