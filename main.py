#importing libreraris
import pygame
from defs.config import *

pygame.init()

screen = pygame.display.set_mode((screen_h ,screen_w))
pygame.display.set_caption('Janina')



#runner
run = True
while run:
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False

pygame.quit()