import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400,400))
screen.fill('white')

circle(screen, (0, 0, 0), (200, 200), 102)
circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (255, 0, 0), (150, 150), 20)
circle(screen, (255, 0, 0), (250, 150), 20)
circle(screen, (0, 0, 0), (150, 150), 10)
circle(screen, (0, 0, 0), (250, 150), 10)
rect(screen, (0, 0, 0), (150, 250, 100, 20))
polygon(screen, (0, 0, 0), [(210,140), (215, 145), (285, 105), (280, 100)])
polygon(screen, (0, 0, 0), [(110,105), (115, 100), (185, 140), (180, 145)])





pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
	for event in pygame.event.get():
		clock.tick(FPS)
		if event.type == pygame.QUIT:
			finished = True
			
			
pygame.quit()