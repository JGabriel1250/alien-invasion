import pygame
from settings import *
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    #inicializa o jogo e cria um objeto para a tela
    pygame.init()
    al_settings = Settings()
    screen = pygame.display.set_mode((al_settings.screen_width, al_settings.screen_height))
    pygame.display.set_caption("Alien invasion")

    # Criaa o botão play
    play_button = Button(al_settings, screen, 'Play')

    # Cria uma instância para armazenar dados estatísticos do jogo e cria painel de pontuação
    stats = GameStats(al_settings)
    sb = Scoreboard(al_settings, screen, stats)

    # Cria uma espaçonave, um grupo de projéteis e um grupo de alienígenas
    ship = Ship(screen, al_settings)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(al_settings, screen, ship, aliens)

    #Inicia o laço principal do jogo
    while True:
        gf.check_events(al_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(al_settings, screen, ship, aliens, bullets)
            gf.update_aliens(al_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(al_settings, screen, stats, sb, ship, aliens, bullets, play_button)


        


run_game()