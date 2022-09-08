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
BUTTONS_FONT = pygame.font.SysFont('ubuntu', 40, italic=True)

# define table geometry
TABLE_RADIUS = 400 
TABLE_CENTER_X, TABLE_CENTER_Y = (int(WIDTH / 2), int(HEIGHT / 2))
CUP_RADIUS = 100

# define dice geometry
DICE_SIZE_X, DICE_SIZE_Y = (50, 50)

# define players' position on the table
PLAYER_ONE_POSITION = (TABLE_CENTER_X, HEIGHT - CUP_RADIUS - 50)

# visualise background
def background():
    WIN.fill(WHITE)
    pygame.draw.circle(WIN, BROWN_SIENNA, (TABLE_CENTER_X, TABLE_CENTER_Y), TABLE_RADIUS)
    pygame.display.update()


def button(colour: pygame.Color, location: tuple, size: tuple, border=False, border_colour = None):
    BUTTON_LOCATION = (location[0] - size[0] / 2, location[1] - size[1] / 2)
    button_rectangle = pygame.draw.rect(WIN, colour, (BUTTON_LOCATION, size))
    if border:
        pygame.draw.rect(WIN, border_colour, (BUTTON_LOCATION, size), 4) 
    return button_rectangle


def button_text(text, font: pygame.font, colour: pygame.Color, location: tuple):
    button_text_surface = BUTTONS_FONT.render(text, True, colour)
    button_text_rectangle = button_text_surface.get_rect()
    button_text_rectangle.center = location
    return button_text_surface, button_text_rectangle


# dices 
def random_dices(CUP_CENTER):
    dices_locations = {
    'dice_1': (CUP_CENTER[0] - DICE_SIZE_X / 2, CUP_CENTER[1] - 1.5 * DICE_SIZE_Y),
    'dice_2': (CUP_CENTER[0] - DICE_SIZE_X - 30, CUP_CENTER[1] - DICE_SIZE_Y),
    'dice_3': (CUP_CENTER[0] + DICE_SIZE_X - 20, CUP_CENTER[1] - 0.75 * DICE_SIZE_Y),
    'dice_4': (CUP_CENTER[0] - 1.1 * DICE_SIZE_X, CUP_CENTER[1] + 0.25 * DICE_SIZE_Y),
    'dice_5': (CUP_CENTER[0] + 0.25 * DICE_SIZE_X, CUP_CENTER[1] + DICE_SIZE_Y / 2)
    }
    dices = np.random.randint(1, 7, 5)
    print(dices)
    for dice in enumerate(dices):
        dice_img = pygame.image.load(f'pics/Dice-{dice[1]}-Y.jpg')
        dice_img = pygame.transform.scale(dice_img, (DICE_SIZE_X, DICE_SIZE_Y))
        WIN.blit(dice_img, (dices_locations[f'dice_{dice[0] + 1}'][0], dices_locations[f'dice_{dice[0] + 1}'][1]))
        pygame.display.update()
    return dices


# possible moves
def liar_or_bid_window():
    BUTTON_SIZE_X, BUTTON_SIZE_Y = (150, 50)
    BID_BUTTON_LOCATION = (TABLE_CENTER_X - BUTTON_SIZE_X / 2, TABLE_CENTER_Y + BUTTON_SIZE_Y / 2)
    LIAR_BUTTON_LOCATION = (TABLE_CENTER_X + BUTTON_SIZE_X / 2 + 20, TABLE_CENTER_Y + BUTTON_SIZE_Y / 2)
    
    bid_button = button(BUTTON_COLOR, BID_BUTTON_LOCATION, (BUTTON_SIZE_X, BUTTON_SIZE_Y), border=True, border_colour=BUTTON_TEXT_COLOR)
    bid_text_surface, bid_text_rectangle = button_text('BID', BUTTONS_FONT, BUTTON_TEXT_COLOR, BID_BUTTON_LOCATION)

    liar_button = button(BUTTON_COLOR, LIAR_BUTTON_LOCATION, (BUTTON_SIZE_X, BUTTON_SIZE_Y), border=True, border_colour=BUTTON_TEXT_COLOR)
    liar_text_surface, liar_text_rectangle = button_text('LIAR', BUTTONS_FONT, BUTTON_TEXT_COLOR, LIAR_BUTTON_LOCATION)
    WIN.blit(bid_text_surface, bid_text_rectangle)
    WIN.blit(liar_text_surface, liar_text_rectangle)
    pygame.display.update()
    return liar_button, bid_button


background()
first_player_dices = random_dices(PLAYER_ONE_POSITION)
liar_button, bid_button = liar_or_bid_window()

running = True

mouse_x = 0
mouse_y = 0

# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if bid_button.right >= mouse_x >= bid_button.left and bid_button.bottom >= mouse_y >= bid_button.top: 
                print('bid')
            elif liar_button.right >= mouse_x >= liar_button.left and liar_button.bottom >= mouse_y >= liar_button.top:
                print('liar')
            else:
                print('out of range')     
        fps_clock.tick()
