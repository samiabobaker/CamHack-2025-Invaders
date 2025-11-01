from player import Player

class Game:
    def __init__(self):
        self.players = [Player() for i in range(4)]
        for i in range(4):
            self.players[i].x += i * 50
        