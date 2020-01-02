import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Spirit():
    
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



class Main:

    MOVEMENT_SPEED = 3

    def __init__(self, width, height):
        self.spirit = Spirit(width/2, height/2, 0, 0, 15, arcade.color.DARK_PINK)

    def draw(self):
        self.spirit.draw()
        #arcade.draw_text(f'spirit x: {self.spirit.position_x:+.0f}', self.spirit.position_x - 300 , 280 + self.spirit.position_y, arcade.color.BLACK, 15)
        #arcade.draw_text(f'spirit y: {self.spirit.position_y:+.0f}', self.spirit.position_x - 300 , 250 + self.spirit.position_y, arcade.color.BLACK, 15)
    
    def update(self):
        self.spirit.update()
    
    def on_mouse_press(self, x, y, button):
        pass
    
    def on_mouse_release(self, x, y, button):
        pass
    
    def on_key_press(self, key):
        if key == arcade.key.A:
            self.spirit.change_y = 0
            self.spirit.change_x = -Main.MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.spirit.change_y = 0
            self.spirit.change_x = Main.MOVEMENT_SPEED
        elif key == arcade.key.W:
            self.spirit.change_x = 0
            self.spirit.change_y = Main.MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.spirit.change_x = 0
            self.spirit.change_y = -Main.MOVEMENT_SPEED
        if key == 65505:
            Main.MOVEMENT_SPEED = 20

    def on_key_release(self, key):
        if key == arcade.key.A or key == arcade.key.D:
            self.spirit.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.spirit.change_y = 0
        if key == 65505:
            Main.MOVEMENT_SPEED = 3
