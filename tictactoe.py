#!/usr/bin/env python

import pygame, sys
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

w = 450
h = 680

class Graphics:
    screen = 0
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
        l_xy = [(45,130),(155,130), (270,130), (45,270), (155,270), (270,270), (45,410), (155,410),(270,410)]
        i_gtitle = pygame.image.load('images/ttt_title.png')
        i_board = pygame.image.load('images/board.png')
        i_score = pygame.image.load('images/scoreboard.png')
        i_nav = pygame.image.load('images/nav.png')

        i_X = pygame.image.load('images/X.png')
        i_O = pygame.image.load('images/O.png')

        game_screen = pygame.display.set_mode((w,h))
        game_screen.blit(self.i_bg, (0,0))
        game_screen.blit(i_gtitle, (30,60))
        game_screen.blit(i_board, (20, 120))
        game_screen.blit(i_score, (55, 540))
        game_screen.blit(i_nav, (35, 610))
        
        game_screen.blit(i_X, l_xy[0])
        game_screen.blit(i_X, l_xy[1])
        game_screen.blit(i_X, l_xy[2])
        game_screen.blit(i_X, l_xy[3])
        game_screen.blit(i_X, l_xy[4])
        game_screen.blit(i_X, l_xy[5])
        game_screen.blit(i_X, l_xy[6])
        game_screen.blit(i_X, l_xy[7])
        game_screen.blit(i_X, l_xy[8])

class Calc:
    bv = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    moves = 0
    history = [] # stores position of moves

    def __init__(self, graphics):
        self.graphics = graphics

    def makeMove(self, pos, letter):
        self.bv[pos-1] = letter
        self.moves += 1
        history.append(pos)

    def getLetter(self, pos):
        return self.bv[pos-1]

    def undoMove(self):
        self.makeMove(self, history.pop(), ' ')
        self.moves -= 2

    def getCompletedMoves(self):
        return self.moves

    def whoWon(self):
        for i in (1,4,7):
            if(self.getLetter(i) == self.getLetter(i+1) and self.getLetter(i) == self.getLetter(i+2)):
                if(self.getLetter(i) == 'X' or self.getLetter(i) == 'O'):
                    return self.getLetter(i)
        for i in (1,2,3):
            if(self.getLetter(i) == self.getLetter(i+3) and self.getLetter(i) == self.getLetter(i+6)):
                if(self.getLetter(i) == 'X' or self.getLetter(i) == 'O'):
                    return self.getLetter(i)
        if (self.getLetter(1) == self.getLetter(5) and self.getLetter(1) == self.getLetter(9)):
            if(self.getLetter(1) == 'X' or self.getLetter(1) == 'O'):
                return self.getLetter(1)
        elif (self.getLetter(3) == self.getLetter(5) and self.getLetter(3) == self.getLetter(7)):
            if(self.getLetter(1) == 'X' or self.getLetter(i) == 'O'):
                return self.getLetter(1)
        elif(self.moves < 9):
            return 'n' # keep going
        else:
            return 't' # tie

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
