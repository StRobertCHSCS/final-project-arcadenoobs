import math
import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

def test():
    print('Testing Movenment')
    
class Spirit():
    
    def __init__(self, position_x, position_y, change_x, change_y):
        self.position_x = position_x
        self.position_y = position_y
        self.position_x_previous = position_x
        self.position_y_previous = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.display_radius = 25
        self.real_radius = 12.5
        self.animation_h = 1
        self.animation_v = 1
        self.health = 100
        self.mana = 50
        self.mana_limit = 50
        self.texture_Front1 = arcade.load_texture('Resource/Mage/Textures/Front1.png')
        self.texture_Left1 = arcade.load_texture('Resource/Mage/Textures/Left1.png')
        self.texture_Right1 = arcade.load_texture('Resource/Mage/Textures/Right1.png')
        self.texture_Back1 = arcade.load_texture('Resource/Mage/Textures/Back1.png')
        self.texture_Front2 = arcade.load_texture('Resource/Mage/Textures/Front2.png')
        self.texture_Left2 = arcade.load_texture('Resource/Mage/Textures/Left2.png')
        self.texture_Right2 = arcade.load_texture('Resource/Mage/Textures/Right2.png')
        self.texture_Back2 = arcade.load_texture('Resource/Mage/Textures/Back2.png')

    def draw(self, key):
        arcade.draw_text(f'Health {self.health}', 0, 580, arcade.color.RED, 15)
        arcade.draw_text(f'Mana{self.mana}/{self.mana_limit}', 0, 550, arcade.color.BLUE, 15)
        scale = 0.5
        if key == 'S' and key != 'D' and key != 'A':
            if self.animation_v == 1:
                arcade.draw_texture_rectangle(self.position_x, self.position_y + 12.5, self.texture_Front1.width*scale, self.texture_Front1.height*scale, self.texture_Front1, 0)
            else:
                arcade.draw_texture_rectangle(self.position_x, self.position_y + 12.5, self.texture_Front1.width*scale, self.texture_Front1.height*scale, self.texture_Front2, 0)
        elif key == 'A'and key != 'W' and key != 'S':
            if self.animation_h == 1:
                arcade.draw_texture_rectangle(self.position_x - 12.5, self.position_y + 12.5, self.texture_Left1.width*scale, self.texture_Left1.height*scale, self.texture_Left1, 0)
            else:
                arcade.draw_texture_rectangle(self.position_x - 12.5, self.position_y + 12.5, self.texture_Left1.width*scale, self.texture_Left1.height*scale, self.texture_Left2, 0)
        elif key == 'D' and key != 'W' and key != 'S':
            if self.animation_h == 1:
                arcade.draw_texture_rectangle(self.position_x + 12.5, self.position_y + 12.5, self.texture_Right1.width*scale, self.texture_Right1.height*scale, self.texture_Right1, 0)
            else:
                arcade.draw_texture_rectangle(self.position_x + 12.5, self.position_y + 12.5, self.texture_Right1.width*scale, self.texture_Right1.height*scale, self.texture_Right2, 0)
        elif key == 'W' and key != 'D' and key != 'A':
            if self.animation_v == 1:
                arcade.draw_texture_rectangle(self.position_x, self.position_y + 12.5, self.texture_Back1.width*scale, self.texture_Back1.height*scale, self.texture_Back1, 0)
            else:
                arcade.draw_texture_rectangle(self.position_x, self.position_y + 12.5, self.texture_Back1.width*scale, self.texture_Back1.height*scale, self.texture_Back2, 0)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < 2*self.real_radius:
            self.position_x = 2*self.real_radius

        if self.position_x > SCREEN_WIDTH - 2*self.real_radius:
            self.position_x = SCREEN_WIDTH - 2*self.real_radius

        if self.position_y < self.real_radius:
            self.position_y = self.real_radius

        if self.position_y > SCREEN_HEIGHT - 3*self.real_radius:
            self.position_y = SCREEN_HEIGHT - 3*self.real_radius
            
        if abs(self.position_x - self.position_x_previous) >= 20:
            self.position_x_previous = self.position_x
            self.animation_h *= -1
        if abs(self.position_y - self.position_y_previous) >= 20:
            self.position_y_previous = self.position_y
            self.animation_v *= -1

