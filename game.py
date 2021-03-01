import pygame
from player import Player
from field import Field
from enemys import Enemy


def update(objects):
    for obj in objects:
        obj.update()


def draw(surface, objects):
    surface.fill((255, 204, 0))
    for obj in objects:
        obj.draw(surface)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Bomberman')
    size = width, height = 650, 600
    screen = pygame.display.set_mode(size)

    running = True
    clock = pygame.time.Clock()
    fps = 60

    game_objects = []

    field = Field()
    game_objects.append(field)
    field.generate_map()

    player = Player()
    game_objects.append(player)

    for i in range(4):
        response = field.spawn_enemy()
        while response[0] is False:
            response = field.spawn_enemy()
        x, y = response[1] * 50, response[2] * 50
        enemy = Enemy(field, x, y)
        game_objects.append(enemy)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.move_left(field)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.move_right(field)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.move_up(field)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.move_down(field)

        for obj in game_objects:
            if obj.__class__.__name__ == 'Enemy':
                if abs(player.pos_x - obj.pos_x) < 30 and abs(player.pos_y - obj.pos_y) < 30:
                    player.die()

        update(game_objects)
        draw(screen, game_objects)

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
