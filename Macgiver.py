"""This class permit to create and move the hero"""
import pygame
import Constants


class Hero:
    """Class permit to create the hero"""

    def __init__(self, env):
        # loading hero picture
        self.picture = pygame.image.load(Constants.MACGIVER_PICTURE).convert()
        # Position of the hero
        self.sprite_x = 0
        self.sprite_y = 0
        self.x = 0
        self.y = 0
        # Environment of the hero
        self.env = env

    def move(self, env, direction):
        """Method permit to move the hero"""

        # Moving right
        if direction == 'right':
            # Don't go out of the screen
            if self.sprite_x < (Constants.SPRITE_NUM - 1):
                # Check if the position is valid
                if self.env.structure[self.sprite_y][self.sprite_x + 1] != 'X':
                    # moving one sprite right
                    self.sprite_x += 1
                    # Calculate position in pixels
                    self.x = self.sprite_x * Constants.SPRITE_SIZE
            # Refresh picture position
            self.direction = self.picture

        # Moving left
        if direction == 'left':
            if self.sprite_x > 0:
                if self.env.structure[self.sprite_y][self.sprite_x - 1] != 'X':
                    self.sprite_x -= 1
                    self.x = self.sprite_x * Constants.SPRITE_SIZE
            self.direction = self.picture

        # Moving up
        if direction == 'up':
            if self.sprite_y > 0:
                if self.env.structure[self.sprite_y - 1][self.sprite_x] != 'X':
                    self.sprite_y -= 1
                    self.y = self.sprite_y * Constants.SPRITE_SIZE
            self.direction = self.picture

        # Moving Down
        if direction == 'down':
            if self.sprite_y < (Constants.SPRITE_NUM - 1):
                if self.env.structure[self.sprite_y + 1][self.sprite_x] != 'X':
                    self.sprite_y += 1
                    self.y = self.sprite_y * Constants.SPRITE_SIZE
            self.direction = self.picture

        # permit to take items and count them
        take_item = self.env.structure[self.sprite_y][self.sprite_x]
        if take_item == 'E' or take_item == 'T' or take_item == 'N':
            env.score = env.score + 1
            self.env.structure[self.sprite_y][self.sprite_x] = '0'
