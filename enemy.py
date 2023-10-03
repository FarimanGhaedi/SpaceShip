import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    """A class to represent a single enemy in the fleet."""

    def __init__(self, sp_game):
        """Initialize the enemy and set the starting position."""
        super().__init__()
        self.screen = sp_game.screen
        # Load the enemy image and set its rect attribute.
        self.image = pygame.image.load('media/enemy_w90_h60.png')
        self.rect = self.image.get_rect()
        # Start each new enemy near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the exact horizontal position.
        self.x = float(self.rect.x)