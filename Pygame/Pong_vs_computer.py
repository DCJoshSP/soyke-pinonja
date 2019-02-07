import pygame
#Global Constants

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

pygame.init()

size = (640,480)

screen = pygame.display.set_mode(size)

#Title of new window/screen
pygame.display.set_caption("Pong")

#Exit game flag set to false
done = False

#Manages how fast screen refreshes
clock = pygame.time.Clock()

ball_width = 20
x_val = 150
y_val = 200
x_direction = 4
y_direction = 4
padd_length = 15
padd_width = 60
x_padd = 0
y_padd = 20
x_padd2 = 625
y_padd2 = 20
score = 0
score2 = 0
speed = 0
speed2 = 0

font = pygame.font.SysFont("comicsansms", 30)



#Game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #endif
           
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed2 = -5
            elif event.key == pygame.K_DOWN:
                speed2 = 5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                speed = -5    
            elif event.key == pygame.K_s:
                speed = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                speed2 = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                speed = 0
      
    #game logic
    if y_padd == 0 and speed == -5:
        pass
    else:
        y_padd = y_padd + speed
    
    y_padd2 = y_padd2 + speed2
    
    x_val = x_val + x_direction
    y_val = y_val + y_direction
    if y_val == 460:
        y_direction = y_direction * -1
    elif y_val == 0:
        y_direction = y_direction * -1
    if (12 <= x_val <= 16) and (y_padd < y_val and y_val < y_padd + 60):
        x_direction = x_direction * -1
    if (602 <= x_val <= 626) and (y_padd2 < y_val and y_val < y_padd2 + 60):
        x_direction = x_direction * -1        
    if x_val == 0:
        x_val = 150
        y_val = 200
        x_direction = 2
        y_direction = 2
        score2 = score2 + 1
    elif x_val == 640:
        x_val = 150
        y_val = 200
        x_direction = 2
        y_direction = 2
        score = score + 1
    if y_val > y_padd2 + 30:
        speed2 = 3
    elif y_val < y_padd2 + 30:
        speed2 = -3
        
    #screen background is black
    screen.fill(BLACK)

    #draw here
    text = font.render("score: " + str(score), True, WHITE)
    text2 = font.render("score: " + str(score2), True, WHITE)
    screen.blit(text,
        (20,10))
    screen.blit(text2,
        (510,10))
    pygame.draw.rect(screen,BLUE,(x_val,y_val,ball_width,ball_width))
    pygame.draw.rect(screen,WHITE,(x_padd,y_padd,padd_length,padd_width))
    pygame.draw.rect(screen,WHITE,(x_padd2,y_padd2,padd_length,padd_width))
    
    #flip display to reveal new position of objects
    pygame.display.flip()

    #the clock ticks over
    clock.tick(60)
#endwhile
pygame.quit()
    
