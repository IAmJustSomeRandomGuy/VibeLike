import sys
import pygame

from settings import *
from game import Game


pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Isaac Clone")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 32)
big_font = pygame.font.SysFont(None, 72)


def draw_ui(screen, game):
    # Health
    for i in range(PLAYER_MAX_HEALTH):
        color = HEART_COLOR if i < game.player.health else (70, 45, 55)

        pygame.draw.rect(
            screen,
            color,
            (20 + i * 28, 20, 20, 20)
        )

    # Room info
    text = font.render(
        f"Room: ({game.room_x}, {game.room_y})",
        True,
        (255, 255, 255)
    )

    screen.blit(text, (20, 60))

    enemy_text = font.render(
        f"Enemies: {len(game.room.enemies)}",
        True,
        (255, 255, 255)
    )

    screen.blit(enemy_text, (20, 90))

    controls = font.render(
        "WASD Move | Arrow Keys Shoot | E to place bomb | ESC Quit",
        True,
        (180, 180, 180)
    )

    screen.blit(controls, (20, HEIGHT - 40))


def draw_game_over(screen):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 0))

    title = big_font.render("GAME OVER", True, (255, 255, 255))
    subtitle = font.render(
        "Press R to Restart",
        True,
        (255, 255, 255)
    )

    screen.blit(
        title,
        title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
    )

    screen.blit(
        subtitle,
        subtitle.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
    )


def handle_room_transition(game):
    player = game.player

    # Left
    if player.rect.left <= 0:
        if game.room_x > 0:
            game.room_x -= 1
            player.pos.x = WIDTH - 80

    # Right
    elif player.rect.right >= WIDTH:
        if game.room_x < ROOM_GRID_W - 1:
            game.room_x += 1
            player.pos.x = 80

    # Top
    elif player.rect.top <= 0:
        if game.room_y > 0:
            game.room_y -= 1
            player.pos.y = HEIGHT - 80

    # Bottom
    elif player.rect.bottom >= HEIGHT:
        if game.room_y < ROOM_GRID_H - 1:
            game.room_y += 1
            player.pos.y = 80

    player.sync()


def main():
    game = Game()

    running = True

    while running:
        delta = clock.tick(FPS)/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_r:
                    if game.player.health <= 0:
                        game = Game()

        if game.player.health > 0:
            game.update(delta)
            handle_room_transition(game)

            # Enemy collision damage
            for enemy in game.room.enemies:
                if enemy.rect.colliderect(game.player.rect):
                    game.player.take_damage(1, enemy.pos, 350)
                    break

            # Pickup collection
            for pickup in game.room.pickups[:]:
                if pickup.rect.colliderect(game.player.rect):
                    game.player.heal(1)

                    game.room.pickups.remove(pickup)

        # Draw
        game.draw(screen)
        draw_ui(screen, game)

        if game.player.health <= 0:
            draw_game_over(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()