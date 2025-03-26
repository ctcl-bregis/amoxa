# Temporary file to come up with a way to pre-render maps

import pytmx
from PIL import Image, ImageDraw

def loadmap():
    tmx = pytmx.TiledMap("maps/test.tmx")

    mapimage = Image.new("RGBA", (tmx.width * 32, tmx.height * 32))

    for x in range(tmx.width):
        for y in range(tmx.height):
            layer = tmx.layernames["floor"].id
            tile = tmx.get_tile_image(x, y, 0)

            x1 = tile[1][0]
            y1 = tile[1][1]
            x2 = tile[1][0] + tile[1][2]
            y2 = tile[1][1] + tile[1][3]

            image = Image.open(tile[0]).crop((x1, y1, x2, y2))

            if image:
                pos = (x * 32, y * 32, (x + 1) * 32, (y + 1) * 32)
                mapimage.paste(image, pos)

    mapimage.show()

if __name__ == "__main__":
    loadmap()