import pygame
import numpy

# incomplete / missing attraction and repulsion

pygame.init()

screen = pygame.display.set_mode((1280, 1000))
y = 200
x = 600
magnet1 = pygame.Rect(x + 300, y + 100, 75, 155)
magnet2 = pygame.Rect(x, y, 75, 155)
ay = 9.8
dt = 1 / 60
vy = 0
k = 9*10**9
dragging = False
offset_x = 0
offset_y = 0
dragged_magnet = None
m1 = 0.01
m2 = 0.01

running = True
while running:

    # calculate forces
    dx1 = magnet1.centerx - magnet2.centerx
    dy1 = magnet1.y - (magnet2.y + magnet2.height)
    r1 = numpy.hypot(dx1, dy1)
    mforce1 = (k * m1 * m2) / r1**2

    dx2 = magnet1.centerx - magnet2.centerx
    dy2 = (magnet1.y + magnet1.height) - magnet2.y
    r2 = numpy.hypot(dx2, dy2)
    mforce2 = (k * m1 * m2) / r2**2


    screen.fill((70, 70, 70))

    # draw
    pygame.draw.rect(screen, (255, 0, 0), (magnet1.x, magnet1.y, magnet1.width, magnet1.height // 2))
    pygame.draw.rect(screen, (0, 0, 255), (magnet1.x, magnet1.y + magnet1.height // 2, magnet1.width, magnet1.height // 2))
    
    pygame.draw.rect(screen, (255, 0, 0), (magnet2.x, magnet2.y, magnet2.width, magnet2.height // 2))
    pygame.draw.rect(screen, (0, 0, 255), (magnet2.x, magnet2.y + magnet2.height // 2, magnet2.width, magnet2.height // 2))

    # mouse / drag
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if magnet1.collidepoint(event.pos):  
                dragging = True
                dragged_magnet = magnet1
                mouse_x, mouse_y = event.pos
                offset_x = magnet1.x - mouse_x
                offset_y = magnet1.y - mouse_y
            elif magnet2.collidepoint(event.pos):
                dragging = True
                dragged_magnet = magnet2
                mouse_x, mouse_y = event.pos
                offset_x = magnet2.x - mouse_x
                offset_y = magnet2.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
            dragged_magnet = None

        elif event.type == pygame.MOUSEMOTION and dragging:
            mouse_x, mouse_y = event.pos
            if dragged_magnet:
                dragged_magnet.x = mouse_x + offset_x
                dragged_magnet.y = mouse_y + offset_y

    pygame.display.update()

pygame.quit()