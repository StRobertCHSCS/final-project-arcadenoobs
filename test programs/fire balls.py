import arcade
import os

SCREEM_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'title'

SPEED = 20

class spirit:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, 30, arcade.color.BLACK)

class fire_ball:
    
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
    
    def update(self):
        self.x += self.dx
        self.y += self.dy

class Window(arcade.Window):

    def __init__(self):
        super().__init__(SCREEM_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))
        os.chdir(file_path)
        arcade.set_background_color(arcade.color.WHITE)
        self.spirit = spirit(300, 300)
    
    def set_up(self):
        pass

    def on_draw(self):
        arcade.start_render()
        self.spirit.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            pass

    def on_key_press(self, key, modifiers):
        pass

def main():
    window = Window()
    window.set_up()
    arcade.run()

if __name__ == '__main__':
    main()