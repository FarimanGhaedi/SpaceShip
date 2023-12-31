import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    """A class to represent a single enemy in the fleet."""

    def __init__(self, sp_game):
        """Initialize the enemy and set the starting position."""
        super().__init__()
        self.screen = sp_game.screen
        self.settings = sp_game.settings
        # Load the enemy image and set its rect attribute.
        self.image = pygame.image.load('media/enemy_w90_h60.png')
        self.rect = self.image.get_rect()
        # Start each new enemy near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the exact horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move enemy to right or left"""
        self.x += self.settings.enemy_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_enemy_hit_edge(self):
        """Returns True if enemy is at the edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.width) or (self.rect.left <= 0)
