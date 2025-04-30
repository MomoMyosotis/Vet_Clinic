# illness
import extentions.ffile as ffile

class Illness:
    def __init__(self, name, description, cure, lethality, life_cycles):
        # attributes -> what it is or has
        self.name = name
        self.description = description
        self.cure = cure
        self.lethality = lethality
        self.life_cycles = life_cycles

    def __str__(self):
        return f"Illness: {self.name} - Lethality: {'Yes' if self.lethality else 'No'}"

    # methods -> what it does

    def cure_treatment(self):
        if self.cure:
            print(f"Treatment for {self.name}: {self.cure}")
        else:
            print(f"No known cure for {self.name}")

    def disease_info(self):
        print(f"Description of {self.name}: {self.description}")

    def lifecycle_progress(self):
        if self.life_cycles > 0:
            print(f"{self.name} has {self.life_cycles} remaining life cycles.")
        else:
            print(f"{self.name} has no life cycles left and may need urgent attention!")

    def is_lethal(self):
        return self.lethality

# function to simulate action with illness
def action(illness, action_code):
    if action_code == 1:
        # Disease info
        illness.disease_info()
    elif action_code == 2:
        # Cure treatment
        illness.cure_treatment()
    elif action_code == 3:
        # Lifecycle status
        illness.lifecycle_progress()
    elif action_code == 4:
        # Check lethality
        if illness.is_lethal():
            print(f"{illness.name} is lethal!")
        else:
            print(f"{illness.name} is not lethal!")
    else:
        print("Invalid action code!")

# last line