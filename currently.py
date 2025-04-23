# responsable for creaing dynamic array of recovered pets and their owners
import lista as Ls
import impslist

# lar = lista animali registrati
lar = Ls.PL
# lpr = lista proprietari registrati
lpr = Ls.OL

# liste dinamiche
animali = []
proprietari = []

# crea la lista di tutti gli animali presenti allinizio dato quack random nell'elenco di animali totali
def dynamic_pets(quack):
    if quack > len(lar):
        print("error 3")
    print(f"there are currently {quack} pets in the clinic.")
    animali.extend(impslist.random.sample(lar, quack))
    Ls.print_List(animali, "pets")

def dynamic_owners(miao):
    if miao > len(lpr):
        print("error 8")
    print(f"there are currently {miao} owners registred in the clinic.")
    proprietari.extend(impslist.random.sample(lpr, miao))
    Ls.print_List(proprietari, "owners")

# last line