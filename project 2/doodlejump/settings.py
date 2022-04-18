# Settings
# Game title
TITLE = "Doodle Jump"
FONT_NAME = "arial"
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"
# Screen size
WIDTH = 480
HEIGHT= 600
# clock speed
FPS = 60

#Player Properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAVITY = 0.8
#Starting Platforms
PLATFORM_LIST = [(0, HEIGHT-40, WIDTH,40),
                 (WIDTH / 2 -50, HEIGHT * 3 / 4,100,20),
                 (125,HEIGHT-350,100,20),(350,200,100,20),
                 (175,100,100,20)]
# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
cfBLUE = (100, 149, 237)
YELLOW = (255,255,0)