class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""

        # Ship settings
        self.ship_speed = 1.5

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        # Sets the background color
        self.bg_color = (235, 237, 238)