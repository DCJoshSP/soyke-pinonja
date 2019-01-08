import pygame
import math
import random
#Global Constants
#Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)


pygame.init()


size = (640,480)

screen = pygame.display.set_mode(size)

class square(pygame.sprite.Sprite):
    def __init__(self, color, height, width, speed):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 440
        self.speed = speed
    def p1_set_speed(self, val):
        self.speed = val
    def update(self):
        self.rect.x = self.rect.x + self.speed

class floor(pygame.sprite.Sprite):
    def __init__(self,color, height, width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 460

class box(pygame.sprite.Sprite):
    def __init__(self,color, height, width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(70, 620)
        self.rect.y = 450

pygame.display.set_caption("Platform game")

#Exit game flag set to false
done = False

all_sprites_group = pygame.sprite.Group()
box_group = pygame.sprite.Group()
player_hit_group = pygame.sprite.Group()

z = False
w = False
game_over = False

for x in range(3):
    my_box = box(RED, 10, 10)
    box_group.add (my_box)
    all_sprites_group.add (my_box)
    

 
p1 = square(BLUE, 20, 20, 0)
all_sprites_group.add (p1)
ground = floor(WHITE, 20, 640)
all_sprites_group.add (ground)


clock = pygame.time.Clock()

#Game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or game_over == True:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                p1.p1_set_speed(-3)
            if event.key == pygame.K_UP:
                z = True
            elif event.key == pygame.K_RIGHT:
                p1.p1_set_speed(3)   
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                p1.p1_set_speed(0)
        #endif
    #next event
    #game logic goes

    if z == True:
        p1.rect.y = p1.rect.y - 2
        if p1.rect.y == 410:
            z = False
            w = True
    if w == True:
        p1.rect.y = p1.rect.y + 2
        if p1.rect.y == 440:
            w = False

    player_hit_group = pygame.sprite.spritecollide(p1, box_group, True)
    for count in player_hit_group:
        game_over = True
        
        
     
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
    
