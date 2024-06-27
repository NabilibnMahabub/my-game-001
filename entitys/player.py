#importing libreraris
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self ,x ,y ,scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('assets/player/blue/0.png')
        self.image = pygame.transform.scale(img,(int(img.get_width()*scale),int(img.get_height()*scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)


