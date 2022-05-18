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
PLAYER_HEALTH = 100
PLAYER_SPEED = 400
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
BULLET_DMG = 10

#Mob settings
MOB_IMG = "zombie1.png"
MOB_SPEED = 150
MOB_HEALTH = 100
MOB_DMG = 10
MOB_KNOCKBACK = 20
MOB_HIT_RECT = pg.Rect(0,0,30,30)
AVOID_RADIUS = 50
DETECT_RADIUS = 400

#Effects
MUZZLE_FLASHES = ["whitePuff15.png","whitePuff16.png","whitePuff17.png"
    ,"whitePuff18.png"]
FLASH_DURATION = 40

BOB_SPEED = 0.26
BOB_RANGE = 5

#Layers
WALL_LAYER = 1
ITEMS_LAYER = 1
PLAYER_LAYER = 2
BULLET_LAYER = 3
MOB_LAYER = 2
EFFECTS_LAYER = 4

#Itemms
ITEM_IMAGES = {'health':'health_pack.png'}
HEALTH_PACK_AMOUNT = 20

#sounds
BG_MUSIC = 'espionage.ogg'
PLAYER_HIT_SOUNDS = ['pain/8.wav', 'pain/9.wav', 'pain/10.wav', 'pain/11.wav']
ZOMBIE_MOAN_SOUNDS = ['brains2.wav', 'brains3.wav', 'zombie-roar-1.wav', 'zombie-roar-2.wav',
                      'zombie-roar-3.wav', 'zombie-roar-5.wav', 'zombie-roar-6.wav', 'zombie-roar-7.wav']
ZOMBIE_HIT_SOUNDS = ['splat-15.wav']
WEAPON_SOUNDS_GUN = ['sfx_weapon_singleshot2.wav']
EFFECTS_SOUNDS = {'level_start': 'level_start.wav',
                  'health_up': 'health_pack.wav'}