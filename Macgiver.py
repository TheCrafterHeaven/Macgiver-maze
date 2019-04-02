import pygame
import Constants


class Hero:
    """Class permit to create the hero"""

    def __init__(self, env):
        # loading hero picture
        self.picture = pygame.image.load(Constants.MACGIVER_PICTURE).convert()
        # Position of the hero
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        # Environment of the hero
        self.env = env

    def move(self, env, direction):
        """Method permit to move the hero"""

        # Moving right
        if direction == 'right':
            # Don't go ouf of the screen
            if self.case_x < (Constants.SPRITE_NUM - 1):
                # Check if the position is valid
                if self.env.structure[self.case_y][self.case_x + 1] != 'm':
                    # moving one sprite
                    self.case_x += 1
                    # Calculate position in pixels
                    self.x = self.case_x * Constants.SPRITE_SIZE
            # Refresh picture position
            self.direction = self.picture

        # Moving left
        if direction == 'left':
            if self.case_x > 0:
                if self.env.structure[self.case_y][self.case_x - 1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * Constants.SPRITE_SIZE
            self.direction = self.picture

        # Moving up
        if direction == 'up':
            if self.case_y > 0:
                if self.env.structure[self.case_y - 1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * Constants.SPRITE_SIZE
            self.direction = self.picture

        # Moving Down
        if direction == 'down':
            if self.case_y < (Constants.SPRITE_NUM - 1):
                if self.env.structure[self.case_y + 1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * Constants.SPRITE_SIZE
            self.direction = self.picture
