import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """uma classe que representa um único alienígina da frota"""

    def __init__(self, al_settings, screen):
        """Inicializa o alienígina e define sua posição inicial"""
        super(Alien, self).__init__()
        self.screen = screen
        self.al_settings = al_settings

        # Carrega a imagem do alienígina e define seu atributo rect
        self.image = pygame.image.load('pygame/imagens/alien_100x100.png')
        self.rect = self.image.get_rect()

        # inicia cada novo alienígena próximo à parte superior esqueda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata do alienígena
        self.x = float(self.rect.x)

    def blitme(self):
        """Desenha o alienígena"""
        self.screen.blit(self.image, self.rect)