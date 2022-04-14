#Gavin Murdock
#4/14/22
#Doodle Jump
import pygame as pg
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        #initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
    def new(self):
        #start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        p1 = Platform(0, HEIGHT - 40, WIDTH, 40)
        self.all_sprites.add(p1)
        self.platforms.add(p1)
        p2 = Platform( WIDTH /2 - 50,HEIGHT * 3/4, 100,20)
        self.all_sprites.add(p2)
        self.platforms.add(p2)

        self.run()
    def run(self):
        #game loop

        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    def update(self):
        #game loop-update
        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player,self.platforms,False)
        if hits:

            self.player.vel.y = 1
            self.player.pos.y = hits[0].rect.top

    def events(self):
        #game loop events
        for event in pg.event.get():
            # If the red X was clicked, close the program
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
    def draw(self):
        #game loop draw
        self.screen.fill(cfBLUE)
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