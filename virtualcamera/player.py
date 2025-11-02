from virtualcamera.canvas import SquareSprite, CameraSprite
from random import randint
import numpy as np

class PlayerBullet:
    def __init__(self, canvas, colour, x, y):
        self.sprite = SquareSprite(colour, x, y, 10, 20)
        canvas.add_sprite(self.sprite)
    
    def next_step(self):
        self.sprite.y -= 10

class Player:
    def __init__(self, game, canvas, img, x, y):
        self.sprite = CameraSprite(img, x, y, 100, 100)
        self.bullets = []
        self.canvas = canvas
        self.game = game
        canvas.add_sprite(self.sprite)

    def set_image(self, img):
        self.sprite.img = img

    def spawn_bullet(self):
        bullet = PlayerBullet(self.canvas, np.array([255, 255, 255]), self.sprite.x + 50, self.sprite.y)
        self.bullets.append(bullet)
    
    def next_step(self, x):
        keep_bullets = []

        self.sprite.x = x

        for bullet in self.bullets:
            bullet.next_step()
            for i, enemy in enumerate(self.game.enemy):
                if enemy.is_colliding_with_bullet(bullet):
                    self.game.remove_enemy(i)
                    continue

            if bullet.sprite.y >= 0:
                keep_bullets.append(bullet)
        self.bullets = keep_bullets

    def is_colliding_with_bullet(self, bullet):
        if bullet.sprite.y > self.sprite.y and bullet.sprite.y < self.sprite.y + self.sprite.height and bullet.sprite.x > self.sprite.x and bullet.sprite.x < self.sprite.x + self.sprite.width:
            return True
        return False 



    