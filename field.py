import pygame
from random import randint


class Field:
    def __init__(self):
        self.cell_size = 50
        self.field = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    def generate_map(self):
        for row in range(len(self.field)):
            for col in range(len(self.field[row])):
                if str(self.field[row][col]) not in ('1', '3'):
                    if randint(0, 100) >= 79:
                        self.field[row][col] = 2

    def get_position(self, pos):
        x, y = 0, 0
        for i in range(1, 12):
            if pos[0] < i * self.cell_size:
                break
            else:
                x += 1
        for i in range(1, 12):
            if pos[1] < i * self.cell_size:
                break
            else:
                y += 1
        return x, y

    def clear(self):
        self.field = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    def update(self):
        pass

    def draw(self, surface):
        tile = pygame.image.load('images/tile.png')
        tile = pygame.transform.scale(tile, (50, 50))
        brick = pygame.image.load('images/brick.png')
        brick = pygame.transform.scale(brick, (50, 50))
        y = 0
        for row in self.field:
            x = 0
            for col in row:
                if col == 1:
                    surface.blit(tile, (x, y))
                elif col == 2:
                    surface.blit(brick, (x, y))
                x += self.cell_size
            y += self.cell_size
