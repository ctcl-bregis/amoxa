# PyRPG - CTCL 2025
# File: src/main.py
# Purpose: Main game script
# Created: February 22, 2025
# Modified: March 26, 2025

from pathlib import Path
import pytmx
from pytmx.util_pygame import load_pygame
import pygame
from . import maputils
import random

import logging
logger = logging.Logger
logger.setLevel(logger, level=logging.DEBUG)

game_size = (512,384)
scale = 1

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
    player_pos = cmap.player_start

    anim = 0
    direction = 1
    timer = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        display.blit(maputils.pil2pyg(cmap.image), (0,0))

        if random.random() < 0.001:
            for i in range(random.randint(1, 3)):
                ind1 = 0
                ind2 = 1
                display.blit(randomeffects, (random.randint(0, game_size[0]), random.randint(0, game_size[1])), (ind1 * 8, ind2 * 8, 8, 8))

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            player_pos = (player_pos[0] - dt * 100, player_pos[1])
            direction = 1
        if keys[pygame.K_RIGHT]:
            player_pos = (player_pos[0] + dt * 100, player_pos[1])
            direction = 2
        if keys[pygame.K_UP]:
            player_pos = (player_pos[0], player_pos[1] - dt * 100)
            direction = 3
        if keys[pygame.K_DOWN]:
            player_pos = (player_pos[0], player_pos[1] + dt * 100)
            direction = 0
    
        frame = (anim * 24, direction * 32, 24, 32)
        
        display.blit(player, player_pos, frame)
        
        dt = clock.tick(60) / 1000
        print(dt)

        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
            timer += dt  # Increment the timer.
            if timer >= .1:
                timer = 0  # Reset the timer.
                anim += 1  # Increment the frame index.
                anim %= 4  # Keep the index in the range.
        else:
            anim = 0



        output.blit(pygame.transform.scale(display, output.get_size()), (0,0))
        pygame.display.flip()