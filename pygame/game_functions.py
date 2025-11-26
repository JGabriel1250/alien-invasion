import sys
import pygame

def check_keydown_events(event, ship):
    """Responde a pressionamento de tecla."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    """responde a solturas de tecla."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    """Responde o eventos pressionamento de teclas e de mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Move a espaçonave para a direita  ou esquerda quando a tecla é pressionada
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        # Quando a tecla da direita ou esqueda e solta a nave para
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            

def update_screen(al_settings, screen, ship):
    # Redesenha a tela a cada passagem pelo
    screen.fill(al_settings.bg_color)
    ship. blitime()

    # Deixa a tela mais recente visivel
    pygame.display.flip()