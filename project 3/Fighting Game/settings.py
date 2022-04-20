import pygame as pg
# Settings
# Game title
TITLE = "Fighting Game"
FONT_NAME = "arial"
SPRITESHEET = "spritesheet.png"
# Screen size
WIDTH = 1920
HEIGHT= 1080
# clock speed
FPS = 60

#Player Properties
PLAYER_ACC = 2
PLAYER_FRICTION = -0.12
PLAYER_GRAVITY = 0.9

PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH + 40, 40)]
# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
cfBLUE = (100, 149, 237)
YELLOW = (255,255,0)
#KEYBINDS [Jump,Left,Right,Punch]
PLAYER_ONE_KB = [pg.K_w, pg.K_a,pg.K_d,pg.K_e]
PLAYER_TWO_KB = [pg.K_UP,pg.K_LEFT,pg.K_RIGHT,pg.K_KP1]
KEYBIND_GP = [PLAYER_ONE_KB, PLAYER_TWO_KB]
PLAYER_COLORS = [BLUE,RED]
