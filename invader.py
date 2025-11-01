from virtualcamera.canvas import SquareSprite
import numpy as np

class Invader:
    def __init__(self):
        self.sprite = SquareSprite(np.array([255, 255, 255]), 500, 300, 20, 20)