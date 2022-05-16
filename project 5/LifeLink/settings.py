import pygame as pg
# Settings
vec = pg.math.Vector2
# Game title
TITLE = "LifeLink"
FONT_NAME = "EightBitDragon-anqx.ttf"
# Screen size
WIDTH = 1920
HEIGHT= 1080
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
BGCOLOR = GREY
TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

#BASE SETTINGS
BASE_IMG = "baseIMG.png"
MAP_FILE = "map.txt"

#Upgrade Settings
DMG_IMG = "dmgImg.png"
SPEED_IMG = "speedImg.png"
LIFE_IMG = "lifeImg.png"
ROF_IMG = "rofImg.png"
PHOENIX_IMG = "pheonixImg.png"
PLAY_IMG = "play.png"
QUIT_IMG = "Quit.png"
#Player Settings
PLAYER_HEALTH = 100
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 300 #drg/s
PLAYER_HIT_RECT = pg.Rect(0,0,35,35)
BARREL_OFFSET = vec(30,10)
PLAYER_IMG = "Player.png"

#Gun settings
BULLET_SPEED = 500
BULLET_LIFE = 1000
BULLET_RATE = 150
KICKBACK = 200
GUN_SPREAD = 5
BULLET_DMG = 10

#Mob settings
MOB_SPEED = 150
MOB_HEALTH = 100
MOB_DMG = 10
MOB_KNOCKBACK = 20
MOB_HIT_RECT = pg.Rect(0,0,30,30)
MOB_IMG = "Enemy.png"


