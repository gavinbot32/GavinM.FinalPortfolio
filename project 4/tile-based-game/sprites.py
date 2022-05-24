import random
import pytweening as pyt
import pygame as pg
from random import uniform
from settings import *

#Collison Code for Sprites
def collide_hit_rect(one,two):
    return one.hit_rect.colliderect(two.rect)
def collide_with_walls(sprite,group,dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite,group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centerx > sprite.hit_rect.centerx :
                sprite.pos.x = hits[0].rect.left- sprite.hit_rect.width / 2
            if hits[0].rect.centerx < sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.right+ sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery :
                sprite.pos.y = hits[0].rect.top- sprite.hit_rect.height / 2
            if hits[0].rect.centery < sprite.hit_rect.centery :
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y

vec = pg.math.Vector2
#player game object
class Player(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(0,0)
        self.pos = vec(x,y)
        self.rot = 0
        self.last_shot = 0
        self.health = PLAYER_HEALTH
    #Detecting Key Presses and reacts accordingly
    def get_keys(self):
        self.rot_speed = 0
        self.vel = vec(0,0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rot_speed = PLAYER_ROT_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rot_speed = -PLAYER_ROT_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel = vec(PLAYER_SPEED,0).rotate(-self.rot)
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel = vec(-PLAYER_SPEED / 2, 0).rotate(-self.rot)

        if keys[pg.K_SPACE]:
            now = pg.time.get_ticks()
            if now- self.last_shot>BULLET_RATE:
                self.last_shot = now
                dir = vec(1,0).rotate(-self.rot)
                pos = self.pos + BARREL_OFFSET.rotate(-self.rot)
                Bullet(self.game,pos,dir)
                self.vel = vec(-KICKBACK,0).rotate(-self.rot)
                MuzzleFlash(self.game,pos)
                random.choice(self.game.weapon_sounds['gun']).play()

        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071


    def add_health(self,amount):
        self.health += amount
        if self.health > PLAYER_HEALTH:
            self.health = PLAYER_HEALTH
    #every frame this is called and updates sprites data
    def update(self):
        self.get_keys()
        self.rot = (self.rot + self.rot_speed * self.game.dt) % 360
        self.image = pg.transform.rotate(self.game.player_img,self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self,self.game.walls,'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self,self.game.walls,'y')
        self.rect.center = self.hit_rect.center
    def draw_health(self):
        if self.health > 60:
            col = GREEN
        elif self.health > 30:
            col = YELLOW
        else:
            col = RED
        width = int(self.rect.width * self.health / PLAYER_HEALTH)
        self.health_bar = pg.Rect(0,0,width, 7)
        if self.health < PLAYER_HEALTH:
            pg.draw.rect(self.image,col,self.health_bar)
#sprite class for Mob game object
class Mob(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self._layer = MOB_LAYER
        self.game = game
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self,self.groups)
        self.image = game.mob_img.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.hit_rect = MOB_HIT_RECT.copy()
        self.hit_rect_center = self.rect.center
        self.pos = vec(x,y)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.rect.center = self.pos
        self.rot = 0
        self.speed = MOB_SPEED + random.randint(-21,21)
        self.health = MOB_HEALTH
        self.target = game.player
    #spaces each mob out away from another
    def avoid_mobs(self):
        for mob in self.game.mobs:
            if mob != self:
                dist = self.pos - mob.pos
                if dist.length() == 0:
                    dist =vec(1,0)
                if 0 < dist.length() < AVOID_RADIUS:
                    self.acc += dist.normalize()
#updates sprite info
    def update(self):
        target_dist = self.target.pos - self.pos
        if target_dist.length_squared() < DETECT_RADIUS**2:
            if random.random() < 0.002:
                random.choice(self.game.zombie_moan_sounds).play()
            self.rot = target_dist.angle_to(vec(1,0))
            self.image = pg.transform.rotate(self.game.mob_img,self.rot)
            # self.rect = self.image.get_rect()
            self.rect.center = self.pos
            #
            self.acc = vec(1,0).rotate(-self.rot)
            self.avoid_mobs()
            self.acc.scale_to_length(self.speed)
            #
            self.acc += self.vel * -1
            self.vel += self.acc * self.game.dt
            self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2
            self.hit_rect.centerx = self.pos.x
            collide_with_walls(self,self.game.walls,'x')
            self.hit_rect.centery = self.pos.y
            collide_with_walls(self,self.game.walls,'y')
            self.rect.center = self.hit_rect.center
        if self.health <= 0:
            random.choice(self.game.zombie_hit_sounds).play()
            self.kill()


    def draw_health(self):
        if self.health > 60:
            col = GREEN
        elif self.health > 30:
            col = YELLOW
        else:
            col = RED
        width = int(self.rect.width * self.health / MOB_HEALTH)
        self.health_bar = pg.Rect(0,0,width, 7)
        if self.health < MOB_HEALTH:
            pg.draw.rect(self.image,col,self.health_bar)

class Bullet(pg.sprite.Sprite):
    def __init__(self,game,pos,dir):
        self._layer = BULLET_LAYER
        self.groups = game.all_sprites, game.bullets
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.bullet_img
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.pos = vec(pos)
        self.rect.center = pos
        spread = uniform(-GUN_SPREAD,GUN_SPREAD)
        self.vel = dir.rotate(spread) * BULLET_SPEED
        self.spawn_time = pg.time.get_ticks()
    def update(self):
        self.pos += self.vel *self.game.dt
        self.rect.center = self.pos
        if pg.sprite.spritecollideany(self,self.game.walls):
            self.kill()
        if pg.time.get_ticks() - self.spawn_time > BULLET_LIFE:
            self.kill()

class Wall(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self._layer = WALL_LAYER
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Obstacle(pg.sprite.Sprite):
    def __init__(self,game,x,y,w,h):
        self.groups = game.walls
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = pg.Rect(x,y,w,h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

class MuzzleFlash(pg.sprite.Sprite):
    def __init__(self,game,pos):
        self._layer = EFFECTS_LAYER
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        size = random.randint(20,50)
        self.image = pg.transform.scale(random.choice(game.gun_flashes),(size,size))
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = pos
        self.spawn_time = pg.time.get_ticks()

    def update(self):
        if pg.time.get_ticks() - self.spawn_time > FLASH_DURATION:
            self.kill()

class Item(pg.sprite.Sprite):
    def __init__(self,game,pos,type):
        self._layer = ITEMS_LAYER
        self.groups = game.all_sprites, game.items
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.item_images[type]
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.type = type
        self.pos = pos
        self.rect.center = pos
        self.tween = pyt.easeInOutSine
        self.step = 0
        self.dir = 1
    def update(self):
        offset = BOB_RANGE *(self.tween(self.step/BOB_RANGE)-0.5)
        self.rect.centery = self.pos.y + offset *self.dir
        self.step += BOB_SPEED
        if self.step > BOB_RANGE:
            self.step = 0
            self.dir *=-1
