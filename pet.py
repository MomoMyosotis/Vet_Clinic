# pet
import ffile

class Pet:
    # INIT METHOD COSTRUISCE I METODI -> __init__(self):

    def __init__(self, species, age, weight, height, name, id, condition, owner):
        # attributes -> what it is or has
        self.species = species
        self.age = age
        self.weight = weight
        self.height = height
        self.name = name
        self.condition = condition
        self.id = id
        self.owner = owner

    def __str__(self):
        return f"{self.id}" # -> owner is: {self.owner}"

    # methods -> what it does

    def birth(self):

        print(f"{self.name} has born at ", end="")
        ffile.rtime()

    def death(self):
        print(f"{self.name} has died at ", end="")
        ffile.rtime()

    def eat(self):
        print(f"{self.name} is eating at ", end="")
        ffile.rtime()

    def move(self):
        print(f"{self.name} is moving according to what being {self.species} allows")

    def play(self):
        print(f"{self.name} loves to play with {self.owner}")

    def sleep(self):
        print(f"{self.name} has been sleeping since: ", end="")
        ffile.rtime()

    def judge(self):
        print(f"{self.name} is judging you")

    def admitted(self):
        print(f"{self.name} has been admitted to the clinic at ", end="")
        ffile.rtime()

    def dismissed(self):
        print(f"{self.name} has been dismissedd from the clinc at ", end="")
        ffile.rtime()

def action(miao, pet):
    if miao == 1:
        # Caso 1: far nascere l'animale
        pet.birth()

    elif miao == 2:
        # Caso 2: l'animale è morto
        pet.death()

    elif miao == 3:
        # Caso 3: l'animale mangia
        pet.eat()

    elif miao == 4:
        # Caso 4: l'animale si muove
        pet.move()

    elif miao == 5:
        # Caso 5: l'animale gioca
        pet.play()

    elif miao == 6:
        # Caso 6: l'animale dorme
        pet.sleep()

    elif miao == 7:
        # Caso 7: l'animale ti giudica
        pet.judge()

    elif miao == 8:
        # Caso 8: l'animale viene ammesso in clinica
        pet.admitted()

    elif miao == 9:
        # Caso 9: l'animale viene dimesso dalla clinica
        pet.dismissed()

    else:
        # Caso di errore se miao non è valido
        print("error 5!")

# last line