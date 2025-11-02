import colorsys
import numpy as np
import pyvirtualcam
from virtualcamera.canvas import Canvas, SquareSprite
from virtualcamera.enemy import Enemy
from virtualcamera.player import Player
import pyautogui
import cv2
from PIL import Image
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np
import GestureRecognition as gr

model_path = "hand_landmarker.task"

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode


class Game:
    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.canvas = Canvas(width, height)

        self.players = []
        self.enemies = []

        # Load in enemy image
        enemy_img = np.asarray(Image.open('PublicEnemyNumber1.png').convert('RGB'))
        self.resized_enemy_img = cv2.resize(enemy_img, dsize=(100,100))

        for i in range(4):
            self.players.append(Player(self, self.canvas, np.array([255, 255, 255]), 100 + 140 * i, 500))
        
        self.spawn_enemies()

    def get_player_screenshots(self, screen):

        imgs = []

        clipped_screen = screen[131:131+186, 1509:1509+331]
        new_im = cv2.resize(clipped_screen, dsize=(100,100))
        imgs.append(new_im)

        clipped_screen = screen[331:331+186, 1509:1509+331]
        new_im = cv2.resize(clipped_screen, dsize=(100,100))
        imgs.append(new_im)

        clipped_screen = screen[532:532+186, 1509:1509+331]
        new_im = cv2.resize(clipped_screen, dsize=(100,100))
        imgs.append(new_im)

        clipped_screen = screen[734:734+186, 1509:1509+331]
        new_im = cv2.resize(clipped_screen, dsize=(100,100))
        imgs.append(new_im)

        return imgs

    def next_step(self, screenshot_frame):

        screenshots = self.get_player_screenshots(screenshot_frame)

        for index, p in enumerate(self.players):
                p.set_image(screenshots[index])

        for player in self.players:
            player.next_step()
        for enemy in self.enemies:
            enemy.next_step()
        
        if self.enemies is None:
            self.spawn_enemies()

    def spawn_enemies(self):
        for i in range(9):
            self.enemies.append(Enemy(self, self.canvas, 100 + 120 * i, 100, self.resized_enemy_img))

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
    options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path='hand_landmarker.task'),
    running_mode=VisionRunningMode.IMAGE, num_hands=1)
    with pyvirtualcam.Camera(width=1280, height=720, fps=20) as cam:
        with HandLandmarker.create_from_options(options) as landmarker:
            #print(f'Using virtual camera: {cam.device}')
            frame = np.zeros((cam.height, cam.width, 3), np.uint8)  # RGB

            game = Game(cam.width, cam.height)

            while True:
                img = pyautogui.screenshot()
                screenshot_frame = np.array(img)

                mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(screenshot_frame, cv2.COLOR_RGB2BGR))
                detection_result = landmarker.detect(mp_image)
                gr.detect_shoot(detection_result)
                gr.get_xpos(detection_result)

                game.next_step(screenshot_frame)

                frame = game.draw_frame()

                cam.send(frame)

                cam.sleep_until_next_frame()