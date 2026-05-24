def handle_bullets(delta: float, bullets, enemies):
    for bullet in bullets[:]:
        bullet._physics_update(delta)

        if bullet.life <= 0:
            bullets.remove(bullet)
            continue

        for enemy in enemies[:]:
            if bullet.rect.colliderect(enemy.rect):
                enemy.take_damage(1, bullet.pos, bullet.knockback)

                if bullet in bullets:
                    bullets.remove(bullet)

                if enemy.health <= 0:
                    enemies.remove(enemy)

                break

def handle_bombs(delta: float, bombs, enemies, player):
    explosions = []
    for bomb in bombs[:]:
        bomb._physics_update(delta)

        if bomb.detonation_delay <= 0:
            explosion = bomb.explode()
            explosions.append(explosion)
            bombs.remove(bomb)

            for enemy in enemies[:]:
                if explosion.rect.colliderect(enemy.rect):
                    enemy.take_damage(3, explosion.pos, bomb.knockback)

                    if enemy.health <= 0:
                        enemies.remove(enemy)
            
            if explosion.rect.colliderect(player.rect):
                player.take_damage(1, explosion.pos, bomb.knockback)
    return explosions


def handle_explosions(delta: float, explosions):
    for explosion in explosions[:]:
        explosion._physics_update(delta)

        if explosion.life <= 0:
            explosions.remove(explosion)