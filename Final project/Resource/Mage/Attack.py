import math
import arcade

class Fire_ball:
    
    def __init__(self, x, y, dx, dy):
        '''A class to store all datas of a specific fire ball
        '''
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
    
    def update(self):
        '''calculate the positions in time
        '''
        self.x += self.dx
        self.y += self.dy
    
    def draw(self):
        '''draw the fire ball
        '''
        arcade.draw_circle_filled(self.x, self.y, 5, arcade.color.RED)

def create_fire_ball(sx, sy, mx, my):
    '''create a fire ball

    Argument:
        sx{float} -- spirit_x: x coordinate the spirit at
        sy{float} -- spirit_y: y coordinate the spirit at
        mx{float} -- mouse_pressed_x: x coordinate the mouse pressed at
        my{fliat} -- mouse_pressed_y: y coordinate the mouse pressed at

    Returns:
        [object] -- a data package of the fire ball created
    '''
    dh = 20
    if mx != sx and my != sy:
        rx = (mx - sx)/abs(mx - sx)
        ry = (my - sy)/abs(my - sy)
        theta = math.atan(1/(abs(mx - sx)/abs(my - sy)))
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
    fire_ball = Fire_ball(sx, sy, dx, dy)
    
    return fire_ball
    