import arcade
import os
import math
import Movement as W_M

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):

    MOVEMENT_SPEED = 3

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.set_mouse_visible(True)
        arcade.set_background_color(arcade.color.WHITE)

        self.spirit = W_M.Spirit(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 0, 0, 15, arcade.color.DARK_PINK)
        print('上下左右移动，按住shift疾跑，有个小bug就是在已经按住走路时按疾跑不会加速，这个挺难修的可能要从写代码')

        #######
        self.Up = False
        self.Down = False
        self.Left = False
        self.Right = False
        
    def on_draw(self):
        arcade.start_render()
        self.spirit.draw()
        if self.Up == True:
            arcade.draw_text('UP', 290, 500, arcade.color.BLACK, 15)
        if self.Down == True:
            arcade.draw_text('DOWN', 290, 500, arcade.color.BLACK, 15)
        if self.Left == True:
            arcade.draw_text('LEFT', 290, 500, arcade.color.BLACK, 15)
        if self.Right == True:
            arcade.draw_text('RIGHT', 290, 500, arcade.color.BLACK, 15)
            
    def update(self, delta_time):
        self.spirit.update()
        
    def on_mouse_press(self, x, y, button, modifiers):
        
        if x != self.spirit.position_x and y != self.spirit.position_y:
            radian = math.atan((y - self.spirit.position_y)/(x - self.spirit.position_x))
            print(radian)
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
            
                

    def on_mouse_release(self, x, y, button, modifiers):
        self.Up = False
        self.Down = False
        self.Left = False
        self.Right = False

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.spirit.change_x = -MyGame.MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.spirit.change_x = MyGame.MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.spirit.change_y = MyGame.MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.spirit.change_y = -MyGame.MOVEMENT_SPEED
        if key == 65505:
            MyGame.MOVEMENT_SPEED = 20

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.spirit.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.spirit.change_y = 0
        if key == 65505:
            MyGame.MOVEMENT_SPEED = 3


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Melee Attack")
    arcade.run()

if __name__ == '__main__':
    main()