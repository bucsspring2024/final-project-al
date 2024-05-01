import pygame
import random
from src.target import mole
bg =pygame.image.load("./assets/Background.jpg")
pos = [(251,160),(412,156),(565,155),(243,293),(411,291),(572,287),(247,414),(415,415),(575,408)]
count = 0

class Controller:
  def __init__(self):
    
    pygame.init()
    width=900
    height=525
    z=[width,height]
    self.screen= pygame.display.set_mode(z)
    self.screen.blit(bg,(0,0))
    self.moles = pygame.sprite.Group()
    posi = random.randrange(0,9)
    blank = pos[posi]
    self.moles.add(mole(blank[0],blank[1]))

  def make(self):
    posi = random.randrange(0,9)
    blank = pos[posi]
    self.moles.add(mole(blank[0],blank[1]))
    
  def mainloop(self):
    count = 0 
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
          for x in self.moles:
            if x.rect.collidepoint(event.pos):
              x.kill()
              self.moles.remove(x)
              self.make()
              count= count + 1
              print(count)
  

      self.screen.blit(bg,(0,0))
      
      self.moles.draw(self.screen)
      pygame.display.flip()
      
    
    #select state loop
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    pass
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
    pass
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
    pass
      #event loop

      #update data

      #redraw
