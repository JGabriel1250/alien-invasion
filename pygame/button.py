import pygame.ftfont

class Button():

    def __init__(self, al_settings, screen, msg):
        """Inicializa os atributos do botão."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # define as dimensões e as propriedades do botão
        self.width = 200
        self.height = 50
        self.button_color = (0,255,0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Constrói o objeto rect botão e o centraliza

        self.rect = pygame.Rect(0,0, self.widht, self.height)
        self.rect.center = self.screen_rect.center

        # A mensagem do botão deve ser preparada apenas uma vez
        self.prep_msg(msg)