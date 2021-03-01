import pygame


class Explosion:
    def __init__(self, field, enemys, pos):
        self.field = field
        self.enemys = enemys
        self.timer = 0
        self.ended = False
        self.row, self.col = pos

    def is_ended(self):
        return self.ended

    def update(self):
        for enemy in self.enemys:
            if abs(enemy.get_field_pos()[0] - self.row) <= 1 and abs(enemy.get_field_pos()[1] - self.col) <= 1:
                enemy.die()
        if self.timer >= 120:
            self.ended = True
        self.timer += 1

    def draw(self, surface):
        pygame.draw.rect(surface, (252, 107, 3), ((self.col - 1) * 50, self.row * 50,
                                                  (self.col + 1) * 50, (self.row + 1) * 50))
