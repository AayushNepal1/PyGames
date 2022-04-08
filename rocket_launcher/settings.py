class Settings:
    """Store all settings for Rocket Launcher."""

    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (235, 237, 238)
    
        # Rocket Speed
        self.speed = 1.5