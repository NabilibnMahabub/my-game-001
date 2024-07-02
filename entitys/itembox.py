import pygame

from defs.spritesheet import *

BLACK = (0,0,0)

class Itembox(pygame.sprite.Sprite):
    def __init__(self,item_type,x,y,player):
        pygame.sprite.Sprite.__init__(self)
        self.frame_index = 0
        self.player = player
        self.item_type = item_type
        self.animation = [ ]
        self.update_time = pygame.time.get_ticks()

        img = pygame.image.load(f'assets/itembox/{self.item_type}.png').convert_alpha()
        sheet = spritesheet(img)

        for i in range(2):
            image = sheet.get_image(i,32,32,2,BLACK)
            self.animation.append(image)
        
        self.image = self.animation[self.frame_index]

        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update(self):
        self.update_animation()

        if pygame.sprite.collide_rect(self,self.player):
            if self.item_type == 'health_box':
                self.kill()
                self.player.health += 25
                if self.player.health > self.player.max_health:
                    self.player.health = self.player.max_health
            elif self.item_type == 'ammo_box':
                self.kill()
                self.player.ammo += 100
                if self.player.ammo > self.player.max_ammo:
                    self.player.ammo = self.player.max_ammo
            elif self.item_type == 'grenade_box':
                self.kill()
                self.player.grenades += 10
                if self.player.grenades > self.player.max_g:
                    self.player.grenades = self.player.max_g



        
    def update_animation(self):
        ANIMATION_COOLDOWN = 300

        self.image = self.animation[self.frame_index]

        #game tick
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #looping the images
        if self.frame_index == len(self.animation):
            self.frame_index = 0
    
    def draw(self,screen):
        screen.blit(self.image, self.rect)