import pygame
from pygame.locals import *

width = 800
height = 500
#Tao khung hien thi game
display_surf = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping Pong")

WHITE = (255, 255, 255)
# pygame.draw.line(display_surf, WHITE, (width/2, 0), (width/2, height), 3)
# pygame.draw.rect(display_surf, WHITE, (10, 10, 20, 20))
fps = 200 #so frame tren giay
fps_clock = pygame.time.Clock()

class Paddle:
    def __init__(self, w, h, x, y):
        self.width = w
        self.height = h
        self.x = x
        self.y = y
    def Draw(self):
        pygame.draw.rect(display_surf, WHITE, (self.x, self.y, self.width, self.height))
    def Move(self, pos):
        self.y += pos[1]

class AutoPaddle(Paddle):
    def __init__(self, w, h, x, y, speed):
        super.__init__(w, h, x, y)
        self.speed = speed
    def AutoMove(self, ball):
        self.y = ball.y - self.height/2

class Ball:
    def __init__(self, w, h, x, y, speed):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.speed = speed
        self.dir_x = 1 # 1 right and -1 left
        self.dir_y = 1 # 1 down and -1 up
    def Draw(self):
        pygame.draw.rect(display_surf, WHITE, (self.x, self.y, self.width, self.height))
    def Move(self):
        self.x = self.x + self.dir_x * self.speed
        self.y = self.y + self.dir_y * self.speed
    def Bounce(self, axis):
        if axis == "x":
            self.dir_y = self.dir_y * -1
        if axis == "y":
            self.dir_x = self.dir_x * -1
    def HitCeiling(self):
        if self.y == 0:
            return True
        else:
            return False
    def HitFloor(self):
        if self.x == (height - self.height):
            return True
        else:
            return False
    def HitAutoPaddle(self, autopaddle):
        if self.y >= (autopaddle.y - self.height) and self.y <= (autopaddle.y + autopaddle.height) and (self.x + self.width) >= autopaddle.x:
            return True
        else:
            return False