import colorsys
import numpy as np
import pyvirtualcam
from virtualcamera.canvas import Canvas, SquareSprite
from virtualcamera.enemy import Enemy

def start_game():
    with pyvirtualcam.Camera(width=1280, height=720, fps=20) as cam:
        print(f'Using virtual camera: {cam.device}')
        frame = np.zeros((cam.height, cam.width, 3), np.uint8)  # RGB

        canvas = Canvas(cam.width, cam.height)

        enemies = []

        for i in range(9):
            enemies.append(Enemy(canvas, np.array([50, 168, 82]), 100 + 120 * i, 100))


        while True:
            frame = canvas.draw_frame(cam)

            for enemy in enemies:
                enemy.next_step()

            cam.send(frame)

            cam.sleep_until_next_frame()