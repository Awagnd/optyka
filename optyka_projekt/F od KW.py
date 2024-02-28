import pygame, sys
from pygame.locals import *
import random
def pryzmat_współrzęne(a):
    ilość_hitboxów_pixel = 5

    wszystkie_hitboxy = []
    #róznica x
    różnica_x_abc = [abs(a[0][0] - a[1][0]),abs(a[1][0] - a[2][0]),abs(a[2][0] - a[0][0])]

    # róznica y
    różnica_y_abc = [abs(a[0][1] - a[1][1]),abs(a[1][1] - a[2][1]),abs(a[2][1] - a[0][1])]

    ab_długość = (różnica_x_abc[0] ** 2 + różnica_y_abc[0] ** 2) ** (0.5)
    bc_długość = (różnica_x_abc[1] ** 2 + różnica_y_abc[1] ** 2) ** (0.5)
    ca_długość = (różnica_x_abc[2] ** 2 + różnica_y_abc[2] ** 2) ** (0.5)

    ilość_hitboxów_abc = [int(ab_długość / ilość_hitboxów_pixel) + 1,int(bc_długość / ilość_hitboxów_pixel) + 1,int(ca_długość / ilość_hitboxów_pixel) + 1]

    #hitboxy abc
    for n in range(3):
        mx = 1
        my = 1
        if a[n][0] > a[(n + 1) %3][0]:
            mx = -1
        if a[n][1] > a[(n + 1) %3][1]:
            my = -1
        wartość_x = (różnica_x_abc[n] / (ilość_hitboxów_abc[n] ))  * mx
        wartość_y = (różnica_y_abc[n] / (ilość_hitboxów_abc[n] )) * my
        if n==2:

            print(wartość_y)
        for i in range(int(ilość_hitboxów_abc[n])):
            x = a[n][0] + wartość_x* (i + 1)
            y = a[n][1] + wartość_y * (i + 1)
            punkt = x,y
            wszystkie_hitboxy.append(punkt)


    # katy
    return wszystkie_hitboxy

pygame.init()

FPS = 30 #frames per second setting
fpsClock = pygame.time.Clock()

#set up the window
width1 = 500
height = 500
screen = pygame.display.set_mode((width1, height), 0, 32)
pygame.display.set_caption('taktyczny pryzmat krysiaczka')

#set up the colors
red = (255,   0,   0)
white = (255, 255, 255)
green = (0, 255, 0)
# mały program sprawdzający czy działa i wizualizujący wszystko (czerwone punkty to a,b,c kolejno od największego do najmniejszego czerrwonego punktu) z zielone to te ktore wygenerowała moja funkcja
c = (random.randint(0, screen.get_width()),random.randint(0, screen.get_height()))
b = (random.randint(0, screen.get_width()),random.randint(0, screen.get_height()))
a = (random.randint(0, screen.get_width()),random.randint(0, screen.get_height()))
wsp=pryzmat_współrzęne((a,b,c))
while True: # the main game loop
    # Create a temporary surface that supports alpha values
    surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    color = (255, 0, 0,75)  # or '#ffffffdd'
    pygame.draw.line(surface, color, (0,0), (100,100), 10)
    surface1 = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    color = (0, 255, 0, 75)  # or '#ffffffdd'
    pygame.draw.rect(surface1, color, (0, 0), (100, 100), 10)
    surface2 = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    color = (0, 0, 255, 75)  # or '#ffffffdd'
    pygame.draw.line(surface2, color, (0, 0), (300, 100), 10)
    screen.blit(surface, (0, 0))
    screen.blit(surface1, (0, 0))
    screen.blit(surface2, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)