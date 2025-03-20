# PyRPG - CTCL 2025
# File: src/main.py
# Purpose: Main game script
# Created: February 22, 2025
# Modified: March 20, 2025

from pathlib import Path
import pytmx
from pytmx.util_pygame import load_pygame
import pygame
from . import maputils

import logging
logger = logging.Logger
logger.setLevel(logger, level=logging.DEBUG)

def main():
    running = True
    display = pygame.display.set_mode((640,480), depth = 24, vsync = 1)
    clock = pygame.time.Clock()

    maps = maputils.loadmaps()

    cmap = maps[0]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for x in range(cmap.tmx.width):
            for y in range(cmap.tmx.height):
                layer = cmap.tmx.layernames["floor"].id
                image = cmap.tmx.get_tile_image(x, y, 0)
                if image:
                    display.blit(image, (x * 32, y * 32))

        keys = pygame.key.get_pressed()
        

        clock.tick(60)
        pygame.display.flip()

