import pygame
import numpy as np 
import sys

pygame.init()

# define frames per second 
FPS = 60
fps_clock = pygame.time.Clock()

# create window
WIDTH, HEIGHT = 1200, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Liars Dice')

# define colours 
WHITE = pygame.Color(255, 255, 255)
BROWN_SIENNA = pygame.Color(160, 82, 45)
GREEN = pygame.Color(0, 255, 0)
PLAYER_ONE_COLOR = pygame.Color(253, 253, 150) # yellow player
PLAYER_TWO_COLOR = pygame.Color(177, 156, 217) # purple player


# define fonts 
BUTTONS_FONT = pygame.font.SysFont('Calibri', 50)

# define table geometry
TABLE_RADIUS = 400 
TABLE_CENTER = (int(WIDTH / 2), int(HEIGHT / 2))
CUP_RADIUS = 100

# define dice geometry
DICE_SIZE = (50, 50)

# move buttons
BUTTON_SIZE = (150, 50)
BUTTON_BID_LOCATION = (TABLE_CENTER[0] - BUTTON_SIZE[0], TABLE_CENTER[1])
BUTTON_LIAR_LOCATION = (TABLE_CENTER[0] + 20, TABLE_CENTER[1])

# define players' position on the table
PLAYER_ONE_POSITION = (TABLE_CENTER[0], HEIGHT - CUP_RADIUS - 50)

# visualise background
def background():
    WIN.fill(WHITE)
    pygame.draw.circle(WIN, BROWN_SIENNA, (TABLE_CENTER), TABLE_RADIUS)
    pygame.display.update()

background()

running = True

# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        fps_clock.tick()
