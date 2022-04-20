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
        image = pg.transform.scale(image, (w, h))
        image.set_colorkey(GREEN)
        return image
class Player(pg.sprite.Sprite):
    def __init__(self,game,keybinds,color):
        pg.sprite.Sprite.__init__(self)
        self.keybinds = keybinds
        self.game = game
        self.walking = False
        self.jumping = False
        self.facingR = True
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.idle_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(40, HEIGHT -100)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    def jump(self):
        # jump only if standing on a platform
        self.rect.x += 2
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 2
        if hits:
            self.vel.y = -25
    def punch(self):
        now = pg.time.get_ticks()
        self.arm = pg.Surface((20,10))
        self.arm.fill(BLACK)
        self.arm_rect = self.arm.get_rect()
        if self.facingR:
            self.arm_rect.center = (self.rect.x + self.rect.x // 2, self.rect.y // 2 - 10)
        else:
            self.arm_rect.center = (self.rect.x - self.rect.x // 2, self.rect.y // 2 - 10)
        if now - self.last_update > 140:
            self.last_update = now
            self.arm = self.pg.Surface((0, 0))




    def update(self):
        #movement
        self.animate()
        self.acc = vec(0,PLAYER_GRAVITY)
        keys = pg.key.get_pressed()
        if keys[self.keybinds[1]]:
            self.acc.x = -PLAYER_ACC
            self.facingR = False
        if keys[self.keybinds[2]]:
            self.acc.x = PLAYER_ACC
            self.facingR = True

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
            self.pos.x = WIDTH +self.rect.width/2

        self.rect.midbottom = self.pos
    def load_images(self):
        self.idle_frames = [self.game.spritesheet.get_image(1,1,172,367),self.game.spritesheet.get_image(175,1,172,367),
                            self.game.spritesheet.get_image(349,1,172,367),self.game.spritesheet.get_image(1,370,172,367),self.game.spritesheet.get_image(349,1,172,367)
            ,self.game.spritesheet.get_image(175,1,172,367),self.game.spritesheet.get_image(1,1,172,367)]
        self.idle_frames_L = []
        for frame in self.idle_frames:
            self.idle_frames_L.append(pg.transform.flip(frame,True,False))
        # self.walk_frames_r = [self.game.spritesheet.get_image(678,860,120,201),self.game.spritesheet.get_image(692,1458,120,207)]
        # self.walk_frames_l = []
        # for frame in self.walk_frames_r:
        #     self.walk_frames_l.append(pg.transform.flip(frame,True,False))
    def animate(self):
        now = pg.time.get_ticks()
        if self.vel.x !=0:
            self.walking = True
        else:
            self.walking = False
        if now - self.last_update > 100:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.idle_frames_L)
            bottom = self.rect.bottom
            if self.vel.x > 0:
                self.image = self.idle_frames[self.current_frame]
            elif self.vel.x < 0:
                self.image = self.idle_frames_L[self.current_frame]
            else:
                if self.facingR:
                    self.image = self.idle_frames[self.current_frame]
                else:
                    self.image = self.idle_frames_L[self.current_frame]
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom
class Platform(pg.sprite.Sprite):
    def __init__(self,game,x,y,w,h):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y