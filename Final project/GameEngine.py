import arcade
import os
import Resource.Engine.chr as chr
import Resource.Obstacles.Main as OMain

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'title'

class Window(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))
        os.chdir(file_path)
        arcade.set_background_color(arcade.color.WHITE)

        self.character = chr.Main(600, 600)
        self.obstacles = None
        self.mouse_x = 0
        self.mouse_y = 0

    def set_up(self):
        self.obstacles = OMain.Obstacles([[400, 400, 20, 0], [200, 200, 20, 1]])

    def on_update(self, delta_time):
        arcade.set_viewport(self.character.spirit.position_x - SCREEN_WIDTH/2 - 1, self.character.spirit.position_x + SCREEN_WIDTH/2 - 1, self.character.spirit.position_y - SCREEN_HEIGHT/2, self.character.spirit.position_y + SCREEN_HEIGHT/2 - 1)
        self.character.update()
        self.obstacles.update()

    def on_draw(self):
        arcade.start_render()

        self.obstacles.draw()
        self.character.draw()


    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_key_press(self, key, modifiers):
        self.character.on_key_press(key)
        if key == arcade.key.SPACE:
            self.obstacles.make_a_object(round(self.character.spirit.position_x, -1), round(self.character.spirit.position_y, -1), 20, 1)
    
    def on_key_release(self, key, modifiers):
        self.character.on_key_release(key)

def main():
    window = Window()
    window.set_up()
    arcade.run()

if __name__ == '__main__':
    main()