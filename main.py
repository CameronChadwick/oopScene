import math
import pygame
# in terminal -> pip install pygame

# color constants
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# game constants
SIZE = (800, 800)
FPS = 60

##########################################################################

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Pygame Picture")

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():

        # check for user input
        if event.type == pygame.QUIT:
            running = False

    # game logic

    screen.fill(WHITE)

    pygame.display.flip()

    clock.tick(FPS)

# quit
pygame.quit()
