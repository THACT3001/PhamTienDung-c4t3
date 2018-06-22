import random
import pygame
from pygame.locals import *

width = 500
height = 600

#Tao khung hien thi game
display_surf = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

GREEN = (0, 255, 0)

YELLOW = (255, 140, 0)

fps = 200 #so frame tren giay
fps_clock = pygame.time.Clock()

class Point:
    def __init__(self, r, x, y):
        self.centerx = x
        self.centery = y
        self.radius = r
    def Draw(self):
        pygame.draw.circle(display_surf, YELLOW, (self.centerx, self.centery), self.radius)

class Snake:
    def __init__(self, part_position, radius):
        self.radius = radius
        self.part_position = part_position

    def Draw(self):
        for part in self.part_position:
            pygame.draw.circle(display_surf, GREEN, part, self.radius)

    def HitPoint(self, Point):
        if Point.centery - Point.radius <= self.part_position[-1].y + self.radius \
            or Point.centery + Point.radius >= self.part_position[-1].x - self.radius and Point.centerx + Point.radius >= \
            self.part_position[-1].x - self.radius or Point.centerx - Point.radius <= self.part_position[-1].x + self.radius:
            return True
        else:
            return False

    def HitBody(self):
        for part in range(len(self.part_position) - 1):
            if self.part_position[part] == self.part_position[-1]:
                return True
            else:
                return False

    def HitWall(self):
        if self.part_position[-1][0] <= 0 or self.part_position[-1][0] >= width or self.part_position[-1][1] <= 0 \
            or self.part_position.[-1][1] >= height:
            return True
        else:
            return False

    def EatPoint(self, point, part):
        point.centerx = random.randrange(0, width)
        point.centery = random.randrange(0, height)
        self.part_position.insert(self, 0, part)

    def Move(self, direction):
        if direction == "Forward":
            self.part_position.insert(self, 0, self.part_position[0])
            self.part_position.pop(self, 0)
        elif direction == "Backward":
            self.part_position.insert(self, -1, self.part_position[0])
            self.part_position.pop(self, -1)
        elif direction == "Right":
            self.part_position.insert



if __name__ == "__main__":
    main()







