from virtualcamera.canvas import SquareSprite
from random import randint

class PlayerBullet:
    def __init__(self, canvas, colour, x, y):
        self.sprite = SquareSprite(colour, x, y, 10, 20)
        canvas.add_sprite(self.sprite)
    
    def next_step(self):
        self.sprite.y -= 10

class Player:
    def __init__(self, canvas, colour, x, y):
        self.sprite = SquareSprite(colour, x, y, 100, 100)
        self.bullets = []
        self.canvas = canvas
        canvas.add_sprite(self.sprite)
        self.frame_count = 0

    def spawn_bullet(self):
        bullet = PlayerBullet(self.canvas, self.sprite.colour, self.sprite.x + 50, self.sprite.y)
        self.bullets.append(bullet)
    
    def next_step(self, x):
        self.frame_count += 1
        keep_bullets = []

        self.sprite.x = x

        for bullet in self.bullets:
            bullet.next_step()
            if bullet.sprite.y >= 0:
                keep_bullets.append(bullet)
        self.bullets = keep_bullets
        #print(self.frame_count)



    