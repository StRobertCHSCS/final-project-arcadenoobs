import arcade
import os

SCREEM_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'title'

class Window(arcade.Window):

    def __init__(self):
        super().__init__(SCREEM_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))
        os.chdir(file_path)
        arcade.set_background_color(arcade.color.WHITE)
    
    def set_up(self):
        pass

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        arcade.start_render()
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_key_press(self, key, modifiers):
        pass

def main():
    window = Window()
    window.set_up()
    arcade.run()

if __name__ == '__main__':
    main()