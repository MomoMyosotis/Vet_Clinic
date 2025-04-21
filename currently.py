# responsable for creaing dynamic array of recovered pets and their owners
import impslist

# lar = lista animali registrati
lar = impslist.Ls.PL
# lpr = lista proprietari registrati
Lpr = impslist.Ls.OL

# liste dinamiche
animali = []
proprietari = []

# crea la lista di tutti gli animali presenti allinizio dato quack random nell'elenco di animali totali
def dynamic_pets(quack):

    if quack > len(lar):
        print("error 3")
    print(f"there are currentl {quack} pets in the clinic.")
    animali.extend(impslist.random.sample(lar, quack))
    impslist.Ls.POL(animali)


# stampa la lista dei proprietari -> deve trovare i CF legati agli animali
#               YET TO DO

# last line