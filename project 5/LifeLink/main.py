#Gavin Murdock
#4/14/22
#Doodle Jump
import pygame
import pygame as pg
import random
import sys
from os import path
from settings import *
from tilemap import *
from sprites import *


#HUD
def draw_player_health(game,surf,x,y,pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 250
    BAR_HEIGHT = 30
    fill = pct * BAR_LENGTH
    fill_rect = pg.Rect(x,y,fill, BAR_HEIGHT)
    if pct > 0.6:
        col = GREEN
    elif pct > 0.3:
        col = YELLOW
    else:
        col = RED
    if game.player.health > PLAYER_HEALTH:
        outline_rect = pg.Rect(x, y, fill + 2, BAR_HEIGHT)
    else:
        outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
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
        self.game_folder = path.dirname(__file__)
        img_folder = path.join(self.game_folder,'img')
        sound_folder = path.join(self.game_folder,'sounds')
        self.map_imgs = []
        self.font_folder = path.join(self.game_folder,'fonts')
        self.map = Map(path.join(self.game_folder,MAP_FILE))
        for i in range(5):
            map = pg.image.load(path.join(img_folder, "map{}.png".format(i))).convert_alpha()
            map = pg.transform.scale(map,(map.get_width()//4 , map.get_height()// 4))
            self.map_imgs.append(map)
        self.base_img = pg.image.load(path.join(img_folder, BASE_IMG)).convert_alpha()
        self.control_img = pg.image.load(path.join(img_folder, CONTROL_IMG)).convert_alpha()
        self.play_img = pg.image.load(path.join(img_folder, PLAY_IMG)).convert_alpha()
        self.quit_img = pg.image.load(path.join(img_folder, QUIT_IMG)).convert_alpha()
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.dmg_img = pg.image.load(path.join(img_folder, DMG_IMG)).convert_alpha()
        self.speed_img = pg.image.load(path.join(img_folder, SPEED_IMG)).convert_alpha()
        self.life_img = pg.image.load(path.join(img_folder, LIFE_IMG)).convert_alpha()
        self.phoenix_img = pg.image.load(path.join(img_folder, PHOENIX_IMG)).convert_alpha()
        self.rof_img = pg.image.load(path.join(img_folder, ROF_IMG)).convert_alpha()
        self.mob_img = pg.image.load(path.join(img_folder, MOB_IMG)).convert_alpha()
        # self.font_name = pg.font.Font(path.join(font_folder,FONT_NAME),35)
        # self.mob_img = pg.image.load(path.join(img_folder, MOB_IMG)).convert_alpha()
        # self.bullet_img = pg.image.load(path.join(img_folder, BULLET_IMG)).convert_alpha()
        # self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()
        # self.wall_img = pg.transform.scale(self.wall_img, (TILESIZE,TILESIZE))
        # self.player_img = pg.transform.scale(self.player_img, (int(TILESIZE*0.75),int(TILESIZE*0.75)))
        self.shootSnds = []

        shoot01 = pg.mixer.Sound(path.join(sound_folder,'explosion00.wav'))
        shoot02 = pg.mixer.Sound(path.join(sound_folder,'explosion01.wav'))
        self.hurtSound = pg.mixer.Sound(path.join(sound_folder,'hurt.wav'))
        self.hurtSound.set_volume(0.4)
        self.shootSnds.append(shoot01)
        self.shootSnds.append(shoot02)
        self.life_img = pg.transform.scale(self.life_img,(100,100))
        self.dmg_img = pg.transform.scale(self.dmg_img,(100,100))
        self.speed_img = pg.transform.scale(self.speed_img,(100,100))
        self.rof_img = pg.transform.scale(self.rof_img,(100,100))
        self.phoenix_img = pg.transform.scale(self.phoenix_img,(100,100))
        self.play_img = pg.transform.scale(self.play_img,(self.play_img.get_width() * 2,self.play_img.get_height()*2))
        self.quit_img = pg.transform.scale(self.quit_img,(self.quit_img.get_width() * 2,self.quit_img.get_height()*2))
        self.base_img = pg.transform.scale(self.base_img, (int(TILESIZE),int(TILESIZE)))
        self.player_img = pg.transform.scale(self.player_img, (int(TILESIZE-10),int(TILESIZE-10)))
        self.mob_img = pg.transform.scale(self.mob_img, (int(TILESIZE-10),int(TILESIZE-10)))
        self.bullet_img = pg.transform.scale(self.base_img, (10,10))
    def new(self):
        #start a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.players = []
        self.round = 0
        self.click = False
        # self.life_button = pg.Rect(WIDTH//3 -300, HEIGHT-110, 100, 100)
        self.life_button = Button(self,WIDTH//3 -300,HEIGHT-110,self.life_img)
        self.dmg_button = Button(self,WIDTH//3, HEIGHT-110,self.dmg_img)
        self.speed_button = Button(self,WIDTH//3+150, HEIGHT-110,self.speed_img)
        self.rof_button = Button(self,WIDTH//3 - 150, HEIGHT-110,self.rof_img)
        self.phoenix_button = Button(self,WIDTH//3+300, HEIGHT-110,self.phoenix_img)
        # self.rof_button = pg.Rect(WIDTH//3 - 150, HEIGHT-110, 100, 100)
        # self.dmg_button = pg.Rect(WIDTH//3, HEIGHT-110, 100, 100)
        # self.speed_button = pg.Rect(WIDTH//3+150, HEIGHT-110, 100, 100)
        # self.phoenix_button = pg.Rect(WIDTH//3+300, HEIGHT-110, 100, 100)
        upgrade_height = 117
        self.upgrade_rect = pg.Rect(0,HEIGHT-upgrade_height,WIDTH,upgrade_height)
        self.lifeCost = 20
        self.rofCost = 10
        self.dmgCost = 25
        self.speedCost = 15
        self.phoenixCost = 250
        self.clicktimer = 3
        #Stats
        self.statKills = 0
        self.statLife = 0
        self.statDmg = 0
        self.statLifeLost = 0
        self.statLink = 0
        self.statROF = 0
        self.statDMG = 0
        self.statSpeed = 0
        self.statPhoenix = 0
        for row, tiles in enumerate(self.map.data):
            for col,tile in enumerate(tiles):
                if tile == '1':
                    Wall(self,col,row)
                if tile == 'M':
                    Mob(self,col,row)
                if tile == 'P':
                    if len(self.players) >= 1:
                        pass
                    else:
                        self.player = Player(self, col,row)
                        self.players.append(self.player)

        self.camera = Camera(self.map.width,self.map.height)
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
        # self.camera.update(self.player)


    def events(self):
        self.mx, self.my = pg.mouse.get_pos()
        self.mousePos = (self.mx,self.my)
        self.clicktimer -= 1
        if self.player.lifeBuys <= 1:
            self.lifeCost = 20
        else:
            if self.player.lifeBuys < 11:
                self.lifeCost = 20 * (self.player.lifeBuys **2)
            else:
                self.lifeCost = "Locked"
        if self.player.rofBuys <= 1:
            self.rofCost = 10
        else:
            if self.player.rate_of_fire > 2:
                self.rofCost = 10 * (self.player.rofBuys **2)
            else:
                self.rofCost = "Locked"
        if self.player.dmgBuys <= 1:
            self.dmgCost = 25
        else:
            self.dmgCost = 25 * (self.player.dmgBuys**2)
        if self.player.speedBuys <= 1:
            self.speedCost = 15
        else:
            self.speedCost = 15 * (self.player.speedBuys**2)

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
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True
        #Buttons
        if self.clicktimer <= 0:
            if self.life_button.draw():
                self.clicktimer = 3
                if self.player.lifeBuys < 11:
                    if self.player.health > self.lifeCost:
                        self.player.health -= self.lifeCost
                        self.player.life_multiplier += 10
                        self.player.lifeBuys += 1
                        self.statLink += 1
                    else:
                        self.player.lives = 0
                        self.player.health = 0
                else:
                    self.lifeCost = "Locked"
                    self.player.life_multiplier = self.player.life_multiplier
            if self.rof_button.draw():
                self.clicktimer = 3

                if self.player.rate_of_fire > 2:
                    if self.player.health > self.rofCost:
                        self.player.health -= self.rofCost
                        self.player.rofBuys += 1
                        self.player.rate_of_fire -= 10
                        self.statROF += 1
                    else:
                        self.player.lives = 0
                        self.player.health = 0
                else:
                    self.rofCost = "Locked"
            if self.dmg_button.draw():
                self.clicktimer = 3

                if self.player.dmgBuys < 20:
                    if self.player.health > self.dmgCost:
                        self.player.health -= self.dmgCost
                        self.player.dmgBuys += 1
                        self.player.damage += 5
                        self.statDMG += 1
                    else:
                        self.player.lives = 0
                        self.player.health = 0
            if self.speed_button.draw():
                self.clicktimer = 3

                if self.player.speedBuys < 25:
                    if self.player.health > self.speedCost:
                        self.player.health -= self.speedCost
                        self.player.speedBuys += 1
                        self.player.speedMultiplier += 1
                        self.statSpeed += 1
                    else:
                        self.player.lives = 0
                        self.player.health = 0
            if self.phoenix_button.draw():
                self.clicktimer = 3
                if self.player.health > self.phoenixCost:


                    self.player.health -= self.phoenixCost
                    self.player.lives += 1
                    self.statPhoenix += 1
                    self.phoenixCost *= (self.player.lives * 2)
                else:
                    self.player.lives = 0
                    self.player.health = 0

        self.click = False
        hits = pg.sprite.groupcollide(self.mobs, self.bullets, False, True)
        for hit in hits:
            hit.health -= self.player.damage
            self.statDmg += self.player.damage
            hit.vel = vec(0,0)
            self.player.life_hits += 1
            self.hurtSound.play()
        hits = pg.sprite.spritecollide(self.player, self.mobs, False, False)
        for hit in hits:
            self.player.health -= MOB_DMG
            self.statLifeLost += MOB_DMG
            hit.vel = vec(0, 0)
            self.hurtSound.play()
        if self.player.health <=0:
            self.player.lives -= 1
            if self.player.lives <= 0:
                self.playing = False
            else:
                self.player.health = PLAYER_HEALTH

        if hits:
            self.player.pos += vec(MOB_KNOCKBACK,0).rotate(-hits[0].rot)
        if len(self.mobs) <= 0:
            self.new_round()
            self.round += 1

    def new_round(self):
        if self.round == 0:
            for i in range(self.round + 1 * 5):
                Mob(self,random.randint(3,28),random.randint(3,14))
        else:
            for i in range(self.round * 5):
                x = random.randint(3,28)
                y = random.randint(3,14)
                Mob(self,x,y)

    def draw_grid(self):
        for x in range(0,WIDTH,TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x,0),(x,HEIGHT))
        for y in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))
    def draw_text(self,text,size,color,x,y):
        font = pg.font.Font(path.join(self.font_folder,FONT_NAME),size)
        text_surface = font.render(text,True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface,text_rect)
    def draw(self):
        pg.display.set_caption("{:.1f}".format(self.clock.get_fps()))
        #game loop draw
        self.screen.fill(BGCOLOR)
        # self.draw_grid()
        # for sprite in self.all_sprites:
        #     if isinstance(sprite,Bullet):
        #         for i in range(10):
        #             glow = pg.Surface((sprite.rect.width + i+1, sprite.rect.height+i+1))
        #             glow.fill((20,20,20))
        #             self.screen.blit(glow,((sprite.rect.centerx - sprite.rect.width)-i//2, (sprite.rect.centery - sprite.rect.height)-i//2),special_flags=pg.BLEND_RGB_ADD)
        #     if isinstance(sprite,Player):
        #         for i in range(6):
        #             glow = pg.Surface((TILESIZE+i*2,TILESIZE+i*2))
        #             glow.fill((0,30,0))
        #             self.screen.blit(glow,((sprite.hit_rect.centerx - sprite.hit_rect.width)-i//2, (sprite.hit_rect.centery - sprite.hit_rect.height)+i//2),special_flags=pg.BLEND_RGB_ADD)
        #     if isinstance(sprite,Mob):
        #         for i in range(6):
        #             glow = pg.Surface((TILESIZE+i*2,TILESIZE+i*2))
        #             glow.fill((20,0,0))
        #             self.screen.blit(glow,((sprite.hit_rect.centerx - sprite.hit_rect.width)-i//2, (sprite.hit_rect.centery - sprite.hit_rect.height)+i//2),special_flags=pg.BLEND_RGB_ADD)
        #
        #     if isinstance(sprite,Wall):
        #         for i in range(10):
        #             glow = pg.Surface((sprite.rect.width + i + 1, sprite.rect.height + i + 1))
        #             glow.fill((0,0, 20))
        #             self.screen.blit(glow, ((sprite.rect.centerx - sprite.rect.width) - i *2,
        #                                     (sprite.rect.centery - sprite.rect.height) - i *2),
        #                              special_flags=pg.BLEND_RGB_ADD)
        # Draw all sprites
        for sprite in self.all_sprites:
            if isinstance(sprite,Mob):
                sprite.draw_health()
            self.screen.blit(sprite.image,self.camera.apply(sprite))
        self.all_sprites.draw(self.screen)
        # Must be the last thing called in the draw section

        #HUD
        pg.draw.rect(self.screen, GREY, self.upgrade_rect)

        draw_player_health(self,self.screen,10,10,self.player.health/PLAYER_HEALTH)
        self.life_button.draw()
        self.dmg_button.draw()
        self.rof_button.draw()
        self.speed_button.draw()
        self.phoenix_button.draw()

        # pg.draw.rect(self.screen,LIGHTGREY,self.life_button)
        # pg.draw.rect(self.screen,LIGHTGREY,self.rof_button)
        # pg.draw.rect(self.screen,LIGHTGREY,self.dmg_button)
        # pg.draw.rect(self.screen,LIGHTGREY,self.speed_button)
        # pg.draw.rect(self.screen,LIGHTGREY,self.phoenix_button)

        self.draw_text("Round "+ str(self.round),72,WHITE,WIDTH /2,10)
        self.draw_text("Health: "+ str(self.player.health),44,WHITE,150,60)
        self.draw_text("Lives: "+ str(self.player.lives),44,WHITE,WIDTH //4 ,10)
        if self.life_button.hover:
            self.draw_text("+LifeSteal", 22, WHITE,self.life_button.rect.centerx, self.life_button.rect.y-10)
            self.draw_text("Cost: "+str(self.lifeCost), 22, WHITE,self.life_button.rect.centerx, self.life_button.rect.y+self.life_button.rect.width-25)
        if self.rof_button.hover:
            self.draw_text("+ROF", 22, WHITE,self.rof_button.rect.centerx, self.rof_button.rect.y-10)
            self.draw_text("Cost: "+str(self.rofCost), 22, WHITE,self.rof_button.rect.centerx, self.rof_button.rect.y+self.rof_button.rect.width-25)
        if self.dmg_button.hover:
            self.draw_text("+DMG", 22, WHITE,self.dmg_button.rect.centerx, self.dmg_button.rect.y-10)
            self.draw_text("Cost: "+str(self.dmgCost), 22, WHITE,self.dmg_button.rect.centerx, self.dmg_button.rect.y+self.dmg_button.rect.width-25)
        if self.speed_button.hover:
            self.draw_text("+Speed", 22, WHITE,self.speed_button.rect.centerx, self.speed_button.rect.y-10)
            self.draw_text("Cost: "+str(self.speedCost), 22, WHITE,self.speed_button.rect.centerx, self.speed_button.rect.y+self.speed_button.rect.width-25)
        if self.phoenix_button.hover:
            self.draw_text("+1 Life", 22, WHITE, self.phoenix_button.rect.centerx, self.phoenix_button.rect.y-10)
            self.draw_text("Cost: " + str(self.phoenixCost), 22, WHITE, self.phoenix_button.rect.centerx, self.phoenix_button.rect.y+self.phoenix_button.rect.height-25)
        self.draw_text("Upgrades:", 45,WHITE,150,HEIGHT-100)
        self.draw_text("(Note: If you can't afford ", 15, WHITE, 150,HEIGHT-45)
        self.draw_text("and you buy your game is over)", 15, WHITE, 150,HEIGHT-30)

        pg.display.flip()

    def show_map_screen(self):
        clicktimer = 3
        self.screen.fill(GREY)
        control_width = self.control_img.get_width()
        self.control_img = pg.transform.scale(self.control_img,(control_width //2, self.control_img.get_height() //2 ))
        map_zero = self.map_imgs[0]
        map_width = map_zero.get_width()
        map_height = map_zero.get_height()
        map_button_0 = Button(self,map_width//2,HEIGHT - map_height*3,self.map_imgs[0])
        map_button_1 = Button(self,map_width//2 + map_width,HEIGHT - map_height*3,self.map_imgs[1])
        map_button_2 = Button(self,map_width//2 + map_width*2,HEIGHT - map_height*3,self.map_imgs[2])
        map_button_3 = Button(self,map_width//2,HEIGHT - map_height*2,self.map_imgs[3])
        map_button_4 = Button(self,map_width//2+ map_width,HEIGHT - map_height*2,self.map_imgs[4])
        control = Button(self,map_button_4.rect.x + control_width //4, HEIGHT-self.control_img.get_height(),self.control_img)

        waiting = True
        while waiting:
            self.clock.tick(FPS)
            clicktimer -=1
            self.draw_text("Select a Map", 154, RED, WIDTH // 2, (HEIGHT // 10) - 2)
            self.draw_text("Select a Map", 152, BLUE, WIDTH // 2, HEIGHT // 10)
            self.draw_text("Select a Map", 150, WHITE, WIDTH // 2, HEIGHT // 10)
            control.draw()
            for event in pg.event.get():
                if clicktimer <= 0:
                    if map_button_0.draw():
                        self.map = Map(path.join(self.game_folder,"map.txt"))
                        waiting = False
                    if map_button_1.draw():
                        self.map = Map(path.join(self.game_folder,"map2.txt"))
                        waiting = False
                    if map_button_2.draw():
                        self.map = Map(path.join(self.game_folder,"map3.txt"))
                        waiting = False
                    if map_button_3.draw():
                        self.map = Map(path.join(self.game_folder,"map4.txt"))
                        waiting = False
                    if map_button_4.draw():
                        self.map = Map(path.join(self.game_folder,"map5.txt"))
                        waiting = False
            pg.display.flip()
    def show_start_screen(self):
        self.screen.fill(GREY)
        start_width = self.play_img.get_width()
        start_height = self.play_img.get_height()
        start_button = Button(self, WIDTH // 2 - start_width//2, HEIGHT - start_height*3, self.play_img)
        quit_button = Button(self, WIDTH // 2 - start_width//2, HEIGHT - start_height*2, self.quit_img)

        waiting = True
        while waiting:
            self.clock.tick(FPS)
            self.draw_text(TITLE, 154, RED, WIDTH // 2, (HEIGHT // 4)-2)
            self.draw_text(TITLE, 152, BLUE, WIDTH // 2, HEIGHT // 4)
            self.draw_text(TITLE, 150, WHITE, WIDTH // 2, HEIGHT // 4)

            for event in pg.event.get():
                if start_button.draw():
                    waiting = False
                if quit_button.draw():
                    waiting = False
                    self.running = False
                    quit()
            pg.display.flip()
    def show_go_screen(self):
        self.screen.fill(GREY)
        link_img = self.life_img
        dmg_img = self.dmg_img
        speed_img = self.speed_img
        phoenix_img = self.phoenix_img
        rof_img = self.rof_img
        link_img = pg.transform.scale(link_img,(200,200))
        rof_img = pg.transform.scale(rof_img,(200,200))
        speed_img = pg.transform.scale(speed_img,(200,200))
        phoenix_img = pg.transform.scale(phoenix_img,(200,200))
        dmg_img = pg.transform.scale(dmg_img,(200,200))
        link = Button(self, WIDTH //2, HEIGHT//4,link_img)
        rof = Button(self, WIDTH //2+ 250, HEIGHT//4,rof_img)
        speed = Button(self, WIDTH //2+ 500, HEIGHT//4,speed_img)
        dmg = Button(self, WIDTH //2, HEIGHT//4+350,dmg_img)
        phoenix = Button(self, WIDTH //2+250, HEIGHT//4+350,phoenix_img)
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            self.draw_text("Game Over", 154, RED, WIDTH // 2, (HEIGHT // 10)-2)
            self.draw_text("Game Over", 152, BLUE, WIDTH // 2, HEIGHT // 10)
            self.draw_text("Game Over", 150, WHITE, WIDTH // 2, HEIGHT // 10)
            self.draw_text("Press Enter to Restart", 102, RED, WIDTH // 2, (HEIGHT -150)-2)
            self.draw_text("Press Enter to Restart", 102, BLUE, WIDTH // 2, HEIGHT -150)
            self.draw_text("Press Enter to Restart", 100, WHITE, WIDTH // 2, HEIGHT -150)
            self.draw_text("Statistics:", 64, RED, WIDTH // 8, (HEIGHT // 4)-32)
            self.draw_text("Statistics:", 64, BLUE, WIDTH // 8, (HEIGHT // 4)-30)
            self.draw_text("Statistics:", 62, WHITE, WIDTH // 8, (HEIGHT // 4)-30)
            self.draw_text("Kills: "+ str(self.statKills), 64, RED, (WIDTH // 8)+50, (HEIGHT // 4)+68)
            self.draw_text("Kills: "+ str(self.statKills), 64, BLUE, (WIDTH // 8)+50, (HEIGHT // 4)+70)
            self.draw_text("Kills: "+ str(self.statKills), 62, WHITE, (WIDTH // 8)+50, (HEIGHT // 4)+70)
            self.draw_text("DMG Dealt: "+ str(self.statDmg), 64, RED, (WIDTH // 8)+50, (HEIGHT // 4)+168)
            self.draw_text("DMG Dealt: "+ str(self.statDmg), 64, BLUE, (WIDTH // 8)+50, (HEIGHT // 4)+170)
            self.draw_text("DMG Dealt: "+ str(self.statDmg), 62, WHITE, (WIDTH // 8)+50, (HEIGHT // 4)+170)
            self.draw_text("Life Gained: "+ str(self.statLife), 64, RED, (WIDTH // 8)+50, (HEIGHT // 4)+268)
            self.draw_text("Life Gained: "+ str(self.statLife), 64, BLUE, (WIDTH // 8)+50, (HEIGHT // 4)+270)
            self.draw_text("Life Gained: "+ str(self.statLife), 62, WHITE, (WIDTH // 8)+50, (HEIGHT // 4)+270)
            self.draw_text("Life Lost: "+ str(self.statLifeLost), 64, RED, (WIDTH // 8)+50, (HEIGHT // 4)+368)
            self.draw_text("Life Lost: "+ str(self.statLifeLost), 64, BLUE, (WIDTH // 8)+50, (HEIGHT // 4)+370)
            self.draw_text("Life Lost: "+ str(self.statLifeLost), 62, WHITE, (WIDTH // 8)+50, (HEIGHT // 4)+370)
            self.draw_text("Round: "+ str(self.round), 64, RED, (WIDTH // 8)+50, (HEIGHT // 4)+468)
            self.draw_text("Round: "+ str(self.round), 64, BLUE, (WIDTH // 8)+50, (HEIGHT // 4)+470)
            self.draw_text("Round: "+ str(self.round), 62, WHITE, (WIDTH // 8)+50, (HEIGHT // 4)+470)
            link.draw()
            rof.draw()
            phoenix.draw()
            speed.draw()
            dmg.draw()

            self.draw_text(str(self.statLink), 44, RED, link.rect.centerx,link.rect.centery +98 + 20)
            self.draw_text(str(self.statLink), 44, BLUE, link.rect.centerx,link.rect.centery+100+20)
            self.draw_text(str(self.statLink), 42, WHITE, link.rect.centerx,link.rect.centery+100+20)
            self.draw_text(str(self.statDMG), 44, RED, dmg.rect.centerx,dmg.rect.centery +98+20)
            self.draw_text(str(self.statDMG), 44, BLUE, dmg.rect.centerx,dmg.rect.centery+100+20)
            self.draw_text(str(self.statDMG), 42, WHITE, dmg.rect.centerx,dmg.rect.centery+100+20)
            self.draw_text(str(self.statROF), 44, RED, rof.rect.centerx,rof.rect.centery +98+20)
            self.draw_text(str(self.statROF), 44, BLUE, rof.rect.centerx,rof.rect.centery+100+20)
            self.draw_text(str(self.statROF), 42, WHITE, rof.rect.centerx,rof.rect.centery+100+20)
            self.draw_text(str(self.statSpeed), 44, RED, speed.rect.centerx,speed.rect.centery +98+20)
            self.draw_text(str(self.statSpeed), 44, BLUE, speed.rect.centerx,speed.rect.centery+100+20)
            self.draw_text(str(self.statSpeed), 42, WHITE, speed.rect.centerx,speed.rect.centery+100+20)
            self.draw_text(str(self.statPhoenix), 44, RED, phoenix.rect.centerx,phoenix.rect.centery +98+20)
            self.draw_text(str(self.statPhoenix), 44, BLUE, phoenix.rect.centerx,phoenix.rect.centery+100+20)
            self.draw_text(str(self.statPhoenix), 42, WHITE, phoenix.rect.centerx,phoenix.rect.centery+100+20)


            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    if event.key == pg.K_RETURN:
                        waiting = False
                    if event.key == pg.K_ESCAPE:
                        waiting = False
                        self.running = False

            pg.display.flip()
    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

g = Game()
g.show_start_screen()
g.show_map_screen()
while g.running:
    g.new()
    g.show_go_screen()
pg.quit()