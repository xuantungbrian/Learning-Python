import pygame, sys, time, random
from pygame.locals import *



pygame.init()

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

b1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':RED, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect(200, 200, 20, 20), 'color':GREEN, 'dir':UPLEFT}
b3 = {'rect':pygame.Rect(100, 150, 60, 60), 'color':BLUE, 'dir':DOWNLEFT}
blocks = [b1, b2, b3]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    windowSurface.fill(BLACK)
    for b in blocks:
        if b['dir'] == UPLEFT:
            b['rect'].top -= MOVESPEED
            b['rect'].left -= MOVESPEED
        elif b['dir'] == UPRIGHT:
            b['rect'].top -= MOVESPEED
            b['rect'].left += MOVESPEED
        elif b['dir'] == DOWNLEFT:
            b['rect'].top += MOVESPEED
            b['rect'].left -= MOVESPEED
        elif b['dir'] == DOWNRIGHT:
            b['rect'].top += MOVESPEED
            b['rect'].left += MOVESPEED

        if b['rect'].top <= 0:
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            elif b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT
        elif b['rect'].bottom >= WINDOWHEIGHT:
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            elif b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT
        elif b['rect'].left <= 0:
            if b['dir'] == UPLEFT:
                b['dir'] = UPRIGHT
            elif b['dir'] == DOWNLEFT:
                b['dir'] = DOWNRIGHT
        elif b['rect'].right >= WINDOWWIDTH:
            if b['dir'] == UPRIGHT:
                b['dir'] = UPLEFT
            elif b['dir'] == DOWNRIGHT:
                b['dir'] = DOWNLEFT
        pygame.draw.rect(windowSurface, b['color'], b['rect'])

    pygame.display.update()
    time.sleep(0.02)
