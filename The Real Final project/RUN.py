import Data.Mage.Mage as Mage
import Data.Obs.Obs as Obs
import Data.Monster.Monster1 as Monster
import Data.Chest.Chest as Chest
import arcade
import os
import json
import threading

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'THE CAVE'
lock = threading.Lock()

class Window(arcade.Window):

    def __init__(self, job):
        '''Main class of the game, call this class to start 
        '''
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.abspath(os.path.dirname(__file__))
        os.chdir(file_path)

        arcade.set_background_color(arcade.color.GRAY)

        self.character = Mage.Mage()
        self.obs = Obs.Obstacle()
        self.monster = Monster.Monster()
        self.chest = Chest.Chest()
        self.physics_engine = None
        self.physics_engine2 = None
        self.job = job
        self.refresh_damage = 0
        self.refresh_in_sec = 0
        self.key = 0

    def set_up(self):
        '''initialize everything
        '''
        self.character.setup()
        self.obs.setup()
        self.monster.setup()
        self.chest.setup()

    def on_update(self, delta_time):
        #Refreshing
        if self.refresh_in_sec < 60:
            self.refresh_in_sec += 1
        else:
            self.refresh_in_sec = 0
        if self.refresh_damage < 60:
            self.refresh_damage += 1

        #Characters
        self.character.update()
        self.physics_engine = arcade.PhysicsEngineSimple(self.character.sprite, self.obs.obs_list)
        self.physics_engine.update()

        if self.refresh_damage == 60:
            hit_list = arcade.check_for_collision_with_list(self.character.sprite, self.monster.monster_list)
            if len(hit_list) > 0:
                hurt = 0
                for mon in hit_list:
                    hurt += mon.attack
                self.character.health -= hurt
                self.refresh_damage = 0

        if len(self.chest.chest_list) > 0:
            for c in self.chest.chest_list:
                hit = arcade.check_for_collision(self.character.sprite, c)
                if hit == True and c.type != None:
                    c.health = 0

        if len(self.monster.bullet_list) > 0:
            hit_list = arcade.check_for_collision_with_list(self.character.sprite, self.monster.bullet_list)
            if len(hit_list) > 0:
                for fire in hit_list:
                    self.character.health -= fire.attack
                    fire.remove_from_sprite_lists()

        
        if len(self.chest.drops_list) > 0:
            for d in self.chest.drops_list:
                hit = arcade.check_for_collision(self.character.sprite, d)
                if hit == True:
                    if d.type == 'mana':
                        self.character.mana += 10
                    elif d.type == 'health':
                        self.character.health += 3
                    elif d.type == 'skill1':
                        self.character.skill1 = 1
                    d.remove_from_sprite_lists()

        #Monsters
        self.monster.update(self.character.sprite.center_x, self.character.sprite.center_y)
        for mon in self.monster.monster_list:
            self.physics_engine2 = arcade.PhysicsEngineSimple(mon, self.obs.obs_list)
            self.physics_engine2.update()
        for fire in self.monster.bullet_list:
            hit_list = arcade.check_for_collision_with_list(fire, self.obs.obs_list)
            if len(hit_list) > 0:
                lock.acquire()
                for obs in hit_list:
                    if obs.health < 10000:
                        obs.health -= fire.attack
                        self.obs.color_change(obs.center_x, obs.center_y)
                fire.remove_from_sprite_lists()
                lock.release()

        #Fireballs
        if self.job == 0 and len(self.character.fireball_list) > 0:
            con = 0
            for obs in self.obs.obs_list:
                hit_list = arcade.check_for_collision_with_list(obs, self.character.fireball_list)
                if len(hit_list) > 0:

                    for fireball in hit_list:
                        fireball.remove_from_sprite_lists()
                    if obs.health < 10000:
                        obs.health -= 1
                        self.obs.color_change(obs.center_x, obs.center_y)
                    con = 1
            if con == 0:
                for mon in self.monster.monster_list:
                    hit_list = arcade.check_for_collision_with_list(mon, self.character.fireball_list)
                    if len(hit_list) > 0:
                        for fireball in hit_list:
                            fireball.remove_from_sprite_lists()
                        mon.health -= 1
                        mon.injued = True
                        con = 1
            if con == 0:
                for c in self.chest.chest_list:
                    hit_list = arcade.check_for_collision_with_list(c, self.character.fireball_list)
                    if len(hit_list) > 0:
                        for fireball in hit_list:
                            fireball.remove_from_sprite_lists()
                        if c.type == 'wooden':
                            c.health -= 1
                        con = 1

        #Others
        self.obs.update()
        self.chest.update()
        
    def on_draw(self):
        '''draw everything
        '''
        arcade.start_render()

        self.obs.draw()
        self.chest.draw()
        self.monster.draw()
        self.character.draw()
        
    def on_mouse_press(self, x, y, button, modifiers):
        '''calls everything when mouse buttons are pressed
        '''
        pass
    
    def on_mouse_release(self, x, y, button, modifiers):
        '''calls everything when mouse buttons are released
        '''
        if self.key == 1:
            self.character.skill_1(x, y, self.obs.obs_list)
        else:
            self.character.mouse_release(x, y)

    def on_key_press(self, key, modifiers):
        '''calls everything when keys are pressed
        '''
        if key == arcade.key.ESCAPE:
            arcade.close_window()
        if key == 49 and self.character.skill1 == 1:
            self.key = 1
        else:
            self.character.key_press(key)

    def on_key_release(self, key, modifiers):
        '''calls everything when keys are released
        '''
        if key == 49:
            self.key = 0
        else:
            self.character.key_release(key)

def main():
    '''calls the whole program
    '''
    print('Running as Alpha ver. 1.5')
    print('Good Luck Folks')
    window = Window(0)
    window.set_up()
    arcade.run()

if __name__ == '__main__':
    main()