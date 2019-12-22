import math
import arcade
import Movement as Mage_M
import Attack as Mage_A

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600  

class MyGame(arcade.Window):

    MOVEMENT_SPEED = 3

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.set_mouse_visible(True)
        arcade.set_background_color(arcade.color.WHITE)

        self.spirit = Mage_M.Spirit(width/2, height/2, 0, 0, 15, arcade.color.BLACK)
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
            self.fire_ball_list.append(Mage_A.create_fire_ball(self.spirit.position_x, self.spirit.position_y, x, y))


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Mage")
    arcade.run()

if __name__ == '__main__':
    main()