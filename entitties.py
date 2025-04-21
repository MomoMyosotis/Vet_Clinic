# gli oggetti creatis
from impslist import Owner
from impslist import Pet

# owner -> 0 dipendenze (goes up)
owner_1 = Owner("Puffetto", "Spaziale", "MY050T1S", "14th of december", "M")
owner_2 = Owner("Moffettina", "Pinguinosa", "P4P4V3R1", "8th of october", "F")
owner_3 = Owner("Greta", "Crotone", "G1R450L1", "22th of november", "F")
owner_4 = Owner("Emily", "IDK", "C1CL4M1N1", "3th of genuary", "F")
owner_5 = Owner("Nicole", "Chinellato", "M4RGH3R1T4", "28th of april", "F")
owner_6 = Owner("Jacopo", "Moraldini", "L0T0814NC0", "2th of october", "M")

# pet -> 1 dipendenza (goes down)
pet_1 = Pet("Pollosauro", 1.2, "120 g", "30 cm", "Nooty", "00001", "Healthy", owner_1)
pet_2 = Pet("Sonnus canis", 20, "30 kg", "100 cm", "bianca", "00002", "Sonnite acuta", owner_2)
pet_3 = Pet("strambus selvaticus", 911, "84 kg", "69 cm", "weirdass thing", "0003", "mentally ill owner", owner_3)
pet_4 = Pet("Felis combustibilis", 3, "5.5 kg", "45 cm", "Zampa", "00004", "Flammable fur", owner_4)
pet_5 = Pet("Canis depressus", 7, "20 kg", "80 cm", "Tristezza", "00005", "Existential dread", owner_5)
pet_6 = Pet("Capra lunatica", 5, "32 kg", "60 cm", "Becky la Svitata", "00006", "Mania acuta", owner_6)
pet_7 = Pet("Draconis minus", 0.4, "1.2 kg", "25 cm", "Pufflet", "00007", "Needs constant supervision", owner_2)
pet_8 = Pet("Tartaruga turbo", 80, "70 kg", "90 cm", "Nitro", "00008", "Hyperactive", owner_5)
pet_9 = Pet("Gatto quantico", 2, "3 kg", "40 cm", "Schrödy", "00009", "Alive and dead", owner_1)
pet_10 = Pet("Cane a molla", 1, "8 kg", "50 cm", "Slinky", "00010", "Joint issues", owner_2)
pet_11 = Pet("Coniglius paranoicus", 6, "4.2 kg", "30 cm", "Twitch", "00011", "Mild conspiracy tendencies", owner_3)
pet_12 = Pet("Topus gladiator", 0.9, "0.8 kg", "20 cm", "Spartacchio", "00012", "Aggressively patriotic", owner_4)
pet_13 = Pet("Cacatua metallum", 10, "12 kg", "55 cm", "Rocky", "00013", "Addicted to heavy metal", owner_5)

# last line