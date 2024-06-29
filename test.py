import pygame
from defs.spritesheet import *
import os
# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption('test')

BG = (144,201,120)
BLACK = (0,0,0)

player = pygame.image.load('assets/player/blue/run.png').convert_alpha()
sheet = spritesheet(player)

char_type = 'blue'
animation_list = [ ]
frame_index = 0
action = 0
update_time = pygame.time.get_ticks()
animation_types = ['idle','run','jump']
for animation in animation_types:
    temp_list = []
    num = len(os.listdir(f'assets/player/count/{animation}'))
    img = pygame.image.load(f'assets/player/{char_type}/{animation}.png').convert_alpha()
    sheet = spritesheet(img)
    for i in range(num):
        image = sheet.get_image(i,28,34,2,BLACK)
        temp_list.append(image)
    animation_list.append(temp_list)




# Main game loop
running = True
while running:

    screen.fill(BG)

    #update animation
    ANIMATION_COOLDOWN = 100
    #updating image
    image = animation_list[action][frame_index]
    #game tick
    if pygame.time.get_ticks() - update_time > ANIMATION_COOLDOWN:
        update_time = pygame.time.get_ticks()
        frame_index += 1
    #looping the images
    if frame_index == len(animation_list[action]):
        frame_index = 0

    screen.blit(pygame.transform.flip(image,True,False),(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.update()

pygame.quit()



