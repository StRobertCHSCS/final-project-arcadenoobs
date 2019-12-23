import Resource.Mage.Main as MMain
import Resource.Warrior.Main as WMain
import arcade
import os

SCREEM_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'MyGame'


class Window(arcade.Window):

    def __init__(self, character):
        super().__init__(SCREEM_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.abspath(os.path.dirname(__file__))
        os.chdir(file_path)
        arcade.set_background_color(arcade.color.WHITE)

        if character == 'mage':
            self.character = MMain.Mage(SCREEM_WIDTH, SCREEN_HEIGHT)
        elif character == 'warrior':
            self.character = WMain.Warrior(SCREEM_WIDTH, SCREEN_HEIGHT)
    
    def set_up(self):
        pass

    def on_update(self, delta_time):
        self.character.update()

    def on_draw(self):
        arcade.start_render()

        self.character.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        self.character.on_mouse_press(x, y, button)
    
    def on_mouse_release(self, x, y, button, modifiers):
        self.character.on_mouse_release(x, y, button)

    def on_key_press(self, key, modifiers):
        self.character.on_key_press(key)

    def on_key_release(self, key, modifiers):
        self.character.on_key_release(key)

def main():
    character = input('Which character do you want to play: input mage or warrior')
    window = Window(character)
    window.set_up()
    arcade.run()

if __name__ == '__main__':
    main()