class Settings:
    """A class to store all settings for Space Ship game."""

    def __init__(self):
        # Screen setting
        self.background_color = (230, 230, 230)
        self.screen_size = (1200, 800)
        # Bullet settings
        self.bullet_speed = 30.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # Enemy settings
        self.enemy_speed = 1.0
        self.enemy_drop_speed = 10
        self.fleet_direction = 1  # direction: value 1 means right and -1 means left
