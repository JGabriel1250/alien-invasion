import pygame
from settings import *
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():
    #inicializa o jogo e cria um objeto para a tela
    pygame.init()
    al_settings = Settings()
    screen = pygame.display.set_mode((al_settings.screen_width, al_settings.screen_height))
    pygame.display.set_caption("Alien invasion")
    # Cria uma espaçonave
    ship = Ship(screen, al_settings)
    # cria um grupo no qual serão armazenados os projéteis
    bullets = Group()
    # Cria um alienígena
    alien = Alien(al_settings, screen)

    #Inicia o laço principal do jogo
    while True:
        gf.check_events(al_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        gf.update_screen(al_settings, screen, ship, alien, bullets)


        


run_game()