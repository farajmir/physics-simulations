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
mass = 0.2 # mass should be =< 1, negative numbers work

running = True
while running:

    # physics
    vy += ay * dt
    vx += ax * dt
    y += vy * dt
    x += vx * dt
    
    # collisions
    ramp_y = 230 + x * slope
    if y >= ramp_y:
        y = ramp_y
        y = 230 + x * slope
        vx *= 0.996

    
    if y + radius < ramp_y:
            y = ramp_y - radius

    if x >= 620:
        x = 620
        vx *= -1 + mass

    # draw
    screen.fill((33, 33, 33))
    pygame.draw.polygon(screen, triangle_color, triangle_points)
    pygame.draw.circle(screen, (50, 145, 255), (int(x), int(y)), radius)

   
    # game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()