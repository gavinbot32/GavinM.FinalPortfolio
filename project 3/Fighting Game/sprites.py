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
        self.game.all_sprites.add(self)
        self.walking = False
        self.jumping = False
        self.facingR = True
        self.disabled = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.idle_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        spawn = random.choice(game.SPAWN_ZONES)
        game.SPAWN_ZONES.remove(spawn)
        self.pos = vec(spawn)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.health = 100
        self.heal_timer = 50
    def jump(self):
        # jump only if standing on a platform
        if not self.disabled:
            self.rect.x += 2
            hits = pg.sprite.spritecollide(self, self.game.platforms, False)
            self.rect.x -= 2
            if hits:
                self.vel.y = -25
    def punch(self):
        if not self.disabled:
            self.vel.x = 0
            self.acc.x = 0
            if self.facingR:
                Collider(self.rect.centerx, self.rect.centery, self.rect.width, 30,self.game,2,self,10)
            else:
                Collider(self.rect.centerx-self.rect.width , self.rect.centery,  self.rect.width, 30,self.game,2,self,10)
    def kick(self):
        if not self.disabled:
            self.vel.x = 0
            self.acc.x = 0
            if self.facingR:
                Collider(self.rect.centerx, self.rect.centery+ self.rect.centery /8, self.rect.width, 30,self.game,2,self,20)
            else:
                Collider(self.rect.centerx-self.rect.width , self.rect.centery + self.rect.centery /8,  self.rect.width, 30,self.game,2,self,20)
    def update(self):
        #movement
        self.heal_timer -=1
        if self.heal_timer <= 0:
            if self.health < 100:
                self.health += 10
            self.heal_timer = 100
        self.animate()
        self.acc = vec(0,PLAYER_GRAVITY)
        keys = pg.key.get_pressed()
        if not self.disabled:
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
class Collider(pg.sprite.Sprite):
    def __init__(self, x, y, width, height,game,kill_timer,owner,damage):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.game.colliders.add(self)
        self.owner = owner
        self.damage = damage
        self.image = pg.Surface((width, height)).convert()
        #self.image.fill(c.RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = None
        self.kill_timer = kill_timer
        self.kill_time = kill_timer
        self.game.all_sprites.add(self)
    def update(self):
        self.kill_timer -= 1
        if self.kill_timer == 0:
            self.kill()
            # self.rect.y + 3000
            self.kill_timer = self.kill_time
class Bar(pg.sprite.Sprite):
    def __init__(self,game,w,h,x,y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        if w <= 0:
            w = 10
        self.image = pg.Surface((w,h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.kill_timer = 2
        self.kill_time = 2
        self.game.all_sprites.add(self)
    def update(self):
        self.kill_timer -= 1
        if self.kill_timer == 0:
            self.kill()
            # self.rect.y + 3000
            self.kill_timer = self.kill_time
