from cgitb import grey
import pygame
import sys

pygame.init()

size = width, height = 640, 480
speed = [1,1]
green = (0,255,0)

screen = pygame.display.set_mode(size)

head = pygame.image.load("canavarim1.png")
head_rect = head.get_rect()

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    head_rect = head_rect.move(speed)
    if head_rect.left < 0 or head_rect.right > width:
        speed[0] = -speed[0]
    if head_rect.top < 0 or head_rect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(green)
    screen.blit(head, head_rect)
    pygame.display.flip()

pygame.quit()