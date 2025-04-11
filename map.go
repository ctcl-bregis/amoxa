// AMOXA - CTCL 2025
// File: map.go
// Purpose: Map utilities
// Created: April 11, 2025
// Modified: April 11, 2025

package main

import (
    "fmt"
    "os"

    "github.com/lafriks/go-tiled"
    "github.com/lafriks/go-tiled/render"
)

const mapPath = "maps/test.tmx"

func loadmap() {
    gameMap, err := tiled.LoadFile(mapPath)
    if err != nil {
        fmt.Printf("error parsing map: %s", err.Error())
        os.Exit(2)
    }

    fmt.Println(gameMap)

    renderer, err := render.NewRenderer(gameMap)
    if err != nil {
        fmt.Printf("map unsupported for rendering: %s", err.Error())
        os.Exit(2)
    }

    err = renderer.RenderLayer(0)
    if err != nil {
        fmt.Printf("layer unsupported for rendering: %s", err.Error())
        os.Exit(2)
    }

    img := renderer.Result

    renderer.Clear()
}