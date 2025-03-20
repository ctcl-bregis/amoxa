# PyRPG - CTCL 2025
# File: src/main.py
# Purpose: Main game script
# Created: February 22, 2025
# Modified: March 20, 2025

from pathlib import Path
import pytmx
import pygame
from . import maputils

import logging
logger = logging.Logger
logger.setLevel(logger, level=logging.DEBUG)

def main():
    maps = maputils.loadmaps()
    
    running = True
    display = pygame.display.set_mode((640,480), depth = 24, vsync = 1)
    clock = pygame.time.Clock()

    cmap = maps[0]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for x in range(cmap.tmx.width):
            for y in range(cmap.tmx.height):
                image = tmx_data.get_tile_image(x, y, "floor")

        clock.tick(60)
        pygame.display.flip()

