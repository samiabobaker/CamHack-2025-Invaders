from player import Player

class Game:
    def __init__(self):
        self.players = [Player(), Player(), Player(), Player()]
        self.invaders = []
        for i in range(4):
            self.players[i].x += i * 50