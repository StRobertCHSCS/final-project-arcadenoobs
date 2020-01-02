import arcade

class Mage:
    
    MOVEMENT_SPEED = 5

    def __init__(self, width, height):
        '''The package of Mage
        '''
        self.spirit = M_M.Spirit(width/2, height/2, 0, 0)
        self.fire_ball_list = []
        self.key = 'S'

    def draw(self):
        '''draw the spirit and fire balls
        '''
        self.spirit.draw(self.key)

        for fire_ball in self.fire_ball_list:
            fire_ball.draw()

    def update(self):
        '''update the spirit and fire balls
        '''
        self.spirit.update()

        for fire_ball in self.fire_ball_list:
            fire_ball.update()
            if fire_ball.x < 0 or fire_ball.x > 600:
                self.fire_ball_list.remove(fire_ball)
            elif fire_ball.y < 0 or fire_ball.y > 600:
                self.fire_ball_list.remove(fire_ball) 
    
    def on_key_press(self, key):
        '''move the spirit
        '''
        if key == arcade.key.A:
            self.key = 'A'
            self.spirit.change_y = 0
            self.spirit.change_x = -Mage.MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.key = 'D'
            self.spirit.change_y = 0
            self.spirit.change_x = Mage.MOVEMENT_SPEED
        elif key == arcade.key.W:
            self.key = 'W'
            self.spirit.change_x = 0
            self.spirit.change_y = Mage.MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.key = 'S'
            self.spirit.change_x = 0
            self.spirit.change_y = -Mage.MOVEMENT_SPEED

    def on_key_release(self, key):
        '''stop the character from moving
        '''
        if key == arcade.key.A or key == arcade.key.D:
            self.spirit.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.spirit.change_y = 0

    def on_mouse_press(self, x, y, button):
        pass

    def on_mouse_release(self, x, y, button):
        '''create fire balls
        '''
        if button == arcade.MOUSE_BUTTON_LEFT and self.spirit.mana > 0:
            self.fire_ball_list.append(M_A.create_fire_ball(self.spirit.position_x, self.spirit.position_y, x, y))
            self.spirit.mana -= 1

if __name__ == '__main__':
    print('Main runs as a main file')
else: 
    import Resource.Mage.Attack as M_A
    import Resource.Mage.Movement as M_M
    import Resource.Functions.Collisions as FCollision

