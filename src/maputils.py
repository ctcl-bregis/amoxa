# PyRPG - CTCL 2025
# File: src/map.py
# Purpose: Provide functions for loading and processing map files
# Created: March 11, 2025
# Modified: March 21, 2025

import os
import pytmx 
from pytmx.util_pygame import load_pygame
import pathlib
from PIL import Image, ImageDraw
from typing import List
import pygame

# Apparently naming this "Map" clobbers something else?
class GameMap:
    def __init__(self, path):
        self.path = pathlib.Path(path)
        self.tmx = pytmx.TiledMap("maps/test.tmx")

        mapimage = Image.new("RGBA", (self.tmx.width * 32, self.tmx.height * 32))

        for x in range(self.tmx.width):
            for y in range(self.tmx.height):
                layer = self.tmx.layernames["floor"].id
                tile = self.tmx.get_tile_image(x, y, 0)

                x1 = tile[1][0]
                y1 = tile[1][1]
                x2 = tile[1][0] + tile[1][2]
                y2 = tile[1][1] + tile[1][3]

                image = Image.open(tile[0]).crop((x1, y1, x2, y2))

                if image:
                    pos = (x * 32, y * 32, (x + 1) * 32, (y + 1) * 32)
                    mapimage.paste(image, pos)

        self.image = mapimage

def pil2pyg(image) -> pygame.Surface:
    return pygame.image.fromstring(image.tobytes(), image.size, image.mode).convert()

def loadmaps() -> List[GameMap]:
    mapfiles = ["maps/" + f for f in os.listdir("maps/") if f.endswith(".tmx") and os.path.isfile("maps/" + f)]
    maps = [GameMap(m) for m in mapfiles]
    return maps

