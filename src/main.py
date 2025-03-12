# PyRPG - CTCL 2025
# File: src/main.py
# Purpose: Main game script
# Created: February 22, 2025
# Modified: March 11, 2025

from pathlib import Path
import pytiled_parser
import pygame
from . import maputils

import logging
logger = logging.Logger
logger.setLevel(logger, level=logging.DEBUG)

def main():
    maputils.loadmaps()
    
    running = True
    pygame.display.set_mode((640,480), depth = 24, vsync = 1)
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        clock.tick(60)
        pygame.display.flip()

