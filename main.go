// AMOXA - CTCL 2025
// File: main.go
// Purpose: Main game loop
// Created: April 11, 2025
// Modified: April 11, 2025

package main

import (
    "log"

    "github.com/hajimehoshi/ebiten/v2"
    "github.com/hajimehoshi/ebiten/v2/ebitenutil"
)

type Game struct{}

func (g *Game) Update() error {
    return nil
}

func (g *Game) Draw(screen *ebiten.Image) {
    ebitenutil.DebugPrint(screen, "Hello, World!")
    
}

func (g *Game) Layout(outsideWidth, outsideHeight int) (screenWidth, screenHeight int) {
    return 640, 480
}

func main() {
    ebiten.SetWindowSize(640, 480)
    ebiten.SetWindowTitle("Hello, World!")
    if err := ebiten.RunGame(&Game{}); err != nil {
        log.Fatal(err)
    }
}