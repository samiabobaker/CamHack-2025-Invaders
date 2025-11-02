import numpy as np

class Canvas:
    def __init__(self, width, height):
        self.sprites = []
        self.width = width
        self.height = height

    def add_sprite(self, sprite):
        self.sprites.append(sprite)

    def remove_sprite(self, sprite):
        self.sprites.remove(sprite)

    def draw_frame(self, width, height):
        frame = np.zeros((height, width, 3), np.uint8)
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
        if self.x + self.width >= len(frame[0]) or self.y + self.height >= len(frame):
            return

        square = np.full((self.height, self.width, 3), self.colour)

        frame[self.y:self.y+self.height, self.x:self.x+self.width] = square

class CameraSprite:
    def __init__(self, img, x, y, width, height):
        self.img = img
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, frame):
        if self.x + self.width >= len(frame[0]) or self.y + self.height >= len(frame):
            return

        frame[self.y:self.y+self.height, self.x:self.x+self.width] = self.img