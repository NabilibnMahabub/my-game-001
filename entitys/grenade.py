import pygame

from defs.config import *
from defs.spritesheet import *

BLACK = (0,0,0)


grenade_group =pygame.sprite.Group()

class Grenade(pygame.sprite.Sprite):
    def __init__(self,x,y,direction,player,enemy):
        pygame.sprite.Sprite.__init__(self)
        self.timer = 100
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

        


        if self.direction == 1:
            self.flip =True
        else:
            self.flip =False
        
        
    def update_animation(self):
        pass
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
















"""# Check collision with player
        if pygame.sprite.spritecollide(self.player,grenade_group,False):
            if self.player.alive:
                self.player.health -= 5
                self.kill()
        
        # Check collision with enemy
        if pygame.sprite.spritecollide(self.enemy,grenade_group,False):
            if self.enemy.alive:
                self.enemy.health -= 5
                self.kill()"""