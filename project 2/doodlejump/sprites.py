#Sprite Classes
import random

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
        image = pg.Surface((w,h))
        image.blit(self.spritesheet,(0,0), (x,y,w,h))
        image = pg.transform.scale(image, (w//2, h//2))
        image.set_colorkey(BLACK)
        return image
class Player(pg.sprite.Sprite):
    def __init__(self,game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.standing_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = (40, HEIGHT -100)
        self.pos = vec(40, HEIGHT -100)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    def load_images(self):
        self.standing_frames = [self.game.spritesheet.get_image(614,1063,120,191),self.game.spritesheet.get_image(690,406,120,201)]
        self.walk_frames_r = [self.game.spritesheet.get_image(678,860,120,201),self.game.spritesheet.get_image(692,1458,120,207)]
        self.walk_frames_l = []
        for frame in self.walk_frames_r:
            self.walk_frames_l.append(pg.transform.flip(frame,True,False))
        self.jump_frame = self.game.spritesheet.get_image(382,763,150,181)
    def jump(self):
        # jump only if standing on a platform
        self.rect.x += 2
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 2
        if hits:
            self.vel.y = -20

    def update(self):
        #movement
        self.animate()
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
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        #wrap around the sides of the screen
        if self.pos.x > WIDTH + self.rect.width / 2:
            self.pos.x = - self.rect.width / 2
        if self.pos.x < -self.rect.width/2:
            self.pos.x = WIDTH -self.rect.width/2
        self.rect.midbottom = self.pos
    def animate(self):
        now = pg.time.get_ticks()
        if self.vel.x !=0:
            self.walking = True
        else:
            self.walking = False
        if self.walking:
            if now -self.last_update > 150:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walk_frames_l)
                bottom = self.rect.bottom
                if self.vel.x > 0:
                    self.image = self.walk_frames_r[self.current_frame]
                else:
                    self.image = self.walk_frames_l[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
        if not self.jumping and not self.walking:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame+1)  % len(self.standing_frames)
                bottom = self.rect.bottom
                self.image = self.standing_frames[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
class Platform(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        images = [self.game.spritesheet.get_image(0,288,380,94),self.game.spritesheet.get_image(213,1662,201,100)]
        self.image = random.choice(images)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
