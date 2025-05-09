# vet clinic emulator
import extentions.impslist as impslist

# variabili globali
generator = 1

##################################################
#           Flow
def main():

#   crea lista per tutti gli owner e i pet
    impslist.ffile.initial_check()
    impslist.ffile.cls()
    print("\n\n_________________________________________")

    impslist.C.dynamic_pets(impslist.random.randint(1,21))
    impslist.C.dynamic_owners(impslist.random.randint(1,10))
    while True:
    #   sceglie se è il pet o l'owner o fare l'azione
        generator = impslist.random.randint(1,2,3)

        if generator == 1:
            #   PET CYCLE
            impslist.ffile.pet_cycle()
        elif generator == 2:
            #   OWNER CYCLE
            impslist.ffile.owner_cycle()
        elif generator == 3:
            print("WIP")
        else:
            print("error 999")
            return

        impslist.time.sleep(impslist.random.uniform(0.02 , 2))

main()