"""Class Maze of the game Macgiver Maze"""

import pygame
import Constants


class Labyrinth:
    """class permit to create the maze"""

    def __init__(self, file):
        self.file = file
        self.structure = 0

    def load_from_file(self):
        """Method for generating the level according to the file.
         We create a general list, containing a list by line to display"""

        # opening the file
        with open(self.file, "r") as file:
            maze_matrice = []
            # We go through the lines in our file
            for line in file:
                line_maze = []
                # We go through the sprites (letters) in the file
                for sprite in line:
                    # We ignore the end of line "\ n"
                    if sprite != '\n':
                        # we add the sprite that correspond
                        line_maze.append(sprite)
                # We add the line to the list
                maze_matrice.append(line_maze)
            # We take this structure in a list of list
            self.structure = maze_matrice

    def print_maze(self, window):
        """Method for displaying the level according to
        the structure returned by load_from_file()"""

        # Loading pictures
        wall = pygame.image.load(Constants.WALL_PICTURE).convert()
        guardian = pygame.image.load(Constants.GUARDIAN_PICTURE).convert_alpha()
        ether = pygame.image.load(Constants.ETHER_PICTURE).convert()
        tube = pygame.image.load(Constants.TUBE_PICTURE).convert()
        needle = pygame.image.load(Constants.NEEDLE_PICTURE).convert()

        # We go through the level list
        line_number = 0
        for line in self.structure:
            # On parcourt les listes de lignes
            sprite_number = 0
            for sprite in line:
                # On calcule la position réelle en pixels
                x = sprite_number * Constants.SPRITE_SIZE
                y = line_number * Constants.SPRITE_SIZE
                if sprite == 'X':  # X = wall
                    window.blit(wall, (x, y))
                elif sprite == 'F':  # F = final
                    window.blit(guardian, (x, y))
                elif sprite == 'E':  # E = object ether
                    window.blit(ether, (x, y))
                elif sprite == 'T':  # T = object tube
                    window.blit(tube, (x, y))
                elif sprite == 'N':  # N = object needle
                    window.blit(needle, (x, y))
                sprite_number += 1
            line_number += 1
