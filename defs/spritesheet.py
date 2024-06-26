import pygame 

class spritesheet():
    def __init__(self,image):
        self.sheet = image
    def get_image(self,frame,width,hight,scale,color):
        image = pygame.Surface((width,hight,)).convert_alpha()
        image.blit(self.sheet,(0,0),((frame * width),0,width,hight))
        image = pygame.transform.scale(image ,(width *scale,hight*scale))
        image.set_colorkey(color)
        return image
    