import sys
import pygame
from bullet import *
from alien import Alien

def check_keydown_events(event, al_settings, screen, ship, bullets):
    """Responde a pressionamento de tecla."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(al_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """responde a solturas de tecla."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(al_settings, screen, ship, bullets):
    """Responde o eventos pressionamento de teclas e de mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Move a espaçonave para a direita  ou esquerda quando a tecla é pressionada
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, al_settings, screen, ship, bullets)
        # Quando a tecla da direita ou esqueda e solta a nave para
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            

def update_screen(al_settings, screen, ship, aliens, bullets):
    # Redesenha a tela a cada passagem pelo
    screen.fill(al_settings.bg_color)

    # Redesenha todos os projéteis atrás da espaçonave e dos alienígenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship. blitme()
    aliens.draw(screen)

    # Deixa a tela mais recente visivel
    pygame.display.flip()


def update_bullets(aliens, bullets):
    """Atuali a posição dos projéteis e se livra dos projéteis antigos."""
    # Atualiza as posições dos projéteis
    bullets.update()

    # Livra-se dos projéteis que desaparecem
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Verifica se algum projétil atingiu os alienígenas
    # Em caso afirmativo, livra-se do projétil e do alienígena
    collisons = pygame.sprite.groupcollide(bullets, aliens, True, True)

def fire_bullet(al_settings, screen, ship, bullets):
    # Cria um novo projétil e o adiciona ao grupo de projéteis
        if len(bullets) < al_settings.bullets_alowed:
            new_bullet = Bullet(al_settings, screen, ship)
            bullets.add(new_bullet)


def get_number_rows(al_settings, ship_height, alien_height):
    """Determina o número de linhas com alienígenas que cabem na tela"""
    available_space_y = (al_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
    

def get_number_aliens_x(al_settings, alien_width):
    """Determina o número de alienígenas que cabem em uma linha."""

    avaliable_space_x = al_settings.screen_width - 2 * alien_width
    number_alien_x = int(avaliable_space_x/ (2* alien_width))
    return number_alien_x


def create_alien(al_settings, screen, aliens, alien_number, row_number):
    # Cria um alienígina e o posiciona na linha
    alien = Alien(al_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(al_settings, screen, ship, aliens):
    """Cria uma frota completa de alienígenas"""
    # Cria um alienígina e calcula o número de alienígenas em uma linha
    # O espaçamento entre os alienígenas é igual á largura de um alienígena

    alien = Alien(al_settings, screen)
    number_aliens_x = get_number_aliens_x(al_settings,alien.rect.width)
    number_row = get_number_rows(al_settings, ship.rect.height, alien.rect.height)

    # Cria a primeira linha de alieníginas

    for row_number in range(number_row):
        for alien_number in range(number_aliens_x):
            create_alien(al_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(al_settings, aliens):
    """Responde apropriadamente se algum alienígena alcançou a borda."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(al_settings, aliens)
            break

            
def change_fleet_direction(al_settings, aliens):
    """Faz toda frota descer e muda a sua direção"""
    for alien in aliens.sprites():
        alien.rect.y += al_settings.fleet_drop_speed
    al_settings.fleet_direction *= -1


def update_aliens(al_settings, aliens):
    """Verifica se a frota está em uma das bordas e então atualiza as posições de todos os alienígenas da frota"""
    check_fleet_edges(al_settings, aliens)
    aliens.update()