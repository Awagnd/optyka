
import math
import pygame
pygame.init()
font2 = pygame.font.Font('SuperFunkyFreeFont.ttf', 20)
def collidecircle(a,b,r):
    return (a[0]-b[0])**2+(a[1]-b[1])**2<=r**2
def collidecircles(a,b,r,r2):
    return (a[0]-b[0])**2+(a[1]-b[1])**2<=(r+r2)**2
def glass_quartz_mm(n):
    n/=1000
    return (2.33+0.015/n**2)**0.5
def fluoryt_mm(n):
    n/=1000
    return (2.034+0.075/n**2)**0.5
def kitchensalt_mm(n):
    n/=1000
    return (3.034+0.0166/n**2)**0.5
def font_render(text, s,r):
    font2_render = font2.render(text, True, (255, 255, 255))
    fr = font2_render.get_rect()
    fr.x = r.center[0] - fr.width / 2
    fr.y = r.center[1] - fr.height / 2
    s.blit(font2_render, fr)
def fonts_render(s,zy,y,texts,r):
    y-=font2.get_height()/2
    for n in texts:
        font2_render = font2.render(n, True, (255, 255, 255))
        fr = font2_render.get_rect()
        fr.x = r.center[0] - fr.width / 2
        fr.y = y
        s.blit(font2_render, fr)
        y+=zy
def pryzmat_współrzęne(a):
    ilość_hitboxów_pixel = 2
    wszystkie_hitboxy = []
    #róznica x
    różnica_x_abc = [abs(a[0][0] - a[1][0]),abs(a[1][0] - a[2][0]),abs(a[2][0] - a[0][0])]

    # róznica y
    różnica_y_abc = [abs(a[0][1] - a[1][1]),abs(a[1][1] - a[2][1]),abs(a[2][1] - a[0][1])]

    ab_długość = (różnica_x_abc[0] ** 2 + różnica_y_abc[0] ** 2) ** (0.5)
    bc_długość = (różnica_x_abc[1] ** 2 + różnica_y_abc[1] ** 2) ** (0.5)
    ca_długość = (różnica_x_abc[2] ** 2 + różnica_y_abc[2] ** 2) ** (0.5)

    ilość_hitboxów_abc = [int(ab_długość / ilość_hitboxów_pixel) + 1,int(bc_długość / ilość_hitboxów_pixel) + 1,int(ca_długość / ilość_hitboxów_pixel) + 1]
    ps=[]
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
        wszystkie_hitboxy.append([])
        for i in range(int(ilość_hitboxów_abc[n])):
            x = a[n][0] + wartość_x* (i + 1)
            y = a[n][1] + wartość_y * (i + 1)
            if ilość_hitboxów_abc[n]//2==i:
                ps.append((x,y))
            punkt = int(x),int(y)
            wszystkie_hitboxy[-1].append(punkt)

    return wszystkie_hitboxy

def autistic_lines(surface,st, en, width,k,alfa, cp=(0,0,0),spr=0):
    px=pygame.PixelArray(surface)
    rx = int(en[0] - st[0])
    ry = int(en[1] - st[1])
    k= [k[0]-cp[0],k[1]-cp[1],k[2]-cp[2]]
    if k[0]<0:
        k[0]=0
    if  k[1]<0:
        k[1]=0
    if  k[2] < 0:
        k[2] = 0
    k = int(k[0] * alfa), int(k[1] * alfa), int(k[2] * alfa)
    if spr==1:
        print(k)
    i = max(abs(rx), abs(ry))
    if i!=0:
        zx = rx / i
        zy = ry / i
        w = int(width / 2)
        if rx == 0:
            a = 90
        else:
            if st[0]<=en[0] and st[1]<=en[1]:
                a =math.degrees(math.atan(ry / (rx)))
            elif st[0]<=en[0] and st[1]>=en[1]:
                a =math.degrees(math.atan(ry / (rx)))*-1
            elif st[0]>=en[0] and st[1]<=en[1]:
                a =math.degrees(math.atan(ry / (rx)))*-1
            elif st[0]>=en[0] and st[1]>=en[1]:
                a =math.degrees(math.atan(ry / (rx)))
        if a>=45:
            for c in range(width):
                x = st[0] - w + c
                y = st[1]
                for n in range(i):
                    nx=int(x)
                    ny=int(y)
                    if nx >= 1200 or nx <= 0 or ny >= 800:
                        break
                    kolor=surface.get_at((nx,ny))
                    if k[0]+kolor[0]<255:
                        kolor[0] = (k[0]+kolor[0])
                    else:
                        kolor[0]=255
                    if k[1] + kolor[1] < 255:
                        kolor[1] = k[1] + kolor[1]
                    else:
                        kolor[1] = 255
                    if k[2] + kolor[2] < 255:
                        kolor[2] = (k[2] + kolor[2])
                    else:
                        kolor[2] = 255
                    px[nx][ny] = kolor
                    x += zx
                    y += zy
        else:
            for c in range(width):
                x = st[0]
                y = st[1]- w + c
                for n in range(i):
                    nx = int(x)
                    ny = int(y)
                    if nx >= 1200 or nx <= 0 or ny >= 800:
                        break
                    kolor = surface.get_at((nx, ny))
                    if k[0] + kolor[0] < 255:
                        kolor[0] = k[0] + kolor[0]
                    else:
                        kolor[0] = 255
                    if k[1] + kolor[1] < 255:
                        kolor[1] =k[1] + kolor[1]
                    else:
                        kolor[1] = 255
                    if k[2] + kolor[2] < 255:
                        kolor[2] = k[2] + kolor[2]
                    else:
                        kolor[2] = 255
                    px[nx][ny] = kolor
                    x += zx
                    y += zy

def wavelength_to_rgb(wavelength, gamma=0.8):
    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    R *= 255
    G *= 255
    B *= 255
    return [int(R), int(G), int(B)]

def autistic_colors(kolory):
    kolor=[0,0,0,0]
    kl=[]
    for n in range(len(kolory)):
        kl.append(kolory[n][1])
    print(kl)
    for k in kl:
        if k[0] + kolor[0] < 255:
            kolor[0] = (k[0] + kolor[0])
        else:
            kolor[0] = 255
        if k[1] + kolor[1] < 255:
            kolor[1] = k[1] + kolor[1]
        else:
            kolor[1] = 255
        if k[2] + kolor[2] < 255:
            kolor[2] = (k[2] + kolor[2])
        else:
            kolor[2] = 255
    return kolor
