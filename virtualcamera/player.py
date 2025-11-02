from virtualcamera.canvas import SquareSprite, CameraSprite
from random import randint
import numpy as np
import cv2

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
        self.lives = 3
        self.cooldown = 0
        canvas.add_sprite(self.sprite)

    def apply_tint(self, img):
        tint_color = np.array([255, 0, 0], dtype=np.uint8)  # Light orange-blue tint
        # Create a solid color image of the same size
        tint_layer = np.full_like(img, tint_color)

        # Blend the original image with the tint layer
        alpha = 0.25*(3-self.lives)  # Tint strength (0 = no tint, 1 = full tint)
        tinted_image = cv2.addWeighted(img, 1 - alpha, tint_layer, alpha, 0)
        return tinted_image

    def set_image(self, img):
        self.sprite.img = self.apply_tint(img)

    def spawn_bullet(self):
        bullet = PlayerBullet(self.canvas, np.array([255, 255, 255]), self.sprite.x + 50, self.sprite.y)
        self.bullets.append(bullet)
    
    def next_step(self):
        keep_bullets = []

        if self.cooldown > 0:
            self.cooldown -= 1

        for bullet in self.bullets:
            bullet.next_step()
            for i, enemy in enumerate(self.game.enemy):
                if enemy.is_colliding_with_bullet(bullet):
                    self.game.remove_enemy(i)
                    continue

            if bullet.sprite.y >= 0:
                keep_bullets.append(bullet)
        self.bullets = keep_bullets

    def set_position(self, x):
        self.sprite.x = x

    def shoot(self):
        if self.cooldown == 0:
            self.spawn_bullet()
            self.cooldown = 100

    def is_colliding_with_bullet(self, bullet):
        if bullet.sprite.y > self.sprite.y and bullet.sprite.y < self.sprite.y + self.sprite.height and bullet.sprite.x > self.sprite.x and bullet.sprite.x < self.sprite.x + self.sprite.width:
            return True
        return False 



    