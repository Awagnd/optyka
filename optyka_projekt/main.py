import time
from funtons import *
from particles import *
import pygame
import math
from pygame.locals import *
import sys
running=True
fps=60
pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((1200, 800))

font = pygame.font.Font('GLARY TROPIC SMOOTH.ttf',200)
starttext = font.render(f'Optyka', True, (124,252,0))


texts=[]

Up_img=pygame.image.load("add.png")
Up_img=pygame.transform.scale(Up_img, (30, 30))
up=Up_img.get_rect()

Down_img=pygame.image.load("remove.png")
Down_img=pygame.transform.scale(Down_img, (30, 30))
down=Down_img.get_rect()

Up2_img=pygame.transform.scale(Up_img, (30, 30))
up2=Up2_img.get_rect()

Down2_img=pygame.transform.scale(Down_img, (30, 30))
down2=Down2_img.get_rect()

up.y = 85
down.y = 115

Światło_src=pygame.image.load("laser.png")
Światło_src=pygame.transform.rotate(Światło_src, -90)
Światło_src=pygame.transform.scale(Światło_src, (100, 60))
Swiatłosrc=Światło_src.get_rect()
Swiatłosrc.x=100
Swiatłosrc.y=80

WL_img=pygame.image.load("laser.png")
WL_img=pygame.transform.rotate(WL_img,-90)
WL_img=pygame.transform.scale(WL_img, (100, 60))
WL=WL_img.get_rect()

WL.y=80

zakres_img=pygame.image.load("zakres.png")
zakres_img=pygame.transform.scale(zakres_img, (150, 45))
zakres=zakres_img.get_rect()
zakres.y=100-zakres.height
zakres.x=400


pointer_img=pygame.image.load("pointer.png")
pointer_img=pygame.transform.scale(pointer_img, (20, 30))
pointer_img=pygame.transform.rotate(pointer_img, -90)
pointer=pointer_img.get_rect()
pointer.y=zakres.y-pointer.height

pointer2=pointer_img.get_rect()
pointer2.y=zakres.y-pointer2.height


trash_img=pygame.image.load("trash.png")
trash_img=pygame.transform.scale(trash_img, (100, 120))
trash=trash_img.get_rect()
trash.y=40

BUTTonstart=pygame.image.load("BUTTon.png")
BUTTonstart=pygame.transform.scale(BUTTonstart, (700, 200))
BUTTonstartRect=BUTTonstart.get_rect()
BUTTonstartRect.x=600-BUTTonstart.get_width()/2
BUTTonstartRect.y=500-BUTTonstart.get_height()/2

Zwierciadło_img=pygame.image.load("fafa.png")
Zwierciadło_img=pygame.transform.scale(Zwierciadło_img, (10, 100))
ZW=Zwierciadło_img.get_rect()
ZW.x=300
ZW.y=50
Zwierciadło_img.set_colorkey("black")

CollZwierciadło_img=pygame.image.load("P.png")
CollZwierciadło_img=pygame.transform.scale(CollZwierciadło_img, (10, 10))

Soczewka_img=pygame.image.load("lens.png")
Soczewka_img=pygame.transform.scale(Soczewka_img, (110, 110))
Soczewka=Soczewka_img.get_rect()
Soczewka.x=500
Soczewka.y=50


bg=pygame.image.load("background.png")
bg=pygame.transform.scale(bg, (1200, 800))

pryzmat_img=pygame.image.load("prism.png")
pryzmat_img=pygame.transform.scale(pryzmat_img, (120, 120))
pryzmat=pryzmat_img.get_rect()
pryzmat.x=700
pryzmat.y=30

substance_choice=pygame.Rect(0,0,200,50)

acc_img=pygame.image.load("P.png")
acc_img=pygame.transform.scale(acc_img, (30, 30))
acc=acc_img.get_rect()

R=[(0,0),4]

CollHashmap=[]
for n in range(screen.get_width()):
    CollHashmap.append([])
    for i in range(screen.get_height()):
        CollHashmap[-1].append(0)
Interface_img=pygame.image.load("W.jpg")
Interface_img=pygame.transform.scale(Interface_img, (1200, 200))
INf=Interface_img.get_rect()
INf.x=0
INf.y=0

Wkolory=[]

start=False
Slider_img=pygame.image.load("slider.png")
Slider_img=pygame.transform.scale(Slider_img, (150, 10))
Slider=Slider_img.get_rect()

Slider2=Slider_img.get_rect()
Slider2.y=100+Slider.height/2


Slider3=Slider_img.get_rect()
Slider3.y=50+Slider.height/2


Slider4=Slider_img.get_rect()
Slider4.y=150+Slider.height/2

JDO=False
JDO2=False
PointSlider_img=pygame.image.load("sliderpoint.png")
PointSlider_img=pygame.transform.scale(PointSlider_img, (30, 30))
PointSlider=PointSlider_img.get_rect()

PointSlider_img=pygame.image.load("sliderpoint.png")
PointSlider_img=pygame.transform.scale(PointSlider_img, (30, 30))
PointSlider2=PointSlider_img.get_rect()
PointSlider2.y=Slider2.center[1]-PointSlider2.height/2

PointSlider3=PointSlider_img.get_rect()
PointSlider3.y=Slider3.center[1]-PointSlider3.height/2


PointSlider4=PointSlider_img.get_rect()
PointSlider4.y=Slider4.center[1]-PointSlider4.height/2

prism_material=[]
flat2=False
flat=False
gruby=False
Teststart=False
pryzmaty=[]
White_lights=[]
White_lights_img=[]
White_angles=[]
White_width=[]
pryzmatyhitbox=[]
pryzmatkaty=[]
pryzmatyimg=[]
SoczewkiKąty=[]
JDDYY=0
ZWierciadlas=[]
ZWierciadlas_img=[]
ZWkąt=[]
YYY=0
PrismCocklor=[]
Soczewki=[]
IndeksySoczewki=[]
IndeksyPryxmatów=[]
lens_hitboxes=[]
YourJawz_img=[]
HitboxZWierciadlas=[]
lenHitboxZWierciadlas=[]
Kolejność=[]
Kol=0
Light_quantity=[]
KątŚ=[]
SoczewkiRect2=[]
leng=0
SRCes=[]
SRCes_img=[]
gruboschit=[]
SoczewkiRect=[]
Change=False
Move=False
Clicked1=False
pygame.init()
Raz=False
JDDY=0
Part=[]
zk=[]
Ork=0
WC=0
SocziRekts=[]
JDDX=0
colorchange=[[255,0,0],0]
colorchangezm=0
WeCooling=False
b =0
WL_refraction_indexes=[]
Prism_transparency=[]
PrismReflectiveindex=[]
WL_refraction_indexes_lens=[]
lens_transparency=[]
lensReflectiveindex=[]
lens_material=[]
lri=[]
WL_colors=[]
colorssum=[]
pri=[]
cpl=[]
while running:
    clock.tick(60)
    mousePos=pygame.mouse.get_pos()
    screen.fill((0,0,0,0))
    keys = pygame.key.get_pressed()
    if start==False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                running = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if BUTTonstartRect.collidepoint(mousePos):
                    start=True
        ch=3
        if colorchange[1]==0:
            colorchange[0][1]+=ch
            colorchangezm+=ch
        elif colorchange[1] == 1:
            colorchange[0][0] += -ch
            colorchangezm += ch
        elif colorchange[1] == 2:
            colorchange[0][2] += ch
            colorchangezm += ch
        elif colorchange[1] == 3:
            colorchange[0][1] += -ch
            colorchangezm += ch
        elif colorchange[1] == 4:
            colorchange[0][0] += ch
            colorchangezm += ch
        elif colorchange[1] == 5:
            colorchange[0][2] += -ch
            colorchangezm += ch
        if colorchangezm==255:
            colorchangezm=0
            colorchange[1]+=1
            colorchange[1]%=6
        starttext = font.render(f'Optyka', True, (colorchange[0]))
        b += random.randint(0,5)
        b+=1
        if b>40:
            b=0

        if b == 0:
            Part.append(Particle(random.randint(100,1100),random.randint(200,600),3,(200, 200, 200),random.randint(0,360),random.randint(1,2)))
        a=0
        for n in Part:
            if n.parpop:
                Part.pop(a)
            else:
                n.fading()
                n.move()
                n.draw(screen)
            a+=1

        screen.blit(BUTTonstart,BUTTonstartRect)
        screen.blit(starttext, (600-starttext.get_width()/2, 400-starttext.get_width()/2))


    else:
        screen.blit(Interface_img, INf)
        Up = False
        Down = False
        if Raz==False:
            if Change:
                ZW.x = -200
                Swiatłosrc.x = -200
                Soczewka.x = -200
                pryzmat.x = -200

                if Typ==1:
                    Swiatłosrc.x = 50
                    PointSlider.x=200+Slider.width/2-PointSlider.width/2
                    Slider.x=200
                    PointSlider.y = 100+Slider.height/2-PointSlider.height/2
                    Slider.y = 100
                elif Typ==2:
                    ZW.x = 50
                    PointSlider.x = 200 + Slider.width / 2 - PointSlider.width / 2
                    Slider.x = 200
                    PointSlider.y = 100 + Slider.height / 2 - PointSlider.height / 2
                    Slider.y = 100
                elif Typ==3:
                    down.x = 250
                    up.x = 250
                    down2.x = 450
                    up2.x = 450
                    up2.y = 85
                    down2.y=115
                    PointSlider.x = 300 - PointSlider.width / 2
                    Grubosc=0
                    Slider.x = 300
                    PointSlider.y = 100 + Slider.height / 2 - PointSlider.height / 2
                    Slider.y = 100

                    Slider2.x = 500
                    Slider2.y = 100
                    PointSlider2.x = Slider2.center[0] - PointSlider2.width / 2
                    Slider4.x = 500
                    Slider4.y = 150
                    Slider3.x = 500
                    PointSlider3.x = Slider3.center[0] - PointSlider3.width / 2
                    PointSlider4.center = Slider4.center[0], Slider4.center[1]
                    zakres.x = 700
                    pointer.x = zakres.center[0] - pointer.width / 2
                    substance_choice.center = (1000, 100)
                    wc=1
                elif Typ==4:
                    acc.center=(400,100)
                    Slider2.x=500
                    PointSlider2.x=Slider2.center[0]-PointSlider2.width/2
                    Slider.x=500
                    Slider.y=150

                    PointSlider.x=Slider.center[0]-PointSlider.width/2
                    Slider3.x=500
                    PointSlider3.x=Slider3.center[0]-PointSlider3.width/2
                    PointSlider.center = PointSlider.center[0],Slider.center[1]
                    zakres.x=700
                    pointer.x=zakres.center[0]-pointer.width/2
                    substance_choice.center=(1000,100)
                elif Typ==5:

                    WL.x = 50
                    PointSlider.x=200+Slider.width/2-PointSlider.width/2
                    Slider.x=200
                    PointSlider.y = 100+Slider.height/2-PointSlider.height/2
                    Slider.y = 100
                    pointer.x = zakres.x-pointer.width/2
                    pointer2.x = zakres.x + zakres.width-pointer.width/2
                    up.x  =600
                    down.x=600
                    WLqua=5


            else:
                Zwierciadło_img = pygame.transform.scale(Zwierciadło_img, (10, 100))
                ZW = Zwierciadło_img.get_rect()
                ZW.x = 300
                ZW.y = 50
                Swiatłosrc.x = 100
                Swiatłosrc.y = 75
                Soczewka.x = 500
                Soczewka.y = 40
                pryzmat.x = 700
                trash.x = 900
                WL.x = 1050

            Raz=True

        if Change:
            if Typ==4:
                for n in pryzmatypkt:
                    pygame.draw.circle(screen,(255,0,0),n,15)
                pygame.draw.polygon(screen,cp,pryzmatypkt,5)
                screen.blit(acc_img, acc)
                screen.blit(Slider_img, Slider2)

                screen.blit(Slider_img, Slider)
                screen.blit(PointSlider_img, PointSlider2)
                screen.blit(Slider_img, Slider3)
                screen.blit(PointSlider_img, PointSlider3)

                screen.blit(PointSlider_img, PointSlider)
                screen.blit(zakres_img, zakres)
                screen.blit(pointer_img, pointer)
                pygame.draw.rect(screen,(100,100,100),substance_choice)
                if substance_choice.height==50:
                    if wc==1:
                        font_render("glass quartz",screen,substance_choice)
                    elif wc==2:
                        font_render("Flourite",screen,substance_choice)
                else:
                    fonts_render(screen,50,100,("glass quartz","Flourite"),substance_choice)

            else:
                screen.blit(Slider_img, Slider)
                screen.blit(PointSlider_img, PointSlider)
                if Typ==3:

                    screen.blit(Slider_img, Slider2)
                    screen.blit(Slider_img, Slider4)
                    screen.blit(PointSlider_img, PointSlider2)
                    screen.blit(Slider_img, Slider3)
                    screen.blit(PointSlider_img, PointSlider3)
                    print(PointSlider3,PointSlider2,PointSlider4)
                    screen.blit(PointSlider_img, PointSlider4)
                    screen.blit(zakres_img, zakres)
                    screen.blit(pointer_img, pointer)
                    pygame.draw.rect(screen, (100, 100, 100), substance_choice)
                    if substance_choice.height == 50:
                        if wc == 1:
                            font_render("glass quartz", screen, substance_choice)
                        elif wc == 2:
                            font_render("Flourite", screen, substance_choice)
                    else:
                        fonts_render(screen, 50, 100, ("glass quartz", "Flourite"), substance_choice)
                    screen.blit(Down_img, down)
                    screen.blit(Up_img, up)
                    screen.blit(Down2_img, down2)
                    screen.blit(Up2_img, up2)
                    if keys[pygame.K_p]:
                        if flat == False and flat2 == False:
                            flat = True
                            JDO = True
                    if keys[pygame.K_o]:
                        if flat == True:
                            flat = False
                            JDO=True

                    elif keys[pygame.K_w]:
                        SoczewkaR1 += 1
                        JDO=True
                        flat=False
                    elif keys[pygame.K_s]:
                        SoczewkaR1 -= 1
                        JDO=True
                        flat=False

                    elif keys[pygame.K_f]:
                        if flat==False and flat2==False:
                            flat2 =True
                            JDO2=True
                    if keys[pygame.K_g]:
                        if flat2 == True:
                            flat2 = False
                            JDO2 = True

                    elif keys[pygame.K_a]:
                        SoczewkaR2 += 1
                        JDO2=True
                        flat2=False
                    elif keys[pygame.K_d]:
                        SoczewkaR2 -= 1
                        JDO2=True
                        flat2=False
                    elif keys[pygame.K_LEFT]:
                        if Soczewkastrona == -1:
                            Soczewkastrona = 1
                            JDO = True
                            flat = False
                    elif keys[pygame.K_RIGHT]:
                        if Soczewkastrona == 1:
                            if SoczewkaX1[0]-SoczewkaX1[1]+SoczewkaX1[0]>SoczewkaX2[1]:
                                JDO=True
                                flat=False
                                Soczewkastrona = -1

                    elif keys[pygame.K_UP]:
                        if Soczewka2strona == 1:
                            if SoczewkaX2[0]-SoczewkaX2[1]+SoczewkaX2[0]<SoczewkaX1[1]:
                                JDO2=True
                                flat2=False
                                Soczewka2strona = -1
                                print("usgh")
                    elif keys[pygame.K_DOWN]:
                        if Soczewka2strona==-1:
                            Soczewka2strona = 1
                            JDO2=True
                            flat2=False
                if Typ==5:
                    screen.blit(zakres_img,zakres)
                    screen.blit(pointer_img,pointer)
                    screen.blit(pointer_img,pointer2)
                    screen.blit(Down_img,up)
                    screen.blit(Down_img,down)

        a=0
        for BALLS in YourJawz_img:
            draw=[]
            for i in BALLS:
                draw.append(i)
            if cpl[a] == (0, 0, 0):
                pygame.draw.polygon(screen, (255, 255, 255), draw, 5)
            else:
                pygame.draw.polygon(screen, cpl[n],draw, 5)
            a+=1

        #print(SoczewkiKąty)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                running = False
            if Change == False:
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                     if Clicked1==False:
                         if Swiatłosrc.collidepoint(mousePos):
                             Typ=1
                             leng=len(SRCes)-1
                             Light_quantity.append(10)

                             Change = True
                             Raz=False
                             break
                         elif ZW.collidepoint(mousePos):
                             Typ=2
                             leng=len(ZWierciadlas)-1
                             lenHitboxZWierciadlas.append(10)
                             Change = True
                             Raz=False
                             break
                         elif Soczewka.collidepoint(mousePos):
                             JDO=True
                             Typ = 3
                             leng = len(SocziRekts)
                             Change = True
                             Raz = False
                             SoczewkaR1=50
                             grubosc=0
                             gruboschit=[]
                             SoczewkiKąty.append([])
                             SoczewkiKąty.append([])
                             SoczewkiKąty.append([])
                             JDO2=True
                             SoczewkaR2 = 50
                             flat = False
                             flat2 = False
                             Soczewkastrona = 1
                             Soczewka2strona = 1
                             cp = (255, 255, 255)

                             break
                         elif pryzmat.collidepoint(mousePos):
                             Typ=4
                             leng=len(ZWierciadlas)-1
                             lenHitboxZWierciadlas.append(10)
                             Change = True
                             Raz=False
                             cp=(255,255,255)
                             pryzmatypkt = [(110,0),(110-200*3**0.5/3,200),(110+200*3**0.5/3,200)]
                             wc=1
                             break
                         elif WL.collidepoint(mousePos):
                             Typ=5
                             leng=len(White_lights)
                             White_width.append(10)
                             Change = True
                             Raz=False

                             break
                         else:
                             a=0
                             for n in SRCes:
                                 if n.collidepoint(mousePos):
                                     Clicked1 = True
                                     Move=True
                                     Typ = 1
                                     leng = a
                                     break
                                 a+=1
                             a = 0
                             for n in SocziRekts:
                                 if n.collidepoint(mousePos):
                                     Clicked1 = True
                                     Move = True
                                     Typ = 3
                                     leng = a
                                     break
                                 a += 1
                             a=0
                             for n in ZWierciadlas:
                                 if n.collidepoint(mousePos):
                                     Clicked1 = True
                                     Move = True
                                     Typ = 2
                                     leng = a
                                     break
                                 a += 1
                         a = 0
                         for n in pryzmaty:
                             if n.collidepoint(mousePos):
                                 Clicked1 = True
                                 Move = True
                                 Typ = 4
                                 leng = a
                                 break
                             a += 1
                         a = 0
                         for n in White_lights:
                             if n.collidepoint(mousePos):
                                 Clicked1 = True
                                 Move = True
                                 Typ = 5
                                 leng = a
                                 break
                             a += 1
                print(lens_transparency)
                if Clicked1:
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                        if Typ==1:
                            if trash.collidepoint(mousePos):
                                for n in range(20):
                                    Part.append(Particle(trash.center[0], trash.center[1], 7.5, (200, 200, 200),random.randint(0, 360), random.randint(500, 1000)/300))
                                SRCes.pop(leng)
                                KątŚ.pop(leng)
                        elif Typ==2:
                            if trash.collidepoint(mousePos):
                                for n in range(20):
                                    Part.append(Particle(trash.center[0], trash.center[1], 7.5, (200, 200, 200),random.randint(0, 360), random.randint(500, 1000)/300))
                                ZWierciadlas.pop(leng)
                                ZWkąt.pop(leng)
                                lenHitboxZWierciadlas.pop(leng)
                                ZWierciadlas_img.pop(leng)
                                HitboxZWierciadlas.pop(leng)
                        elif Typ == 3:
                            if trash.collidepoint(mousePos):
                                for n in range(20):
                                    Part.append(Particle(trash.center[0], trash.center[1], 7.5, (200, 200, 200),random.randint(0, 360), random.randint(500, 1000)/300))
                                SocziRekts.pop(leng)
                                SoczewkiKąty.pop(leng)
                                lens_hitboxes.pop(leng)
                                YourJawz_img.pop(leng)
                                lens_transparency.pop(leng)
                                lensReflectiveindex.pop(leng)
                                lens_material.pop(leng)
                                lri.pop(leng)
                                cpl.pop(leng)
                        elif Typ==4:
                            if trash.collidepoint(mousePos):
                                for n in range(20):
                                    Part.append(Particle(trash.center[0], trash.center[1], 7.5, (200, 200, 200),random.randint(0, 360), random.randint(500, 1000)/300))
                                pryzmatyhitbox.pop(leng)
                                pryzmaty.pop(leng)
                                pryzmatyimg.pop(leng)
                                pryzmatkaty.pop(leng)
                                Prism_transparency.pop(leng)
                                pri.pop(leng)
                                PrismCocklor.pop(leng)

                                PrismReflectiveindex.pop(leng)
                        elif Typ==5:
                            if trash.collidepoint(mousePos):
                                for n in range(20):
                                    Part.append(Particle(trash.center[0], trash.center[1], 7.5, (200, 200, 200),random.randint(0, 360), random.randint(500, 1000)/300))
                                White_lights_img.pop(leng)
                                White_lights.pop(leng)
                                White_angles.pop(leng)
                                White_width.pop(leng)
                                Wkolory.pop(leng)
                                colorssum.pop(leng)


                        Stop = False
                        Clicked1 = False
                        Move= False


                    if keys[pygame.K_UP]:
                        Up=True
                    if keys[pygame.K_DOWN]:
                        Down=True
            else:
                if Typ==2:
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        if ZW.collidepoint(mousePos):
                            Raz = False
                            ZWierciadlas_img.append(pygame.transform.scale(pygame.image.load("fafa.png"), (10, 10* lenHitboxZWierciadlas[leng])))
                            ZWierciadlas.append(Zwierciadło_img.get_rect())
                            leng=len(ZWierciadlas)-1
                            HitboxZWierciadlas.append([])
                            for n in range (0, int(lenHitboxZWierciadlas[leng]*10/2)):
                                HitboxZWierciadlas[leng].append([0,0])
                            Clicked1 = True
                            Change = False
                            ZWkąt.append(90)
                            break
                    if pygame.mouse.get_pressed()[0]==True:
                        if PointSlider.collidepoint(mousePos):
                            if Slider.x +Slider.width> mousePos[0] > Slider.x:
                                PointSlider.x=mousePos[0]-PointSlider.width/2
                                lenHitboxZWierciadlas[leng]=int(10+(PointSlider.x-Slider.x-Slider.width/2)//10)
                                print(lenHitboxZWierciadlas[leng])
                            Zwierciadło_img = pygame.transform.scale(Zwierciadło_img, (10, 10*lenHitboxZWierciadlas[leng] ))
                            ZW = Zwierciadło_img.get_rect()
                            ZW.x = 50
                            ZW.y = 50-(lenHitboxZWierciadlas[leng]-10)*5
                elif Typ==1:
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        if Swiatłosrc.collidepoint(mousePos):
                            Clicked1 = True
                            Change = False
                            Raz = False

                            SRCes_img.append(pygame.transform.scale(pygame.image.load("laser.png"), (100, 45)))
                            SRCes.append(Światło_src.get_rect())
                            leng = len(SRCes) - 1
                            KątŚ.append(90)
                            break
                    if pygame.mouse.get_pressed()[0]==True:
                        if PointSlider.collidepoint(mousePos):
                            if Slider.x +Slider.width> mousePos[0] > Slider.x:
                                PointSlider.x=mousePos[0]-PointSlider.width/2
                                Light_quantity[leng+1]=int(10+(PointSlider.x-Slider.x-Slider.width/2)//10)
                elif Typ==3:
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        if SocziRekt.collidepoint(mousePos):
                            Clicked1 = True
                            Change = False
                            Raz = False
                            lens_hitboxes.append(SoczewkiRect + SoczewkiRect2 + gruboschit)
                            YourJawz_img.append(Soczewkamask)
                            SocziRekts.append(SocziRekt)
                            Soczewkamask=[]
                            SoczewkiKąty[leng]+=SoczewkiKąty[leng+1]
                            SoczewkiKąty[leng] += SoczewkiKąty[leng + 2]
                            SoczewkiKąty.pop(-1)
                            SoczewkiKąty.pop(-1)
                            SoczewkiRect=[]
                            SoczewkiRect2=[]
                            TI =(PointSlider2.center[0]-Slider2.x)/Slider2.width
                            print(TI)
                            ri = (PointSlider4.center[0] - Slider4.x) / Slider4.width +1
                            rei=(PointSlider2.center[0]-Slider2.x)/Slider2.width
                            if cp==(255,255,255):
                                cp=(0,0,0)
                            cpl.append(cp)
                            # sys.exit()
                            lens_transparency.append(TI)
                            lensReflectiveindex.append(rei)
                            lri.append(ri)
                            lens_material.append(wc)
                            for ni in range(len(lens_hitboxes[-1])):
                                CollHashmap[int(lens_hitboxes[-1][ni][0])][int(lens_hitboxes[-1][ni][1])]=(3, SoczewkiKąty[leng][ni])
                            break
                    if pygame.mouse.get_pressed()[0]==True:
                        if up.collidepoint(mousePos):
                            if SoczewkaR1>50:
                                SoczewkaR1 -= 1
                                flat=False
                                JDO=True
                        elif down.collidepoint(mousePos):
                            SoczewkaR1 += 1
                            flat = False
                            JDO = True
                        if up2.collidepoint(mousePos):
                            if SoczewkaR2>50:
                                SoczewkaR2 -= 1
                                flat=False
                                JDO2=True
                        elif down2.collidepoint(mousePos):
                            SoczewkaR2 += 1
                            flat = False
                            JDO2 = True

                        elif PointSlider.collidepoint(mousePos):
                            if Soczewkastrona==1 and Soczewka2strona==1 or SoczewkaX1[1]-20>= SoczewkaX2[1] and SoczewkaX1[0]-20>= SoczewkaX2[0]:
                                if Slider.x +Slider.width> mousePos[0] > Slider.x:
                                    PointSlider.x=mousePos[0]-PointSlider.width/2
                                    grubosc=int(1+(PointSlider.x-Slider.x)//10)
                                JDO=True
                                JDO2 = True
                                gruby=True
                        elif PointSlider2.collidepoint(mousePos):
                            if Slider2.x + Slider2.width >= mousePos[0] >= Slider2.x:
                                PointSlider2.x = mousePos[0] - PointSlider2.width / 2
                        elif PointSlider4.collidepoint(mousePos):
                            if Slider4.x + Slider4.width >= mousePos[0] >= Slider4.x:
                                PointSlider4.x = mousePos[0] - PointSlider4.width / 2

                        elif PointSlider3.collidepoint(mousePos):
                            if Slider3.x + Slider3.width >= mousePos[0] >= Slider3.x:
                                PointSlider3.x = mousePos[0] - PointSlider3.width / 2
                        elif pointer.collidepoint(mousePos):
                            if zakres.x + zakres.width > mousePos[0] > zakres.x:
                                pointer.x = mousePos[0] - pointer.width / 2
                                cp=screen.get_at((pointer.center[0], zakres.center[1]))

                        if substance_choice.collidepoint(mousePos):
                            if mousePos[1]<125:
                                wc=1
                            elif mousePos[1]<175:
                                wc=2
                    if substance_choice.collidepoint(mousePos):
                        substance_choice.height=50*2
                    else:
                        substance_choice.height = 50
                    if keys[pygame.K_b]:
                        cp=(255,255,255)
                elif Typ==4:
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        if acc.collidepoint(mousePos):
                            Clicked1 = True
                            Change = False
                            Raz = False
                            x=pryzmatypkt[0][0],pryzmatypkt[1][0],pryzmatypkt[2][0]
                            w=max(x)-min(x)
                            y = pryzmatypkt[0][1], pryzmatypkt[1][1], pryzmatypkt[2][1]
                            h =max(y)-min(y)
                            pryzmaty.append(Rect(min(x),min(y),w,h))
                            pryzmatyhitbox.append(pryzmat_współrzęne(pryzmatypkt))
                            pryzmatkaty.append((150,270,30))
                            pryzmatyimg.append(pryzmatypkt)
                            l=len(pryzmatyhitbox[-1][0])
                            leng = len(pryzmaty) - 1
                            TI =(PointSlider2.center[0]-Slider2.x)/Slider2.width
                            ri = (PointSlider.center[0] - Slider.x) / Slider.width +1
                            rei=(PointSlider2.center[0]-Slider2.x)/Slider2.width
                            print(ri)
                            if cp ==(255,255,255):
                                cp=(0,0,0)
                            PrismCocklor.append(cp)
                            for n in range(3):
                                for ni in range(l):
                                    CollHashmap[pryzmatyhitbox[-1][n][ni][0]][pryzmatyhitbox[-1][n][ni][1]]=(4, pryzmatkaty[leng][n])
                            pri.append(ri)
                            Prism_transparency.append(TI)
                            PrismReflectiveindex.append(rei)
                            prism_material.append(wc)
                            break
                    if pygame.mouse.get_pressed()[0]==True:
                        if 220 > mousePos[0] > 0 and 200 > mousePos[1] > 0:
                            if collidecircle(mousePos,pryzmatypkt[0],15):
                                pryzmatypkt[0]=mousePos
                            elif collidecircle(mousePos,pryzmatypkt[1],15):
                                pryzmatypkt[1]=mousePos
                            elif collidecircle(mousePos,pryzmatypkt[2],15):
                                pryzmatypkt[2]=mousePos
                        elif PointSlider2.collidepoint(mousePos):
                            if Slider2.x + Slider2.width >= mousePos[0] >= Slider2.x:
                                PointSlider2.x = mousePos[0] - PointSlider2.width / 2
                        elif PointSlider.collidepoint(mousePos):
                            if Slider.x + Slider.width >= mousePos[0] >= Slider.x:
                                PointSlider.x = mousePos[0] - PointSlider.width / 2

                        elif PointSlider3.collidepoint(mousePos):
                            if Slider3.x + Slider3.width >= mousePos[0] >= Slider3.x:
                                PointSlider3.x = mousePos[0] - PointSlider3.width / 2
                        elif pointer.collidepoint(mousePos):
                            if zakres.x + zakres.width > mousePos[0] > zakres.x:
                                pointer.x = mousePos[0] - pointer.width / 2
                                cp=screen.get_at((pointer.center[0], zakres.center[1]))

                        if substance_choice.collidepoint(mousePos):
                            if mousePos[1]<125:
                                wc=1
                            elif mousePos[1]<175:
                                wc=2
                    if substance_choice.collidepoint(mousePos):
                        substance_choice.height=50*2
                    else:
                        substance_choice.height = 50
                    if keys[pygame.K_w]:
                        cp=(255,255,255)
                                
                elif Typ==5:
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        if WL.collidepoint(mousePos):
                            Clicked1 = True
                            Change = False
                            Raz = False
                            White_lights.append(WL_img.get_rect())
                            White_lights_img.append(WL_img)
                            White_angles.append(90)
                            leng = len(White_lights) - 1
                            d=pointer.center[0]-zakres.x
                            WL_colors.append([])
                            a=380,750
                            WL_wave_length = []
                            Wkolory.append([])
                            for n in range(WLqua+1):
                                WL_wave_length.append(380+370*(d/zakres.width))
                                d+=(pointer2.center[0]-pointer.center[0])/WLqua
                            for n in WL_wave_length:
                                Wkolory[-1].append((n, wavelength_to_rgb(n)))
                            print(Wkolory)
                            colorssum.append(autistic_colors(Wkolory[-1]))
                            break
                    if pygame.mouse.get_pressed()[0]==True:
                        if PointSlider.collidepoint(mousePos):
                            if Slider.x +Slider.width> mousePos[0] > Slider.x:
                                PointSlider.x=mousePos[0]-PointSlider.width/2
                                White_width[leng]=int(10+(PointSlider.x-Slider.x-Slider.width/2)//10)
                                print(White_width[leng])
                        if pointer.collidepoint(mousePos):
                            if zakres.x +zakres.width> mousePos[0] > zakres.x and mousePos[0]<pointer2.center[0]:
                                pointer.x=mousePos[0]-pointer.width/2
                        elif pointer2.collidepoint(mousePos):
                            if zakres.x +zakres.width> mousePos[0] > zakres.x and mousePos[0]>pointer.center[0]:
                                pointer2.x=mousePos[0]-pointer2.width/2
                        elif down.collidepoint(mousePos):
                            if WLqua > 1:
                                WLqua -= 1
                        elif up.collidepoint(mousePos):
                            WLqua += 1
        if JDO:
            if SoczewkaR1>=50:
                if flat == False:
                    Angle = math.asin(50/(SoczewkaR1))

                    SoczewkiRect=[]
                    SY=0
                    Teststart=True
                    Scenter= 110+grubosc*5-SoczewkaR1
                    SoczewkaX1 =[]
                    SoczewkiKąty[leng]=[]
                    JDDYY=(50*(50/SoczewkaR1**2))*40+5
                    l=Angle*SoczewkaR1*2
                    i=int(l/2)
                    # if i%2==0:
                    #     i+=1
                    Anglez = 2 * Angle / i
                    # print(SoczewkaR1)
                    #Generacja Soczekwi

                    for n in range(i+1):
                        SoczewkiRect.append([0, 0])
                        SoczewkiRect[n][0]=Scenter+math.cos(Angle)*SoczewkaR1+JDDYY
                        SoczewkiRect[n][1] = 105 +math.sin(Angle)*SoczewkaR1
                        if n==0:
                            SoczewkaX1.append(SoczewkiRect[n][0])
                            auiogh0oaidhg=SoczewkiRect[n][1]
                        if Soczewkastrona == -1:
                            SoczewkiRect[n][0] += (SoczewkaX1[0] - SoczewkiRect[n][0]) * 2
                        if n==int(i / 2):
                            SoczewkaX1.append(SoczewkiRect[n][0])
                        SoczewkiKąty[leng].append(math.degrees(Angle))
                        Angle -= Anglez
                    if Soczewkastrona == 1:
                        SoczewkiKąty[leng] = SoczewkiKąty[leng ][::-1]
                else:
                    SoczewkaX1 = []
                    SoczewkiRect = []
                    SoczewkiKąty[leng] = []
                    i = int(100 / 2)
                    for n in range(i + 1):
                        SoczewkiRect.append([0, 0])
                        SoczewkiRect[n][0] = 110+grubosc*5
                        SoczewkiRect[n][1] = 155 - n * 2
                        SoczewkiKąty[leng].append(0)
                    SoczewkaX1.append(110+grubosc*5)
                    SoczewkaX1.append(110+grubosc*5)
                if WeCooling:
                    SocziRekt=Rect(min(SoczewkaX2), 50,max(SoczewkaX1)-min(SoczewkaX2),105)
                JDO=False

        if JDO2:
            if SoczewkaR2>=50:
                if flat2 == False:
                    Angle = math.asin(50/(SoczewkaR2))
                    SoczewkiRect2=[]
                    SY=0
                    SX=0
                    Teststart=True
                    Scenter= 100-grubosc*5+SoczewkaR2
                    SoczewkiKąty[leng+1] = []
                    SoczewkaX2 =[]
                    JDDYY=(50*(50/SoczewkaR2**2))*40+5
                    l = Angle * SoczewkaR2 * 2
                    i = int(l / 2)
                    # if i%2==0:
                    #     i+=1
                    Anglez = 2 * Angle / i

                    # print(SoczewkaR1)
                    #Generacja Soczekwi

                    for n in range(i+1):

                        SoczewkiRect2.append([0, 0])
                        SoczewkiRect2[n][0] = Scenter - math.cos(Angle) * SoczewkaR2 -JDDYY
                        SoczewkiRect2[n][1] = 105 + math.sin(Angle) * SoczewkaR2
                        if n == 0:
                            SoczewkaX2.append(SoczewkiRect2[n][0])
                        if Soczewka2strona == -1:
                            SoczewkiRect2[n][0] += (SoczewkaX2[0] - SoczewkiRect2[n][0]) * 2
                        if n ==int(i / 2)+1 :
                            SoczewkaX2.append(SoczewkiRect2[n][0])
                            print(math.degrees(Angle))
                        SoczewkiKąty[leng+1].append(math.degrees(Angle)+180)
                        Angle -= Anglez
                    if Soczewka2strona == -1:
                        SoczewkiKąty[leng+1]=SoczewkiKąty[leng+1][::-1]
                else:
                    SoczewkaX2 = []
                    SoczewkiRect2 = []
                    SoczewkiKąty[leng+1] = []
                    i=int(100/2)
                    for n in range(i+1):
                        SoczewkiRect2.append([0,0])
                        SoczewkiRect2[n][0] = SoczewkaX1[0]-grubosc*10
                        SoczewkiRect2[n][1] = 155-n*2
                        SoczewkiKąty[leng + 1].append(0)
                    SoczewkaX2.append(SoczewkaX1[0]-grubosc*5)
                    SoczewkaX2.append(SoczewkaX1[0]-grubosc*5)


                JDO2=False
                WeCooling=True
                SocziRekt = Rect(min(SoczewkaX2), 50,   max(SoczewkaX1)-min(SoczewkaX2), 105)
        if gruby:

            gruboschit = []
            SoczewkiKąty[leng + 2] = []
            i =int((SoczewkaX1[0]-SoczewkaX2[0])/3)
            print(i)
            for n in range(i+1):
                gruboschit.append([SoczewkaX2[0]+(n)*3, 50])
                SoczewkiKąty[leng + 2].append(90)
            for n in range(i+1):
                gruboschit.append([SoczewkaX2[0]+(n)*3, 155])
                SoczewkiKąty[leng + 2].append(270)
            gruby=False
        if WeCooling and grubosc>0:
            pygame.draw.rect(screen, (255, 0, 0), Rect(gruboschit[0][0], gruboschit[0][1],   gruboschit[int(len(gruboschit)/2)][0]-gruboschit[0][0], 30))
        a = 0
        Soczewkamask=[]
        for n in ZWierciadlas:
            screen.blit(ZWierciadlas_img[a], n)
            a += 1

        for n in range(len(SoczewkiRect)):
            Soczewkamask.append(SoczewkiRect[n])
        for n in range(len(SoczewkiRect2)):
            Soczewkamask.append(SoczewkiRect2[len(SoczewkiRect2)-1-n])
        if SoczewkiRect!=[]:
            pygame.draw.polygon(screen, cp, Soczewkamask, 5)
        for n in range(len(pryzmatyimg)):
            if PrismCocklor[n]==(0,0,0):
                pygame.draw.polygon(screen, (255,255,255), pryzmatyimg[n], 5)
            else:
                pygame.draw.polygon(screen, PrismCocklor[n], pryzmatyimg[n], 5)

        # for n in pryzmaty:
        #     pygame.draw.rect(screen, (255, 255, 255), n)
        if Clicked1:
            if Typ==1:
                SRCes[leng].center = mousePos
                if Up:
                    KątŚ[leng]+=5
                if Down:
                    KątŚ[leng] -= 5

                if KątŚ[leng] >= 360:
                    KątŚ[leng] = 360 - KątŚ[leng]
                elif KątŚ[leng] < 0:
                    KątŚ[leng] = 360 + KątŚ[leng]
                mn = 2
                if Up:
                    mn = 1
                if Down:
                    mn = -1
                if mn != 2:
                    Old_center = SRCes[leng].center
                    IMG = Światło_src
                    SRCes_img[leng] = pygame.transform.rotate(IMG, KątŚ[leng] - 90)
                    SRCes[leng] = SRCes_img[leng].get_rect()
                    SRCes[leng].center = Old_center

            elif Typ==2:
                ZWierciadlas[leng].center = mousePos
                for ni in range(len(HitboxZWierciadlas[leng])):
                    if 1200>int(HitboxZWierciadlas[leng][ni][0])>0 and 800>int(HitboxZWierciadlas[leng][ni][1])>0:
                        CollHashmap[int(HitboxZWierciadlas[leng][ni][0])][int(HitboxZWierciadlas[leng][ni][1])] = 0
                if Up:
                    Old_center =ZWierciadlas[leng].center
                    ZWkąt[leng] += 5
                    IMG=pygame.transform.scale(Zwierciadło_img, (10, 10 * lenHitboxZWierciadlas[leng]))
                    ZWierciadlas_img[leng] = pygame.transform.rotate(IMG, ZWkąt[leng]-90)
                    ZWierciadlas[leng]=ZWierciadlas_img[leng].get_rect()
                    ZWierciadlas[leng].center = Old_center
                if Down:
                    Old_center = ZWierciadlas[leng].center
                    ZWkąt[leng] -= 5
                    IMG = pygame.transform.scale(Zwierciadło_img, (10, 10 * lenHitboxZWierciadlas[leng]))
                    ZWierciadlas_img[leng] = pygame.transform.rotate(IMG, ZWkąt[leng]-90)
                    ZWierciadlas[leng] = ZWierciadlas_img[leng].get_rect()
                    ZWierciadlas[leng].center = Old_center
                if ZWkąt[leng] >= 360:
                    ZWkąt[leng] = 360 - ZWkąt[leng]

                elif ZWkąt[leng] < 0:
                    ZWkąt[leng] = 360 + ZWkąt[leng]
                print(ZWkąt)
                StY=ZWierciadlas[leng].center[1]
                StX = ZWierciadlas[leng].center[0]
                Koąt=math.radians(ZWkąt[leng])
                for n in range (len(HitboxZWierciadlas[leng])):
                    HitboxZWierciadlas[leng][n][1]=StY+ math.sin(Koąt) * -(lenHitboxZWierciadlas[leng]*5-2*n)
                    HitboxZWierciadlas[leng][n][0] =StX +math.cos(Koąt) * (lenHitboxZWierciadlas[leng]*5-2*n)
                for ni in range(len(HitboxZWierciadlas[leng])):
                    if 1200 > int(HitboxZWierciadlas[leng][ni][0]) > 0 and 800 > int(HitboxZWierciadlas[leng][ni][1]) > 0:
                        CollHashmap[int(HitboxZWierciadlas[leng][ni][0])][int(HitboxZWierciadlas[leng][ni][1])] = (2, ZWkąt[leng])
            elif Typ==3:
                for ni in range(len(lens_hitboxes[leng])):
                    if 1200 > int(lens_hitboxes[leng][ni][0]) > 0 and 800 > int(lens_hitboxes[leng][ni][1]) > 0:
                        CollHashmap[int(lens_hitboxes[leng][ni][0])][int(lens_hitboxes[leng][ni][1])] = 0
                DISt=[]
                for ni in lens_hitboxes[leng]:
                    DISt.append((ni[0] - SocziRekts[leng].center[0], ni[1] - SocziRekts[leng].center[1]))
                DISt2 = []
                for ni in YourJawz_img[leng]:
                    DISt2.append((ni[0] - SocziRekts[leng].center[0], ni[1] - SocziRekts[leng].center[1]))
                SocziRekts[leng].center=mousePos
                for n in range(len(lens_hitboxes[leng])):
                    lens_hitboxes[leng][n][0]= SocziRekts[leng].center[0] + DISt[n][0]
                    lens_hitboxes[leng][n][1] = SocziRekts[leng].center[1] + DISt[n][1]
                for n in range( len(YourJawz_img[leng])):
                    YourJawz_img[leng][n]=(SocziRekts[leng].center[0]+DISt2[n][0],SocziRekts[leng].center[1]+ DISt2[n][1])
                for ni in range(len(lens_hitboxes[leng])):
                    if 1200 > int(lens_hitboxes[leng][ni][0]) > 0 and 800 > int(lens_hitboxes[leng][ni][1]) > 0:
                        CollHashmap[int(lens_hitboxes[leng][ni][0])][int(lens_hitboxes[leng][ni][1])] = (3, SoczewkiKąty[leng][ni])
            elif Typ == 4:
                for n in range(3):
                    for ni in range(len(pryzmatyhitbox[leng][n])):
                        if 1200 > pryzmatyhitbox[leng][n][ni][0] > 0 and 800 > pryzmatyhitbox[leng][n][ni][1] > 0:
                            CollHashmap[pryzmatyhitbox[leng][n][ni][0]][pryzmatyhitbox[leng][n][ni][1]] = 0
                DISt = []
                for i in range(3):
                    DISt.append([])
                    for ni in pryzmatyhitbox[leng][i]:
                        DISt[i].append((ni[0] - pryzmaty[leng].center[0], ni[1] - pryzmaty[leng].center[1]))
                DISt2 = []
                for i in pryzmatyimg[leng]:
                    DISt2.append((i[0] - pryzmaty[leng].center[0], i[1] - pryzmaty[leng].center[1]))
                pryzmaty[leng].center = mousePos
                for i in range(3):
                    DISt.append([])
                    for n in range( len(pryzmatyhitbox[leng][i])):
                        pryzmatyhitbox[leng][i][n]=(pryzmaty[leng].center[0]+DISt[i][n][0],pryzmaty[leng].center[1]+ DISt[i][n][1])
                for n in range(3):
                    pryzmatyimg[leng][n]=(pryzmaty[leng].center[0]+DISt2[n][0],pryzmaty[leng].center[1]+ DISt2[n][1])
                for n in range(3):
                    for ni in range(len(pryzmatyhitbox[leng][n])):
                        if 1200 > pryzmatyhitbox[leng][n][ni][0] > 0 and 800 > pryzmatyhitbox[leng][n][ni][1] > 0:
                            CollHashmap[pryzmatyhitbox[leng][n][ni][0]][pryzmatyhitbox[leng][n][ni][1]] = (4, pryzmatkaty[leng][n])
            elif Typ==5:
                White_lights[leng].center = mousePos
                if Up:
                    White_angles[leng] += 5
                if Down:
                    White_angles[leng] -= 5

                if White_angles[leng] >= 360:
                    White_angles[leng] = 360 - White_angles[leng]
                elif White_angles[leng] < 0:
                    White_angles[leng] = 360 + White_angles[leng]
                mn = 2
                if Up:
                    mn = 1
                if Down:
                    mn = -1
                if mn != 2:
                    Old_center = White_lights[leng].center
                    IMG = WL_img
                    White_lights_img[leng] = pygame.transform.rotate(IMG, White_angles[leng] - 90)
                    White_lights[leng] = White_lights_img[leng].get_rect()
                    White_lights[leng].center = Old_center
        if Change==False or Typ==5:
            screen.blit(trash_img, trash)

            screen.blit(WL_img, WL)
        a = 0
        for n in Part:
            if n.parpop:
                Part.pop(a)
            else:
                n.fading()
                n.move()
                n.draw(screen)
            a += 1
        screen.blit(Światło_src, Swiatłosrc)
        screen.blit(Zwierciadło_img, ZW)
        screen.blit(Soczewka_img, Soczewka)
        screen.blit(pryzmat_img, pryzmat)
        a=0
        # print(ZWkąt,KątŚ)
        for n in SRCes:
            for i in range (Light_quantity[a]):
                cols = 0
                check = [0,-1]
                check2 = [0, -1]
                Iks = n.center[0]+ math.cos(math.radians(KątŚ[a])) * -(Light_quantity[a] / 2*7-i*7)
                Igrek = n.center[1] + math.sin(math.radians(KątŚ[a])) * (Light_quantity[a] / 2*7-i*7)
                kont=KątŚ[a]
                RY=0
                RX=0
                R[0] = Iks,Igrek

                Old=(Iks, Igrek)
                Unbug=0
                while R[0][0]<1200 and R[0][0]>0 and R[0][1]>200  and R[0][1]<800:
                    Unbug+=1
                    RX+= math.sin(math.radians(kont))*3
                    RY+= math.cos(math.radians(kont))*3
                    Collck = ((0, 0), 0)
                    for ck in range(R[1] ** 2):
                        cx = int(R[0][0] - R[1] / 2 + ck % 3)
                        cy = int(R[0][1] - R[1] / 2 + ck // 3)
                        if 1200 > cx > 0 and cy < 800 and CollHashmap[cx][cy] != 0:
                            if CollHashmap[cx][cy][0] != 0:
                                Collck = CollHashmap[cx][cy], (cx, cy)
                                print("J")
                                break
                    if Collck[0][0]==2:
                        RX = Collck[1][0] - Iks
                        RY = Collck[1][1] - Igrek
                        kont = 180 + 2 * Collck[0][1] - kont
                        if kont > 360:
                            kont -= 360
                        New = (R[0])
                        pygame.draw.line(screen, "RED", Old, New, 3)
                        RX += math.sin(math.radians(kont)) * 12
                        RY += math.cos(math.radians(kont)) * 12
                        R[0] = Iks + RX, Igrek + RY
                        Old = New
                    b=0
                    for x in SocziRekts:
                        if x.collidepoint(R[0]):
                            if Collck[0][0] == 3:
                                if check[0] == 1:
                                    IRS = 1 / 1.5
                                    osidgh = 180
                                else:
                                    IRS = 1.5
                                    osidgh = 0
                                RX = Collck[1][0] - Iks
                                RY = Collck[1][1] - Igrek
                                spr = math.sin(
                                    math.radians(360 - kont) + math.radians(Collck[0][1] + osidgh) - math.radians(
                                        90)) / IRS
                                RX += math.sin(math.radians(kont)) * 8
                                RY += math.cos(math.radians(kont)) * 8
                                if spr < 0:
                                    normalize = -1
                                else:
                                    normalize = 1
                                    add = 0
                                if spr * normalize > 1:
                                    add = 90
                                else:
                                    add = 0
                                kont = math.degrees(
                                    math.radians(270) + math.radians(Collck[0][1] + osidgh) - math.asin(
                                        spr % normalize)) - add * normalize
                                if kont > 360:
                                    kont -= 360
                                check = [1, b]
                                New = R[0]
                                R[0] = Iks + RX, Igrek + RY
                                pygame.draw.line(screen, (255, 0, 0, 255), Old, New, 5)
                                cols += 1
                                RX += math.sin(math.radians(kont)) * 10
                                RY += math.cos(math.radians(kont)) * 10
                                R[0] = Iks + RX, Igrek + RY
                                Old = New
                                break
                        else:
                            if check[1]==b and check[0]==1:
                                check=[-1,0]
                        b+=1

                    b = 0
                    for x in pryzmaty:
                        if x.collidepoint(R[0]):
                            if Collck[0][0] == 4:
                                if check2[0] == 1:
                                    IRS = 1/1.55
                                    osidgh = 180
                                else:
                                    IRS = 1.55
                                    osidgh = 0
                                RX = Collck[1][0] - Iks
                                RY = Collck[1][1] - Igrek
                                spr = math.sin(
                                    math.radians(360 - kont) + math.radians(Collck[0][1] + osidgh) - math.radians(
                                        90)) / IRS
                                RX += math.sin(math.radians(kont)) * 8
                                RY += math.cos(math.radians(kont)) * 8
                                if spr < 0:
                                    normalize = -1
                                else:
                                    normalize = 1
                                    add = 0
                                if spr * normalize > 1:
                                    add = 90
                                else:
                                    add = 0
                                kont = math.degrees(
                                    math.radians(270) + math.radians(Collck[0][1] + osidgh) - math.asin(
                                        spr % normalize)) - add * normalize
                                if kont > 360:
                                    kont -= 360
                                check2 = [1, b]
                                New = R[0]
                                R[0] = Iks + RX, Igrek + RY
                                pygame.draw.line(screen, (255, 0, 0, 255), Old, New,5)
                                cols += 1
                                RX += math.sin(math.radians(kont)) * 20
                                RY += math.cos(math.radians(kont)) * 20
                                R[0] = Iks + RX, Igrek + RY
                                Old = New
                        else:
                            if check2[1]==b and check2[0]==1:
                                check2 = [-1, 0]
                        b += 1

                    if Unbug==5000:
                        break
                    R[0] = Iks+RX,Igrek+RY
                New=R[0]
                pygame.draw.line(screen,(255,0,0), Old, New, 5)

            screen.blit(SRCes_img[a], n)
            a+=1

        a=0
        px = pygame.PixelArray(screen)
        for n in White_lights:
            Reflections=[]
            diss=0
            for k in Wkolory[a]:
                cols = 0
                Mcolors=[0,0,0]
                check = [0, -1]
                check2 = [0, -1]
                Iks = n.center[0]
                Igrek = n.center[1]
                kont = White_angles[a]
                RY = 0
                RX = 0
                R[0] = Iks, Igrek
                Old = (Iks, Igrek)
                alfa=1
                print(alfa)

                Unbug = 0
                while R[0][0] < 1200 and R[0][0] > 0 and R[0][1] > 200 and R[0][1] < 800:
                    Unbug += 1
                    RX += math.sin(math.radians(kont)) * 2
                    RY += math.cos(math.radians(kont)) * 2
                    # print("kont")
                    # screen.blit(Ray, R)
                    Collck = ((0, 0), 0)
                    for ck in range(R[1] ** 2):
                        cx = int(R[0][0] - R[1] / 2 + ck % 3)
                        cy = int(R[0][1] - R[1] / 2 + ck // 3)
                        if 1200 > cx > 0 and cy < 800 and CollHashmap[cx][cy] != 0:
                            if CollHashmap[cx][cy][0] !=0:
                                Collck = CollHashmap[cx][cy],(cx, cy)
                                break
                    if Collck[0][0]==2:
                        RX = Collck[1][0] - Iks
                        RY = Collck[1][1] - Igrek
                        kont = 180 + 2 * Collck[0][1] - kont
                        if kont > 360:
                            kont -= 360
                        New = (R[0])
                        if cols == 0:
                            pygame.draw.line(screen, colorssum[a], Old, New, White_width[a])
                        else:
                            autistic_lines(screen, Old, New, White_width[a],k[1],alfa)
                        RX += math.sin(math.radians(kont)) * 12
                        RY += math.cos(math.radians(kont)) * 12
                        R[0] = Iks + RX, Igrek + RY
                        Old = New
                    b = 0
                    for x in SocziRekts:
                        if x.collidepoint(R[0]):
                            if Collck[0][0] == 3:
                                if lens_material[b]==1:
                                    ir=glass_quartz_mm(k[0])
                                elif lens_material[b]==2:
                                    ir=fluoryt_mm(k[0])
                                if check[0] == 1:
                                    IRS = 1/(1+(ir-1)*(lri[b]*2-2))
                                    osidgh = 180
                                    Mcolors[0] += cpl[b][0]
                                    Mcolors[1] += cpl[b][1]
                                    Mcolors[2] += cpl[b][2]
                                    print("ZD")
                                else:
                                    IRS = (1+(ir-1)*(lri[b]*2-2))
                                    alfa *= lens_transparency[b]
                                    osidgh = 0
                                    print("FJF")
                                print(cpl)
                                if alfa*lensReflectiveindex[b]>0.2:
                                    Reflections.append((Collck[1],k,Mcolors,alfa*lensReflectiveindex[b], 180+ 2 * (Collck[0][1]-90) - kont,0))
                                RX = Collck[1][0] - Iks
                                RY = Collck[1][1] - Igrek
                                spr = math.sin(
                                    math.radians(360 - kont) + math.radians(Collck[0][1] + osidgh) - math.radians(
                                        90)) / IRS
                                RX += math.sin(math.radians(kont)) * 8
                                RY += math.cos(math.radians(kont)) * 8
                                if spr < 0:
                                    normalize = -1
                                else:
                                    normalize = 1
                                    add = 0
                                if spr * normalize > 1:
                                    add = 90
                                else:
                                    add = 0
                                kont = math.degrees(
                                    math.radians(270) + math.radians(Collck[0][1] + osidgh) - math.asin(
                                        spr % normalize)) - add * normalize
                                if kont > 360:
                                    kont -= 360
                                check = [1, b]
                                New = R[0]
                                R[0] = Iks + RX, Igrek + RY
                                if cols == 0:
                                    pygame.draw.line(screen, colorssum[a], Old, New, White_width[a])
                                else:
                                    autistic_lines(screen, Old, New, White_width[a], k[1], alfa)
                                cols += 1
                                RX += math.sin(math.radians(kont)) * 10
                                RY += math.cos(math.radians(kont)) * 10
                                R[0] = Iks + RX, Igrek + RY
                                Old = New
                                break
                        else:
                            if check[1] == b and check[0] == 1:
                                check = [-1, 0]
                        b += 1
                    b = 0
                    b = 0
                    for x in pryzmaty:
                        if x.collidepoint(R[0]):
                            if Collck[0][0]==4:
                                if prism_material[b]==1:
                                    ir=glass_quartz_mm(k[0])
                                elif prism_material[b]==2:
                                    ir=fluoryt_mm(k[0])
                                if check2[0] == 1:
                                    IRS = 1 / (1+(ir-1)*(pri[b]*2-2))
                                    osidgh = 180
                                    Mcolors[0] += PrismCocklor[b][0]
                                    Mcolors[1] += PrismCocklor[b][1]
                                    Mcolors[2] += PrismCocklor[b][2]
                                    alfa *= Prism_transparency[b] #* (1 - PrismReflectiveindex[b])
                                else:
                                    IRS = (1+(ir-1)*(pri[b]*2-2))
                                    osidgh = 0
                                if alfa*PrismReflectiveindex[b]>0.2:
                                    Reflections.append((Collck[1],k,Mcolors,alfa*PrismReflectiveindex[b], 180+ 2 * (Collck[0][1]-90) - kont,0))
                                RX=Collck[1][0]-Iks
                                RY=Collck[1][1]-Igrek
                                spr = math.sin(math.radians(360 - kont) + math.radians(Collck[0][1] + osidgh) - math.radians(90)) / IRS
                                RX += math.sin(math.radians(kont)) * 8
                                RY += math.cos(math.radians(kont)) * 8
                                if spr < 0:
                                    normalize = -1
                                else:
                                    normalize = 1
                                    add = 0
                                if spr * normalize > 1:
                                    add = 90
                                else:
                                    add = 0
                                kont = math.degrees(
                                    math.radians(270) + math.radians(Collck[0][1]+ osidgh) - math.asin(
                                        spr % normalize)) - add * normalize
                                if kont > 360:
                                    kont -= 360
                                check2 = [1, b]
                                New = R[0]
                                R[0] = Iks + RX, Igrek + RY
                                if cols == 0:
                                    pygame.draw.line(screen,colorssum[a], Old, New, White_width[a])
                                else:
                                    autistic_lines(screen, Old, New, White_width[a],k[1],alfa,Mcolors)
                                RX += math.sin(math.radians(kont)) * 5
                                RY += math.cos(math.radians(kont)) * 5
                                R[0] = Iks + RX, Igrek + RY
                                Old = New
                                cols += 1
                                break
                        else:
                            if check2[1] == b and check2[0] == 1:
                                check2 = [-1, 0]
                        b += 1

                    if Unbug == 5000:
                        break
                    R[0] = Iks + RX, Igrek + RY
                New = R[0]

                if cols==0:
                    autistic_lines(screen, Old, New, White_width[a], colorssum[a],1)
                    #pygame.draw.line(screen,(255,255,255,255), Old, New, 100)
                    break
                elif cols>0:
                    autistic_lines(screen, Old, New, White_width[a],k[1],alfa,Mcolors)
                diss+=1
            while Reflections!=[]:
                Mcolors = Reflections[-1][2]
                check = [0, -1]
                check2 = [0, -1]
                k=Reflections[-1][1]

                Iks =  Reflections[-1][0][0]
                Igrek =   Reflections[-1][0][1]
                kont = Reflections[-1][4]
                Old = (Iks, Igrek)
                alfa =  Reflections[-1][3]
                RX=0
                RY=0
                Unbug=0

                RX += math.sin(math.radians(kont)) * 10
                RY += math.cos(math.radians(kont)) * 10
                R[0] = Iks+RX, Igrek+RY
                while R[0][0] < 1200 and R[0][0] > 0 and R[0][1] > 200 and R[0][1] < 800:
                    Unbug += 1
                    RX += math.sin(math.radians(kont)) * 2
                    RY += math.cos(math.radians(kont)) * 2
                    # print("kont")
                    # screen.blit(Ray, R)
                    Collck = ((0, 0), 0)
                    for ck in range(R[1] ** 2):
                        cx = int(R[0][0] - R[1] / 2 + ck % 3)
                        cy = int(R[0][1] - R[1] / 2 + ck // 3)
                        if 1200 > cx > 0 and cy < 800 and CollHashmap[cx][cy] != 0:
                            if CollHashmap[cx][cy][0] !=0:
                                Collck = CollHashmap[cx][cy],(cx, cy)
                                break
                    if Collck[0][0]==2:
                        RX = Collck[1][0] - Iks
                        RY = Collck[1][1] - Igrek
                        kont = 180 + 2 * Collck[0][1] - kont
                        if kont > 360:
                            kont -= 360
                        New = (R[0])
                        if cols == 0:
                            pygame.draw.line(screen, colorssum[a], Old, New, White_width[a])
                        else:
                            autistic_lines(screen, Old, New, White_width[a],k[1],alfa)
                        RX += math.sin(math.radians(kont)) * 12
                        RY += math.cos(math.radians(kont)) * 12
                        R[0] = Iks + RX, Igrek + RY
                        Old = New
                    b = 0
                    for x in SocziRekts:
                        if x.collidepoint(R[0]):
                            if Collck[0][0] == 3:
                                if check[0] == 1:
                                    IRS = 1 / k[0]
                                    osidgh = 180
                                    print("ZD")
                                else:
                                    IRS = k[0]
                                    osidgh = 0
                                    print("FJF")
                                RX = Collck[1][0] - Iks
                                RY = Collck[1][1] - Igrek
                                spr = math.sin(
                                    math.radians(360 - kont) + math.radians(Collck[0][1] + osidgh) - math.radians(
                                        90)) / IRS
                                RX += math.sin(math.radians(kont)) * 8
                                RY += math.cos(math.radians(kont)) * 8
                                if spr < 0:
                                    normalize = -1
                                else:
                                    normalize = 1
                                    add = 0
                                if spr * normalize > 1:
                                    add = 90
                                else:
                                    add = 0
                                kont = math.degrees(
                                    math.radians(270) + math.radians(Collck[0][1] + osidgh) - math.asin(
                                        spr % normalize)) - add * normalize
                                if kont > 360:
                                    kont -= 360
                                check = [1, b]
                                New = R[0]
                                R[0] = Iks + RX, Igrek + RY
                                if cols == 0:
                                    pygame.draw.line(screen, colorssum[a], Old, New, White_width[a])
                                else:
                                    autistic_lines(screen, Old, New, White_width[a], k[1], alfa)
                                cols += 1
                                RX += math.sin(math.radians(kont)) * 10
                                RY += math.cos(math.radians(kont)) * 10
                                R[0] = Iks + RX, Igrek + RY
                                Old = New
                                break
                        else:
                            if check[1] == b and check[0] == 1:
                                check = [-1, 0]
                        b += 1
                    b = 0
                    for x in pryzmaty:
                        if x.collidepoint(R[0]):
                            if Collck[0][0]==4:
                                if prism_material[b]==1:
                                    ir=glass_quartz_mm(k[0])
                                elif prism_material[b]==2:
                                    ir=fluoryt_mm(k[0])
                                if check2[0] == 1:
                                    IRS = 1 / (1+(ir-1)*(pri[b]*2-2))
                                    osidgh = 180
                                    Mcolors[0] += PrismCocklor[b][0]
                                    Mcolors[1] += PrismCocklor[b][1]
                                    Mcolors[2] += PrismCocklor[b][2]
                                    alfa *= Prism_transparency[b]

                                else:
                                    IRS = (1+(ir-1)*(pri[b]*2-2))
                                    osidgh = 0


                                RX=Collck[1][0]-Iks
                                RY=Collck[1][1]-Igrek

                                spr = math.sin(math.radians(360 - kont) + math.radians(Collck[0][1] + osidgh) - math.radians(90)) / IRS
                                RX += math.sin(math.radians(kont)) * 8
                                RY += math.cos(math.radians(kont)) * 8
                                if spr < 0:
                                    normalize = -1
                                else:
                                    normalize = 1
                                    add = 0
                                if spr * normalize > 1:
                                    add = 90
                                else:
                                    add = 0
                                kont = math.degrees(math.radians(270) + math.radians(Collck[0][1]+ osidgh) - math.asin(spr % normalize)) - add * normalize
                                if kont > 360:
                                    kont -= 360
                                check2 = [1, b]
                                New = R[0]
                                R[0] = Iks + RX, Igrek + RY
                                autistic_lines(screen, Old, New, White_width[a],k[1],alfa,Mcolors)
                                RX += math.sin(math.radians(kont)) * 5
                                RY += math.cos(math.radians(kont)) * 5
                                R[0] = Iks + RX, Igrek + RY
                                Old = New
                                break
                        else:
                            if check2[1] == b and check2[0] == 1:
                                check2 = [-1, 0]
                        b += 1

                    if Unbug == 5000:
                        break
                    R[0] = Iks + RX, Igrek + RY
                New = R[0]
                autistic_lines(screen, Old, New, White_width[a],k[1],alfa,Mcolors)
                print(k)
                Reflections.pop(-1)
                print(Reflections)
        px.close()
        a=0
        for n in White_lights:
            screen.blit(White_lights_img[a], n)
            a+=1
    pygame.display.update()
pygame.quit()