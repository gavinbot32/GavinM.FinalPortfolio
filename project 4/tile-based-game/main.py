#Gavin Murdock
import pygame as pg
import pytweening as pyt
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
        map_folder = path.join(game_folder,'maps')
        snd_folder = path.join(game_folder,'snd')
        music_folder = path.join(game_folder,'music')
        pain_folder = path.join(snd_folder,'pain')


        self.map = TiledMap(path.join(map_folder,'tiled1.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.mob_img = pg.image.load(path.join(img_folder, MOB_IMG)).convert_alpha()
        self.bullet_img = pg.image.load(path.join(img_folder, BULLET_IMG)).convert_alpha()
        self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()
        self.wall_img = pg.transform.scale(self.wall_img, (TILESIZE,TILESIZE))
        self.player_img = pg.transform.scale(self.player_img, (int(TILESIZE*0.75),int(TILESIZE*0.75)))
        self.mob_img = pg.transform.scale(self.mob_img, (int(TILESIZE*0.75),int(TILESIZE*0.75)))
        self.gun_flashes = []
        for img in MUZZLE_FLASHES:
            self.gun_flashes.append(pg.image.load(path.join(img_folder,img)).convert_alpha())
        self.item_images = {}
        for item in ITEM_IMAGES:
            self.item_images[item] = pg.image.load(path.join(img_folder,ITEM_IMAGES[item])).convert_alpha()
        #sound
        pg.mixer.music.load(path.join(music_folder,BG_MUSIC))
        self.effects_sounds = {}
        for type in EFFECTS_SOUNDS:
            self.effects_sounds[type] = pg.mixer.Sound(path.join(snd_folder,EFFECTS_SOUNDS[type]))
        self.weapon_sounds = {}
        self.weapon_sounds['gun'] = []
        for snd in WEAPON_SOUNDS_GUN:
            s = pg.mixer.Sound(path.join(snd_folder, snd))
            s.set_volume(0.15)
            self.weapon_sounds['gun'].append(s)
        self.zombie_moan_sounds = []
        for snd in ZOMBIE_MOAN_SOUNDS:

            s = pg.mixer.Sound(path.join(snd_folder, snd))
            s.set_volume(0.1)
            self.zombie_moan_sounds.append(s)
        self.player_hit_sounds = []
        for snd in PLAYER_HIT_SOUNDS:
            self.player_hit_sounds.append(pg.mixer.Sound(path.join(pain_folder,snd)))
        self.zombie_hit_sounds = []
        for snd in ZOMBIE_HIT_SOUNDS:
            self.zombie_hit_sounds.append(pg.mixer.Sound(path.join(pain_folder,snd)))
    def new(self):
        #start a new game
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.items = pg.sprite.Group()
        self.players = []

        # for row, tiles in enumerate(self.map.data):
        #     for col,tile in enumerate(tiles):
        #         if tile == '1':
        #             Wall(self,col,row)
        #         if tile == 'M':
        #             Mob(self,col,row)
        #         if tile == 'P':
        #             if len(self.players) >= 1:
        #                 pass
        #             else:
        #                 self.player = Player(self, col,row)
        #                 self.players.append(self.player)
        for tile_object in self.map.tmxdata.objects:
            obj_center = vec(tile_object.x+tile_object.width/2,tile_object.y+tile_object.height/2)
            if tile_object.name == 'player':
                if len(self.players) < 1:
                    self.player = Player(self,obj_center.x,obj_center.y)
                    self.players.append(self.player)
            if tile_object.name == 'wall':
                Obstacle(self,tile_object.x,tile_object.y,tile_object.width,tile_object.height)
            if tile_object.name == 'mob':
                Mob(self,obj_center.x,obj_center.y)
            if tile_object.name == 'health':
                Item(self,obj_center,tile_object.name)
        self.camera = Camera(self.map.width,self.map.height)
        self.draw_debug = False
        self.effects_sounds['level_start'].play()
        self.run()
    def run(self):
        #game loop

        self.playing = True
        pg.mixer.music.play(loops=-1)
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
            # If the red X waas clicked, close the program
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if self.playing:
                        self.playing = False
                    self.running = False
                if event.key == pg.K_h:
                    self.draw_debug = not self.draw_debug
        hits = pg.sprite.groupcollide(self.mobs, self.bullets, False, True)
        for hit in hits:
            hit.health -= BULLET_DMG
            hit.vel = vec(0,0)
        hits = pg.sprite.spritecollide(self.player, self.mobs, False, False)
        for hit in hits:
            if random.random() < 0.7:
                random.choice(self.player_hit_sounds).play()
            self.player.health -= MOB_DMG
            hit.vel = vec(0, 0)
            if self.player.health <=0:
                self.playing = False
        if hits:
            self.player.pos += vec(MOB_KNOCKBACK,0).rotate(-hits[0].rot)

        #player hits items
        hits = pg.sprite.spritecollide(self.player,self.items,False)
        for hit in hits:
            if hit.type == 'health' and self.player.health < PLAYER_HEALTH:
                hit.kill()
                self.player.add_health(HEALTH_PACK_AMOUNT)
                self.effects_sounds['health_up'].play()


    def draw_grid(self):
        for x in range(0,WIDTH,TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x,0),(x,HEIGHT))
        for y in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        pg.display.set_caption("{:.1f}".format(self.clock.get_fps()))
        #game loop draw
        # self.screen.fill(BGCOLOR)
        self.screen.blit(self.map_img,self.camera.apply_rect(self.map_rect))
        # self.draw_grid()
        # Draw all sprites
        for sprite in self.all_sprites:
            if isinstance(sprite,Mob):
                sprite.draw_health()
            self.screen.blit(sprite.image,self.camera.apply(sprite))
            if self.draw_debug:
                pg.draw.rect(self.screen,BLUE,self.camera.apply_rect(sprite.hit_rect),1)
        if self.draw_debug:
            for wall in self.walls:
                pg.draw.rect(self.screen,BLUE,self.camera.apply_rect(wall.rect),1)

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