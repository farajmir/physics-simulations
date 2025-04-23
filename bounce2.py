import pygame
import numpy

pygame.init()


screen = pygame.display.set_mode((1280, 1000))
y1, y2, y3 = 15, 15, 15
radius = 100
ay = 9.8
dt = 1 / 60
vy1 = 0
vy2 = 0
vy3 = 0
mass1 = 0.1  # very light
mass2 = 0.3  # light
mass3 = 0.5  # heavy
running = True


while running:


    # physics
    vy1 += ay * dt
    vy2 += ay * dt
    vy3 += ay * dt

    y1 += vy1 * dt
    y2 += vy2 * dt
    y3 += vy3 * dt

    screen.fill((33, 33, 33))

    pygame.draw.circle(screen, (255, 0, 0), (300, int(y1)), radius)
    pygame.draw.circle(screen, (0, 255, 0), (600, int(y2)), radius)
    pygame.draw.circle(screen, (0, 0, 255), (900, int(y3)), radius)

    # collisions and bouncing
    if y1 >= 900:
        y1 = 900
        vy1 *= -1 + mass1

    if y2 >= 900:
        y2 = 900
        vy2 *= -1 + mass2

    if y3 >= 900:
        y3 = 900
        vy3 *= -1 + mass3

    # game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()