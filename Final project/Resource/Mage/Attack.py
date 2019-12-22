import math
import arcade

def test():
    print('Testing Attack')

class Fire_ball:
    
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
    
    def update(self):
        self.x += self.dx
        self.y += self.dy
    
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, 5, arcade.color.RED)

def create_fire_ball(sx, sy, mx, my):
    dh = 15
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