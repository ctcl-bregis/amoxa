# PyRPG - CTCL 2025
# File: src/map.py
# Purpose: Provide functions for loading and processing map files
# Created: March 11, 2025
# Modified: March 12, 2025

import os
import pytiled_parser 
import pathlib
from PIL import Image, ImageDraw

class Tileset:
    def __init__(self, path):
        self.path = pathlib.Path(path)
        self.tsx = pytiled_parser.parse_tileset(self.path)
        print(self.tsx.properties())


class Map: 
    def __init__(self, path):
        self.path = pathlib.Path(path)
        self.tmx = pytiled_parser.parse_map(self.path)
        
        mapsize = (self.tmx.tile_size[0] * self.tmx.map_size[0], self.tmx.tile_size[1] * self.tmx.map_size[1])
        im = Image.new("RGBA", mapsize, color = (0,0,0,0))
        draw = ImageDraw(im)

def loadtilesets():
    tsfiles = ["assets/tiles/" + f for f in os.listdir("maps/") if f.endswith(".tsx") and os.path.isfile("maps/" + f)]
    tilesets = [Tileset(t) for t in tsfiles]
    return tilesets

def loadmaps():
    mapfiles = ["maps/" + f for f in os.listdir("maps/") if f.endswith(".tmx") and os.path.isfile("maps/" + f)]
    maps = [Map(m) for m in mapfiles]
    return maps

