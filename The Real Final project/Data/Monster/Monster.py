import arcade
import math
import json

class Slime(arcade.Sprite):

    def __init__(self, filename, health):
        super().__init__(filename)
        self.health = 3
        self.type = 'slime'
        self.attack = 1

class Ghost(arcade.Sprite):

    def __init__(self, filename):
        super().__init__(filename, 2)
        self.type = 'ghost'
        self.health = 5
        self.attack = 1

class GhostFire(arcade.Sprite):
    
    def __init__(self, filename, x, y, dx, dy):
        super().__init__(filename, 1.5)
        self.center_x = x
        self.center_y = y
        self.change_x = dx
        self.change_y = dy
        self.attack = 1

class BiggySlime(arcade.Sprite):

    def __init__(self, filename):
        super().__init__(filename, 2)
        self.type = 'biggyslime'
        self.health = 8
        self.attack = 2

class IceSlime(arcade.Sprite):

    def __init__(self, filename):
        super().__init__(filename)
        self.type = 'iceslime'
        self.health = 3
        self.attack = 1

class Monster:

    def __init__(self):
        self.monster_list = None
        self.injued_list = None
        self.actived_list = None
        self.bullet_list = None
        self.slime = None

    def setup(self):
        self.monster_list = arcade.SpriteList()
        self.injued_list = arcade.SpriteList()
        self.actived_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        slime = open('Data/Map/Slime.json')
        data = json.load(slime)
        for dict in data:
            s = Slime('Data/Monster/Textures/Slime.png', 0)
            s.center_x = dict['x']
            s.center_y = dict['y']
            s.health = dict['h']
            self.monster_list.append(s)
        
        ghost = open('Data/Map/Ghost.json')
        data = json.load(ghost)
        for dict in data:
            g = Ghost('Data/Monster/Textures/Ghost.png')
            g.center_x = dict['x']
            g.center_y = dict['y']
            self.monster_list.append(g)

        bs = open('Data/Map/BiggySlime.json')
        data = json.load(bs)
        for dict in data:
            s = BiggySlime('Data/Monster/Textures/BiggySlime.png')
            s.center_x = dict['x']
            s.center_y = dict['y']
            self.monster_list.append(s)

        isl = open('Data/Map/IceSlime.json')
        data = json.load(isl)
        for dict in data:
            s = BiggySlime('Data/Monster/Textures/IceSlime.png')
            s.center_x = dict['x']
            s.center_y = dict['y']
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
        if len(self.bullet_list) > 0:
            self.bullet_list.draw()

    def update(self, x, y):
        for mon in self.monster_list:
            if abs(mon.center_x - x) < 300 and abs(mon.center_y - y) < 300:
                if mon.type == 'slime':
                    s = Slime('Data/Monster/Textures/Slime.png', 0)
                    s.center_x = mon.center_x
                    s.center_y = mon.center_y
                    s.health = mon.health
                    self.actived_list.append(s)
                elif mon.type == 'ghost':
                    g = Ghost('Data/Monster/Textures/Ghost.png')
                    g.center_x = mon.center_x
                    g.center_y = mon.center_y
                    g.health = mon.health
                    self.actived_list.append(g)
                elif mon.type == 'biggyslime':
                    s = BiggySlime('Data/Monster/Textures/BiggySlime.png')
                    s.center_x = mon.center_x
                    s.center_y = mon.center_y
                    self.actived_list.append(s)
                elif mon.type == 'iceslime':
                    s = BiggySlime('Data/Monster/Textures/IceSlime.png')
                    s.center_x = mon.center_x
                    s.center_y = mon.center_y
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
                elif mon.type == 'ghost':
                    g = Ghost('Data/Monster/Textures/Ghost.png')
                    g.center_x = mon.center_x
                    g.center_y = mon.center_y
                    g.health = mon.health
                    self.monster_list.append(g)
                elif mon.type == 'biggyslime':
                    s = BiggySlime('Data/Monster/Textures/BiggySlime.png')
                    s.center_x = mon.center_x
                    s.center_y = mon.center_y
                    self.monster_list.append(s)
                elif mon.type == 'iceslime':
                    s = IceSlime('Data/Monster/Textures/IceSlime.png')
                    s.center_x = mon.center_x
                    s.center_y = mon.center_y
                    self.monster_list.append(s)        
                mon.remove_from_sprite_lists()

        for mon in self.actived_list:
            if mon.health == 0:
                mon.remove_from_sprite_lists()
        
        self.bullet_list.update()

    def path_update(self, mon, x, y, collision, refresh):
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
            if abs(mon.center_x - x) < 20:
                mon.change_x = 0
            if abs(mon.center_y - y) < 20:
                mon.change_y = 0
        elif mon.type == 'ghost' and refresh == 60:
            speed = 1
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

            sx = mon.center_x
            sy = mon.center_y
            mx = x
            my = y
            dh = 5
            if mx != sx and my != sy:
                rx = (mx - sx)/abs(mx - sx)
                ry = (my - sy)/abs(my - sy)
                theta = math.atan(abs(my - sy)/abs(mx - sx))
                dx = (dh*math.cos(theta))*rx
                dy = (dh*math.sin(theta))*ry
            elif mx == sx and my > sy:
                dx = 0
                dy = dh
            elif mx == sx and my < sy:
                dx = 0
                dy = -dh
            elif mx > sx and my == sy:
                dx = dh
                dy = 0
            elif mx < sx and my == sy:
                dx = -dh
                dy = 0
            fire = GhostFire('Data/Monster/Textures/Ghost Fire.png', sx, sy, dx, dy)
            self.bullet_list.append(fire)

        elif mon.type == 'biggyslime':
            speed = 2
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
            if abs(mon.center_x - x) < 20:
                mon.change_x = 0
            if abs(mon.center_y - y) < 20:
                mon.change_y = 0

        elif mon.type == 'iceslime':
            speed = 3.5
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
            if abs(mon.center_x - x) < 20:
                mon.change_x = 0
            if abs(mon.center_y - y) < 20:
                mon.change_y = 0

    def key_press(self, key, x, y, type):
        if type == 3:
            s = Slime('Data/Monster/Textures/Slime.png', 0)
            s.center_x = x
            s.center_y = y
            s.health = 3
            self.monster_list.append(s)
        elif type == 4:
            g = Ghost('Data/Monster/Textures/Ghost.png')
            g.center_x = x
            g.center_y = y
            self.monster_list.append(g)
        elif type == 5:
            s = BiggySlime('Data/Monster/Textures/BiggySlime.png')
            s.center_x = x
            s.center_y = y
            self.monster_list.append(s) 
        elif type == 6:
            s = IceSlime('Data/Monster/Textures/IceSlime.png')
            s.center_x = x
            s.center_y = y
            self.monster_list.append(s) 

    def color_change(self, x, y, type):
        if type == 'slime':
            n = arcade.Sprite('Data/Monster/Textures/Slime1.png')
            n.center_x = x
            n.center_y = y
            self.injued_list.append(n)
        elif type == 'ghost':
            n = arcade.Sprite('Data/Monster/Textures/Ghost1.png')
            n.center_x = x
            n.center_y = y
            self.injued_list.append(n)
        elif type == 'biggyslime':
            n = arcade.Sprite('Data/Monster/Textures/BiggySlime1.png', 2)
            n.center_x = x
            n.center_y = y
            self.injued_list.append(n)
        elif type == 'iceslime':
            n = arcade.Sprite('Data/Monster/Textures/IceSlime1.png', 2)
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
        with open('Data/Map/Ghost.json', 'w+') as f:
            list = []
            for mon in self.monster_list:
                if mon.type == 'ghost':
                    g = {"x": mon.center_x, "y": mon.center_y}
                    list.append(g)
            j = json.dump(list, f, ensure_ascii=False)
        with open('Data/Map/BiggySlime.json', 'w+') as f:
            list = []
            for mon in self.monster_list:
                if mon.type == 'biggyslime':
                    s = {"x": mon.center_x, "y": mon.center_y}
                    list.append(s)
            j = json.dump(list, f, ensure_ascii=False)
        with open('Data/Map/IceSlime.json', 'w+') as f:
            list = []
            for mon in self.monster_list:
                if mon.type == 'iceslime':
                    s = {"x": mon.center_x, "y": mon.center_y}
                    list.append(s)
            j = json.dump(list, f, ensure_ascii=False)
        print('Monsters Saved')
        
    def delete(self, x, y):
        for mon in self.monster_list:
            if round(x, -1) == mon.center_x and round(y, -1) == mon.center_y:
                mon.remove_from_sprite_lists()
                return 'pass'