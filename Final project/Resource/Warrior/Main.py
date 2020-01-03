import arcade
import math

class Warrior:

    MOVEMENT_SPEED = 3

    def __init__(self, width, height):
        self.spirit = W_M.Spirit(width/2, height/2, 0, 0, 15, arcade.color.DARK_PINK)

        self.Up = False
        self.Down = False
        self.Left = False
        self.Right = False
        self.fire_ball_list = []

    def draw(self):
        self.spirit.draw()
        if self.Up == True:
            arcade.draw_text('UP', 290, 500, arcade.color.BLACK, 15)
            arcade.draw_arc_filled(self.spirit.position_x, self.spirit.position_y, 50, 50, arcade.color.GRAY, 45, 135, 0)
        if self.Down == True:
            arcade.draw_text('DOWN', 290, 500, arcade.color.BLACK, 15)
            arcade.draw_arc_filled(self.spirit.position_x, self.spirit.position_y, 50, 50, arcade.color.GRAY, 45, 135, 180)
        if self.Left == True:
            arcade.draw_text('LEFT', 290, 500, arcade.color.BLACK, 15)
            arcade.draw_arc_filled(self.spirit.position_x, self.spirit.position_y, 50, 50, arcade.color.GRAY, 45, 135, 90)
        if self.Right == True:
            arcade.draw_text('RIGHT', 290, 500, arcade.color.BLACK, 15)
            arcade.draw_arc_filled(self.spirit.position_x, self.spirit.position_y, 50, 50, arcade.color.GRAY, 45, 135, 270)
    
    def update(self):
        self.spirit.update()
    
    def on_mouse_press(self, x, y, button):
        
        if x != self.spirit.position_x and y != self.spirit.position_y:
            radian = math.atan((y - self.spirit.position_y)/(x - self.spirit.position_x))
            if self.spirit.position_y < y and radian > 0:
                if radian >= (math.pi/4):
                    self.Up = True
                if radian < (math.pi/4):
                    self.Right = True
            if self.spirit.position_y < y and radian < 0:
                if radian >= (-math.pi/4):
                    self.Left = True
                if radian < (-math.pi/4):
                    self.Up = True
            if self.spirit.position_y > y and radian > 0:
                if radian >= (math.pi/4):
                    self.Down = True
                if radian < (math.pi/4):
                    self.Left = True
            if self.spirit.position_y > y and radian < 0:
                if radian >= (-math.pi/4):
                    self.Right = True
                if radian < (-math.pi/4):
                    self.Down = True
        elif self.spirit.position_x == x and self.spirit.position_y != y:
            if self.spirit.position_y < y:
                self.Up = True
            else:
                self.Down = True
        elif self.spirit.position_x != x and self.spirit.position_y == y:
            if self.spirit.position_x < x:
                self.Right = True
            else:
                self.Left = True
    
    def on_mouse_release(self, x, y, button):
        self.Up = False
        self.Down = False
        self.Left = False
        self.Right = False
    
    def on_key_press(self, key):
        if key == arcade.key.A:
            self.spirit.change_x = -Warrior.MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.spirit.change_x = Warrior.MOVEMENT_SPEED
        elif key == arcade.key.W:
            self.spirit.change_y = Warrior.MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.spirit.change_y = -Warrior.MOVEMENT_SPEED
        if key == 65505:
            Warrior.MOVEMENT_SPEED = 20

    def on_key_release(self, key):
        if key == arcade.key.A or key == arcade.key.D:
            self.spirit.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.spirit.change_y = 0
        if key == 65505:
            Warrior.MOVEMENT_SPEED = 3
    

if __name__ == '__main__':
    print('Main runs as a main file')
else: 
    import Resource.Warrior.Movement as W_M

