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


def update_bullets(bullets):
    """Atuali a posição dos projéteis e se livra dos projéteis antigos."""
    # Atualiza as posições dos projéteis
    bullets.update()

    # Livra-se dos projéteis que desaparecem
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(al_settings, screen, ship, bullets):
    # Cria um novo projétil e o adiciona ao grupo de projéteis
        if len(bullets) < al_settings.bullets_alowed:
            new_bullet = Bullet(al_settings, screen, ship)
            bullets.add(new_bullet)

def create_fleet(al_settings, screen, aliens):
    """Cria uma frota completa de alieníginas"""
    # Cria um alienígina e calcula o número de alieníginas em uma linha
    # O espaçamento entre os alieníginas é igual á largura de um alienígina

    alien = Alien(al_settings, screen)
    alien_width = alien.rect.width
    avaliable_space_x = al_settings.screen_width - 2 * alien_width
    number_alien_x = int(avaliable_space_x/ (2* alien_width))

    # Cria a primeira linha de alieníginas

    for alien_number in range(number_alien_x):
        # Cria um alienígina e o posiciona na linha
        alien = Alien(al_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
