class Settings():
    """Uma claase para armazenar todas as configurações do jogo"""

    def __init__(self):
        """Inicializa as configurações do jogo"""
        self.screen_width = 952
        self.screen_height = 600
        self.bg_color = (230,230,230)


        #
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        


        # Configurações dos projéteis
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_alowed = 3

        # Configuração dos alienígenas
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10

        # fleet_direction igual a 1 representa a direita; -1 representa a esquerda
        self.fleet_direction = 1