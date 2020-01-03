import Resource.Mage.Main as MMain
import Resource.Warrior.Main as WMain
import Resource.Obstacles.Main as OMain
import Resource.Functions.Collisions as FCollision
import arcade
import os
import json

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'MyGame'


class Window(arcade.Window):

    def __init__(self, character):
        '''Main class of the game, call this class to start 
        '''
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.abspath(os.path.dirname(__file__))
        os.chdir(file_path)
        arcade.set_background_color(arcade.color.WHITE)

        if character == 'mage':
            self.character = MMain.Mage(SCREEN_WIDTH, SCREEN_HEIGHT)
        elif character == 'warrior':
            self.character = WMain.Warrior(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.obstacles = OMain.Obstacles()
        self.file = None
        self.data = None
        self.key = None
    
    def set_up(self):
        '''initialize everything
        '''
        self.file = open('Resource/Map/Obs.json')
        self.data = json.load(self.file)
        for dict in self.data:
            object = [dict['x'], dict['y'], dict['r'], dict['t']]
            self.obstacles.obstacles1_list.append(OMain.make_obstacles(object))

    def on_update(self, delta_time):
        '''update everything
        '''
        arcade.set_viewport(self.character.spirit.position_x - SCREEN_WIDTH/2 - 1, self.character.spirit.position_x + SCREEN_WIDTH/2 - 1, self.character.spirit.position_y - SCREEN_HEIGHT/2, self.character.spirit.position_y + SCREEN_HEIGHT/2 - 1)
        self.character.update()
        self.obstacles.update()
        FCollision.square_collision(self.key, self.character.spirit, self.obstacles.obstacles1_list)
        FCollision.fire_ball_collision(self.character.fire_ball_list, self.obstacles.obstacles1_list)

    def on_draw(self):
        '''draw everything
        '''
        arcade.start_render()

        self.character.draw()
        self.obstacles.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        '''calls everything when mouse buttons are pressed
        '''
        self.character.on_mouse_press(x, y, button)
    
    def on_mouse_release(self, x, y, button, modifiers):
        '''calls everything when mouse buttons are released
        '''
        self.character.on_mouse_release(x, y, button)

    def on_key_press(self, key, modifiers):
        '''calls everything when keys are pressed
        '''
        self.key = key
        self.character.on_key_press(key)

    def on_key_release(self, key, modifiers):
        '''calls everything when keys are released
        '''
        self.character.on_key_release(key)

def main():
    '''calls the whole program
    '''
    character = input('Which character do you want to play: input mage or warrior')
    window = Window(character)
    window.set_up()
    arcade.run()

if __name__ == '__main__':
    main()