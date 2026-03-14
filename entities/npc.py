class NPC:

    def __init__(self, name, dialogue):
        self.name = name
        self.dialogue = dialogue

    def talk(self):
        print(f"{self.name} says: {self.dialogue}")


ncp1 = NPC("Old Man", "Welcome to the world of Pokemon!")
ncp1.talk()  # Output: Old Man says: Welcome to the world of Pokemon!