 #Gavin Murdock
#4/14/22
#Doodle Jump
import pygame as pg
import random
from settings import *
from sprites import *
from os import path

class Game:
    def __init__(self):
        #initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.last_update = 0
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data()
    def load_data(self):
        # load high score
        self.dir = path.dirname(__file__)
        asset_dir = path.join(self.dir,'assets')
        img_dir = path.join(asset_dir,'imgs')
        #load spritesheet
        self.spritesheet = Spritesheet(path.join(img_dir, SPRITESHEET))

    def update(self):
        #game loop-update
        self.all_sprites.update()
        for player in self.players:
            if player.vel.y > 0:
                hits = pg.sprite.spritecollide(player, self.platforms, False)
                if hits:
                    lowest = hits[0]
                    for hit in hits:
                        if hit.rect.bottom > lowest.rect.bottom:
                            lowest = hit
                    if player.pos.y < lowest.rect.bottom:
                        player.pos.y = lowest.rect.top
                        player.vel.y = 0




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
                for player in self.players:
                    now = pg.time.get_ticks()
                    if event.key == player.keybinds[0]:
                        player.jump()
                    if event.key == player.keybinds[3]:
                        if now - self.last_update > 150:
                            self.last_update = now
                            player.punch()
    def new(self):
        #start a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.players = []
        for i in range(2):
            player = Player(self, KEYBIND_GP[i],PLAYER_COLORS[i])
            self.players.append(player)
            self.all_sprites.add(player)
        for plat in PLATFORM_LIST:
            p = Platform(self, *plat)
            self.all_sprites.add(p)
            self.platforms.add(p)

        self.run()
    def run(self):
        #game loop

        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def draw(self):
        #game loop draw
        self.screen.fill(cfBLUE)
        # Draw all sprites
        self.all_sprites.draw(self.screen)
        for i in range(len(self.players)):
            player = self.players[i]
            self.screen.blit(player.image,player.rect)
        for i in range(len(self.players)):
            player = self.players[i]
            self.draw_text(str(i+1),22,WHITE,player.rect.x+ player.rect.width / 2,player.rect.y- player.rect.width // 4)
        # Must be the last thing called in the draw section
        pg.display.flip()
    def show_start_screen(self):
        #start screen Template
        self.screen.fill(cfBLUE)
        self.draw_text(TITLE,48,WHITE,WIDTH/2, HEIGHT/4)
        self.draw_text("This is a Template Screen", 22,WHITE,WIDTH / 2, HEIGHT/2)
        self.draw_text("Press a key to play", 22,WHITE,WIDTH/2,HEIGHT * 3/4)
        pg.display.flip()
        self.wait_for_key()
    def show_go_screen(self):
        #game over screen
        if not self.running:
            return
        self.screen.fill(cfBLUE)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH / 2, HEIGHT / 2 - 30)
        self.draw_text("Press a key to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()
    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(30)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False
    def draw_text(self,text,size,color,x,y):
        font = pg.font.Font(self.font_name,size)
        text_surface = font.render(text,True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface,text_rect)
g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()