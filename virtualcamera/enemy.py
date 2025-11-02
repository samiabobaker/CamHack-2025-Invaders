from virtualcamera.canvas import CameraSprite, SquareSprite
from random import randint
import numpy as np

class EnemyBullet:
    def __init__(self, canvas, colour, x, y):
        self.sprite = SquareSprite(colour, x, y, 10, 20)
        canvas.add_sprite(self.sprite)
    
    def next_step(self):
        self.sprite.y += 10

class Enemy:
    def __init__(self, game, canvas, x, y, img):
        self.sprite = CameraSprite(img, x, y, 100, 100)
        self.og_x = x
        self.og_y = y
        self.delta = 0
        self.delta_dir = 1
        self.bullets = []
        self.canvas = canvas
        self.game = game
        canvas.add_sprite(self.sprite)

    def spawn_bullet(self):
        bullet = EnemyBullet(self.canvas, np.array([255,255,255]), self.sprite.x + 50, self.sprite.y)
        self.bullets.append(bullet)
    
    def next_step(self):
        keep_bullets = []

        self.delta += self.delta_dir
        self.sprite.x = self.og_x + self.delta

        if abs(self.delta) > 50:
            self.delta_dir *= -1

        for bullet in self.bullets:
            bullet.next_step()
            for i, player in enumerate(self.game.players):
                if player.is_colliding_with_bullet(bullet):
                    self.game.remove_player(i)
                    continue


            if bullet.sprite.y < self.canvas.height:
                keep_bullets.append(bullet)
        self.bullets = keep_bullets
        if randint(0,199) == 0:
            #print("SPAWN")
            self.spawn_bullet()

    def is_colliding_with_bullet(self, bullet):
        if bullet.sprite.y > self.sprite.y and bullet.sprite.y < self.sprite.y + self.sprite.height and bullet.sprite.x > self.sprite.x and bullet.sprite.x < self.sprite.x + self.sprite.width:
            return True
        return False 



    