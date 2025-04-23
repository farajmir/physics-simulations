import pygame
import numpy 


pygame.init()
width, height = 800, 800
rows, cols = 100, 100
cell_size = width // cols

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

grid = numpy.random.choice([0, 1], size=(rows, cols), p=[0.8, 0.2])

def update(grid):

    new_grid = numpy.copy(grid)

    for i in range(rows):

        for j in range(cols):

            total = int(numpy.sum(grid[i-1:i+2, j-1:j+2]) - grid[i, j])

            if grid[i, j] == 1:
                if total < 2 or total > 3:
                    new_grid[i, j] = 0
            else:
                if total == 3:
                    new_grid[i, j] = 1
    return new_grid

running = True
while running:
    clock.tick(10)
    screen.fill((0, 0, 0))
    
    for i in range(rows):
        for j in range(cols):
            color = (255, 255, 255) if grid[i, j] == 1 else (0, 0, 0)
            pygame.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))


    grid = update(grid)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()