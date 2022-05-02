#Gavin Murdock
#4/14/22
#Doodle Jump
import pygame as pg
import random
from os import path
from settings import *
from tilemap import *
from sprites import *
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
        self.map = Map(path.join(game_folder,'map.txt'))
    def new(self):
        #start a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.players = []
        for row, tiles in enumerate(self.map.data):
            for col,tile in enumerate(tiles):
                if tile == '1':
                    Wall(self,col,row)
                if tile == 'P':
                    if len(self.players) >= 1:
                        pass
                    else:
                        self.player = Player(self, col,row)
                        self.players.append(self.player)

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

    def draw_grid(self):
        for x in range(0,WIDTH,TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x,0),(x,HEIGHT))
        for y in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        #game loop draw
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        # Draw all sprites
        self.all_sprites.draw(self.screen)
        # Must be the last thing called in the draw section
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