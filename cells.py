import pygame
import numpy



pygame.init()


width, height = 800, 800
rows, cols = 100, 100
cell_size = width // cols
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
grid = numpy.random.choice([0, 1], size=(rows, cols), p=[0.8, 0.2])
age_grid = numpy.zeros((rows, cols), dtype=int)
paused = False


def count_neighbors(grid, x, y):
    total = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if not (i == 0 and j == 0):
                total += grid[(x + i) % rows, (y + j) % cols]
    return total


def update(grid, age_grid):
    new_grid = numpy.copy(grid)
    new_age_grid = numpy.copy(age_grid)

    for i in range(rows):

        for j in range(cols):

            total = count_neighbors(grid, i, j)

            if grid[i, j] == 1:

                if total < 2 or total > 3:
                    new_grid[i, j] = 0
                    new_age_grid[i, j] = 0

                else:
                    new_age_grid[i, j] += 1  

            else:

                if total == 3:
                    new_grid[i, j] = 1
                    new_age_grid[i, j] = 1 

    return new_grid, new_age_grid


def toggle_cell(x, y):

    i = y // cell_size
    j = x // cell_size
    grid[i, j] = 1 - grid[i, j]
    age_grid[i, j] = 0 if grid[i, j] == 0 else 1  

def place_glider(x, y):

    i = y // cell_size
    j = x // cell_size
    glider = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

    for dx, dy in glider:
        grid[(i + dy) % rows, (j + dx) % cols] = 1
        age_grid[(i + dy) % rows, (j + dx) % cols] = 1  

def get_cell_color(age):
    fade = min(age * 5, 255)
    return (255 - fade, 255 - fade, 255 - fade)

running = True

while running:
    clock.tick(10)
    screen.fill((0, 0, 0))

    for i in range(rows):

        for j in range(cols):

            if grid[i, j] == 1:

                color = get_cell_color(age_grid[i, j])
                pygame.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))

    if not paused:

        grid, age_grid = update(grid, age_grid)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                paused = not paused

            elif event.key == pygame.K_g:
                x, y = pygame.mouse.get_pos()
                place_glider(x, y)

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:
                toggle_cell(*event.pos)


    pygame.display.flip()

pygame.quit()
