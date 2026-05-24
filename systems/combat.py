def handle_bullets(bullets, enemies):
    for bullet in bullets[:]:
        bullet.update()

        if bullet.life <= 0:
            bullets.remove(bullet)
            continue

        for enemy in enemies[:]:
            if bullet.rect.colliderect(enemy.rect):
                enemy.health -= 1

                if bullet in bullets:
                    bullets.remove(bullet)

                if enemy.health <= 0:
                    enemies.remove(enemy)

                break

def handle_bombs(bombs, enemies):
    explosions = []
    for bomb in bombs[:]:
        bomb.update()

        if bomb.detonation_delay <= 0:
            explosion = bomb.explode()
            explosions.append(explosion)
            bombs.remove(bomb)

            for enemy in enemies[:]:
                if explosion.rect.colliderect(enemy.rect):
                    enemy.health -= 3

                    if enemy.health <= 0:
                        enemies.remove(enemy)
    return explosions


def handle_explosions(explosions):
    for explosion in explosions[:]:
        explosion.update()

        if explosion.life <= 0:
            explosions.remove(explosion)