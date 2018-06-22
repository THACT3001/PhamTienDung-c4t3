import pygame
from pygame import *

width = 500
height = 600

display_surf = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

fps = 200 #so frame tren giay
fps_clock = pygame.time.Clock()

def main():
    pygame.init()

    while True:

        pygame.display.update()
        fps_clock.tick(fps)

if __name__ == "__main__":
    main()
