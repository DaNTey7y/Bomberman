import pygame
from random import choice


class Enemy:
    def __init__(self, field, pos_x, pos_y):
        self.pos_x, self.pos_y = pos_x, pos_y
        self.field = field
        self.field_pos = self.field.get_position((self.pos_x + 24, self.pos_y + 24))
        self.alive = True
        self.direction = choice(range(4))
        self.speed = 2
        self.left_flip_anim = [pygame.transform.scale(pygame.image.load('images/el0.png'), (50, 50)),
                               pygame.transform.scale(pygame.image.load('images/el1.png'), (50, 50)),
                               pygame.transform.scale(pygame.image.load('images/el2.png'), (50, 50)),
                               pygame.transform.scale(pygame.image.load('images/el1.png'), (50, 50))]
        self.current_anim = self.left_flip_anim
        self.anim_counter = 0

        self.frame = None
        self.rect = None

        self.alive = True

    def get_pos(self):
        return self.pos_x, self.pos_y

    def sync_with_field(self):
        cur_pos = self.field.get_position((self.pos_x + 24, self.pos_y + 24))
        if self.field_pos != cur_pos:
            if self.field.field[cur_pos[1]][cur_pos[0]] == 0:
                self.field.field[self.field_pos[1]][self.field_pos[0]] = 0
                self.field.field[cur_pos[1]][cur_pos[0]] = 4
                self.field_pos = cur_pos

    def move(self):
        if self.direction == 0:
            angle_0 = self.field.get_position((self.pos_x - 1, self.pos_y))
            angle_1 = self.field.get_position((self.pos_x - 1, self.pos_y + 49))
            if str(self.field.field[angle_0[1]][angle_0[0]]) not in ('1', '2') and \
                    str(self.field.field[angle_1[1]][angle_1[0]]) not in ('1', '2'):
                self.pos_x -= self.speed
                self.anim_counter += 1
            else:
                self.direction = choice((1, 2, 3))
        elif self.direction == 1:
            angle_0 = self.field.get_position((self.pos_x, self.pos_y - 1))
            angle_1 = self.field.get_position((self.pos_x + 49, self.pos_y - 1))
            if str(self.field.field[angle_0[1]][angle_0[0]]) not in ('1', '2') and \
                    str(self.field.field[angle_1[1]][angle_1[0]]) not in ('1', '2'):
                self.pos_y -= self.speed
                self.anim_counter += 1
            else:
                self.direction = choice((0, 2, 3))
        elif self.direction == 2:
            angle_0 = self.field.get_position((self.pos_x + 50, self.pos_y))
            angle_1 = self.field.get_position((self.pos_x + 50, self.pos_y + 49))
            if str(self.field.field[angle_0[1]][angle_0[0]]) not in ('1', '2') and \
                    str(self.field.field[angle_1[1]][angle_1[0]]) not in ('1', '2'):
                self.pos_x += self.speed
                self.anim_counter += 1
            else:
                self.direction = choice((0, 1, 3))
        elif self.direction == 3:
            angle_0 = self.field.get_position((self.pos_x, self.pos_y + 50))
            angle_1 = self.field.get_position((self.pos_x + 49, self.pos_y + 50))
            if str(self.field.field[angle_0[1]][angle_0[0]]) not in ('1', '2') and \
                    str(self.field.field[angle_1[1]][angle_1[0]]) not in ('1', '2'):
                self.pos_y += self.speed
                self.anim_counter += 1
            else:
                self.direction = choice((0, 1, 2))
        self.sync_with_field()

    def die(self):
        self.field.field[self.field_pos[0]][self.field_pos[1]] = 0
        self.alive = False
        return False

    def update(self):
        if self.anim_counter >= 64:
            self.anim_counter = 0

        self.frame = self.current_anim[self.anim_counter // 16]
        self.rect = self.frame.get_rect()

        self.move()

    def draw(self, surface):
        surface.blit(self.frame, self.get_pos())
