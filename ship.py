import pygame

class Ship:
    # A class describing a ship object.

    def __init__(self, ai_game):
        # Initialize a ship and set its starting position.
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load a ship image and get its rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Position the ship rect at the middle bottom part of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # Draw the ship at its current position.
        self.screen.blit(self.image, self.rect)

