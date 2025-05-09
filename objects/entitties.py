# gli oggetti creatis
from objects.owner import Owner
from objects.pet import Pet

# owner -> 0 dipendenze (goes up)
owner_1 = Owner("Puffetto", "Spaziale", "MY050T1S", "14th of december", "M")
owner_2 = Owner("Moffettina", "Pinguinosa", "P4P4V3R1", "8th of october", "F")
owner_3 = Owner("Greta", "Crotone", "G1R450L1", "22th of november", "F")
owner_4 = Owner("Emily", "IDK", "C1CL4M1N1", "3th of genuary", "F")
owner_5 = Owner("Nicole", "Chinellato", "M4RGH3R1T4", "28th of april", "F")
owner_6 = Owner("Jacopo", "Moraldini", "L0T0814NC0", "2th of october", "M")
owner_7 = Owner("Luca", "Bertoldi", "P1L4V3L0", "15th of March", "M")
owner_8 = Owner("Giulia", "Verdi", "G4L123V", "22th of May", "F")
owner_9 = Owner("Stefano", "D'Ambrosio", "S3TA1C0", "12th of June", "M")
owner_10 = Owner("Francesca", "Giansanti", "F4NC3S9", "5th of July", "F")

# pet -> 1 dipendenza (goes down)
pet_1 = Pet("Pollosauro", 1.2, "120 g", "30 cm", "Nooty", "00001", "Healthy", "MY050T1S")
pet_2 = Pet("Sonnus canis", 20, "30 kg", "100 cm", "bianca", "00002", "Sonnite acuta", "P4P4V3R1")
pet_3 = Pet("strambus selvaticus", 911, "84 kg", "69 cm", "weirdass thing", "0003", "mentally ill owner", "G1R450L1")
pet_4 = Pet("Felis combustibilis", 3, "5.5 kg", "45 cm", "Zampa", "00004", "Flammable fur", "C1CL4M1N1")
pet_5 = Pet("Canis depressus", 7, "20 kg", "80 cm", "Tristezza", "00005", "Existential dread", "M4RGH3R1T4")
pet_6 = Pet("Capra lunatica", 5, "32 kg", "60 cm", "Becky la Svitata", "00006", "Mania acuta", "L0T0814NC0")
pet_7 = Pet("Draconis minus", 0.4, "1.2 kg", "25 cm", "Pufflet", "00007", "Needs constant supervision", "P4P4V3R1")
pet_8 = Pet("Tartaruga turbo", 80, "70 kg", "90 cm", "Nitro", "00008", "Hyperactive", "M4RGH3R1T4")
pet_9 = Pet("Gatto quantico", 2, "3 kg", "40 cm", "Schrödy", "00009", "Alive and dead", "MY050T1S")
pet_10 = Pet("Cane a molla", 1, "8 kg", "50 cm", "Slinky", "00010", "Joint issues", "P4P4V3R1")
pet_11 = Pet("Coniglius paranoicus", 6, "4.2 kg", "30 cm", "Twitch", "00011", "Mild conspiracy tendencies", "G1R450L1")
pet_12 = Pet("Topus gladiator", 0.9, "0.8 kg", "20 cm", "Spartacchio", "00012", "Aggressively patriotic", "C1CL4M1N1")
pet_13 = Pet("Cacatua metallum", 10, "12 kg", "55 cm", "Rocky", "00013", "Addicted to heavy metal", "M4RGH3R1T4")
pet_14 = Pet("Leone Ballerino", 200, "250 kg", "120 cm", "Rex", "00014", "Dancer at heart", "P1L4V3L0")
pet_15 = Pet("Squalo Sognante", 1500, "800 kg", "6 m", "Sharky", "00015", "Dreams of the ocean", "G4L123V")
pet_16 = Pet("Cervo Curioso", 20, "200 kg", "150 cm", "Bambi", "00016", "Loves to explore", "S3TA1C0")
pet_17 = Pet("Cane Nube", 9, "20 kg", "65 cm", "Cloudy", "00017", "Is afraid of rain", "F4NC3S9")
pet_18 = Pet("Gatto Cosmico", 4, "4 kg", "45 cm", "Nebula", "00018", "Not of this world", "P1L4V3L0")
pet_19 = Pet("Tigre Elettrica", 300, "220 kg", "180 cm", "Volt", "00019", "Electrified fur", "S3TA1C0")
pet_20 = Pet("Foca Acrobatica", 70, "100 kg", "150 cm", "Flippy", "00020", "Master of flips", "G4L123V")
pet_21 = Pet("peachy penguosus", 10, "2 kg", "40 cm", "pingu", "00021", "peachy", "P4P4V3R1")


# last line