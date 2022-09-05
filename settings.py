class Settings():
    """класс для хронение всех настроек игры Alien Invasion"""

    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (65, 160, 255)
        self.ship_speed = 1.5

        #параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)