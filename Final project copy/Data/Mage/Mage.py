import arcade
import math
import json

class Sprite(arcade.Sprite):

    def __init__(self, filename):
        super().__init__(filename, 0.5)
        self.previous_x = self.center_x
        self.previous_y = self.center_y

class Fireball(arcade.Sprite):

    def __init__(self, filename, scale, x, y, dx, dy):
        super().__init__(filename, scale)
        self.center_x = x
        self.center_y = y
        self.change_x = dx
        self.change_y = dy

class Mage:
    
    MOVEMENT_SPEED = 3

    def __init__(self):
        self.sprite_list = None
        self.fireball_list = None

        self.back1 = None
        self.back2 = None
        self.front1 = None
        self.front2 = None
        self.left1 = None
        self.left2 = None
        self.right1 = None
        self.right2 = None
        self.a_v = 1
        self.a_h = 1
        self.fireball = None
        self.sprite = None

        self.health = 10
        self.mana = 50
        self.mana_limit = 50

    def setup(self):
        self.sprite_list = arcade.SpriteList()
        self.fireball_list = arcade.SpriteList()

        self.back1 = 'Data/Mage/Textures/Back1.png'
        self.back2 = 'Data/Mage/Textures/Back2.png'
        self.front1 = 'Data/Mage/Textures/Front1.png'
        self.front2 = 'Data/Mage/Textures/Front2.png'
        self.left1 = 'Data/Mage/Textures/Left1.png'
        self.left2 = 'Data/Mage/Textures/Left2.png'
        self.right1 = 'Data/Mage/Textures/Right1.png'
        self.right2 = 'Data/Mage/Textures/Right2.png'

        self.sprite = Sprite(self.front1)
        sprite = open('Data/map/Spawnpoint.json')
        data = json.load(sprite)
        for dict in data:
            self.sprite.center_x = dict['x']
            self.sprite.center_y = dict['y']
        self.sprite_list.append(self.sprite)

    def update(self):
        arcade.set_viewport(self.sprite.center_x - 301, self.sprite.center_x +299, self.sprite.center_y - 301, self.sprite.center_y + 299)
        self.sprite_list.update()
        self.fireball_list.update()
        if self.health == 0:
            print("GAME OVER\nWASTED")
            arcade.close_window()
    
    def draw(self):
        self.sprite.draw()
        self.fireball_list.draw()
        arcade.draw_text(f'Health: {self.health}', self.sprite.center_x - 300, 280 + self.sprite.center_y, arcade.color.RED, 15)
        arcade.draw_text(f'Mana: {self.mana}/{self.mana_limit}', self.sprite.center_x - 300, 250 + self.sprite.center_y, arcade.color.BLUE, 15)
    
    def mouse_release(self, x, y):
        if self.mana > 0:
            self.mana -= 1
            sx = self.sprite.center_x
            sy = self.sprite.center_y
            mx = x + self.sprite.center_x - 300
            my = y + self.sprite.center_y - 300
            dh = 20
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
            fireball = Fireball('Data/Mage/Textures/Fireball.png', 1, sx, sy, dx, dy)
            self.fireball_list.append(fireball)
        else:
            print('Insufficient Mana')

    def key_press(self, key):
        if key == arcade.key.W:
            x = self.sprite.center_x
            y = self.sprite.center_y
            self.sprite.remove_from_sprite_lists()
            self.sprite = Sprite(self.back1)
            self.sprite.center_x = x
            self.sprite.center_y = y
            self.sprite_list.append(self.sprite)
            self.sprite.change_x = 0
            self.sprite.change_y = Mage.MOVEMENT_SPEED
        elif key == arcade.key.S:
            x = self.sprite.center_x
            y = self.sprite.center_y
            self.sprite.remove_from_sprite_lists()
            self.sprite = Sprite(self.front1)
            self.sprite.center_x = x
            self.sprite.center_y = y
            self.sprite_list.append(self.sprite)
            self.sprite.change_x = 0
            self.sprite.change_y = -Mage.MOVEMENT_SPEED
        elif key == arcade.key.A:
            x = self.sprite.center_x
            y = self.sprite.center_y
            self.sprite.remove_from_sprite_lists()
            self.sprite = Sprite(self.left1)
            self.sprite.center_x = x
            self.sprite.center_y = y
            self.sprite_list.append(self.sprite)
            self.sprite.change_y = 0
            self.sprite.change_x = -Mage.MOVEMENT_SPEED
        elif key == arcade.key.D:
            x = self.sprite.center_x
            y = self.sprite.center_y
            self.sprite.remove_from_sprite_lists()
            self.sprite = Sprite(self.right1)
            self.sprite.center_x = x
            self.sprite.center_y = y
            self.sprite_list.append(self.sprite)
            self.sprite.change_y = 0
            self.sprite.change_x = Mage.MOVEMENT_SPEED

    def key_release(self, key):
        if key == arcade.key.W or key == arcade.key.S:
            self.sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.sprite.change_x = 0
