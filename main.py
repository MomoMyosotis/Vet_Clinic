from pet import Pet
from owner import Owner
import os
import time
import random
import lista as Ls

# pulizia
def cls():
    time.sleep(4)
    os.system("clear")

# liste dinamiche
animali = []
proprietari = []

Ls.owner_list()
Ls.pets_list()
Ls.POL()
print("\n________________________\n")
Ls.PPL()

def starting():
    # all'inizio la clinca ha 4 animali in cura

    print("starting() started")


    generator = random.randint(1,13)
    x = 0

    while x < generator:


        x += 1

    print("starting() ended.")




# last line