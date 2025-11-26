import pygame

class Ship():
    def __init__(self, screen, al_settings):
        """inicializa a espaçonave e obtém seu rect"""
        self.screen = screen
        self.al_settings = al_settings

        # Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('pygame/imagens/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicia cada nova espaçonave em sua posição atual
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Armazena um valor decimal para o centro da espaçonave
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Atualiza a posição da espaçonave em sua posição atual."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.al_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.al_settings.ship_speed_factor
            
        # Atualiza o objeto rect de acordo com o self.center    
        self.rect.centerx = self.center

    def blitime(self):
        """Desenha a espaçonave em sua posição atual"""
        self.screen.blit(self.image, self.rect)