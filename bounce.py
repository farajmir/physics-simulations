import pygame
import numpy

pygame.init()

screen = pygame.display.set_mode((1280, 1000))
y = 15
radius = 100
ay = 9.8
dt = 0
vy = 0
mass = 0.3 # mass should be =< 1, negative numbers work

running = True
while running:

    # physics
    dt = 1/60
    vy += ay * dt
    y += vy * dt

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (255, 0, 0), (600, int(y)), radius)

    # collisions and bouncing
    if y >= 900:
        y = 900
        vy *= -1 + mass

    # game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()