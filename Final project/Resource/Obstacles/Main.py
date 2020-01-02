import arcade
import random

def make_obstacles(object):
    '''make a specific obstacle

    Argument:
        object{list} -- a list that contains 4 varibles:
                        x coodinate{float}, y coodinate{float}, raidus(half width){float}, type{int}
        
    Returns:
        [Object] -- convert the list to a object of a obstacle
    '''
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
        '''A class to store all datas of a specific indestructible obstacle
        '''
        self.position_x = x
        self.position_y = y
        self.display_radius = r
        self.real_radius = r
        self.health = 99999
        self.color = 0
    
    def draw(self):
        '''draw the obstacle
        '''
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.display_radius*2, self.display_radius*2, arcade.color.BLACK)

class Destructible:
    
    def __init__(self, x, y, r):
        '''A class to store all datas of a specific destructible obstacle
        '''
        self.position_x = x
        self.position_y = y
        self.display_radius = r
        self.real_radius = r
        self.health = 5
        self.color = 0
    
    def draw(self):
        '''draw the obstacle
        '''
        if self.color == 0:
            arcade.draw_rectangle_filled(self.position_x, self.position_y, self.display_radius*2, self.display_radius*2, arcade.color.BLUE)
        else:
            arcade.draw_rectangle_filled(self.position_x, self.position_y, self.display_radius*2, self.display_radius*2, arcade.color.RED)
            self.color = 0

class Obstacles:

    def __init__(self, list):
        '''The package of all obstacles
        '''
        self.obstacles1_list = []
        self.obstacles2_list = []
        if len(list) > 0:
            for object in list:
                self.obstacles1_list.append(make_obstacles(object))
    
    def draw(self):
        '''draw all obstacles
        '''
        for obstancles in self.obstacles1_list:
            obstancles.draw()

    def update(self):
        '''update all obstacles
        '''

        for obstacles in self.obstacles1_list:
            if obstacles.health == 0:
                self.obstacles1_list.remove(obstacles)
        #create a new one if there is no destructible obstacle
        #if len(self.obstacles1_list) == 1:
         #   list = [random.randrange(30, 570), random.randrange(30, 570), 20, 1]
          #  self.obstacles1_list.append(make_obstacles(list))
    
    def make_a_object(self, x, y, r, t):
        object = [x, y, r, t]
        self.obstacles1_list.append(make_obstacles(object))

if __name__ == '__main__':
    print('Main runs as a main file')

