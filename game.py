import pygame
from player import Player


def update(objects):
    for obj in objects:
        obj.update()


def draw(screen, objects):
    screen.fill((255, 204, 0))
    for obj in objects:
        obj.draw(screen)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Bomberman')
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    running = True
    clock = pygame.time.Clock()
    fps = 60

    game_objects = []

    player = Player()
    game_objects.append(player)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.move_left()
        if keys[pygame.K_RIGHT]:
            player.move_right()
        if keys[pygame.K_UP]:
            player.move_up()
        if keys[pygame.K_DOWN]:
            player.move_down()

        update(game_objects)
        draw(screen, game_objects)

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
