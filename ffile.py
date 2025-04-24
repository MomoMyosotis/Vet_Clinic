import impslist
import currently as C

##################################################
# generate a rondom time
def rtime():
    hour = impslist.random.randint(1,23)
    minute = impslist.random.randint(1,59)
    if hour > 9 and minute > 9:
        return print(f"{hour}:{minute}")
    elif hour < 9 and minute > 9:
        return print(f"0{hour}:{minute}")
    elif hour > 9 and minute < 9:
        return print(f"{hour}:0{minute}")
    else:
        return print(f"0{hour}:0{minute}")
###################################################
# clean
def cls():
    impslist.time.sleep(2)
    impslist.os.system("cls" if impslist.os.name == "nt" else "clear")


#################################################
# create a list with all pets and owners
def initial_check():
    impslist.Ls.owner_list()
    impslist.Ls.pets_list()

##################################################
# restituisce direttamente l'oggetto Pet, non solo il nome
def gar(obj_list, target_value, attr_name):
    for obj in obj_list:
        if getattr(obj, attr_name) == target_value:
            return obj
    raise ValueError(f"No object with {attr_name} = {target_value}")

####################################################
def pet_cycle():

    new_action = impslist.random.randint(1,9)
    related_pet = []
    # avalable -> lista complementare a C.animali
    avalable_P = [pet for pet in impslist.Ls.PL if pet not in C.animali]

    if new_action in [1, 8]:
    # pesca da lista di non presenti
        if avalable_P:
            related_pet = impslist.random.choice(avalable_P)
            C.animali.append(related_pet)
            impslist.pet.action(new_action, related_pet)

    elif new_action in [2, 9]:
    #remove from list
        if not avalable_P:
            related_pet = impslist.random.sample(C.lar,1)[0]
            impslist.pet.action(new_action, related_pet)
            C.animali.remove(related_pet)

    elif new_action in [3, 4, 5, 6, 7]:
        related_pet = impslist.random.sample(C.animali, 1)[0]
        impslist.pet.action(new_action, related_pet)

    else:
        print("error 6")

####################################################
def owner_cycle():

    new_action = impslist.random.randint(1,9)
    related_owner = []
    # avalable -> lista complementare a C.proprietari
    avalable_O = [owner for owner in impslist.Ls.OL if owner not in C.proprietari]

    if new_action in [3, 4, 10]:
    # pesca da lista di non presenti
        if avalable_O:
            related_owner = impslist.random.choice(avalable_O)
            C.proprietari.append(related_owner)
            impslist.owner.action(new_action, related_owner)

    elif new_action in [5, 11]:
    #remove from list
        if not avalable_O:
            related_owner = impslist.random.sample(C.lpr,1)[0]
            impslist.owner.action(new_action, related_owner)
            C.proprietari.remove(related_owner)

    elif new_action in [2, 6, 7, 8, 9]:
        related_owner = impslist.random.sample(C.proprietari, 1)[0]
        impslist.owner.action(new_action, related_owner)

    elif new_action == 1:
        related_owner = impslist.random.sample(C.lpr, 1)[0]
        impslist.owner.action(new_action, related_owner)
    else:
        print("error 8")

# last line