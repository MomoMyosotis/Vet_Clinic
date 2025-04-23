# owner
import ffile

class Owner:
    def __init__(self, name, surname, CF, bday, gender):
        self.name = name
        self.surname = surname
        self.CF = CF
        self.bday = bday
        self.gender = gender

    def __str__(self):
        return f"{self.CF}"

    def birthday(self):
        if self.gender == 'M':
            print(f"mr. {self.surname}'s birthday is {self.bday}")
        elif self.gender == 'F':
            print(f"miss {self.surname}'s birthday is {self.bday}")
        else:
            print(f"{self.surname} the fuck is wrong with you? get out of here!\n*grabs a shotgun*")
            print(f"*the assistant throws at {self.name} it's pet*")

    def check(self, pet):
        print(f"{self.surname} called to check on {pet}", end="")
        ffile.rtime()

    def pav(self):
        print(f"{self.surname} booked a vet visit for ", end="")
        ffile.rtime()

    def register_pet(self, pet):
        print(f"{self.surname} registered {pet} at ", end="")
        ffile.rtime()

    def report_death(self, pet):
        print(f"{self.surname} reported that {pet} has died at ", end="")
        ffile.rtime()

    def feed_pet(self, pet):
        print(f"{self.surname} is feeding {pet} at ", end="")
        ffile.rtime()

    def walk_pet(self, pet):
        print(f"{self.surname} is walking {pet} around the block")

    def play_with_pet(self, pet):
        print(f"{self.surname} is playing with {pet} — happy tails and wagging guaranteed")

    def judge_pet(self, pet):
        print(f"{self.surname} is judging {pet}'s behavior silently... but deeply.")

    def adopt_pet(self, pet):
        print(f"{self.surname} adopted {pet} from the clinic at ", end="")
        ffile.rtime()

    def abandon_pet(self, pet):
        print(f"{self.surname} abandonet {pet} at the clinic at ", end="")
        ffile.rtime()

# usare la funzione ffile.get_by_attribute(obj_list, target_value, attr_name) per trovareil nome del pet relativo

def action(code, owner):
    from lista import PL
    # l'idea è di prendere il codice dell'animale relativo al proprietario
    pet = ffile.gar(PL, owner.CF, "owner")

    if code == 1:
        owner.birthday()
    elif code == 2:
        owner.check(pet)
    elif code == 3:
        owner.pav()
    elif code == 4:
        owner.register_pet(pet)
    elif code == 5:
        owner.report_death(pet)
    elif code == 6:
        owner.feed_pet(pet)
    elif code == 7:
        owner.walk_pet(pet)
    elif code == 8:
        owner.play_with_pet(pet)
    elif code == 9:
        owner.judge_pet(pet)
    elif code == 10:
        owner.adopt_pet(pet)
    elif code == 11:
        owner.abandon_pet(pet)
    else:
        print("error 7")


# last line