#importing libreraris
import pygame
import time

pygame.init()

#defs
from defs.config import *
from defs.screen_obj import *
from entitys.player import *
from entitys.bullet import *
from entitys.grenade import *
from entitys.itembox import *
from defs.spritesheet import *


side_margin = 300
lower_margin = 100

scrol_r = False
scrol_l = False
scroll = 0


screen = pygame.display.set_mode((screen_w+side_margin ,screen_h+lower_margin))
pygame.display.set_caption('Janina kivhabe banay')

#entitys
player = pygame.image.load(f'assets/player/blue/idle.png').convert_alpha()
enemy = pygame.image.load(f'assets/player/black/idle.png').convert_alpha()
enemy1 = pygame.image.load(f'assets/player/green/idle.png').convert_alpha()
enemy2 = pygame.image.load(f'assets/player/red/idle.png').convert_alpha()
enemy3 = pygame.image.load(f'assets/player/yellow/idle.png').convert_alpha()

#backgrounds
bg_0 = pygame.image.load(f'assets/background/sky.png').convert_alpha()
bg_1 = pygame.image.load(f'assets/background/cloud.png').convert_alpha()
bg_2 = pygame.image.load(f'assets/background/mountain.png').convert_alpha()
bg_3 = pygame.image.load(f'assets/background/pine1.png').convert_alpha()
bg_4 = pygame.image.load(f'assets/background/pine2.png').convert_alpha()

#item boxs
ammo_box = pygame.image.load(f'assets/itembox/ammo_box.png').convert_alpha()
grenade_box = pygame.image.load(f'assets/itembox/grenade_box.png').convert_alpha()
player_box = pygame.image.load(f'assets/itembox/health_box.png').convert_alpha()

#scale
bg_0 = pygame.transform.scale(bg_0,(bg_0.get_width()*2,bg_0.get_height()*2))
bg_1 = pygame.transform.scale(bg_1,(bg_1.get_width()*2,bg_1.get_height()*2))
bg_2 = pygame.transform.scale(bg_2,(bg_2.get_width()*2,bg_2.get_height()*2))
bg_3 = pygame.transform.scale(bg_3,(bg_3.get_width()*2,bg_3.get_height()*2))
bg_4 = pygame.transform.scale(bg_4,(bg_4.get_width()*2,bg_4.get_height()*2))

player_ = spritesheet(player)
enemy_ = spritesheet(enemy)
enemy_1 = spritesheet(enemy1)
enemy_2 = spritesheet(enemy2)
enemy_3 = spritesheet(enemy3)

player_.get_image(0,28,34,1.5,BLACK)
enemy_.get_image(0,28,34,1.5,BLACK)
enemy_1.get_image(0,28,34,1.5,BLACK)
enemy_2.get_image(0,28,34,1.5,BLACK)
enemy_3.get_image(0,28,34,1.5,BLACK)

rect = pygame.Rect(0,0,screen_w,screen_h)


def draw_bg(screen):
    width_1 = bg_0.get_width()
    screen.fill(BG)
    for j in range(5):
        #screen.blit(bg_0,((j * width_1)-scroll,0))
        screen.blit(bg_1,((j * width_1)-scroll*0.6,0))
        screen.blit(bg_2,((j * width_1)-scroll*0.7,290))
        screen.blit(bg_3,((j * width_1)-scroll*0.8,400))
        screen.blit(bg_4,((j * width_1)-scroll*0.9,402))
    pygame.draw.rect(screen,WHITE,rect,1)


#runner
run = True
while run:

    draw_bg(screen)

    if scrol_l == True and scroll > 0:
        scroll -= 5
    elif scroll == False:
        scroll = scroll
    if scrol_r == True:
        scroll += 5
    elif scroll == False:
        scroll = scroll
    
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                scrol_r = True
            elif event.key == pygame.K_LEFT:
                scrol_l = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                scrol_r = False
            elif event.key == pygame.K_LEFT:
                scrol_l = False

    
    pygame.display.update()


pygame.quit()