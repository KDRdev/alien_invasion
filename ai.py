import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    # Main class to manage app resources.

    def __init__(self):
        # Initializes a game and creates game resources.
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.bg_color = self.settings.screen_bg
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        # A main game loop.
        while True:
            self._check_updates()
            self.screen.fill(self.bg_color)
            self.ship.update()
            self.update_bullet()
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            pygame.display.flip()
    
    def _check_updates(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def update_bullet(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            print(len(self.bullets))

    def _check_keydown_events(self, event):
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

    def _fire_bullet(self):
        if len(self.bullets)<self.settings.bullet_limit:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()    