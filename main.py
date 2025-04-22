# vet clinic emulator
import impslist
import currently as C

# variabili globali
generator = 1

# pulizia
def cls():
    impslist.time.sleep(2)
    impslist.os.system("clear")


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


    while True:
        new_action = impslist.random.randint(1,9)
        related_pet = []
        if new_action == 1 or 8:
            # pesca da lista di non presenti
            while related_pet not in C.animali:
                related_pet = impslist.random.sample(C.lar, 1)[0]
        elif new_action == 2 or 9:
            #remove from list
            related_pet = impslist.random.sample(C.lar,1)[0]
            C.lar.remove(related_pet)
        elif new_action == 3 or 4 or 5 or 6 or 7:
            related_pet = impslist.random.sample(C.animali, 1)[0]
            impslist.pet.action(new_action, related_pet)
        else:
            print("error 6")
        impslist.time.sleep(1)

main()
# last line