import arcade
import os
import _thread

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'title'

def draw_text():
    arcade.draw_circle_filled(300, 200, 20, arcade.color.GREEN)

class Window(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))
        os.chdir(file_path)
        arcade.set_background_color(arcade.color.WHITE)

        self.text = 0
    
    def set_up(self):
        self.text = 1

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        arcade.start_render()
        
        arcade.draw_circle_filled(300, 300, 20, arcade.color.BLACK)
        if self.text == 1:
            draw_text()


    def on_mouse_press(self, x, y, button, modifiers):
        self.text = 0

    def on_key_press(self, key, modifiers):
        pass



def main():
    window = Window()
    window.set_up()
    arcade.run()

if __name__ == '__main__':
    main()