#importing libreraris
import pygame

pygame.init()

#defs
from defs.config import *
from entitys.player import *
from entitys.bullet import *


screen = pygame.display.set_mode((screen_w ,screen_h))
pygame.display.set_caption('Janina')
pygame.mouse.set_visible(False)

moving_L = False
moving_R = False
jump = False
shoot = False


player = Player('blue',300,300,2,5,11,600)
enemy = Player('red',500,300,2,5,11,600)

corsor = pygame.image.load('assets/corsor/corsor.png').convert_alpha()


#runner
run = True
while run:
    pos = pygame.mouse.get_pos()
    
    clock.tick(FPS)
    draw_bg(screen)

    player.update()
    player.draw(screen)
    
    enemy.update_animation()
    enemy.draw(screen)
    
    #bullet group
    bullet_group.update()
    bullet_group.draw(screen)
    
    if player.alive:
        if shoot:
            player.shoot()
        if player.in_air == True:
            player.update_action(2)#2 = jump
        elif moving_L or moving_R:
            player.update_action(1)#1 = run
        else:
            player.update_action(0)#0 = idle
    
    player.move(moving_L,moving_R)
    
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                shoot = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                shoot = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_L = True
            if event.key == pygame.K_d:
                moving_R = True
            if event.key == pygame.K_SPACE and player.alive:
                player.jump = True
            if event.key == pygame.K_ESCAPE:
                run = False
    
        #on relise
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_L = False
            if event.key == pygame.K_d:
                moving_R = False
    screen.blit(corsor,pos)
    
    pygame.display.update()


pygame.quit()