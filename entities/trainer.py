from entities.npc import NPC

class Trainer(NPC):

    def __init__(self, name, dialogue, team):
        super().__init__(name, dialogue)
        self.team = team

    def battle(self):
        print(f"{self.name} challenges you to a battle!")

trainer1 = Trainer(
    "Ash",
    "I choose you, Pikachu!",
    ["Pikachu", "Bulbasaur", "Charmander"]
)

trainer1.talk()  # Output: Ash says: I choose you, Pikachu!
trainer1.battle()  # Output: Ash challenges you to a battle!