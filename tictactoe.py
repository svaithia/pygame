#!/usr/bin/env python

import pygame, sys
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

w = 640
h = 480
screen = pygame.display.set_mode((w,h))

while True:
   clock.tick(60)
   pygame.display.update()
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

