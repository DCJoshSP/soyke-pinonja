import pygame
#Global Constants
#Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

#Initialise pygame
pygame.init()

#Blank Screen
size = (640,480)

screen = pygame.display.set_mode(size)

#Title of new window/screen
pygame.display.set_caption("My window")

#Exit game flag set to false
done = False

sun_x = 40
sun_y = 100
#Manages how fast screen refreshes
clock = pygame.time.Clock()

#Game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #endif
    #next event
    #game logic goes after this comment
    sun_x = sun_x + 5
    #screen background is black
    screen.fill(BLACK)

    #draw here
    pygame.draw.rect(screen, BLUE, (220,165,200,150))
    pygame.draw.circle(screen, YELLOW, (sun_x, sun_y),40,0)

    #flip display to reveal new position of objects
    pygame.display.flip()

    #the clock ticks over
    clock.tick(60)
#endwhile
pygame.quit()
    
