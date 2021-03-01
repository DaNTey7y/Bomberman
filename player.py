import pygame


class Player:
    def __init__(self):
        # Задаю параметры игрока
        self.pos_x = 50
        self.pos_y = 50
        self.field_pos = (1, 1)
        self.color = (255, 0, 0)
        self.radius = 20
        self.speed = 2.5

        self.walk_up = [pygame.transform.scale(pygame.image.load('images/pu0.png'), (50, 50)),
                        pygame.transform.scale(pygame.image.load('images/pu1.png'), (50, 50)),
                        pygame.transform.scale(pygame.image.load('images/pu0.png'), (50, 50)),
                        pygame.transform.scale(pygame.image.load('images/pu2.png'), (50, 50))]
        self.walk_down = [pygame.transform.scale(pygame.image.load('images/pd0.png'), (50, 50)),
                          pygame.transform.scale(pygame.image.load('images/pd1.png'), (50, 50)),
                          pygame.transform.scale(pygame.image.load('images/pd0.png'), (50, 50)),
                          pygame.transform.scale(pygame.image.load('images/pd2.png'), (50, 50))]
        self.walk_left = [pygame.transform.scale(pygame.image.load('images/pl0.png'), (50, 50)),
                          pygame.transform.scale(pygame.image.load('images/pl1.png'), (50, 50)),
                          pygame.transform.scale(pygame.image.load('images/pl0.png'), (50, 50)),
                          pygame.transform.scale(pygame.image.load('images/pl2.png'), (50, 50))]
        self.walk_right = [pygame.transform.scale(pygame.image.load('images/pr0.png'), (50, 50)),
                           pygame.transform.scale(pygame.image.load('images/pr1.png'), (50, 50)),
                           pygame.transform.scale(pygame.image.load('images/pr0.png'), (50, 50)),
                           pygame.transform.scale(pygame.image.load('images/pr2.png'), (50, 50))]
        self.current_animation = self.walk_left
        self.anim_counter = 0

        self.frame = None
        self.rect = None

        self.alive = True

    # возвращает координаты игрока
    def get_pos(self):
        return self.pos_x, self.pos_y

    """
    следующие четыре функции изменяют и возвращают 
    измененную позицию игрока
    """
    def move_right(self, field):
        self.current_animation = self.walk_right
        self.anim_counter += 1
        next_cell_0 = field.get_position((self.pos_x + 50, self.pos_y))
        next_cell_1 = field.get_position((self.pos_x + 50, self.pos_y + 49))
        if str(field.field[next_cell_0[1]][next_cell_0[0]]) not in ('1', '2') \
                and str(field.field[next_cell_1[1]][next_cell_1[0]]) not in ('1', '2'):
            self.pos_x += self.speed
        else:
            if str(field.field[next_cell_0[1]][next_cell_0[0]]) not in ('1', '2') and \
                    str(field.field[next_cell_1[1]][next_cell_1[0]]) in ('1', '2'):
                if self.pos_y < ((50 * next_cell_1[1] + 1) - 28):
                    self.pos_y -= self.speed
                    self.pos_x += self.speed
            elif str(field.field[next_cell_1[1]][next_cell_1[0]]) not in ('1', '2') and \
                    str(field.field[next_cell_0[1]][next_cell_0[0]]) in ('1', '2'):
                if self.pos_y + 49 > ((50 * next_cell_1[1] - 1) + 24):
                    self.pos_y += self.speed
                    self.pos_x += self.speed
        self.sync_with_field(field)

    def move_left(self, field):
        self.current_animation = self.walk_left
        self.anim_counter += 1
        next_cell_0 = field.get_position((self.pos_x - 1, self.pos_y))
        next_cell_1 = field.get_position((self.pos_x - 1, self.pos_y + 49))
        if str(field.field[next_cell_0[1]][next_cell_0[0]]) not in ('1', '2') \
                and str(field.field[next_cell_1[1]][next_cell_1[0]]) not in ('1', '2'):
            self.pos_x -= self.speed
        else:
            if str(field.field[next_cell_0[1]][next_cell_0[0]]) not in ('1', '2') and \
                    str(field.field[next_cell_1[1]][next_cell_1[0]]) in ('1', '2'):
                if self.pos_y < ((50 * next_cell_1[1] + 1) - 28):
                    self.pos_y -= self.speed
                    self.pos_x -= self.speed
            elif str(field.field[next_cell_1[1]][next_cell_1[0]]) not in ('1', '2') and \
                    str(field.field[next_cell_0[1]][next_cell_0[0]]) in ('1', '2'):
                if self.pos_y + 49 > ((50 * next_cell_1[1] - 1) + 24):
                    self.pos_y += self.speed
                    self.pos_x -= self.speed
        self.sync_with_field(field)

    def move_up(self, field):
        self.current_animation = self.walk_up
        self.anim_counter += 1
        next_cell_0 = field.get_position((self.pos_x, self.pos_y - 1))
        next_cell_1 = field.get_position((self.pos_x + 49, self.pos_y - 1))
        if str(field.field[next_cell_0[1]][next_cell_0[0]]) not in ('1', '2') \
                and str(field.field[next_cell_1[1]][next_cell_1[0]]) not in ('1', '2'):
            self.pos_y -= self.speed
        else:
            if str(field.field[next_cell_0[1]][next_cell_0[0]]) in ('1', '2') and \
                    str(field.field[next_cell_1[1]][next_cell_1[0]]) not in ('1', '2'):
                if self.pos_x > (50 * next_cell_1[0] - 30):
                    self.pos_y -= self.speed
                    self.pos_x += self.speed
            elif str(field.field[next_cell_1[1]][next_cell_1[0]]) in ('1', '2') and \
                    str(field.field[next_cell_0[1]][next_cell_0[0]]) not in ('1', '2'):
                if self.pos_x < (50 * (next_cell_0[0] + 1)) - 24:
                    self.pos_y -= self.speed
                    self.pos_x -= self.speed
        self.sync_with_field(field)

    def move_down(self, field):
        self.current_animation = self.walk_down
        self.anim_counter += 1
        next_cell_0 = field.get_position((self.pos_x, self.pos_y + 50))
        next_cell_1 = field.get_position((self.pos_x + 49, self.pos_y + 50))
        if str(field.field[next_cell_0[1]][next_cell_0[0]]) not in ('1', '2') \
                and str(field.field[next_cell_1[1]][next_cell_1[0]]) not in ('1', '2'):
            self.pos_y += self.speed
        else:
            if str(field.field[next_cell_0[1]][next_cell_0[0]]) in ('1', '2') and \
                    str(field.field[next_cell_1[1]][next_cell_1[0]]) not in ('1', '2'):
                if self.pos_x > (50 * next_cell_1[0] - 30):
                    self.pos_y += self.speed
                    self.pos_x += self.speed
            elif str(field.field[next_cell_1[1]][next_cell_1[0]]) in ('1', '2') and \
                    str(field.field[next_cell_0[1]][next_cell_0[0]]) not in ('1', '2'):
                if self.pos_x < (50 * (next_cell_0[0] + 1)) - 22:
                    self.pos_y += self.speed
                    self.pos_x -= self.speed
        self.sync_with_field(field)

    def sync_with_field(self, field):
        cur_pos = field.get_position((self.pos_x + 24, self.pos_y + 24))
        if self.field_pos != cur_pos:
            if field.field[cur_pos[1]][cur_pos[0]] == 0:
                field.field[self.field_pos[1]][self.field_pos[0]] = 0
                field.field[cur_pos[1]][cur_pos[0]] = 3
                self.field_pos = cur_pos

    # обновляет состояние игрока
    def update(self):
        if self.anim_counter >= 16:
            self.anim_counter = 0

        self.frame = self.current_animation[self.anim_counter // 4]
        self.rect = self.frame.get_rect()

    # рисует игрока
    def draw(self, surface):
        surface.blit(self.frame, self.get_pos())
