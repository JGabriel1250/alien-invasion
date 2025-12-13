import pygame
from settings import *
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats

def run_game():
    #inicializa o jogo e cria um objeto para a tela
    pygame.init()
    al_settings = Settings()
    screen = pygame.display.set_mode((al_settings.screen_width, al_settings.screen_height))
    pygame.display.set_caption("Alien invasion")

    # Cria uma instância para armazenar dados estatísticos
    stats = GameStats(al_settings)

    # Cria uma espaçonave, um grupo de projéteis e um grupo de alienígenas
    ship = Ship(screen, al_settings)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(al_settings, screen, ship, aliens)

    #Inicia o laço principal do jogo
    while True:
        gf.check_events(al_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(al_settings, screen, ship, aliens, bullets)
        gf.update_aliens(al_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(al_settings, screen, ship, aliens, bullets)


        


run_game()