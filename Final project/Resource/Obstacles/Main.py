import arcade
import random

def make_obstacles(object):
    x = object[0]
    y = object[1]
    r = object[2]
    type = object[3]
    if type == 0:
        obstacles = Indestructible(x, y, r)
    else:
        obstacles = Destructible(x, y, r)
    return obstacles

class Indestructible:

    def __init__(self, x, y, r):
        self.position_x = x
        self.position_y = y
        self.display_radius = r
        self.real_radius = r
        self.health = 99999
        self.color = 0
    
    def draw(self):
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.display_radius*2, self.display_radius*2, arcade.color.BLACK)

class Destructible:
    
    def __init__(self, x, y, r):
        self.position_x = x
        self.position_y = y
        self.display_radius = r
        self.real_radius = r
        self.health = 5
        self.color = 0
    
    def draw(self):
        if self.color == 0:
            arcade.draw_rectangle_filled(self.position_x, self.position_y, self.display_radius*2, self.display_radius*2, arcade.color.BLUE)
        else:
            arcade.draw_rectangle_filled(self.position_x, self.position_y, self.display_radius*2, self.display_radius*2, arcade.color.RED)
            self.color = 0

class Obstacles:

    def __init__(self, list):
        self.obstacles1_list = []
        self.obstacles2_list = []
        for object in list:
            self.obstacles1_list.append(make_obstacles(object))
    
    def draw(self):
        for obstancles in self.obstacles1_list:
            obstancles.draw()

    def update(self):
        for obstacles in self.obstacles1_list:
            if obstacles.health == 0:
                self.obstacles1_list.remove(obstacles)

if __name__ == '__main__':
    print('Main runs as a main file')

