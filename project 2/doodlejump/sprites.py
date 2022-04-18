#Sprite Classes
import pygame
from settings import *
import pygame as pg
vec = pg.math.Vector2
class Spritesheet:
    #utility class for loading and parsing spritesheets
    def __init__(self,filename):
        self.spritesheet = pg.image.load(filename).convert()
    def get_image(self,x,y,w,h):
        #grab an image from SSHEET
        image = pg.surface((w,h))
        image.blit(self.spritesheet,(0,0), (x,y,w,h))
        return image
class Player(pg.sprite.Sprite):
    def __init__(self,game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.jumps_left = 0
        self.image = pg.Surface((30,40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
        self.pos = vec(WIDTH/2,HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    def jump(self):
        #jump only if standing on playform
        self.rect.x += 1
        if self.vel.y > 0:
            hits = pg.sprite.spritecollide(self, self.game.platforms, False)
            self.rect.x -= 1
            if hits:
                self.jumps_left = 1
        if self.jumps_left > 0:
            self.jumps_left -=1
            self.vel.y = -20

    def update(self):
        #movement
        self.acc = vec(0,PLAYER_GRAVITY)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        #Friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        #equations of motion
        self.vel += self.acc
        self.pos += self.vel + PLAYER_ACC * self.acc
        #wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        self.rect.midbottom = self.pos
class Platform(pg.sprite.Sprite):
    def __init__(self,x,y,w,h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y