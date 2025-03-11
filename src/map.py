# PyRPG - CTCL 2025
# File: src/map.py
# Purpose: Provide functions for loading and processing map files
# Created: March 11, 2025
# Modified: March 11, 2025

import os

class Map: 
    def __init__(self, path):
        self.path = path

def loadmaps():
    mapfiles = [f for f in os.listdir("maps/") if f.endswith(".tmx") and os.path.isfile("maps/" + f)]
    maps = [Map(m) for m in mapfiles]
    return maps

