import sys
import pygame
from settings import *
from ship import Ship
import game_functions as gf

def run_game():
    #inicializa o jogo e cria um objeto para a tela
    pygame.init()
    al_settings = Settings()
    screen = pygame.display.set_mode((al_settings.screen_widht, al_settings.screen_height))
    pygame.display.set_caption("Alien invasion")
    ship = Ship(screen, al_settings)

    #Inicia o laço principal do jogo
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(al_settings, screen, ship)


run_game()