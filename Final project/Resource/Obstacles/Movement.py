import arcade

class Obstacles:

    def __init__(self, x, y, r):
        self.position_x = x
        self.position_y = y
        self.display_radius = r
        self.real_radius = r
    
    def draw(self):
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.display_radius*2, self.display_radius*2, arcade.color.BLACK)