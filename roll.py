import pygame
import numpy

pygame.init()

screen = pygame.display.set_mode((640, 640))
y = 240
x = 20
radius = 20
triangle_points = [(0, 250), (0, 640), (640, 640)]
triangle_color = (155, 155, 175)
a_grav = 9.8
theta = 0.547
ay = a_grav * numpy.cos(theta)
ax = a_grav * numpy.sin(theta)
slope = numpy.tan(theta)
dt = 1/60
vy = 0
vx = 0

running = True
while running:

    # physics
    vy += ay * dt
    vx += ax * dt
    y += vy * dt
    x += vx * dt

    screen.fill((0, 0, 0))

    pygame.draw.polygon(screen, triangle_color, triangle_points)
    pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), radius)
    
    # collisions
    ramp_y = 230 + x * slope
    if y >= ramp_y:
        y = ramp_y
        y = 230 + x * slope
        vx *= 0.996
    
    if y < ramp_y:
            y = ramp_y


    # game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()