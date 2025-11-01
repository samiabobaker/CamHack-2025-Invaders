from virtualcamera.canvas import SquareSprite
import numpy as np

class Player:
    def __init__(self):
        self.sprites = [SquareSprite(np.array([255, 255, 255]), 500, 300, 20, 20)]
    
    def move_right(self):
        self.sprite.x += 10

    def move_left(self):
        self.sprite.x -= 10
    
    def shoot(self):
        self.sprites.append(PlayerBullet())

class PlayerBullet:
    def __init__(self):
        self.sprite = SquareSprite(np.array([255, 255, 255]), 500, 300, 2, 5)