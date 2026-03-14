
"""
Pokemon

Attributes:
- name (str): The name of the Pokemon.
- type (str): The type of the Pokemon (e.g., Electric, Grass/Poison).
- hp (int): The health points of the Pokemon.
- attack (int): The attack stat of the Pokemon.
- defense (int): The defense stat of the Pokemon.

Methods:
- attack_opponent(self, opponent): Simulates an attack on another Pokemon, reducing their HP.
- evolve(): Simulates the evolution of a Pokemon, increasing its stats.


"""


class Pokemon:

    def __init__(self, name, type, hp, attack, defense):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def attack_opponent(self, opponent):
        dmg = 10
        opponent.hp -= dmg
        print(f"{self.name} attacks {opponent.name} and deals {dmg} damage!")

    def evolve(self):
        self.hp += 20
        self.attack += 10
        self.defense += 10
        self.name 
        print(f"{self.name} has evolved! Stats increased!")


    
pikachu = Pokemon("Pikachu", "Electric", 35, 55, 40)
bulbasaur = Pokemon("Bulbasaur", "Grass/Poison", 45, 49, 49)

print(pikachu.name)  # Output: Pikachu
print(pikachu.hp)  # Output: 35

pikachu.attack_opponent(bulbasaur)  # Output: Pikachu attacks Bulbasaur and deals 10 damage!