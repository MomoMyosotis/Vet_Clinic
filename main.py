# vet clinic emulator
import impslist
import currently as C

# pulizia
def cls():
    impslist.time.sleep(2)
    impslist.os.system("clear")

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
    impslist.Ls.avvio()
    starting()

main()
# last line