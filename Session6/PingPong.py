import pygame
from pygame.locals import *

width = 800
height = 500
#Tao khung hien thi game
display_surf = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping Pong")

WHITE = (255, 255, 255)
pygame.draw.line(display_surf, WHITE, (width/2, 0), (width/2, height), 3)
pygame.draw.rect(display_surf, WHITE, (10, 10, 20, 20))
fps = 200 #so frame tren giay
fps_clock = pygame.time.Clock()

def main():
    pygame.init()

    while True:

        pygame.display.update()
        fps_clock.tick(fps)

if __name__ == "__main__":
    main()

