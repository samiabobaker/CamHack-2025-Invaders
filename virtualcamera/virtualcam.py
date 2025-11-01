import colorsys
import numpy as np
import pyvirtualcam
from virtualcamera.canvas import Canvas, SquareSprite

def start_game():
    with pyvirtualcam.Camera(width=1280, height=720, fps=20) as cam:
        print(f'Using virtual camera: {cam.device}')
        frame = np.zeros((cam.height, cam.width, 3), np.uint8)  # RGB

        canvas = Canvas()
        sprite = SquareSprite(np.array([50, 168, 82]), 500, 300, 20, 20)

        canvas.add_sprite(sprite)

        while True:
            frame = canvas.draw_frame(cam)

            cam.send(frame)

            cam.sleep_until_next_frame()