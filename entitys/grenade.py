import pygame

from defs.config import *
from defs.spritesheet import *
from entitys.player import *


BLACK = (0,0,0)

enemy_group = pygame.sprite.Group()
grenade_group =pygame.sprite.Group()
explosion_group = pygame.sprite.Group()

class Grenade(pygame.sprite.Sprite):
    def __init__(self,x,y,direction,player,enemy):
        pygame.sprite.Sprite.__init__(self)
        self.timer = 100
        self.range_ = 64
        self.speed = 15
        self.val_y = -11
        self.frame_index = 0
        self.flip = False
        self.player = player
        self.enemy = enemy
        self.animation = [ ]
        self.update_time = pygame.time.get_ticks()

        img = pygame.image.load('assets/grenade/grenade_5.png').convert_alpha()
        sheet = spritesheet(img)

        for i in range(3):
            image = sheet.get_image(i,16,16,1,BLACK)
            self.animation.append(image)
        
        self.image = self.animation[self.frame_index]

        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction
    
    def update(self):
        self.update_animation()
        dy = 0 
        #shoot bulet
        self.rect.x += self.direction *self.speed
        self.rect.y += self.val_y


        #gravity
        self.val_y += GRAVITY
        if self.val_y > 10:
            self.val_y
        dy += self.val_y

        #FAke platform
        if self.rect.bottom + dy > 400:
            dy = 400 - self.rect.bottom
            self.speed = 0
        if self.rect.right < 0 or self.rect.left > screen_w:
            self.direction *= -1
            self.rect.x += self.direction *self.speed

        self.rect.y += dy
        
        #timer out
        self.timer -= 1
        if self.timer <= 0:
            self.kill()
            explosion = Explosion(self.rect.x,self.rect.y,3,self.range_,self.player,self.enemy)
            explosion_group.add(explosion)
        
    def update_animation(self):
        ANIMATION_COOLDOWN = 200

        self.image = self.animation[self.frame_index]

        #game tick
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #looping the images
        if self.frame_index == len(self.animation):
            self.frame_index = len(self.animation) - 1
        
        

    def draw(self,screen):
        screen.blit(self.image, self.rect)

class Explosion(pygame.sprite.Sprite):
    def __init__(self,x,y,scale,range_,player,enemy):
        pygame.sprite.Sprite.__init__(self)
        self.frame_index = 0
        self.scale = scale
        self.player = player
        self.enemy = enemy
        self.range_ = range_
        self.animation = [ ]
        self.update_time = pygame.time.get_ticks()

        img = pygame.image.load('assets/grenade/explosion.png').convert_alpha()
        sheet = spritesheet(img)

        for i in range(9):
            image = sheet.get_image(i,32,32,self.scale,BLACK)
            self.animation.append(image)
        
        self.image = self.animation[self.frame_index]

        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update(self):
        self.update_animation()
        if abs(self.rect.centerx - self.player.rect.centerx) <  TILE_SIZE *3 and abs(self.rect.centery - self.player.rect.centery) <  TILE_SIZE *3:
            self.player.health -= 50
        for enemy in enemy_group:
            if abs(self.rect.centerx - enemy.rect.centerx) <  TILE_SIZE *3 and abs(self.rect.centery - enemy.rect.centery) <  TILE_SIZE *3:
                enemy.health -= 50
            else:
                pass
        
        
    def update_animation(self):
        ANIMATION_COOLDOWN = 100

        self.image = self.animation[self.frame_index]

        #game tick
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #looping the images
        if self.frame_index == len(self.animation):
            self.frame_index = len(self.animation) - 1
        elif self.frame_index >= len(self.animation):
            self.kill()
        else:
            pass
        
        

    def draw(self,screen):
        screen.blit(self.image, self.rect)