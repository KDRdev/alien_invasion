class Settings:
    # A class for storing app settings.

    def __init__(self):
        self.screen_width = 1024
        self.screen_height = 768
        self.screen_bg = (230, 230, 230)
        self.ship_speed = 1.5

        self.bullet_speed = 1.0
        self.bullet_limit = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        self.alien_speed = 1.0
        self.aliens_drop_speed = 1
        # Direction 1 is right, -1 is left
        self.aliens_direction = 1