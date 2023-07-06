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
MOVESPEED = 4
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
bouncer = {'rect':pygame.Rect(300, 100, 50, 50), 'dir':UPLEFT}
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))
mainClock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    foodCounter +=1
    if foodCounter >= NEWFOOD:
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))
    
    windowSurface.fill(BLACK)
    
    
    if bouncer['dir'] == UPLEFT:
        bouncer['rect'].top -= MOVESPEED
        bouncer['rect'].left -= MOVESPEED
    elif bouncer['dir'] == UPRIGHT:
        bouncer['rect'].top -= MOVESPEED
        bouncer['rect'].left += MOVESPEED
    elif bouncer['dir'] == DOWNLEFT:
        bouncer['rect'].top += MOVESPEED
        bouncer['rect'].left -= MOVESPEED
    elif bouncer['dir'] == DOWNRIGHT:
        bouncer['rect'].top += MOVESPEED
        bouncer['rect'].left += MOVESPEED

    if bouncer['rect'].top <= 0:
        if bouncer['dir'] == UPLEFT:
            bouncer['dir'] = DOWNLEFT
        elif bouncer['dir'] == UPRIGHT:
            bouncer['dir'] = DOWNRIGHT
    elif bouncer['rect'].bottom >= WINDOWHEIGHT:
        if bouncer['dir'] == DOWNLEFT:
            bouncer['dir'] = UPLEFT
        elif bouncer['dir'] == DOWNRIGHT:
            bouncer['dir'] = UPRIGHT
    elif bouncer['rect'].left <= 0:
        if bouncer['dir'] == UPLEFT:
            bouncer['dir'] = UPRIGHT
        elif bouncer['dir'] == DOWNLEFT:
            bouncer['dir'] = DOWNRIGHT
    elif bouncer['rect'].right >= WINDOWWIDTH:
        if bouncer['dir'] == UPRIGHT:
            bouncer['dir'] = UPLEFT
        elif bouncer['dir'] == DOWNRIGHT:
            bouncer['dir'] = DOWNLEFT

    pygame.draw.rect(windowSurface, WHITE, bouncer['rect'])

    for i in foods[:]:
        if doRectsOverlap(i, bouncer['rect']):
            foods.remove(i)

    for i in range(len(foods)):
        pygame.draw.rect(windowSurface, GREEN, foods[i])

    pygame.display.update()
    mainClock.tick(40)
