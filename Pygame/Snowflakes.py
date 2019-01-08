import pygame
import random
import math
#Global Constants
#Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
speed = 1

#Initialise pygame
pygame.init()



#Blank Screen
size = (640,480)

screen = pygame.display.set_mode(size)

#Title of new window/screen
pygame.display.set_caption("Snow")

class Snow(pygame.sprite.Sprite):
    #Define the constructor for snow
    def __init__(self, color, width, height, speed):
        #Call the spritee constructor
        super().__init__()
        #Create sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        #Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(0, 400)
        #Set speed of sprite
        self.speed = speed
        #End procedure
    def update(self):
        self.rect.y = self.rect.y + self.speed
        if self.rect.y == 475:
            self.rect.y = 0
    #End class


#Exit game flag set to false
done = False

#Create a list of the snow blocks
snow_group = pygame.sprite.Group()
#Create a list of all the sprites
all_sprites_group = pygame.sprite.Group()

#Create the snowflakes
number_of_flakes = 50
for x in range (number_of_flakes):
    my_snow = Snow(WHITE, 5, 5, 1)
    snow_group.add (my_snow)
    all_sprites_group.add (my_snow)
#next x

#Manages how fast screen refreshes
clock = pygame.time.Clock()

#Game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #endif
    #next event
                           
    #game logic

    all_sprites_group.update()
    #screen background is black
    screen.fill(BLACK)

    #draw here
    all_sprites_group.draw (screen)
    #flip display to reveal new position of objects
    pygame.display.flip()

    #the clock ticks over
    clock.tick(60)
#endwhile
pygame.quit()
