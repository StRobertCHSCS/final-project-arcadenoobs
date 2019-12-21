import arcade
import os
import math

SCREEM_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'title'

SPEED = 20

class spirit:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, 30, arcade.color.BLACK)

class fire_ball:
    
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

class Window(arcade.Window):

    def __init__(self):
        super().__init__(SCREEM_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))
        os.chdir(file_path)
        arcade.set_background_color(arcade.color.WHITE)
        self.spirit = spirit(300, 300)
        self.fire_ball_list = []
    
    def on_update(self, delta_time):
        for fire_ball in self.fire_ball_list:
            fire_ball.update()
            if fire_ball.x < 0 or fire_ball.x > 600:
                self.fire_ball_list.remove(fire_ball)
            elif fire_ball.y < 0 or fire_ball.y > 600:
                self.fire_ball_list.remove(fire_ball)  

    def set_up(self):
        pass

    def on_draw(self):
        arcade.start_render()
        self.spirit.draw()
        for ball in self.fire_ball_list:
            ball.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            dh = 20
            rx = (x - 300)/abs(x - 300)
            ry = (y - 300)/abs(y - 300)
            p = (abs(x) - 300)/(abs(y) - 300)
            dy = math.sqrt(dh**2/(1 + p**2))
            dx = p*dy
            ball = fire_ball(300, 300, abs(dx)*rx, abs(dy)*ry)
            self.fire_ball_list.append(ball)
            print(rx, ry)
            print(self.fire_ball_list)

    def on_key_press(self, key, modifiers):
        pass

def main():
    window = Window()
    window.set_up()
    arcade.run()

if __name__ == '__main__':
    main()