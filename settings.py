class Settings:
    # A class for storing app settings.

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_bg = (230, 230, 230)
        self.ship_speed = 1.5

        self.bullet_speed = 1.0
        self.bullet_limit = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)