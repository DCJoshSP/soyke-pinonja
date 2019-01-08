import pygame
import random
import math
# -- Global Constants    
 
BLACK = (0,0,0)   
WHITE = (255,255,255)   
BLUE = (50,50,255)   
YELLOW = (255,255,0)
RED = (255,0,0)

pygame.init()    

size = (640,480)   

screen = pygame.display.set_mode(size)   
 
pygame.display.set_caption("Pacman")

pacman_old_x = 0
pacman_old_y = 0

count = 0
map = [[1,1,1,1,1,1,1,1,1,1],  [1,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,1],  [1,1,0,1,1,1,1,1,0,1],  [1,0,0,0,0,0,1,0,0,1], [1,0,1,1,1,0,1,0,0,1], [1,0,1,1,1,0,1,0,0,1],  [1,0,1,1,1,0,1,0,0,1],  [1,0,0,0,0,0,0,0,0,1],  [1,1,1,1,1,1,1,1,1,1]]
font = pygame.font.SysFont("comicsansms", 30)
time_sec = 10

class tile(pygame.sprite.Sprite):
    def __init__(self,color,width,height,x_ref,y_ref):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x_ref
        self.rect.y = y_ref

class cherry(pygame.sprite.Sprite):
    def __init__(self,color,width,height,xval,yval):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = xval
        self.rect.y = yval      

class player(pygame.sprite.Sprite):
    def __init__(self, color, width, height, xcor, ycor, score):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = xcor
        self.rect.y = ycor
        self.speedx = 0
        self.speedy = 0
        self.score = score
    def player_set_speed(self, speedx, speedy):
        self.speedx = speedx
        self.speedy = speedy
    def update(self):
        self.rect.x = self.rect.x + self.speedx
        self.rect.y = self.rect.y + self.speedy

##class AI(pygame.sprite.Sprite):
##    def __init__(self,color,width,height,xval,yval):
##        super().__init__()
##        self.image = pygame.Surface([width, height])
##        self.image.fill(color)
##        self.rect = self.image.get_rect()
##        self.rect.x = xval
##        self.rect.y = yval
     

all_sprites_list = pygame.sprite.Group()

pacman = player(RED, 10, 10, 20, 20, 0)
all_sprites_list.add(pacman)
##monster = AI(WHITE, 10, 10, 40, 100)
##all_sprites_list.add(monster)

wall_list = pygame.sprite.Group()
cherry_list = pygame.sprite.Group()

for y in range(10):
    for x in range(10):
        if map[x][y] == 1:
            my_wall = tile(BLUE, 20, 20, x * 20, y * 20)
            wall_list.add(my_wall)
            all_sprites_list.add(my_wall)
            
while count <= 3:
    a = random.randrange(0, 9)
    b = random.randrange(0, 9)
    if map[a][b] == 0:
        cherry_tile = cherry(YELLOW,20, 20, a * 20, b * 20)
        cherry_list.add (cherry_tile)
        all_sprites_list.add(cherry_tile)
        count = count + 1
    
            

# -- Exit game flag set to false   
done = False  
   
clock = pygame.time.Clock()

### -- Game Loop   
while not done:   
    # -- User input and controls 
    for event in pygame.event.get():   
        if event.type == pygame.QUIT or time_sec <= 0:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pacman.player_set_speed(-1, 0)
            if event.key == pygame.K_RIGHT:
                pacman.player_set_speed(1, 0)
            if event.key == pygame.K_UP:
                pacman.player_set_speed(0, -1)
            if event.key == pygame.K_DOWN:
                pacman.player_set_speed(0, 1)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                pacman.player_set_speed(0, 0)
                
 
    # -- Game logic goes after this comment
    
    
    player_hit_list = pygame.sprite.spritecollide(pacman, wall_list, False)
    cherry_hit_list = pygame.sprite.spritecollide(pacman, cherry_list, True)

    for j in cherry_hit_list:
        pacman.score = pacman.score + 10
        
    for i in player_hit_list:
        pacman.player_set_speed(0, 0)
        pacman.rect.x = pacman_old_x
        pacman.rect.y = pacman_old_y

    pacman_old_x = pacman.rect.x
    pacman_old_y = pacman.rect.y
    all_sprites_list.update()
    
    screen.fill (BLACK)

    time_sec = time_sec - (1/60)
    # -- Draw here
    text = font.render("score: " + str(pacman.score), True, WHITE)
    text2 = font.render("time: " + str(round(time_sec,2)), True, WHITE)
    screen.blit(text,(300,70))
    screen.blit(text2,(300,110))
    all_sprites_list.draw (screen)
    
    pygame.display.flip()
    
    clock.tick(60)   
#End While - End of game loop   
pygame.quit()
