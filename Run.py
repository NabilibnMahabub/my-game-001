#importing libreraris
import pygame

pygame.init()

#defs
from defs.config import *
from defs.screen_obj import *
from entitys.player import *
from entitys.bullet import *
from entitys.grenade import *
from entitys.itembox import *




screen = pygame.display.set_mode((screen_w ,screen_h))
pygame.display.set_caption('Janina')
pygame.mouse.set_visible(False)

moving_L = False
moving_R = False
jump = False
sneek = False
shoot = False
grenade = False
hitbox = False



player = Player('blue',300,300,2,5,11,600,10)
enemy = Player('red',600,300,2,2,11,600,0)
enemy2 = Player('black',800,300,2,2,11,600,0)
enemy3 = Player('yellow',900,300,2,2,11,600,0)
enemy4 = Player('green',700,300,2,2,11,600,0)

health_box = Itembox('health_box',500,350,player)
ammo_box = Itembox('ammo_box',600,350,player)
grenade_box = Itembox('grenade_box',700,350,player)



enemy_group.add(enemy)
enemy_group.add(enemy2)
enemy_group.add(enemy3)
enemy_group.add(enemy4)

itembox_group.add(health_box)
itembox_group.add(ammo_box)
itembox_group.add(grenade_box)




corsor = pygame.image.load('assets/corsor/corsor.png').convert_alpha()
corsor = pygame.transform.scale(corsor,(5*2,5*2))

health_bar = Healthbar(5,5,100,10,100)
ammo_bar = AmmoBar(5,20, 16.8,10,100)
grenade_bar = GrenadeBar(5,35,1000,10,100)



#runner
run = True
while run:
    pos = pygame.mouse.get_pos()
    
    clock.tick(FPS)
    draw_bg(screen)

    ammo_bar.draw(screen,player.ammo)
    health_bar.draw(screen,player.health)
    grenade_bar.draw(screen,player.grenades)


    player.controll(hitbox)
    player.update()
    player.draw(screen)
    player.move(moving_L,moving_R)


    for enemy in enemy_group:
        enemy.ai(player)
        enemy.controll(hitbox)
        enemy.update()
        enemy.draw(screen)
    
    grenade_group.update()
    grenade_group.draw(screen)

    explosion_group.update()
    explosion_group.draw(screen)

    bullet_group.update()
    bullet_group.draw(screen)

    itembox_group.update()
    itembox_group.draw(screen)
    
    if player.alive:
        if shoot:
            player.shoot(player)
        if grenade:
            player.grenade(player)
        
        if sneek:
            player.update_action(3)# 3 = sneek
        elif player.in_air == True:
            player.update_action(2)#2 = jump
        elif moving_L or moving_R:
            player.update_action(1)#1 = run
        else:
            player.update_action(0)#0 = idle
    
    
    
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
            if event.key == pygame.K_LSHIFT:
                sneek = True
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_g:
                grenade = True
            if event.key == pygame.K_b:
                if hitbox:
                    hitbox=False
                else:
                    hitbox=True
        #on relise
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_L = False
            if event.key == pygame.K_d:
                moving_R = False
            if event.key == pygame.K_SPACE and player.alive:
                player.jump = False
            if event.key == pygame.K_LSHIFT:
                sneek = False
            if event.key == pygame.K_g:
                grenade = False

    screen.blit(corsor,pos)
    
    pygame.display.update()


pygame.quit()