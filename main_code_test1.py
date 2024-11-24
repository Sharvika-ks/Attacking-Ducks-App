import pygame
import random

pygame.init()

window = pygame.display.set_mode((800,600))
background = pygame.image.load('forest_background_image.jpeg')
background = pygame.transform.smoothscale(background, window.get_size())

#screen = pygame.display.set_mode((800, 600))

window.blit(background, (0, 0))

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

pygame.quit()