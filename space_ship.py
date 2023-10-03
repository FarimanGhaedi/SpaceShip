import sys
import pygame
from settings import Settings
from ship import Ship
from enemy import Enemy
from bullet import Bullet


class SpaceShip:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        pygame.display.set_caption("Space Ship")
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_size = (self.screen.get_rect().width, self.screen.get_rect().height)
        self.background_color = self.settings.background_color
        self.ship = Ship(self)
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        # Respond to keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down_events(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up_events(event)

    def _check_key_down_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_key_up_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        if event.key == pygame.K_LEFT:
            self.ship.move_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.background_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blit_me()
        self.enemies.draw(self.screen)
        pygame.display.flip()

    def _create_fleet(self):
        """Create the fleet of enemies."""
        # Create an enemy
        new_enemy = Enemy(self)
        self.enemies.add(new_enemy)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    sp = SpaceShip()
    sp.run_game()
