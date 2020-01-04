import arcade
import json

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Main:

    MOVEMENT_SPEED = 1

    def __init__(self):
        self.sprite_list = None
        self.sprite = None
        self.spawnpoint = None

    def setup(self):
        self.sprite_list = arcade.SpriteList()
        self.spawnpoint = arcade.SpriteList()
        self.sprite = arcade.Sprite('Data/Engine/Textures/Select.png')
        sprite = open('Data/map/Spawnpoint.json')
        data = json.load(sprite)
        for dict in data:
            self.spawnpoint.append(arcade.Sprite('Data/Engine/Textures/Spawnpoint.png', center_x=dict['x'], center_y=dict['y']))
            self.sprite.center_x = dict['x']
            self.sprite.center_y = dict['y']
        self.sprite_list.append(self.sprite)

    def draw(self):
        self.spawnpoint.draw()
        self.sprite_list.draw()
    
    def update(self):
        self.sprite_list.update()
        arcade.set_viewport(self.sprite.center_x - 301, self.sprite.center_x +299, self.sprite.center_y - 301, self.sprite.center_y + 299)
    
    def mouse_press(self, x, y, button):
        pass
    
    def mouse_release(self, x, y, button):
        pass
    
    def key_press(self, key):
        if key == arcade.key.A:
            self.sprite.change_y = 0
            self.sprite.change_x = -Main.MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.sprite.change_y = 0
            self.sprite.change_x = Main.MOVEMENT_SPEED
        elif key == arcade.key.W:
            self.sprite.change_x = 0
            self.sprite.change_y = Main.MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.sprite.change_x = 0
            self.sprite.change_y = -Main.MOVEMENT_SPEED
        if key == 65505:
            Main.MOVEMENT_SPEED = 5
        
    def renew_spawnpoint(self, x, y):
        for sprite in self.spawnpoint:
            sprite.remove_from_sprite_lists()
            s = arcade.Sprite('Data/Engine/Textures/Spawnpoint.png', center_x=x, center_y=y)
            self.spawnpoint.append(s)

    def key_release(self, key):
        if key == 65505:
            Main.MOVEMENT_SPEED = 1
        if key == arcade.key.A or key == arcade.key.D:
            self.sprite.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.sprite.change_y = 0

    def save(self):
        with open('Data/Map/Spawnpoint.json', 'w+') as f:
            list = []
            for s in self.spawnpoint:
                a = {"x": s.center_x, "y": s.center_y}
                list.append(a)
            j = json.dump(list, f, ensure_ascii=False)
        print('Spawnpoint Saved')