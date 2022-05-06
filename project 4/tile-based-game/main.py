#Gavin Murdock
#4/14/22
#Doodle Jump
import pygame as pg
import random
import sys
from os import path
from settings import *
from tilemap import *
from sprites import *


#HUD
def draw_player_health(surf,x,y,pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 250
    BAR_HEIGHT = 30
    fill = pct * BAR_LENGTH
    outline_rect = pg.Rect(x,y,BAR_LENGTH,BAR_HEIGHT)
    fill_rect = pg.Rect(x,y,fill, BAR_HEIGHT)
    if pct > 0.6:
        col = GREEN
    elif pct > 0.3:
        col = YELLOW
    else:
        col = RED
    pg.draw.rect(surf,col,fill_rect)
    pg.draw.rect(surf,WHITE,outline_rect,2)

class Game:
    def __init__(self):
        #initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500,100)
        self.running = True
        self.load_data()
    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder,'imgs')
        self.map = Map(path.join(game_folder,'map.txt'))
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.mob_img = pg.image.load(path.join(img_folder, MOB_IMG)).convert_alpha()
        self.bullet_img = pg.image.load(path.join(img_folder, BULLET_IMG)).convert_alpha()
        self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()
        self.wall_img = pg.transform.scale(self.wall_img, (TILESIZE,TILESIZE))
        self.player_img = pg.transform.scale(self.player_img, (int(TILESIZE*0.75),int(TILESIZE*0.75)))
        self.mob_img = pg.transform.scale(self.mob_img, (int(TILESIZE*0.75),int(TILESIZE*0.75)))
    def new(self):
        #start a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.players = []
        for row, tiles in enumerate(self.map.data):
            for col,tile in enumerate(tiles):
                if tile == '1':
                    Wall(self,col,row)
                if tile == 'M':
                    Mob(self,col,row)
                if tile == 'P':
                    if len(self.players) >= 1:
                        pass
                    else:
                        self.player = Player(self, col,row)
                        self.players.append(self.player)
        self.camera = Camera(self.map.width,self.map.height)
        self.run()
    def run(self):
        #game loop

        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
    def update(self):
        #game loop-update
        self.all_sprites.update()
        self.camera.update(self.player)


    def events(self):
        #game loop events
        for event in pg.event.get():
            # If the red X was clicked, close the program
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if self.playing:
                        self.playing = False
                    self.running = False
        hits = pg.sprite.groupcollide(self.mobs, self.bullets, False, True)
        for hit in hits:
            hit.health -= BULLET_DMG
            hit.vel = vec(0,0)
        hits = pg.sprite.spritecollide(self.player, self.mobs, False, False)
        for hit in hits:
            self.player.health -= MOB_DMG
            hit.vel = vec(0, 0)
            if self.player.health <=0:
                self.playing = False
        if hits:
            self.player.pos += vec(MOB_KNOCKBACK,0).rotate(-hits[0].rot)
    def draw_grid(self):
        for x in range(0,WIDTH,TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x,0),(x,HEIGHT))
        for y in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        pg.display.set_caption("{:.1f}".format(self.clock.get_fps()))
        #game loop draw
        self.screen.fill(BGCOLOR)
        # self.draw_grid()
        # Draw all sprites
        for sprite in self.all_sprites:
            if isinstance(sprite,Mob):
                sprite.draw_health()
            self.screen.blit(sprite.image,self.camera.apply(sprite))
        # Must be the last thing called in the draw section

        #HUD
        draw_player_health(self.screen,10,10,self.player.health/PLAYER_HEALTH)

        pg.display.flip()
    def show_start_screen(self):
        #start screen
        pass
    def show_go_screen(self):
        #game over screen
        pass
g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()