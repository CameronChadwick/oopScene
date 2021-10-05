import math
import pygame
# in terminal -> pip install pygame

# color constants
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRASSGREEN = (19, 112, 30)
BLUE = (0, 0, 255)
SKYBLUE = (66, 135, 245)
BLACK = (0, 0, 0)

# game constants
SIZE = (800, 600)
FPS = 60

########################################################################


class Grass():
    def __init__(self, grass_x, grass_y, width, height, color):
        self.x = grass_x
        self.y = grass_y
        self.width = width
        self.height = height
        self.color = color

    def draw_grass(self):
        point_list = (self.x, self.y, self.width, self.height)

        pygame.draw.rect(screen, self.color, point_list)


class Sky():
    def __init__(self, sky_x, sky_y, width, height, color):
        self.x = sky_x
        self.y = sky_y
        self.width = width
        self.height = height
        self.color = color

    def draw_sky(self):
        point_list = (self.x, self.y, self.width, self.height)

        pygame.draw.rect(screen, self.color, point_list)


class Road():
    def __init__(self, road_x, road_y, height, width, color1, color2):
        self.x = road_x
        self,y = road_y
        self.width = width
        self.height = height
        self.color1 = color1
        self.line = height//2-5
        self.linewidth = width
        self.lineheight = height//10
        self.color2 = color2

    def draw_road(self):
        road_points = ()


grass = Grass(0, 250, 800, 350, GRASSGREEN)
sky = Sky(0, 0, 800, 250, SKYBLUE)

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

    grass.draw_grass()
    sky.draw_sky()

    pygame.display.flip()

    clock.tick(FPS)

# quit
pygame.quit()
