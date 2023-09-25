import sys
import pygame
from settings import Settings
from ship import Ship


class SpaceShip:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.screen_size)
        self.background_color = self.settings.background_color
        self.ship = Ship(self)
        pygame.display.set_caption("Space Ship")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.background_color)
            self.ship.blit_me()
            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    sp = SpaceShip()
    sp.run_game()
