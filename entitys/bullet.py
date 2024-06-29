import pygame
from defs.config import *
from entitys.player import *

bullet_group = pygame.sprite.Group()

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,direction ):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 20
        self.flip = False
        self.image = pygame.image.load('assets/bullet.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction
    
    def update(self):
        #shoot bulet
        self.rect.x += self.direction *self.speed

        if self.rect.right < 0 or self.rect.left > screen_w:
            self.kill()

        if self.direction == 1:
            self.flip =True
            print(self.direction , self.flip)
        else:
            print(self.direction , self.flip)
            self.flip =False
        
        """# Check collision with player
        if self.rect.collidedict(self.rect_dir):
            if self.player.alive:
                self.player.health -= 5
                self.kill()
        
        # Check collision with enemy
        if self.rect.colliderect(self.rect_dir):
            if self.enemy.alive:
                self.enemy.health -= 25
                self.kill()"""
        
        

    def draw(self,screen):
        screen.blit(pygame.transform.flip(self.image , self.flip , False),self.rect)

