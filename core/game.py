
# Main loop of the game, where we will update and render all entities

from entities.player import Player
from world.map import Map

class Game:

    def init__(self):
        self.running = True
        self.player = Player("Ignacio", "Male")
        self.game_map = Map()

    def game_loop(self):
        return