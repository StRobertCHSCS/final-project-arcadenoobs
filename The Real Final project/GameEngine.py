import Data.Engine.Creator as Creator
import Data.Mage.Mage as Mage
import Data.Obs.Obs as Obs
import Data.Monster.Monster1 as Monster
import Data.Chest.Chest as Chest
import arcade
import os
import json

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Engine of the Cave'


class Window(arcade.Window):

    def __init__(self):
        '''Main class of the game, call this class to start 
        '''
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.abspath(os.path.dirname(__file__))
        os.chdir(file_path)

        arcade.set_background_color(arcade.color.WHITE)
        self.character = Creator.Main()
        self.obs = Obs.Obstacle()
        self.monster = Monster.Monster()
        self.chest = Chest.Chest()
        self.physics_engine = None
        self.type = 0

    def set_up(self):
        '''initialize everything
        '''
        self.character.setup()
        self.obs.setup()
        self.monster.setup()
        self.chest.setup()

        self.spawnpoint = arcade.load_texture('Data/Engine/Textures/Spawnpoint.png', scale=1)
        self.cracked_stone = arcade.load_texture('Data/Obs/Textures/Cracked Stone.png', scale=2)
        self.stone = arcade.load_texture('Data/Obs/Textures/Stone.png')
        self.slime = arcade.load_texture('Data/Monster/Textures/Slime.png')
        self.wooden_chest = arcade.load_texture('Data/Chest/Textures/Wooden Chest.png', scale=2)
        self.ghost = arcade.load_texture('Data/Monster/Textures/Ghost.png')
        self.biggyslime = arcade.load_texture('Data/Monster/Textures/BiggySlime.png')
        self.iceslime = arcade.load_texture('Data/Monster/Textures/IceSlime.png')

    def on_update(self, delta_time):
        '''update everything
        '''
        self.character.update()

    def on_draw(self):
        '''draw everything
        '''
        arcade.start_render()
        self.obs.draw()
        self.character.draw()
        self.monster.draw()
        self.chest.draw()

        if self.type == 0:
            arcade.draw_texture_rectangle(self.character.sprite.center_x + 280, self.character.sprite.center_y, self.stone.width*2, self.stone.height*2, self.stone)
        elif self.type == 1:
            arcade.draw_texture_rectangle(self.character.sprite.center_x + 280, self.character.sprite.center_y, self.cracked_stone.width*2, self.cracked_stone.height*2, self.cracked_stone)
        elif self.type == 2:
            arcade.draw_texture_rectangle(self.character.sprite.center_x + 280, self.character.sprite.center_y, self.spawnpoint.width, self.spawnpoint.height, self.spawnpoint)
        elif self.type == 3:
            arcade.draw_texture_rectangle(self.character.sprite.center_x + 280, self.character.sprite.center_y, self.slime.width, self.slime.height, self.slime)
        elif self.type == 4:
            arcade.draw_texture_rectangle(self.character.sprite.center_x + 280, self.character.sprite.center_y, self.ghost.width, self.ghost.height, self.ghost)
        elif self.type == 5:
            arcade.draw_texture_rectangle(self.character.sprite.center_x + 280, self.character.sprite.center_y, self.biggyslime.width, self.biggyslime.height, self.biggyslime)
        elif self.type == 6:
            arcade.draw_texture_rectangle(self.character.sprite.center_x + 280, self.character.sprite.center_y, self.iceslime.width, self.iceslime.height, self.iceslime)
        elif self.type == 7:
            arcade.draw_texture_rectangle(self.character.sprite.center_x + 280, self.character.sprite.center_y, self.wooden_chest.width*2, self.wooden_chest.height*2, self.wooden_chest)


    def on_mouse_press(self, x, y, button, modifiers):
        '''calls everything when mouse buttons are pressed
        '''
        pass
    
    def on_mouse_release(self, x, y, button, modifiers):
        '''calls everything when mouse buttons are released
        '''
        pass

    def on_key_press(self, key, modifiers):
        '''calls everything when keys are pressed
        '''
        self.character.key_press(key)

        if key == arcade.key.SPACE:
            if self.type == 0 or self.type == 1:
                self.obs.key_press(key, round(self.character.sprite.center_x, -1), round(self.character.sprite.center_y, -1), self.type)
            elif self.type == 2:
                self.character.renew_spawnpoint(round(self.character.sprite.center_x, -1), round(self.character.sprite.center_y, -1))
            elif self.type == 3 or 4 or 5 or 6:
                self.monster.key_press(key, round(self.character.sprite.center_x, -1), round(self.character.sprite.center_y, -1), self.type)
            elif self.type == 7:
                self.chest.key_press(key, round(self.character.sprite.center_x, -1), round(self.character.sprite.center_y, -1), self.type)

        elif key == arcade.key.E:
            if self.obs.delete(self.character.sprite.center_x, self.character.sprite.center_y):
                pass
            elif self.monster.delete(self.character.sprite.center_x, self.character.sprite.center_y):
                pass
            elif self.chest.delete(self.character.sprite.center_x, self.character.sprite.center_y):
                pass
            
        if key == arcade.key.R:
            if self.type <= 6:
                self.type += 1
            else:
                self.type = 0

        if key == arcade.key.L:
            self.obs.save()
            self.character.save()
            self.monster.save()
            self.chest.save()

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