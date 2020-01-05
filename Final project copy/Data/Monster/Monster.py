import arcade
import math
import json

class Slime(arcade.Sprite):

    def __init__(self, filename, health):
        super().__init__(filename)
        self.health = health
        self.type = 'slime'

class Monster:

    def __init__(self):
        self.monster_list = None
        self.injued_list = None
        self.actived_list = None
        self.slime = None

    def setup(self):
        self.monster_list = arcade.SpriteList()
        self.injued_list = arcade.SpriteList()
        self.actived_list = arcade.SpriteList()

        slime = open('Data/Map/Slime.json')
        data = json.load(slime)
        for dict in data:
            s = Slime('Data/Monster/Textures/Slime.png', 0)
            s.center_x = dict['x']
            s.center_y = dict['y']
            s.health = dict['h']
            self.monster_list.append(s)

    def draw(self):
        if len(self.monster_list) > 0:
            self.monster_list.draw()
        if len(self.actived_list) > 0:
            self.actived_list.draw()
        if len(self.injued_list) >= 0:
            self.injued_list.draw()
            for i in self.injued_list:
                i.remove_from_sprite_lists()

    def update(self, x, y):
        for mon in self.monster_list:
            if abs(mon.center_x - x) < 300 and abs(mon.center_y - y) < 300:
                if mon.type == 'slime':
                    s = Slime('Data/Monster/Textures/Slime.png', 0)
                    s.center_x = mon.center_x
                    s.center_y = mon.center_y
                    s.health = mon.health
                    self.actived_list.append(s)
                mon.remove_from_sprite_lists()

        for mon in self.actived_list:
            if abs(mon.center_x - x) > 300 and abs(mon.center_y - y) > 300:
                if mon.type == 'slime':
                    s = Slime('Data/Monster/Textures/Slime.png', 0)
                    s.center_x = mon.center_x
                    s.center_y = mon.center_y
                    s.health = mon.health
                    self.monster_list.append(s)
                mon.remove_from_sprite_lists()

        for mon in self.actived_list:
            if mon.health == 0:
                mon.remove_from_sprite_lists()

    def path_update(self, mon, x, y, collision):
        if mon.type == 'slime':
            speed = 1.5
            if abs(mon.center_x - x) > 20 and abs(mon.center_y - y) > 20:
                if abs(mon.center_x - x) > abs(mon.center_y - y) and abs(mon.center_x - x) > 20 and collision == False:
                    if mon.center_x > x:
                        mon.change_x = -speed
                    else:
                        mon.change_x = speed
                else:
                    if abs(mon.center_y - y) > 20:
                        if mon.center_y > y:
                            mon.change_y = -speed
                        else:
                            mon.change_y = speed
            elif abs(mon.center_x - x) < 20 and abs(mon.center_y - y) < 20:
                mon.change_x = 0
                mon.change_y = 0
                        
    def key_press(self, key, x, y, type):
        if type == 3:
            s = Slime('Data/Monster/Textures/Slime.png', 0)
            s.center_x = x
            s.center_y = y
            s.health = 3
            self.monster_list.append(s)

    def color_change(self, x, y):
        n = arcade.Sprite('Data/Monster/Textures/Slime1.png')
        n.center_x = x
        n.center_y = y
        self.injued_list.append(n)
    
    def save(self):
        with open('Data/Map/Slime.json', 'w+') as f:
            list = []
            for mon in self.monster_list:
                if mon.type == 'slime':
                    s = {"x": mon.center_x, "y": mon.center_y, "h": mon.health}
                    list.append(s)
            j = json.dump(list, f, ensure_ascii=False)
        print('Monsters Saved')
        
    def delete(self, x, y):
        for mon in self.monster_list:
            if round(x, -1) == mon.center_x and round(y, -1) == mon.center_y:
                mon.remove_from_sprite_lists()
                return 'pass'
