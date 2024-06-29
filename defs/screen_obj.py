import pygame

RED = (255,0,0)
GREEN = (0,255,0)

class Healthbar():
    def __init__(self,x,y,width,hight,max_hp):
        self.x = x
        self.y = y
        self.width = width
        self.hight = hight
        self.hp = max_hp
        self.max_hp = self.hp

    def draw(self,screen):
        retio =  (self.hp/self.max_hp)
        pygame.draw.rect(screen, RED,(self.x,self.y,self.width,self.hight))
        pygame.draw.rect(screen, GREEN,(self.x,self.y,self.width*retio,self.hight))

class AmmoBar():
    def __init__(self,x,y,width,hight,max_hp):
        self.x = x
        self.y = y
        self.width = width
        self.hight = hight
        self.hp = max_hp
        self.max_hp = self.hp

    def draw(self,screen):
        retio =  (self.hp/self.max_hp)
        pygame.draw.rect(screen, RED,(self.x,self.y,self.width,self.hight))
        pygame.draw.rect(screen, GREEN,(self.x,self.y,self.width*retio,self.hight))
