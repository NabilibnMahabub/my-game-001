#importing libreraris
import pygame

pygame.init()

#defs
from defs.config import *
from entitys.player import *


screen = pygame.display.set_mode((screen_h ,screen_w))
pygame.display.set_caption('Janina')

player = Player(300,300,2)

#runner
run = True
while run:

    screen.blit(player.image , player.rect)

    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False

pygame.quit()