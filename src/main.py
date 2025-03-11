# PyRPG - CTCL 2025
# File: src/main.py
# Purpose: Main game script
# Created: February 22, 2025
# Modified: March 11, 2025

from pathlib import Path
import pytiled_parser
import pygame
pygame.display.set_mode((640,480), depth = 24, vsync = 1)

clock = pygame.time.Clock()

test_map = pytiled_parser.parse_map(Path("maps/test.tmx"))

print(test_map)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    clock.tick(60)
    pygame.display.flip()