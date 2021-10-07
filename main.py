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
WINDOWBLUE = (148, 189, 255)
BLACK = (0, 0, 0)
BROWN = (43, 24, 14)
GRAY = (117, 109, 102)

# game constants
SIZE = (800, 600)
FPS = 60

########################################################################

class House():
    def __init__(self, x, y, width, height, radius, color1, color2, color3, color4, color5):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.radius = radius
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.color4 = color4
        self.color5 = color5


    def draw_house(self):
        mainhouse = (self.x, self.y, self.width, self.height)
        roof = ([self.x, self.y], [self.x + 50, self.y - 50], [self.x + 100, self.y])
        door = (self.x + 10, self.y + 50, self.width - 70, self.height - 50)
        doorknob = ([self.x + 15, self.y + 75], self.radius)
        path = (self.x + 5, self.y + 100, self.width - 60, self.height - 75)
        window1 = (self.x + 55, self.y + 55, self. width - 70, self.height - 70)
        window2 = (self.x + 35, self.y, self.width - 70, self.height - 70)


        pygame.draw.rect(screen, self.color1, mainhouse)
        pygame.draw.polygon(screen, self.color1, roof)
        pygame.draw.rect(screen, self.color2, door)
        pygame.draw.circle(screen, self.color5, doorknob)
        pygame.draw.rect(screen, self.color3, path)
        pygame.draw.rect(screen, self.color4, window1)
        pygame.draw.rect(screen, self.color4, window2)


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
    def __init__(self, road_x, road_y, height, width, color1, linex, liney, linewidth, lineheight, color2):
        self.x = road_x
        self.y = road_y
        self.width = width
        self.height = height
        self.color1 = color1
        self.linex = linex
        self.liney = liney
        self.linewidth = linewidth
        self.lineheight = lineheight
        self.color2 = color2

    def draw_road(self):
        road_points = (self.x, self.y, self.width, self.height)
        line_points = (self.linex, self.liney, self.linewidth, self.lineheight)

        pygame.draw.rect(screen, self.color1, road_points)
        pygame.draw.rect(screen, self.color2, line_points)


grass = Grass(0, 200, 800, 400, GRASSGREEN)
sky = Sky(0, 0, 800, 200, SKYBLUE)
road = Road(0, 400, 150, 800, BLACK, 0, 470, 800, 15, YELLOW)
house1 = House(50, 275, 100, 100, 5, BLACK, WHITE, GRAY, WINDOWBLUE, BROWN)

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
    road.draw_road()
    house1.draw_house()

    pygame.display.flip()

    clock.tick(FPS)

# quit
pygame.quit()
