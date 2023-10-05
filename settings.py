class Settings:
    """A class to store all settings for Space Ship game."""

    def __init__(self):
        # Screen setting
        self.background_color = (230, 230, 230)
        self.screen_size = (1200, 800)
        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # Enemy settings
        self.enemy_speed = 1.0