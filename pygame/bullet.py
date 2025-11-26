import pygame
from pygame.sprite import Sprite

class bullet(Sprite):
    """Uma classe que administra projéteis disparados pela espaçonave."""

    def __init__(self, al_settings, screen, ship):
        #Cria um objeto para o projétil na posição atual da espaçonave.
        super(bullet, self).__init__()
        self.screen = screen

        # Cria um retângulo para o projétil em (0,0) e, em seguida, define a posição correta 
        self.rect = pygame.Rect(0 ,0, al_settings.bullet_width, al_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Armazena a posição do projétil com valor decimal
        self.y = float(self.rect.y)

        self.color = al_settings.bullet._color
        self.speed_factor = al_settings.bullet_speed_factor