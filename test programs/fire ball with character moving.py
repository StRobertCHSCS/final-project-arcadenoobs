import arcade
import math

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600  

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
    


class Spirit():
    
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color
        self.fire_ball_list = []

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

        self.spirit = Spirit(width/2, height/2, 0, 0, 15, arcade.color.BLACK)
        self.fire_ball_list = []

    def on_draw(self):
        arcade.start_render()
        self.spirit.draw()

        for ball in self.fire_ball_list:
            ball.draw()

    def update(self, delta_time):
        self.spirit.update()

        for fire_ball in self.fire_ball_list:
            fire_ball.update()
            if fire_ball.x < 0 or fire_ball.x > 600:
                self.fire_ball_list.remove(fire_ball)
            elif fire_ball.y < 0 or fire_ball.y > 600:
                self.fire_ball_list.remove(fire_ball) 


    def on_key_press(self, key, modifiers):
        if key == arcade.key.A:
            self.spirit.change_x = -MyGame.MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.spirit.change_x = MyGame.MOVEMENT_SPEED
        elif key == arcade.key.W:
            self.spirit.change_y = MyGame.MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.spirit.change_y = -MyGame.MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.D:
            self.spirit.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.spirit.change_y = 0

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.fire_ball_list.append(create_fire_ball(self.spirit.position_x, self.spirit.position_y, x, y))


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Moving by Key")
    arcade.run()

if __name__ == '__main__':
    main()