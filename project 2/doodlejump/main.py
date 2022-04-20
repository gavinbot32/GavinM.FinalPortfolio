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
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data()

    def load_data(self):
        # load high score
        self.dir = path.dirname(__file__)
        asset_dir = path.join(self.dir,'assets')
        img_dir = path.join(asset_dir,'imgs')
        with open(path.join(self.dir,HS_FILE),'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
        #load spritesheet image
        self.spritesheet = Spritesheet(path.join(img_dir,SPRITESHEET))
    def new(self):
        #start a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
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
    def update(self):
        #game loop-update
        self.all_sprites.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit
                if self.player.pos.y < lowest.rect.bottom:
                    self.player.pos.y = lowest.rect.top
                    self.player.vel.y = 0
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += max(abs(self.player.vel.y),10)
            for plat in self.platforms:
                plat.rect.y += max(abs(self.player.vel.y),10)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    self.score +=1

        #DIE
        if self.player.rect.bottom > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -=max(self.player.vel.y,10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.platforms) == 0:
            self.playing = False
        #spawn new platforms to keep same average
        while len(self.platforms) < 6:
            width = random.randrange(50,100)
            p = Platform(self,random.randrange(0,WIDTH - width),
                         random.randrange(-50,-30))
            self.platforms.add(p)
            self.all_sprites.add(p)

    def events(self):
        #game loop events
        for event in pg.event.get():
            # If the red X was clicked, close the program
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    def draw(self):
        #game loop draw
        self.screen.fill(cfBLUE)
        # Draw all sprites
        self.all_sprites.draw(self.screen)
        self.screen.blit(self.player.image,self.player.rect)
        self.draw_text(str(self.score),22,WHITE,WIDTH/2,15)
        # Must be the last thing called in the draw section
        pg.display.flip()
    def show_start_screen(self):
        #start screen
        self.screen.fill(cfBLUE)
        self.draw_text(TITLE,48,WHITE,WIDTH/2, HEIGHT/4)
        self.draw_text("Arrows to move, Space to jump", 22,WHITE,WIDTH / 2, HEIGHT/2)
        self.draw_text("Press a key to play", 22,WHITE,WIDTH/2,HEIGHT * 3/4)
        self.draw_text("High Score: " + str(self.highscore),22,WHITE,WIDTH / 2,15)
        pg.display.flip()
        self.wait_for_key()
    def show_go_screen(self):
        #game over screen
        if not self.running:
            return
        self.screen.fill(cfBLUE)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH / 2, HEIGHT / 2 - 30)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("NEW HIGH SCORE!", 22, GREEN,WIDTH/2,HEIGHT / 2 + 50)
            with open(path.join(self.dir,HS_FILE), 'w') as f:
                f.write(str(self.score))
        self.draw_text("High Score: " + str(self.highscore), 22, WHITE, WIDTH / 2,  HEIGHT / 2)
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