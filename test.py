import pygame
from defs.spritesheet import *

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption('test')

BG = (50,50,50)
BLACK = (0,0,0)

player = pygame.image.load('assets/player/blue/run.png').convert_alpha()
sheet = spritesheet(player)



player_0 = sheet.get_image(0,28,34,BLACK)
player_1 = sheet.get_image(1,28,34,BLACK)
player_2 = sheet.get_image(2,28,34,BLACK)
player_3 = sheet.get_image(3,28,34,BLACK)



# Main game loop
running = True
while running:

    screen.fill(BG)

    screen.blit(player_0,(0,0))
    screen.blit(player_1,((1*28*3),0))
    screen.blit(player_2,((2*28*3),0))
    screen.blit(player_3,((3*28*3),0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.update()

pygame.quit()



