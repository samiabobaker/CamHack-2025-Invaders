import numpy as np

class Canvas:
    def __init__(self):
        self.sprites = []

    def add_sprite(self, sprite):
        self.sprites.append(sprite)

    def draw_frame(self, cam):
        frame = np.zeros((cam.height, cam.width, 3), np.uint8)
        for sprite in self.sprites:
            sprite.draw(frame)
        return frame


class SquareSprite:
    def __init__(self, colour, x, y, width, height):
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, frame):
        square = np.full((self.width, self.height, 3), self.colour)
        frame[self.x:self.x+self.width, self.y:self.y+self.height] = square