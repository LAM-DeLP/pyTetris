import pyglet
import tetris

window = pyglet.window.Window(width=400,height=300)
pyglet.gl.glClearColor(0.3, 0.8, 0.5, 1.0)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.LEFT:
        print("左キーが押されました")
    elif symbol == pyglet.window.key.RIGHT:
        print("右キーが押されました")
    else:
        pass
@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == pyglet.window.mouse.LEFT or pyglet.window.mouse.RIGHT:
        print(f"マウスボタンが({x}, {y})で押されました")

pyglet.app.run()