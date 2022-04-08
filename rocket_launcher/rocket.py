from re import S
import pygame

class Rocket:
    """A class to manage a rocket."""

    def __init__(self, rocket):
        """Initialize the rocket and set its starting position."""
        self.screen = rocket.screen
        self.settings = rocket.settings
        self.screen_rect = rocket.screen.get_rect()

        # Load the rocket image and get its rect.
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()

        # Setting a rocket image to center
        self.rect.center = self.screen_rect.center

        # Store a decimal value for the rocket's horizontal and vertical position.
        self.x = float(self.rect.x) 
        self.y = float(self.rect.y) 

        # Movement Flag
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def update(self):
        """Update the rocket position based on the movement flag."""
        # Update the rocket's x and y value, not rect. 
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.speed
        if self.move_left and self.rect.left > 0:
            self.x -= self.settings.speed
        if self.move_up:
            self.y += self.settings.speed
        if self.move_down:
            self.y -= self.settings.speed

        # Update rect object from self.x and self.y.
        self.rect.x = self.x
        self.rect.y = self.y

    def blit(self):
        """Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)
        