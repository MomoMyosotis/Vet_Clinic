import entitties

# lista di tutti i proprietari
OL = []
# lista di tutti i pet
PL = []

# crea la lista di tutti i proprietari esistenti
def owner_list():
    for name in dir(entitties):
        quack = getattr(entitties, name)
        if isinstance(quack, entitties.Owner):
            OL.append(quack)
#    print_List(OL, "owners")

# crea la lista di tutti gli animali esistenti
def pets_list():
    for name in dir(entitties):
        noot = getattr(entitties, name)
        if isinstance(noot, entitties.Pet):
            PL.append(noot)
#    print_list(PL, "pets")

# stampa la lista degli
#   which -> owner o pet
def print_List(n, which):
    print(f"the list of {which}:\n")
    x = 0
    while x != len(n):
        print(f"{x +1}. ", end="")
        print(n[x])
        x += 1
    print("")

# last line