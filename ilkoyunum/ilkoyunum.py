from turtle import pen
import pygame as py
import random

py.init()

Genislik , Yukseklik = 600 , 600
pencere = py.display.set_mode((Genislik,Yukseklik))

py.mixer.music.load("entrymusic.wav")
py.mixer.music.play(-1,0.0)
buyume_sesi = py.mixer.Sound("jump.wav")
yeme_sesi = py.mixer.Sound("yemyeme.wav")

HIZ = 5
saat = py.time.Clock()
FPS = 60

canavar = py.image.load("canavarim1.png")
canavar_koordinat = canavar.get_rect()
canavar_koordinat.topleft=(Genislik/2,Yukseklik/2)

yem = py.image.load("apple.png")
yem_koordinat = yem.get_rect()
yem_koordinat.topleft = (150,150)

arka_plan = py.image.load("background2.jpg")

FONT = py.font.SysFont("consolas",64)

Y = 0

SKOR = 0



durum = True
while durum :
    for i in py.event.get():
        if i.type == py.QUIT:
            durum = False

    
    pencere.blit(arka_plan,(0,0))
    pencere.blit(yem,yem_koordinat)
    pencere.blit(canavar,canavar_koordinat)
    YAZI = FONT.render("Skor : " + str(SKOR),True,(255,0,0),(0,0,255))
    YAZI_Koordinat = YAZI.get_rect()
    YAZI_Koordinat.topleft = (20,20)
    py.draw.line(pencere,(255,0,255),(0,90),(600,90),3)
    pencere.blit(YAZI,YAZI_Koordinat)

    tus = py.key.get_pressed()

    if tus[py.K_LEFT] and canavar_koordinat.left>0:
        canavar_koordinat.x-=HIZ
    elif tus[py.K_RIGHT] and canavar_koordinat.right<Genislik:
        canavar_koordinat.x+=HIZ
    elif tus[py.K_UP] and canavar_koordinat.top>91:
        canavar_koordinat.y-=HIZ
    elif tus[py.K_DOWN] and canavar_koordinat.bottom<Yukseklik:
        canavar_koordinat.y+=HIZ

    if canavar_koordinat.colliderect(yem_koordinat):
        yeme_sesi.play()
        yem_koordinat.x = random.randint(0,Genislik - 32)
        yem_koordinat.y = random.randint(91 , Yukseklik - 32)
        SKOR += 5

    if SKOR > 50:
        canavar = py.image.load("canavarim3.png")
        
        if Y == 0:
            buyume_sesi.play()
            canavar_koordinat = canavar.get_rect()
            canavar_koordinat.topleft=(195,195)
            Y+=1

        if tus[py.K_LEFT] and canavar_koordinat.left>0:
            canavar_koordinat.x-=HIZ
        elif tus[py.K_RIGHT] and canavar_koordinat.right<Genislik:
            canavar_koordinat.x+=HIZ
        elif tus[py.K_UP] and canavar_koordinat.top>91:
            canavar_koordinat.y-=HIZ
        elif tus[py.K_DOWN] and canavar_koordinat.bottom<Yukseklik:
            canavar_koordinat.y+=HIZ

        if canavar_koordinat.colliderect(yem_koordinat):
            yeme_sesi.play()
            yem_koordinat.x = random.randint(0,Genislik - 32)
            yem_koordinat.y = random.randint(91 , Yukseklik - 32)
            SKOR += 5
        
    if SKOR == 100:
        YAZI = FONT.render(" OYUNU KAZANDINIZ ",True,(255,0,0),(0,0,255))
        YAZI_Koordinat = YAZI.get_rect()
        YAZI_Koordinat.topleft = (10,20)
        pencere.blit(YAZI,YAZI_Koordinat)
    py.display.update()
    saat.tick(FPS)
py.quit()