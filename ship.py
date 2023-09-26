import pygame


class Ship:
    """A class to manage ship."""

    def __init__(self, sp_game):
        """Initialize the ship and set its starting position."""
        self.screen = sp_game.screen
        self.screen_rect = sp_game.screen.get_rect()
        # Load the ship image and get its rect.
        self.image = pygame.image.load('media/ship2_w85_h100.png')
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        # moving right and left flag
        self.move_right = False
        self.move_left = False

    def blit_me(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 3
        elif self.move_left and self.rect.left > 0:
            self.rect.x -= 3
