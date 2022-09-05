from binhex import LINELEN
from readline import set_completion_display_matches_hook
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
BUTTON_TEXT_COLOR = pygame.Color(0, 102, 0) # greenish
BUTTON_COLOR = pygame.Color(255, 255, 204) # very pale yellow
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


# dices 
def random_dices(CUP_CENTER):
    dices_locations = {
    'dice_1': (CUP_CENTER[0] - DICE_SIZE[0] / 2, CUP_CENTER[1] - 1.5 * DICE_SIZE[1]),
    'dice_2': (CUP_CENTER[0] - DICE_SIZE[0] - 30, CUP_CENTER[1] - DICE_SIZE[1]),
    'dice_3': (CUP_CENTER[0] + DICE_SIZE[0] - 20, CUP_CENTER[1] - 0.75 * DICE_SIZE[1]),
    'dice_4': (CUP_CENTER[0] - 1.1 * DICE_SIZE[0], CUP_CENTER[1] + 0.25 * DICE_SIZE[1]),
    'dice_5': (CUP_CENTER[0] + 0.25 * DICE_SIZE[0], CUP_CENTER[1] + DICE_SIZE[1] / 2)
    }
    dices = np.random.randint(1, 7, 5)
    print(dices)
    for dice in enumerate(dices):
        dice_img = pygame.image.load(f'pics/Dice-{dice[1]}-Y.jpg')
        dice_img = pygame.transform.scale(dice_img, DICE_SIZE)
        WIN.blit(dice_img, (dices_locations[f'dice_{dice[0] + 1}'][0], dices_locations[f'dice_{dice[0] + 1}'][1]))
        pygame.display.update()
    return dices


# possible moves
def liar_or_bid_window():
    bid_text_surface = BUTTONS_FONT.render('BID', True, BUTTON_TEXT_COLOR)
    bid_text_rectangle = bid_text_surface.get_rect()
    bid_text_rectangle.center = (BUTTON_BID_LOCATION[0] + BUTTON_SIZE[0] / 2, BUTTON_BID_LOCATION[1] + BUTTON_SIZE[1] / 2)

    liar_text_surface = BUTTONS_FONT.render('LIAR', True, BUTTON_TEXT_COLOR)
    liar_text_rectangle = bid_text_surface.get_rect()
    liar_text_rectangle.center = (BUTTON_LIAR_LOCATION[0] + BUTTON_SIZE[0] / 2.3, BUTTON_LIAR_LOCATION[1] + BUTTON_SIZE[1] / 2)

    pygame.draw.rect(WIN, BUTTON_COLOR, (BUTTON_BID_LOCATION, BUTTON_SIZE))
    pygame.draw.rect(WIN, BUTTON_TEXT_COLOR, (BUTTON_BID_LOCATION, BUTTON_SIZE), 4)
    pygame.draw.rect(WIN, BUTTON_COLOR, (BUTTON_LIAR_LOCATION, BUTTON_SIZE))
    pygame.draw.rect(WIN, BUTTON_TEXT_COLOR, (BUTTON_LIAR_LOCATION, BUTTON_SIZE), 4)

    WIN.blit(bid_text_surface, bid_text_rectangle)
    WIN.blit(liar_text_surface, liar_text_rectangle)
    pygame.display.update()

background()
first_player_dices = random_dices(PLAYER_ONE_POSITION)
liar_or_bid_window()

running = True

# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        fps_clock.tick()
