import arcade
import json

class Stone(arcade.Sprite):

    def __init__(self, filename):
        super().__init__(filename, 2)
        self.health = 999999

class Cracked_Stone(arcade.Sprite):

    def __init__(self, filename, health):
        super().__init__(filename, 2)
        self.health = health


class Obstacle:

    def __init__(self):
        self.obs_list = None

    def setup(self):
        self.obs_list = arcade.SpriteList()

        stone = open('Data/Map/Stone.json')
        data = json.load(stone)
        for dict in data:
            s = Stone('Data/Obs/Textures/Stone.png')
            s.center_x = dict['x']
            s.center_y = dict['y']
            self.obs_list.append(s)
        cracked_Stone = open('Data/Map/Cracked Stone.json')
        data = json.load(cracked_Stone)
        for dict in data:
            s = Cracked_Stone('Data/Obs/Textures/Cracked Stone.png', 0)
            s.center_x = dict['x']
            s.center_y = dict['y']
            s.health = dict['h']
            self.obs_list.append(s)

    def draw(self):
        self.obs_list.draw()
    
    def update(self):
        for obs in self.obs_list:
            if obs.health == 0:
                obs.remove_from_sprite_lists()
    
    def key_press(self, key, x, y, type):
        if type == 0:
            s = Stone('Data/Obs/Textures/Stone.png')
            s.center_x = x
            s.center_y = y
            self.obs_list.append(s)
        elif type == 1:
            s = Cracked_Stone('Data/Obs/Textures/Cracked Stone.png', 0)
            s.center_x = x
            s.center_y = y
            s.health = 5
            self.obs_list.append(s)
    
    def save(self):
        with open('Data/Map/Cracked Stone.json', 'w+') as f:
            list = []
            for obs in self.obs_list:
                if obs.health < 10000:
                    s = {"x": obs.center_x, "y": obs.center_y, "h": obs.health}
                    list.append(s)
            j = json.dump(list, f, ensure_ascii=False)
        with open('Data/Map/Stone.json', 'w+') as f:
            list = []
            for obs in self.obs_list:
                if obs.health > 10000:
                    s = {"x": obs.center_x, "y": obs.center_y}
                    list.append(s)
            j = json.dump(list, f, ensure_ascii=False)
        print('Obs Saved')
    
    def delete(self, x, y):
        for obs in self.obs_list:
            if round(x, -1) == obs.center_x and round(y, -1) == obs.center_y:
                obs.remove_from_sprite_lists()
