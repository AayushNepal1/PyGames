import pygame, sys

pygame.init()

size = width, height = 320, 240

screen = pygame.display.set_mode(size)
title = pygame.display.set_caption("Key Events")
bg_color = (255, 255,255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            keys = event.key
            print(ord(keys))
        elif event.type == pygame.KEYUP:
            keys = event.key
            print(ord(keys))
    
    screen.fill(bg_color)
    pygame.display.flip()
    