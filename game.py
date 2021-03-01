import pygame
from player import Player
from field import Field
from enemys import Enemy
# from explosion import Explosion


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

    lose = False

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
        # if keys[pygame.K_SPACE]:
        #     game_objects.append(player.plant_bomb(field))

        for obj in game_objects:
            #enemys = []
            if obj.__class__.__name__ == 'Enemy':
                # if obj.is_dead():
                #     game_objects.remove(obj)
                # else:
                #     if abs(player.pos_x - obj.pos_x) < 30 and abs(player.pos_y - obj.pos_y) < 30:
                #         player.die()
                #     enemys.append(obj)
                if abs(player.pos_x - obj.pos_x) < 30 and abs(player.pos_y - obj.pos_y) < 30:
                    player.die()
                    lose = True
                #enemys.append(obj)
            # if obj.__class__.__name__ == 'Bomb':
            #     if obj.is_blown():
            #         explosion_center = obj.get_row_col()
            #         game_objects.remove(obj)
                    # explos = Explosion(field, enemys, explosion_center)
                    # game_objects.append(explos)
            # if obj.__class__.__name__ == 'Explosion':
            #     if obj.is_ended():
            #         game_objects.remove(obj)
        if not lose:
            update(game_objects)
            draw(screen, game_objects)
        else:
            screen.fill((0, 0, 0))
            font = pygame.font.Font(None, 50)
            text = font.render("Вы проиграли", True, (255, 0, 0))
            text_x = width // 2 - text.get_width() // 2
            text_y = height // 2 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            pygame.draw.rect(screen, (255, 0, 0), (text_x - 10, text_y - 10,
                                                   text_w + 20, text_h + 20), 1)

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
