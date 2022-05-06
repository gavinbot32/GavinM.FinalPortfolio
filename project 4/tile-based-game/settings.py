import pygame as pg
# Settings
vec = pg.math.Vector2
# Game title
TITLE = "Tile Based Game"
# Screen size
WIDTH = 1024
HEIGHT= 768
# clock speed
FPS = 60
# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)
cfBLUE = (100, 149, 237)
GREY = (33,33,33)
LIGHTGREY = (100,100,100)
BROWN = (106,50,5)
BGCOLOR = BROWN
TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE


WALL_IMG = "tileGreen.png"
#Player Settings
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250 #drg/s
PLAYER_IMG = 'playerBlue.png'
PLAYER_HIT_RECT = pg.Rect(0,0,35,35)
BARREL_OFFSET = vec(30,10)

#Gun settings
BULLET_IMG = 'bullet.png'
BULLET_SPEED = 500
BULLET_LIFE = 1000
BULLET_RATE = 150
KICKBACK = 200
GUN_SPREAD = 5

#Mob settings
MOB_IMG = "zombie1.png"
MOB_SPEED = 150
MOB_HIT_RECT = pg.Rect(0,0,30,30)