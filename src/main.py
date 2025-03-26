# PyRPG - CTCL 2025
# File: src/main.py
# Purpose: Main game script
# Created: February 22, 2025
# Modified: March 24, 2025

from pathlib import Path
import pytmx
from pytmx.util_pygame import load_pygame
import pygame
from . import maputils
import random

import logging
logger = logging.Logger
logger.setLevel(logger, level=logging.DEBUG)

game_size = (320,256)
scale = 2

output = pygame.display.set_mode((game_size[0] * scale, game_size[1] * scale), depth = 24, vsync = 1)

def main():
    # According the docs, this may use /dev/urandom when its available
    random.seed()

    running = True
    display = pygame.Surface(game_size)
    clock = pygame.time.Clock()

    maps = maputils.loadmaps()
    cmap = maps[0]

    randomeffects = pygame.image.load("assets/particles/hppd8x8.png")

    player = pygame.image.load("assets/player/p1.png")

    # TODO: Get location of object with "info_player_start" class and use that as the starting point
    #player_pos =

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        display.blit(maputils.pil2pyg(cmap.image), (0,0))

        if random.random() < 0.005:
            ind1 = random.randint(0, 3)
            ind2 = random.randint(0, 3)
            display.blit(randomeffects, (random.randint(0, 640), random.randint(0, 480)), (ind1 * 8, ind2 * 8, 8, 8))

        #display.blit(player, (0,0))

        keys = pygame.key.get_pressed()
        

        clock.tick(60)
        output.blit(pygame.transform.scale(display, output.get_size()), (0,0))
        pygame.display.flip()

