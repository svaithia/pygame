#!/usr/bin/env python

import pygame, sys
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

w = 450
h = 680

class Graphics:
    i_bg = pygame.image.load('images/bg.png')
    def buildMainScreen(self):
        main_screen = pygame.display.set_mode((w,h))
        i_title = pygame.image.load('images/ttt_main.png')
        i_play = pygame.image.load('images/play.png')
        i_help = pygame.image.load('images/help.png')
        i_about = pygame.image.load('images/about.png')

        main_screen.blit(self.i_bg, (0,0))
        main_screen.blit(i_title, (35,60))
        main_screen.blit(i_play, (42,320))
        main_screen.blit(i_help, (42, 400))
        main_screen.blit(i_about, (112, 490))

    def buildGameScreen(self):
        i_gtitle = pygame.image.load('images/ttt_title.png')
        i_board = pygame.image.load('images/board.png')
        i_score = pygame.image.load('images/scoreboard.png')
        i_nav = pygame.image.load('images/nav.png')

        game_screen = pygame.display.set_mode((w,h))
        game_screen.blit(self.i_bg, (0,0))
        game_screen.blit(i_gtitle, (30,60))
        game_screen.blit(i_board, (20, 120))
        game_screen.blit(i_score, (55, 540))
        game_screen.blit(i_nav, (35, 610))
    
    screen = 0

graph = Graphics()
while True:
   clock.tick(60) 
   if graph.screen==1:
        graph.buildGameScreen()
   elif graph.screen==0:
        graph.buildMainScreen() 
   pygame.display.update()

   for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
            sys.exit() 
        elif event.type == KEYDOWN and event.key == K_p:
            graph.screen = 1
        elif event.type == KEYDOWN and event.key == K_b:
            graph.screen = 0
