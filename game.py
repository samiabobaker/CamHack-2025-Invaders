from player import Player
from virtualcamera.canvas import Canvas

class Game:
    def __init__(self):
        self.canvas = Canvas()
        self.players = [Player() for i in range(4)]
        for i in range(4):
            self.players[i].x += i * 50
    