#importing libreraris
import pygame
from defs.config import *

BG = (144,201,120)
RED = (255 ,0,0)
WHITE = (255,255,255)

def draw_bg(screen):
    screen.fill(BG)
    pygame.draw.line(screen, RED ,(0, 400),(screen_w,400))

class Player(pygame.sprite.Sprite):
    def __init__(self ,char_type ,x ,y ,scale, speed, jump):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True

        self.scale = scale

        self.char_type = char_type

        self.speed = speed
        self.jump = jump
        self.val_y = 0

        self.direction = 1
        self.flip = False

        self.animation_list = [ ]
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        idle_list = []
        for i in range(5):
            img = pygame.image.load(f'assets/player/{self.char_type}/idle/{i}.png').convert_alpha()
            img = pygame.transform.scale(img,(int(img.get_width()*self.scale),int(img.get_height()*self.scale)))
            idle_list.append(img)
        self.animation_list.append(idle_list)

        run_list = []
        for i in range(6):
            img = pygame.image.load(f'assets/player/{self.char_type}/run/{i}.png').convert_alpha()
            img = pygame.transform.scale(img,(int(img.get_width()*self.scale),int(img.get_height()*self.scale)))
            run_list.append(img)
        self.animation_list.append(run_list)
        
        
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.shrink_rect()

    def shrink_rect(self):
        # Shrink the rect by a given factor and re-center it
        self.rect = pygame.Rect(
            self.rect.centerx - 29//2, 
            self.rect.centery - 16//2, 
            29, 
            16
        )

    def move(self , moving_L,moving_R):
        #delta x and y velue
        dx = 0
        dy = 0

        #:>
        if moving_L:
            dx = -self.speed
            self.direction = -1
            self.flip = True
        if moving_R:
            dx = self.speed
            self.direction = 1
            self.flip = False
        if self.jump:
            self.val_y = -11
            self.jump = False
        
        #gravity
        self.val_y += GRAVITY
        if self.val_y > 10:
            self.val_y
        dy += self.val_y

        #FAke platform
        if self.rect.bottom + dy > 400:
            dy = 400 - self.rect.bottom 


        #update rect
        self.rect.x += dx
        self.rect.y += dy
    
    def update_animation(self):
        #update animation
        ANIMATION_COOLDOWN = 100
        #updating image
        self.image = self.animation_list[self.action][self.frame_index]
        #game tick
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #looping the images
        if self.frame_index == len(self.animation_list[self.action]):
            self.frame_index = 0
    
    def update_action(self, new_action):
        if new_action != self.action:
            self.frame_index = 0
            self.action = new_action

    def draw(self,screen):
        screen.blit(pygame.transform.flip(self.image, self.flip ,False) , self.rect)
        pygame.draw.rect(screen,WHITE,self.rect,2)


