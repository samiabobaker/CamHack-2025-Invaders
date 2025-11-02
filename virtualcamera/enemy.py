from virtualcamera.canvas import SquareSprite
from random import randint

class EnemyBullet:
    def __init__(self, canvas, colour, x, y):
        self.sprite = SquareSprite(colour, x, y, 10, 20)
        canvas.add_sprite(self.sprite)
    
    def next_step(self):
        self.sprite.y += 10

class Enemy:
    def __init__(self, canvas, colour, x, y):
        self.sprite = SquareSprite(colour, x, y, 100, 100)
        self.og_x = x
        self.og_y = y
        self.delta = 0
        self.delta_dir = 1
        self.bullets = []
        self.canvas = canvas
        canvas.add_sprite(self.sprite)

    def spawn_bullet(self):
        bullet = EnemyBullet(self.canvas, self.sprite.colour, self.sprite.x + 50, self.sprite.y)
        self.bullets.append(bullet)
    
    def next_step(self):
        keep_bullets = []

        self.delta += self.delta_dir
        self.sprite.x = self.og_x + self.delta

        if abs(self.delta) > 50:
            self.delta_dir *= -1

        for bullet in self.bullets:
            bullet.next_step()
            if bullet.sprite.y < self.canvas.height:
                keep_bullets.append(bullet)
        self.bullets = keep_bullets
        if randint(0,99) == 0:
            #print("SPAWN")
            self.spawn_bullet()



    