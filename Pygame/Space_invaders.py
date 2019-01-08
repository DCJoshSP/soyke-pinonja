import pygame
import random
import math
#Global Constants
#Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)
speed = 1


#Initialise pygame
pygame.init()

#Blank Screen
size = (640,480)

screen = pygame.display.set_mode(size)

#Title of new window/screen
pygame.display.set_caption("Space invaders")

class Invader(pygame.sprite.Sprite):
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
        self.rect.y = random.randrange(-50, 0)
        #Set speed of sprite
        self.speed = speed
        #End procedure
    def update(self):
        self.rect.y = self.rect.y + self.speed
        if self.rect.y == 480:
            self.rect.y = 0
        
    #End class
class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height, lives, bullet_count, score):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 470
        self.speed = 0
        self.lives = lives
        self.bullet_count = bullet_count
        self.score = score
        #End procedure
    def player_set_speed(self, val):
        self.speed = val
    def update(self):
        if self.rect.x == 0 and self.speed == -3:
            pass
        elif self.rect.x == 630 and self.speed == 3:
            pass
        else:
            self.rect.x = self.rect.x + self.speed

class Bullet(pygame.sprite.Sprite):
    def __init__(self, color, speed):
        super().__init__()
        self.color = color
        self.speed = speed
        self.speed = -2
    def constructor(self, color, x, y):
        self.speed = -2
        height = 2
        width = 2
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
    def update(self):
        self.rect.y = self.rect.y + self.speed
    
#Exit game flag set to false
done = False

#Create a list of the snow blocks
invader_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
#Create a list of all the sprites
all_sprites_group = pygame.sprite.Group()

#Create the snowflakes
number_of_invaders = 10
for x in range (number_of_invaders):
    my_invader = Invader(BLUE, 10, 10, 1)
    invader_group.add (my_invader)
    all_sprites_group.add (my_invader)
#next x
player = Player(YELLOW, 10, 10, 5, 50, 0)
bullet = Bullet(RED, 2)
bullet.constructor(RED, player.rect.x + 5, 470)
all_sprites_group.add (player)
#Manages how fast screen refreshes
clock = pygame.time.Clock()

font = pygame.font.SysFont("comicsansms", 30)

#Game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or player.lives == 0:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.player_set_speed(-3)
                if player.rect.x == 0:
                    player.player_set_speed(0)
            if event.key == pygame.K_UP:
                if player.bullet_count >0:
                    bullet = Bullet(RED, 2)
                    bullet.constructor(RED, player.rect.x + 5, 470)
                    bullet_group.add (bullet)
                    all_sprites_group.add (bullet)
                    player.bullet_count = player.bullet_count - 1
            elif event.key == pygame.K_RIGHT:
                player.player_set_speed(3)
                if player.rect.x == 630:
                    player.player_set_speed(0)   
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.player_set_speed(0)
    #game logic
    player_hit_group = pygame.sprite.spritecollide(player, invader_group, True)
    bullet_hit_group = pygame.sprite.groupcollide(bullet_group, invader_group, True, True) 

    for z in bullet_hit_group:
        player.score = player.score + 5
        
    for y in player_hit_group:
        player.lives = player.lives - 1
    

        
    all_sprites_group.update()
    
    #screen background is black
    screen.fill(BLACK)

    #draw here
    text = font.render("lives: " + str(player.lives), True, WHITE)
    text2 = font.render("score: " + str(player.score), True, WHITE)
    text3 = font.render("bullets: " + str(player.bullet_count), True, WHITE)
    screen.blit(text,(20,10))
    screen.blit(text2,(20,50))
    screen.blit(text3,(20,90))
    all_sprites_group.draw (screen)
    #flip display to reveal new position of objects
    pygame.display.flip()

    #the clock ticks over
    clock.tick(60)
#endwhile
pygame.quit()
