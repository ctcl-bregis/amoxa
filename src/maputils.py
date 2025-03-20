# PyRPG - CTCL 2025
# File: src/map.py
# Purpose: Provide functions for loading and processing map files
# Created: March 11, 2025
# Modified: March 20, 2025

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
        self.tmx = load_pygame(self.path)

def loadmaps() -> List[GameMap]:
    mapfiles = ["maps/" + f for f in os.listdir("maps/") if f.endswith(".tmx") and os.path.isfile("maps/" + f)]
    maps = [GameMap(m) for m in mapfiles]
    return maps

