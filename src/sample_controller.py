import pygame
import random
from src.target import mole
from src.timer import Timer
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
    self.state="menu"
    
  def mainloop(self):
    while True:
      if self.state== "menu":
        self.menuloop()
      elif self.state == "game":
        self.gameloop()
    #select state loop
  ### below are some sample loop states ###

  def menuloop(self):
    while self.state == "menu":
      self.screen.fill("Black")
      font =pygame.font.Font('freesansbold.ttf',30)
      text= font.render('How many moles can you hit in one minute?',True,"white")
      self.screen.blit(text,(130,100))
      font =pygame.font.Font('freesansbold.ttf',100)
      text= font.render('Play',True,"white","green")
      self.screen.blit(text,(200,250))
      font =pygame.font.Font('freesansbold.ttf',100)
      text= font.render('Quit',True,"white","red")
      self.screen.blit(text,(500,250))
      pygame.display.update()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          mpos= pygame.mouse.get_pos()
          if mpos[0] <=415 and mpos[0] >= 200 and mpos[1] <=350 and mpos[1]>=250:
            self.state = "game"
          if mpos[0] <=715 and mpos[0] >= 500 and mpos[1] <=350 and mpos[1]>=250:
            exit()

  def make(self):
    posi = random.randrange(0,9)
    blank = pos[posi]
    self.moles.add(mole(blank[0],blank[1]))
  def gameloop(self):
    count = 0
    while self.state == "game":
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
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
    while self.state== "endgame":
      pygame.display.update()
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN():
          
          pygame.quit()
          quit()
      #event loop

      #update data

      #redraw
