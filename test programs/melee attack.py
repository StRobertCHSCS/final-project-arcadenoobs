import arcade
import os
import math

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class Ball:
    
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):

    MOVEMENT_SPEED = 3

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.set_mouse_visible(True)
        arcade.set_background_color(arcade.color.WHITE)

        self.ball = Ball(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 0, 0, 15, arcade.color.DARK_PINK)

        #######
        self.Up = False
        self.Down = False
        self.Left = False
        self.Right = False
        
    def on_draw(self):
        arcade.start_render()
        self.ball.draw()
        if self.Up == True:
            arcade.draw_text('UP', 290, 500, arcade.color.BLACK, 15)
        if self.Down == True:
            arcade.draw_text('DOWN', 290, 500, arcade.color.BLACK, 15)
        if self.Left == True:
            arcade.draw_text('LEFT', 290, 500, arcade.color.BLACK, 15)
        if self.Right == True:
            arcade.draw_text('RIGHT', 290, 500, arcade.color.BLACK, 15)
    def update(self, delta_time):
        self.ball.update()
        
    def on_mouse_press(self, x, y, button, modifiers):
        
        if x != self.ball.position_x and y != self.ball.position_y:
            radian = math.atan((y - self.ball.position_y)/(x - self.ball.position_x))
            print(radian)
            if self.ball.position_y < y and radian > 0:
                if radian >= (math.pi/4):
                    self.Up = True
                if radian < (math.pi/4):
                    self.Right = True
            if self.ball.position_y < y and radian < 0:
                if radian >= (-math.pi/4):
                    self.Left = True
                if radian < (-math.pi/4):
                    self.Up = True
            if self.ball.position_y > y and radian > 0:
                if radian >= (math.pi/4):
                    self.Down = True
                if radian < (math.pi/4):
                    self.Left = True
            if self.ball.position_y > y and radian < 0:
                if radian >= (-math.pi/4):
                    self.Right = True
                if radian < (-math.pi/4):
                    self.Down = True
        elif self.ball.position_x == x and self.ball.position_y != y:
            if self.ball.position_y < y:
                self.Up = True
            else:
                self.Down = True
        elif self.ball.position_x != x and self.ball.position_y == y:
            if self.ball.position_x < x:
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
            self.ball.change_x = -MyGame.MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MyGame.MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = MyGame.MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MyGame.MOVEMENT_SPEED
        if key == 65505:
            MyGame.MOVEMENT_SPEED = 20

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0
        if key == 65505:
            MyGame.MOVEMENT_SPEED = 3


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Melee Attack")
    arcade.run()

if __name__ == '__main__':
    main()