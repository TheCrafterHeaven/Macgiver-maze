#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""Game Macgiver-Maze
In this game you will need to move macgiver to catch different objects
With those objects you can asleep the guardian and success

Files :
Constants.py, Main.py, Maze_Struct.txt, pictures, README.md"""

import pygame
import Constants
import Maze

pygame.init()

# Opening pygame window with sizes (width, height)
window = pygame.display.set_mode((Constants.WINDOW_DIM, Constants.WINDOW_DIM))

icon = pygame.image.load(Constants.MACGIVER_PICTURE)
pygame.display.set_icon(icon)

# Title
pygame.display.set_caption(Constants.WINDOW_TITLE)

# First loop
first_loop = 1
while first_loop:
    # loading the home screen
    home = pygame.image.load(Constants.HOME_PICTURE).convert()
    window.blit(home, (0, 0))

    # Refresh
    pygame.display.flip()

    game_loop = 1
    home_loop = 1

    # home loop
    while home_loop:

        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            # if the user exit the game, we put variables to 0
            # that close the window
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:

                first_loop = 0
                game_loop = 0
                home_loop = 0
                # introducing variable to start the game
                go = 0

            elif event.type == pygame.KEYDOWN:
                # playing game loop
                if event.key == pygame.K_F1:
                    home_loop = 0
                    go = "Maze.Struct.txt"

    if go != 0:
        background == pygame.image.load(Constants.BACKGROUND).convert()
        game = Maze.Labyrinth(go)
        game.load_from_file()
        game.print_maze(window)

    # Game loop
    while game_loop:

        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_loop = 0
                home_loop = 0

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    first_loop = 0
                    