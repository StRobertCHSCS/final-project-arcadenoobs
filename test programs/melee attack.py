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

        self.ball = Ball(300, 300, 0, 0, 15, arcade.color.DARK_PINK)
        print('上下左右移动，按住shift疾跑，有个小bug就是在已经按住走路时按疾跑不会加速，这个挺难修的可能要从写代码')

        

    def on_draw(self):
        arcade.start_render()
        self.ball.draw()

    def update(self, delta_time):
        self.ball.update()

    def on_mouse_press(self, x, y, button, modifiers):
        if x != self.ball.position_x and y != self.ball.position_y:
            radian = math.atan((y - self.ball.position_y)/(x - self.ball.position_x))
            print(radian)
            if self.ball.position_y < y and radian > 0:
                if radian >= math.pi/4:
                    arcade.draw_text("UP", 100, 100, arcade.color.BLACK, 10)
                if radian < math.pi/4:
                    arcade.draw_text("RIGHT", 100, 100, arcade.color.BLACK, 10)
            

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