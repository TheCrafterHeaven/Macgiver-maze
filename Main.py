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
import Macgiver

pygame.init()

# Opening pygame window with sizes (width, height)
window = pygame.display.set_mode((Constants.WINDOW_DIM, 75 + Constants.WINDOW_DIM))

icon = pygame.image.load(Constants.MACGIVER_PICTURE)
pygame.display.set_icon(icon)

# Title
pygame.display.set_caption(Constants.WINDOW_TITLE)

# First loop
first_loop = 1
while first_loop:
    # loading the home screen
    home = pygame.image.load(Constants.HOME_PICTURE).convert()
    score_background = pygame.image.load(Constants.SCORE_BACKGROUND).convert()
    window.blit(home, (0, 0))
    window.blit(score_background, (0, Constants.WINDOW_DIM))

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
                    go = "Maze_Struct.txt"

    if go != 0:
        # loading the background
        background = pygame.image.load(Constants.BACKGROUND).convert()

        # Loading the maze
        env = Maze.Labyrinth(go)
        env.load_from_file()
        env.items()
        env.print_maze(window)

        # Loading Macgiver
        mg = Macgiver.Hero(env)

    # Game loop
    while game_loop:

        pygame.time.Clock().tick(30)
        # refresh window
        window.blit(background, (0, 0))
        window.blit(score_background, (0, Constants.WINDOW_DIM))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_loop = 0
                home_loop = 0

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    first_loop = 0
                # Command to move Macgiver
                elif event.key == pygame.K_RIGHT:
                    mg.move(env, 'right')
                elif event.key == pygame.K_LEFT:
                    mg.move(env, 'left')
                elif event.key == pygame.K_UP:
                    mg.move(env, 'up')
                elif event.key == pygame.K_DOWN:
                    mg.move(env, 'down')

            # to print the number of items pick up
            score_font = pygame.font.SysFont("monospace", 28, bold=True)
            print_score = score_font.render\
                ("You have " + str(env.score) + " item(s) in your pocket", 1, (255, 255, 255))
            window.blit(print_score, (20, 620))

            # print the window
            env.print_maze(window)
            # print the hero
            window.blit(mg.picture, (mg.x, mg.y))
            pygame.display.flip()

            if env.structure[mg.sprite_y][mg.sprite_x] == 'F' and env.score == 3:
                win_screen = 1
                while win_screen:
                    game_loop = 0
                    win = pygame.image.load(Constants.WIN_PICTURE).convert()
                    window.blit(win, (0, 0))
                    # Refreshments
                    pygame.display.flip()

                    for evt in pygame.event.get():
                        if evt.type == pygame.KEYDOWN:
                            # If the user press Esc here, we just go back to the menu
                            if evt.key == pygame.K_ESCAPE:
                                win_screen = 0
                                home_loop = 1
                            if evt.key == pygame.QUIT:
                                win_screen = 0
                                first_loop = 0
                                home_loop = 0

            elif env.structure[mg.sprite_y][mg.sprite_x] == 'F' and env.score < 3:

                lose_screen = 1
                while lose_screen:
                    game_loop = 0
                    win = pygame.image.load(Constants.LOSE_PICTURE).convert()
                    window.blit(win, (0, 0))
                    # Refreshments
                    pygame.display.flip()

                    for elt in pygame.event.get():
                        if elt.type == pygame.KEYDOWN:
                            # If the user press Esc here, we just go back to the menu
                            if elt.key == pygame.K_ESCAPE:
                                lose_screen = 0
                                first_loop = 1
                                home_loop = 1
                            if elt.key == pygame.QUIT:
                                lose_screen = 0
                                home_loop = 0
                                first_loop = 0
