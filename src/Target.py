import pygame
class mole(pygame.sprite.Sprite):
    
    def __init__(self,x,y,img="./assets/mole.PNG"):
        
        super().__init__()
        
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        pass
            # pos = [(300,210),(465,210),(620,210),(295,340),(465,340),(625,340),(295,465),(465,465),(630,460)]
            
            # posi = random.randrange(0,8)
            # blank = pos[posi]
            
            # self.rect.x = blank[0]
            # self.rect.y = blank[1]
            
            
            # hole1=[300,210]
            # hole2=[465,210]
            # hole3=[620,210]
            # hole4=[295,340]
            # hole5=[465,340]
            # hole6=[625,340]
            # hole7=[295,465]
            # hole8=[465,465]
            # hole9=[630,460]
            