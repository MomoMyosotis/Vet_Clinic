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

#################################################
# # crea una lista con tutti i pets e gli owner
def initial_check():
    impslist.Ls.owner_list()
    impslist.Ls.pets_list()

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

    initial_check()
    cls()
    print("\n\n_________________________________________")
    generator = impslist.random.randint(1,13)
    temp = C.dynamic_pets(generator)
    print("_________________________________________\n\n")

    """
    nati = impslist.random.randint(1, generator)
    nascituri = impslist.random.sample(C.animali, nati)
    for x in nascituri:
        print(f"{x.name}")
    """
    #    raa = impslist.random.randint(1,9) # random animal action
    #    impslist.Pet.action(impslist.random.sample(C.animali, raa))

    new_action = impslist.random.randint(1,9)
    related_pet = []
    print(len(C.animali))
    related_pet = impslist.random.sample(C.animali, len(related_pet))
    impslist.pet.action(new_action, related_pet)

main()
# last line