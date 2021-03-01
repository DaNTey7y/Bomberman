import pygame


class Bomb:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.timer = 0
        self.blown = False
        self.image = pygame.image.load('images/bomb.png')
        self.image = pygame.transform.scale(self.image, (50, 50))

    def is_blown(self):
        return self.blown

    def get_row_col(self):
        return self.row, self.col

    def update(self):
        if self.timer >= 180:
            self.blown = True
        self.timer += 1

    def draw(self, surface):
        surface.blit(self.image, (50 * self.row, 50 * self.col))
