import pygame
#import your controller

def main():
    pygame.init()
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()

pygame.init()
width=1000
height=1000
z=[width,height]
surface= pygame.display.set_mode(z)
bg =pygame.image.load("./assets/Backgound.jpg")
surface.blit(bg,(0,0))
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()   