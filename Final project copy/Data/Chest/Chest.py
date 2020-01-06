import arcade
import json
import random

class Wooden_Chest(arcade.Sprite):

    def __init__(self, filename, content):
        super().__init__(filename, 2)
        self.type = 'wooden'
        self.health = 3
        self.content = content

class Drops(arcade.Sprite):

    def __init__(self, filename):
        super().__init__(filename)
        self.type = None

class Chest:

    def __init__(self):
        self.chest_list = None
        self.opened_list = None
        self.drops_list = arcade.SpriteList()

    def setup(self):
        self.chest_list = arcade.SpriteList()
        self.opened_list = arcade.SpriteList()
        self.drops_list = arcade.SpriteList()

        chest = open('Data/Map/Chest.json')
        data = json.load(chest)
        for dict in data:
            c = Wooden_Chest('Data/Chest/Textures/Wooden Chest.png', random.sample(dict['c'], 1)[0])
            c.center_x = dict['x']
            c.center_y = dict['y']
            self.chest_list.append(c)

    def draw(self):
        self.chest_list.draw()
        self.opened_list.draw()
        self.drops_list.draw()

    def update(self):
        for c in self.chest_list:
            if c.health == 0:
                x = c.center_x
                y = c.center_y
                a = c.content
                c.remove_from_sprite_lists()
                n = arcade.Sprite('Data/Chest/Textures/Wooden Chest1.png', 2)
                n.center_x = x
                n.center_y = y
                self.opened_list.append(n)
                if a == 'mana':
                    d = Drops('Data/Chest/Textures/Mana.png')
                    d.center_x = x
                    d.center_y = y
                    d.type = a
                    self.drops_list.append(d)
                elif a == 'health':
                    d = Drops('Data/Chest/Textures/Mana.png')
                    d.center_x = x
                    d.center_y = y
                    d.type = a
                    self.drops_list.append(d)
                elif a == 'skill1':
                    d = Drops('Data/Mage/Textures/Skill1.png')
                    d.center_x = x
                    d.center_y = y
                    d.type = a
                    self.drops_list.append(d)
                    
    def key_press(self, key, x, y, type):
        if type == 4:
            c = Wooden_Chest('Data/Chest/Textures/Wooden Chest.png', None)
            c.center_x = x
            c.center_y = y
            self.chest_list.append(c)

    
    def save(self):
        with open('Data/Map/Chest.json', 'w+') as f:
            list = []
            for c in self.chest_list:
                d = {"x": c.center_x, "y": c.center_y, "c": [c.content]}
                list.append(d)
            j = json.dump(list, f, ensure_ascii=False)
            print('Chest Saved')
    
    def delete(self, x, y):
        for c in self.chest_list:
            if round(x, -1) == c.center_x and round(y, -1) == c.center_y:
                c.remove_from_sprite_lists()
                return 'pass'