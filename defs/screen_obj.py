import pygame

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

class Healthbar():
    def __init__(self,x,y,width,hight,max_hp):
        self.x = x
        self.y = y
        self.width = width
        self.hight = hight
        self.hp = max_hp
        self.max_hp = self.hp

    def draw(self,screen,hp):
        self.hp_ = hp
        retio =  (self.hp_/self.max_hp)
        pygame.draw.rect(screen, RED,(self.x,self.y,self.width,self.hight))
        pygame.draw.rect(screen, GREEN,(self.x,self.y,self.width*retio,self.hight))

class AmmoBar():
    def __init__(self,x,y,width,hight,max_ammo):
        self.x = x
        self.y = y
        self.width = width
        self.hight = hight
        self.ammo = max_ammo
        self.max_ammo = self.ammo

    def draw(self,screen,ammo):
        self.ammo_ = ammo
        retio =  (self.ammo_/self.max_ammo)
        pygame.draw.rect(screen, BLUE,(self.x,self.y,self.width*retio,self.hight))
