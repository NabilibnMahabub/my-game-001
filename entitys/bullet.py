import pygame
from defs.config import *
from entitys.player import *



class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,direction,player):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 20
        self.player = player
        self.image = pygame.image.load('assets/bullet.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction
    
    def update(self):
        #shoot bulet
        self.rect.x += self.direction *self.speed

        if self.rect.right < 0 or self.rect.left > screen_w:
            self.kill()

        
       # Check collision with player
        if pygame.sprite.spritecollide(self.player,bullet_group,False):
            if self.player.alive:
                self.player.health -= 5
                self.kill()

        for enemy in enemy_group:
            if pygame.sprite.spritecollide(enemy,bullet_group,False):
                if enemy.alive:
                    enemy.health -= 5
                    self.kill()

        
        

    def draw(self,screen):
        screen.blit(self.image, self.rect)

