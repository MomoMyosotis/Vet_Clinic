# pet

class Pet:
    # INIT METHOD COSTRUISCE I METODI -> __init__(self):

    def __init__(self, species, age, weight, height, name, id, condition, Owner):
        # attributes -> what it is or has
        self.species = species
        self.age = age
        self.weight = weight
        self.height = height
        self.name = name
        self.condition = condition
        self.id = id
        self.owner = Owner

    def __str__(self):
        return f"{self.id}"

    # methods -> what it does
    def eat(self):
        print(f"{self.name} is eating")

    def move(self):
        print(f"{self.name} is moving according to what being {self.species} allows")

    def play(self):
        print(f"{self.name} loves to play with {self.owner.name}")

    def sleep(self):
        print(f"{self.name} is currently sleeping. is it normal at {self.age} years old {self.species}?")

    def judge(self):
        print(f"{self.name} is judging you")

# last line