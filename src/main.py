import pyglet
from pyglet import shapes
import tetris

tetrisApp = tetris.Game()
window = pyglet.window.Window(width=540,height=720)
pyglet.gl.glClearColor(0.3, 0.8, 0.5, 1.0)

@window.event
def on_key_press(symbols, modifiers):
    if symbols == pyglet.window.key.LEFT:
        tetrisApp.dx = -1
    if symbols == pyglet.window.key.RIGHT:
        tetrisApp.dx = 1
    if symbols == pyglet.window.key.DOWN:
        tetrisApp.dy = 1
    if symbols == pyglet.window.key.UP:
        tetrisApp.is_rotate = True

@window.event
def on_draw():
    window.clear()
    batch = pyglet.graphics.Batch()
    square = shapes.Rectangle(20, 20, 320, 640, color=(0, 0, 0), batch=batch)
    rectangles = []
    tetrisApp.update()
    for y,row in enumerate(reversed(tetrisApp.board.grid)):
        for x,grid in enumerate(row):
            if grid == 1:
                rect = shapes.Rectangle(20+x*32, 20+y*32, 31, 31, color=(255, 255, 255), batch=batch)
                rectangles.append(rect)
    
    batch.draw()
pyglet.app.run()