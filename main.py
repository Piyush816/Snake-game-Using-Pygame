# importing module
import pygame
import random

pygame.init()

#global variables
screenwidth = 750
screenheight = 500
exitgame = False
gameover = False
white = (255,255,255)
red = (255,0,0)
fps = 30
snakesize = 20
snakex = 100
snakey = 100
velocityx = 0
velocityy = 0
food = 8
foodx = random.randint(20,screenwidth-50)
foody = random.randint(20,screenheight-50)
score = 0
font = pygame.font.Font(None, 50)
snakelist = []
snakelenght = 1

def snake():
    for x,y in snakelist:
        pygame.draw.rect(window, white,[x,y,snakesize,snakesize])

def display_text(text,var,color,x,y):
    text = font.render(f"{text} : {var}",True,color)
    window.blit(text,[x,y])



# opening images
image = pygame.image.load("background.jpg")
bg = pygame.transform.scale(image,(screenwidth,screenheight))


# main window

window = pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("Snake and the Food! ")
clock = pygame.time.Clock()
pygame.display.update()

#game loop
while not exitgame:

    if gameover == True:
        window.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitgame = True
        # display_text("Game OverHighscore",score,red,250,200)
        text = font.render(f"Game Over", True,red)
        window.blit(text, [280, 200])
        text = font.render(f"Your score is : {score}", True, red)
        window.blit(text, [250, 250])
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitgame = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    velocityx = 5
                    velocityy = 0
                if event.key == pygame.K_LEFT:
                    velocityx = -5
                    velocityy = 0
                if event.key == pygame.K_UP:
                    velocityy = -5
                    velocityx = 0
                if event.key == pygame.K_DOWN:
                    velocityy = 5
                    velocityx = 0

                if abs(snakex-foodx)<40 and abs(snakey-foody)<40:
                    score = score+1
                    foodx = random.randint(20, screenwidth - 50)
                    foody = random.randint(20, screenheight - 50)
                    snakelenght = snakelenght+4

                if snakex<0 or snakex>screenwidth or snakey<0 or snakey>screenheight:
                    gameover = True



        head=[]
        head.append(snakex)
        head.append(snakey)
        snakelist.append(head)



        if len(snakelist) > snakelenght:
            del snakelist[0]


        snakex = snakex+velocityx
        snakey = snakey+velocityy
        window.fill(white)
        window.blit(bg,[0,0])
        display_text("Score",score,white,300,10)
        pygame.draw.circle(window, red, [foodx, foody], food)
        snake()


    clock=fps
    pygame.display.update()


