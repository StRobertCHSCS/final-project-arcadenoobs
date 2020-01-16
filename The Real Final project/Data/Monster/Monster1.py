import arcade
import random
import math
import threading
import json

lock  = threading.Lock()

def create_texture(t, t1):
    '''create a textrue

    Arguments:

    '''
    texture1 = arcade.load_texture(t)
    texture2 = arcade.load_texture(t, mirrored=True)
    texture3 = arcade.load_texture(t1)
    texture4 = arcade.load_texture(t1, mirrored=True)
    return [texture1, texture2, texture3, texture4]

class Slime(arcade.Sprite):

    def __init__(self, texture_list):
        super().__init__(scale=1)
        self.texture_list = texture_list
        self.type = 'slime'
        self.texture = self.texture_list[0]
        self.scale = 1
        self.health = 3
        self.attack = 1
        self.face = 0
        self.injued = False
    
    def update_animation(self):
        if self.change_x > 0 and self.face == 0:
            self.face = 1
        elif self.change_x < 0 and self.face == 1:
            self.face = 0
        lock.acquire()
        if self.face == 0 and self.injued == False:
            self.texture = self.texture_list[0]
        elif self.face == 0 and self.injued == True:
            self.texture = self.texture_list[2]
        elif self.face == 1 and self.injued == False:
            self.texture = self.texture_list[1]
        elif self.face == 1 and self.injued == True:
            self.texture = self.texture_list[3]
        self.scale = 1
        lock.release()
        if self.injued == True:
            self.injued = False

    def path_update(self, x, y, collision):
        speed = 1.5
        if abs(self.center_x - x) > 20 and abs(self.center_y - y) > 20:
            if abs(self.center_x - x) > abs(self.center_y - y) and abs(self.center_x - x) > 20 and collision == False:
                if self.center_x > x:
                    self.change_x = -speed
                else:
                    self.change_x = speed
            else:
                if abs(self.center_x - y) > 20:
                    if self.center_y > y:
                        self.change_y = -speed
                    else:
                        self.change_y = speed
        if abs(self.center_x - x) < 20:
            self.change_x = 0
        if abs(self.center_y - y) < 20:
            self.change_y = 0 
        
        return None

class Ghost(arcade.Sprite):

    def __init__(self, texture_list):
        super().__init__(scale=2)
        self.type = 'ghost'
        self.texture_list = texture_list
        self.texture = texture_list[0]
        self.actived = False
        self.scale = 2
        self.health = 5
        self.attack = 1
        self.face = 0
        self.injued = False
    
    def update_animation(self):
        if self.change_x > 0 and self.face == 0:
            self.face = 1
        elif self.change_x < 0 and self.face == 1:
            self.face = 0
        lock.acquire()
        if self.face == 0 and self.injued == False:
            self.texture = self.texture_list[0]
        elif self.face == 0 and self.injued == True:
            self.texture = self.texture_list[2]
        elif self.face == 1 and self.injued == False:
            self.texture = self.texture_list[1]
        elif self.face == 1 and self.injued == True:
            self.texture = self.texture_list[3]
        self.scale = 2
        lock.release()
        if self.injued == True:
            self.injued = False

    def path_update(self, x, y, collision):
        speed = 1.5
        if abs(self.center_x - x) > 20 and abs(self.center_y - y) > 20:
            if abs(self.center_x - x) > abs(self.center_y - y) and abs(self.center_x - x) > 20 and collision == False:
                if self.center_x > x:
                    self.change_x = -speed
                else:
                    self.change_x = speed
            else:
                if abs(self.center_x - y) > 20:
                    if self.center_y > y:
                        self.change_y = -speed
                    else:
                        self.change_y = speed
        if abs(self.center_x - x) < 20:
            self.change_x = 0
        if abs(self.center_y - y) < 20:
            self.change_y = 0 

        sx = self.center_x
        sy = self.center_y
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
        
        return [sx, sy, dx, dy]
    

class GhostFire(arcade.Sprite):
    
    def __init__(self, x, y, dx, dy):
        super().__init__(scale=1.5)
        texture = arcade.load_texture('Data/Monster/Textures/GhostFire.png')
        self.texture = texture
        self.scale = 1.5
        self.type = 'ghostfire'
        self.center_x = x
        self.center_y = y
        self.change_x = dx
        self.change_y = dy
        self.attack = 1

class BiggySlime(arcade.Sprite):

    def __init__(self, texture_list):
        super().__init__(scale=2)
        self.type = 'biggyslime'
        self.texture_list = texture_list
        self.texture = texture_list[0]
        self.actived = False
        self.scale = 2
        self.health = 8
        self.attack = 2
        self.face = 0
        self.injued = False

    def update_animation(self):
        if self.change_x > 0 and self.face == 0:
            self.face = 1
        elif self.change_x < 0 and self.face == 1:
            self.face = 0
        lock.acquire()
        if self.face == 0 and self.injued == False:
            self.texture = self.texture_list[0]
        elif self.face == 0 and self.injued == True:
            self.texture = self.texture_list[2]
        elif self.face == 1 and self.injued == False:
            self.texture = self.texture_list[1]
        elif self.face == 1 and self.injued == True:
            self.texture = self.texture_list[3]
        self.scale = 2
        lock.release()
        if self.injued == True:
            self.injued = False
    def path_update(self, x, y, collision):
        speed = 2
        if abs(self.center_x - x) > 20 and abs(self.center_y - y) > 20:
            if abs(self.center_x - x) > abs(self.center_y - y) and abs(self.center_x - x) > 20 and collision == False:
                if self.center_x > x:
                    self.change_x = -speed
                else:
                    self.change_x = speed
            else:
                if abs(self.center_x - y) > 20:
                    if self.center_y > y:
                        self.change_y = -speed
                    else:
                        self.change_y = speed
        if abs(self.center_x - x) < 20:
            self.change_x = 0
        if abs(self.center_y - y) < 20:
            self.change_y = 0 
        
        return None
   
class IceSlime(arcade.Sprite):

    def __init__(self, texture_list):
        super().__init__(scale=0.5)
        self.texture_list = texture_list
        self.type = 'iceslime'
        self.texture = texture_list[0]
        self.scale = 0.5
        self.actived = False
        self.health = 3
        self.attack = 1
        self.face = 0
        self.injued = False

    def update_animation(self):
        if self.change_x > 0 and self.face == 0:
            self.face = 1
        elif self.change_x < 0 and self.face == 1:
            self.face = 0
        lock.acquire()
        if self.face == 0 and self.injued == False:
            self.texture = self.texture_list[0]
        elif self.face == 0 and self.injued == True:
            self.texture = self.texture_list[2]
        elif self.face == 1 and self.injued == False:
            self.texture = self.texture_list[1]
        elif self.face == 1 and self.injued == True:
            self.texture = self.texture_list[3]
        self.scale = 3
        lock.release()
        if self.injued == True:
            self.injued = False
            
    def path_update(self, x, y, collision):
        speed = 1.5
        if abs(self.center_x - x) > 20 and abs(self.center_y - y) > 20:
            if abs(self.center_x - x) > abs(self.center_y - y) and abs(self.center_x - x) > 20 and collision == False:
                if self.center_x > x:
                    self.change_x = -speed
                else:
                    self.change_x = speed
            else:
                if abs(self.center_x - y) > 20:
                    if self.center_y > y:
                        self.change_y = -speed
                    else:
                        self.change_y = speed
        if abs(self.center_x - x) < 20:
            self.change_x = 0
        if abs(self.center_y - y) < 20:
            self.change_y = 0 
        
        return None


class Monster:

    def __init__(self):
        self.refresh = 0
        self.monster_list = None
        self.bullet_list = None

    def setup(self):
        self.monster_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        type_of_monsters = ['Slime', 'Ghost', 'BiggySlime', 'IceSlime']
        for mon in type_of_monsters:
            m = open(f'Data/Map/{mon}.json')
            data = json.load(m)
            t = f'Data/Monster/Textures/{mon}.png'
            t1 = f'Data/Monster/Textures/{mon}1.png'
            texture = create_texture(t, t1)
            for dict in data:
                if mon == 'Slime':
                    a = Slime(texture)
                elif mon == 'Ghost':
                    a = Ghost(texture)
                elif mon == 'BiggySlime':
                    a = BiggySlime(texture)
                elif mon == 'IceSlime':
                    a = IceSlime(texture)
                a.center_x = dict['x']
                a.center_y = dict['y']
                self.monster_list.append(a)

    def draw(self):
        self.monster_list.draw()
        self.bullet_list.draw()

    def update(self, x, y):
        self.refresh += 1
        for mon in self.monster_list:
            if abs(mon.center_x - x) < 300 and abs(mon.center_y - y) < 300:
                a = mon.path_update(x, y, False)
                if mon.type == 'ghost' and self.refresh > 60:
                    self.refresh = 0
                    fire = GhostFire(a[0], a[1], a[2], a[3])
                    self.bullet_list.append(fire)
        for mon in self.monster_list:
            if mon.health == 0:
                mon.remove_from_sprite_lists()

        self.bullet_list.update()
        self.monster_list.update_animation()

    def key_press(self, key, x, y, type):
        if type == 3:
            t = f'Data/Monster/Textures/Slime.png'
            t1 = f'Data/Monster/Textures/Slime1.png'
            texture = create_texture(t, t1)
            s = Slime(texture)
        elif type == 4:
            t = f'Data/Monster/Textures/Ghost.png'
            t1 = f'Data/Monster/Textures/Ghost.png'
            texture = create_texture(t, t1)
            s = Ghost(texture)
        elif type == 5:
            t = f'Data/Monster/Textures/BiggySlime.png'
            t1 = f'Data/Monster/Textures/BiggySlime1.png'
            texture = create_texture(t, t1)
            s = BiggySlime(texture)
        elif type == 6:
            t = f'Data/Monster/Textures/IceSlime.png'
            t1 = f'Data/Monster/Textures/IceSlime1.png'
            texture = create_texture(t, t1)
            s = IceSlime(texture)
        s.center_x = x
        s.center_y = y
        self.monster_list.append(s) 
    
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