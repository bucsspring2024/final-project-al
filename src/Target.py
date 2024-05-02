import pygame
class Mole(pygame.sprite.Sprite):
    
    def __init__(self,x,y,img="./assets/mole.PNG"):
        '''
        Initializes the image of the mole into a sprite
        '''
        super().__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
