
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