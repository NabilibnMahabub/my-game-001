#importing libreraris
import pygame
import os
from defs.config import *
from defs.spritesheet import *
from entitys.bullet import *
from entitys.grenade import *

BG = (144,201,120)
RED = (255 ,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)

def draw_bg(screen):
    screen.fill(BG)
    pygame.draw.line(screen, RED ,(0, 400),(screen_w,400))

class Player(pygame.sprite.Sprite):
    def __init__(self ,char_type ,x ,y ,scale, speed, jump ,ammo,grenades):
        pygame.sprite.Sprite.__init__(self)
        self.x =x
        self.y =y
        self.alive = True
        self.health = 100
        self.start_health = self.health
        self.scale = scale
        self.char_type = char_type
        self.speed = speed
        self.shoot_cooldown = 0
        self.grenade_cooldown = 0
        self.ammo = ammo
        self.start_ammo = ammo
        self.grenades = grenades
        self.max_g = self.grenades
        self.jump = jump
        self.val_y = 0
        self.in_air = True
        self.direction = 1
        self.flip = False
        self.hitbox_ =False
        self.animation_list = [ ]
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        self.animation_types = ['idle','run','jump','crouch','death']
        for animation in self.animation_types:
            temp_list = []

            num = len(os.listdir(f'assets/player/count/{animation}'))
            img = pygame.image.load(f'assets/player/{self.char_type}/{animation}.png').convert_alpha()
            sheet = spritesheet(img)
            for i in range(num):
                if animation == 'death':
                    image = sheet.get_image(i,29,34,self.scale,BLACK)
                    temp_list.append(image)
                else:
                    image = sheet.get_image(i,28,34,self.scale,BLACK)
                    temp_list.append(image)
            self.animation_list.append(temp_list)
        
        self.image = self.animation_list[self.action][self.frame_index]

        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.hitbox = pygame.Rect(0, 0, 19*2, 34*2)
        self.hitbox.center = self.rect.center
    
    def update(self):
        self.update_animation()
        self.check_alive()
        #bullet cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        #grenade coollldown
        if self.grenade_cooldown > 0:
            self.grenade_cooldown -= 1

    def shoot(self,player):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 6
            bullet = Bullet(self.rect.centerx+(self.hitbox.size[0]*self.direction),self.rect.centery,self.direction,player)
            bullet_group.add(bullet)
            self.ammo -= 1
        
    def grenade(self,player):
        if self.grenade_cooldown == 0 and self.grenades > 0:
            self.grenade_cooldown = 40
            grenade = Grenade(self.rect.centerx+(0.1*self.hitbox.size[0]*self.direction),self.rect.centery+1,self.direction,player)
            grenade_group.add(grenade)
            self.grenades -= 1


    def move(self , moving_L,moving_R,sneek):
        #delta x and y velue
        dx = 0
        dy = 0

        #:> a
        if moving_L:
            dx = -self.speed
            self.direction = -1
            self.flip = True
        if moving_R:
            dx = self.speed
            self.direction = 1
            self.flip = False
        if self.jump and self.in_air == False:
            self.val_y = -11
            self.jump = False
            self.in_air = True

        #gravity
        self.val_y += GRAVITY
        if self.val_y > 10:
            self.val_y
        dy += self.val_y

        #FAke platform
        if self.rect.bottom + dy > 400:
            dy = 400 - self.rect.bottom
            self.in_air = False


        #update rect
        self.rect.x += dx
        self.rect.y += dy
    def controll(self , hitbox):
        if hitbox:
            self.hitbox_=True
        else:
            self.hitbox_=False

    
    def update_animation(self):
        #update animation
        ANIMATION_COOLDOWN = 100
        #updating image
        self.image = self.animation_list[self.action][self.frame_index]
        #game tick
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #looping the images
        if self.frame_index == len(self.animation_list[self.action]):
            if self.action == 4 or self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0
    
    def update_action(self, new_action):
        if new_action != self.action:
            self.frame_index = 0
            self.action = new_action
        
    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.update_action(4)# 4 = death
            if self.health ==0:
                self.kill()


    def draw(self,screen):
        flipped_image = pygame.transform.flip(self.image, self.flip ,False)
        flipped_image.set_colorkey(BLACK)
        screen.blit(flipped_image, self.rect)
        self.hitbox.center = self.rect.center

        if self.hitbox_:
            pygame.draw.rect(screen,WHITE,self.hitbox,2)
            pygame.draw.rect(screen,WHITE,self.rect,2)

        



