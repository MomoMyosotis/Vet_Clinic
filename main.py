# vet clinic emulator
import impslist
import currently as C

# variabili globali
generator = 1

# pulizia
def cls():
    impslist.time.sleep(2)
    impslist.os.system("clear")

# generate a rondom time
def rtime():
    hour = {impslist.random(1,24)}
    minute = {impslist.random(1,59)}
    return hour, minute

#################################################àà
def initial_check():
    print("\n________________________\n")
    impslist.Ls.PPL()
    impslist.Ls.POL()

def starting():
    # all'inizio la clinca ha random n animali in cura
    generator = impslist.random.randint(1,13)
    C.dynamic_pets(generator)

##################################################
#           Flow
def main():
    impslist.Ls.avvio()     # crea una lista con tutti i pets e gli owner
    starting()              # sceglie n elementi da pets per l'inizio dell'app
    nati = impslist.random.randint(1, generator)
    impslist.Pet.birth(impslist.random.sample(C.animali, nati))

    raa = impslist.random.randint(1,9) # random animal action
    impslist.Pet.action(impslist.random.sample(C.animali, raa))

main()
# last line