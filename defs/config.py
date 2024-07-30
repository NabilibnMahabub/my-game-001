import pygame

#screeen rez
screen_w = 1376
screen_h = 800

TILE_SIZE = 32

#FPS

clock = pygame.time.Clock()
FPS = 60
GRAVITY = .8

#groups
enemy_group = pygame.sprite.Group()
grenade_group =pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
itembox_group = pygame.sprite.Group()

