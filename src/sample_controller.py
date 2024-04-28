import pygame

class Controller:
  
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode()
    self.background = pygame.image.load("assets/Initial_draft.jpg")
    self.state = "menu"
    pygame.display.flip()
    pygame.time.wait(10000)
    pygame.quit()
    
  def mainloop(self):
    pass
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

