import colorsys
import numpy as np
import pyvirtualcam
from virtualcamera.canvas import Canvas, SquareSprite
from virtualcamera.enemy import Enemy
from virtualcamera.player import Player
import pyautogui
import cv2
from PIL import Image


class Game:
    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.canvas = Canvas(width, height)

        self.players = []
        self.enemies = []

        # Load in enemy image
        enemy_img = np.asarray(Image.open('PublicEnemyNumber1.png').convert('RGB'))

        print(enemy_img.shape)
        resized_enemy_img = cv2.resize(enemy_img, dsize=(100,100))

        for i in range(1):
            self.players.append(Player(self, self.canvas, np.array([255, 255, 255]), 100 + 120 * i, 500))
        for i in range(9):
            self.enemies.append(Enemy(self, self.canvas, 100 + 120 * i, 100, resized_enemy_img))

    def next_step(self, screenshot_frame):
        for p in self.players:
                p.set_image(screenshot_frame)

        for player in self.players:
            player.next_step(100)
        for enemy in self.enemies:
            enemy.next_step()
    
    def draw_frame(self):
        return self.canvas.draw_frame(self.width, self.height)
    
    def damage_player(self, i):
        self.players[i].lives -= 1

        if self.players[i].lives == 0: 
            self.canvas.remove_sprite(self.players[i].sprite)
            del self.players[i]

    def remove_enemy(self, i):
        self.canvas.remove_sprite(self.enemies[i].sprite)
        del self.enemies[i]

def start_game():

    with pyvirtualcam.Camera(width=1280, height=720, fps=20) as cam:
        print(f'Using virtual camera: {cam.device}')
        frame = np.zeros((cam.height, cam.width, 3), np.uint8)  # RGB

        game = Game(cam.width, cam.height)

        while True:
            img = pyautogui.screenshot(region=(0,0,500,500))
            screenshot_frame = np.array(img)
            screenshot_frame = cv2.resize(screenshot_frame, dsize=(100,100))

            game.next_step(screenshot_frame)

            frame = game.draw_frame()

            cam.send(frame)

            cam.sleep_until_next_frame()