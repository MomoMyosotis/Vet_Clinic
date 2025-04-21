import impslist

OL = []
PL = []

def avvio():
    # crea la lista di tutti i proprietari esistenti
    def owner_list():
        for name in dir(impslist.entitties):
            quack = getattr(impslist.entitties, name)
            if isinstance(quack, impslist.Owner):
                OL.append(quack)
        #PPL(PL)

    # crea la lista di tutti gli animali esistenti
    def pets_list():
        for name in dir(impslist.entitties):
            noot = getattr(impslist.entitties, name)
            if isinstance(noot, impslist.Pet):
                PL.append(noot)
        #POL(PL)

    owner_list()
    pets_list()

# stampa la lista degli animali
def POL(n):
    print("the list of pets:\n")
    x = 0
    while x != len(n):
        print(f"{x +1}. ", end="")
        print(n[x])
        x += 1

# stampa la lista dei proprietari
def PPL():
    x = 0
    print("the list of owners:\n")
    while x != len(OL):
        print(f"{x +1}. ", end="")
        print(OL[x])
        x +=1