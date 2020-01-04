import Data.Mage.Mage as Mage
import Data.Obs.Obs as Obs
import arcade
import os
import json

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'MyGame'


class Window(arcade.Window):

    def __init__(self):
        '''Main class of the game, call this class to start 
        '''
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.abspath(os.path.dirname(__file__))
        os.chdir(file_path)

        arcade.set_background_color(arcade.color.GRAY)

        
        self.character = Mage.Mage()
        self.obs = Obs.Obstacle()
        self.physics_engine = None

    def set_up(self):
        '''initialize everything
        '''
        self.character.setup()
        self.obs.setup()

    def on_update(self, delta_time):
        '''update everything
        '''
        self.character.update()
        self.physics_engine = arcade.PhysicsEngineSimple(self.character.sprite, self.obs.obs_list)
        self.physics_engine.update()
        
        for obs in self.obs.obs_list:
            hit_list = arcade.check_for_collision_with_list(obs, self.character.fireball_list)
            if len(hit_list) > 0:
                for fireball in hit_list:
                    fireball.remove_from_sprite_lists()
                obs.health -= 1
        self.obs.update()

    def on_draw(self):
        '''draw everything
        '''
        arcade.start_render()

        self.obs.draw()
        self.character.draw()
        
    def on_mouse_press(self, x, y, button, modifiers):
        '''calls everything when mouse buttons are pressed
        '''
        pass
    
    def on_mouse_release(self, x, y, button, modifiers):
        '''calls everything when mouse buttons are released
        '''
        self.character.mouse_release(x, y)

    def on_key_press(self, key, modifiers):
        '''calls everything when keys are pressed
        '''
        self.character.key_press(key)

    def on_key_release(self, key, modifiers):
        '''calls everything when keys are released
        '''
        self.character.key_release(key)

def main():
    '''calls the whole program
    '''
    window = Window()
    window.set_up()
    arcade.run()

if __name__ == '__main__':
    main()