import pygame, sys, time, random
from pygame.locals import *



pygame.init()

def doRectsOverlap(rect1, rect2):
    for a, b in [(rect1, rect2), (rect2, rect1)]:
        if ((isPointInsideRect(a.left, a.top, b)) or (isPointInsideRect(a.left, a.bottom, b)) or (isPointInsideRect(a.right, a.top, b)) or (isPointInsideRect(a.right, a.bottom, b))):
            return True
    return False

def isPointInsideRect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False

WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation')

UPLEFT = 7
UPRIGHT = 9
DOWNLEFT = 1
DOWNRIGHT = 3
MOVESPEED = 6
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player = pygame.Rect(300, 100, 40, 40)
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))
mainClock = pygame.time.Clock()

moveLeft = False
moveRight = False
moveUp = False
moveDown = False

playerImage = pygame.image.load('me.jpg')
playerStretchedImage = pygame.transform.scale(playerImage, (40, 40))
foodImage = pygame.image.load('Rose.jpg')



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == ord('a'):
                moveLeft = True
                moveRight = False
            if event.key == K_RIGHT or event.key == ord('d'):
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == ord('w'):
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == ord('s'):
                moveDown = True
                moveUp = False
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == ord('a'):
                moveLeft = False
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = False
            if event.key == K_UP or event.key == ord('w'):
                moveUp = False
            if event.key == K_DOWN or event.key == ord('s'):
                moveDown = False
            if event.key == ord('x'):
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)


    foodCounter +=1
    if foodCounter >= NEWFOOD:
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))
    
    windowSurface.fill(BLACK)
    
    
    if moveDown and player.bottom < WINDOWHEIGHT:
        player.bottom += MOVESPEED
        #if player.bottom > WINDOWHEIGHT:
           # player.bottom = WINDOWHEIGHT
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
        #if player.top < 0:
           # player.top = 0
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
        #if player.left < 0:
            #player.left = 0
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED
        #if player.right > WINDOWWIDTH:
            #player.right = WINDOWWIDTH

    pygame.draw.rect(windowSurface, WHITE, player)

    for i in foods[:]:
        if doRectsOverlap(i, player):
            foods.remove(i)

    for i in foods:
        pygame.draw.rect(windowSurface, GREEN, i)

    pygame.display.update()
    mainClock.tick(40)
