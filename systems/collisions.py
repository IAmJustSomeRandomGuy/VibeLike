def bullet_enemy_collisions(bullets, enemies):
    bullets_to_remove = []
    enemies_to_remove = []

    for bullet in bullets:
        for enemy in enemies:
            if bullet.rect.colliderect(enemy.rect):
                enemy.health -= 1

                if bullet not in bullets_to_remove:
                    bullets_to_remove.append(bullet)

                if enemy.health <= 0:
                    enemies_to_remove.append(enemy)

    for bullet in bullets_to_remove:
        if bullet in bullets:
            bullets.remove(bullet)

    for enemy in enemies_to_remove:
        if enemy in enemies:
            enemies.remove(enemy)