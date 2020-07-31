import pygame

class Ship:
    # A class describing a ship object.

    def __init__(self, ai_game):
        # Initialize a ship and set its starting position.
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.settings = ai_game.settings

        # Load a ship image and get its rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # A flag for moving the ship
        self.moving_left = False
        self.moving_right = False

        # Position the ship rect at the middle bottom part of the screen and 
        # store its horizontal position as a decimal.
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        # Moves the ship by changing its horizontal position by ship_speed
        if self.moving_left and self.x >= 0:
            self.x -= self.settings.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        # Draw the ship at its current position.
        self.screen.blit(self.image, self.rect)

