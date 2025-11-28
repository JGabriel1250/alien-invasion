class Settings():
    """Uma claase para armazenar todas as configurações do jogo"""

    def __init__(self):
        """Inicializa as configurações do jogo"""
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5

        # Configurações dos projéteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_alowed = 3
