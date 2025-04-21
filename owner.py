# owner
class Owner:
    def __init__(self, name, surname, CF, bday, gender):
        self.name = name
        self.surname = surname
        self.CF = CF
        self.bday = bday
        self.gender = gender

    def __str__(self):
        return f"{self.CF}"

    def birthday(self):  # DEVE essere qui, NON indentato dentro __init__
        if self.gender == 'M':
            print(f"mr. {self.surname}'s birthday is {self.bday}")
        elif self.gender == 'F':
            print(f"miss {self.surname}'s birthday is {self.bday}")
        else:
            print(f"{self.surname} the fuck is wrong with you? get out of here!\n*grabs a shotgun*")
            print(f"*the assistant throws at {self.name} it's pet*")

# last line