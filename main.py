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

#   given the id returns any info you're searching for
#   both for pet && owner
def get_by_attr(obj_list, target_value, attr_name):
    for obj in obj_list:
        if getattr(obj, attr_name) == target_value:
            return obj
    raise ValueError(f"No object {attr_name} = {target_value}")

##################################################
#           Flow
def main():
    impslist.Ls.avvio()     # crea una lista con tutti i pets e gli owner
    starting()              # sceglie n elementi da pets per l'inizio dell'app

"""
    nati = impslist.random.randint(1, generator)
    nascituri = impslist.random.sample(C.animali, nati)
    for x in nascituri:
        print(f"{x.name}")
"""
#    raa = impslist.random.randint(1,9) # random animal action
#    impslist.Pet.action(impslist.random.sample(C.animali, raa))

new_action = impslist.random.randint(1,9)
related_pet = impslist.random.sample(C.animali, 1)[0]
impslist.pet(action(new_action, related_pet))

main()
# last line