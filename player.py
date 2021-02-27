import pygame


class Player:
    def __init__(self):
        # Задаю параметры игрока
        self.pos_x = 250
        self.pos_y = 250
        self.color = (255, 0, 0)
        self.radius = 20
        self.speed = 2.5

        self.walk_up = [pygame.transform.scale(pygame.image.load('images/pu0.png'), (44, 44)),
                        pygame.transform.scale(pygame.image.load('images/pu1.png'), (44, 44)),
                        pygame.transform.scale(pygame.image.load('images/pu0.png'), (44, 44)),
                        pygame.transform.scale(pygame.image.load('images/pu2.png'), (44, 44))]
        self.walk_down = [pygame.transform.scale(pygame.image.load('images/pd0.png'), (44, 44)),
                          pygame.transform.scale(pygame.image.load('images/pd1.png'), (44, 44)),
                          pygame.transform.scale(pygame.image.load('images/pd0.png'), (44, 44)),
                          pygame.transform.scale(pygame.image.load('images/pd2.png'), (44, 44))]
        self.walk_left = [pygame.transform.scale(pygame.image.load('images/pl0.png'), (44, 44)),
                          pygame.transform.scale(pygame.image.load('images/pl1.png'), (44, 44)),
                          pygame.transform.scale(pygame.image.load('images/pl0.png'), (44, 44)),
                          pygame.transform.scale(pygame.image.load('images/pl2.png'), (44, 44))]
        self.walk_right = [pygame.transform.scale(pygame.image.load('images/pr0.png'), (44, 44)),
                           pygame.transform.scale(pygame.image.load('images/pr1.png'), (44, 44)),
                           pygame.transform.scale(pygame.image.load('images/pr0.png'), (44, 44)),
                           pygame.transform.scale(pygame.image.load('images/pr2.png'), (44, 44))]
        self.current_animation = self.walk_left
        self.anim_counter = 0

        self.alive = True

    # возвращает координаты игрока
    def get_pos(self):
        return self.pos_x, self.pos_y

    """
    следующие четыре функции изменяют и возвращают 
    измененную позицию игрока
    """
    def move_right(self):
        self.current_animation = self.walk_right
        self.anim_counter += 1
        self.pos_x += self.speed
        self.get_pos()

    def move_left(self):
        self.current_animation = self.walk_left
        self.anim_counter += 1
        self.pos_x -= self.speed
        self.get_pos()

    def move_up(self):
        self.current_animation = self.walk_up
        self.anim_counter += 1
        self.pos_y -= self.speed
        self.get_pos()

    def move_down(self):
        self.current_animation = self.walk_down
        self.anim_counter += 1
        self.pos_y += self.speed
        self.get_pos()

    # обновляет состояние игрока
    def update(self):
        if self.anim_counter >= 32:
            self.anim_counter = 0

    # рисует игрока
    def draw(self, screen):
        screen.blit(self.current_animation[self.anim_counter // 8], self.get_pos())
