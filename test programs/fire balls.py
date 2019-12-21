import arcade
import os
import math

SCREEM_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'title'

spirit_position_x = 200
spirit_position_y = 300

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
        self.spirit = spirit(spirit_position_x, spirit_position_y)
        #创建一个list用来暂存所有的火球
        self.fire_ball_list = []
    
    def on_update(self, delta_time):
        for fire_ball in self.fire_ball_list:
            #对每个火球进行动画处理，使用每个object设定好varibles，update()参见line 28
            fire_ball.update()
            #如果该火球超出屏幕则从删除该火球 fire_ball_list 参见line 44
            if fire_ball.x < 0 or fire_ball.x > 600:
                self.fire_ball_list.remove(fire_ball)
            elif fire_ball.y < 0 or fire_ball.y > 600:
                self.fire_ball_list.remove(fire_ball)  

    def set_up(self):
        pass

    def on_draw(self):
        arcade.start_render()
        self.spirit.draw()
        #绘制每个火球，使用每个object设定好varibles，draw()参见line 32
        for ball in self.fire_ball_list:
            ball.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            #dh(delta_x)是火球飞行的速度，为固定值
            dh = 15
            #下方为确定飞行方向对运算，只在相对于spirit对第一象限生效(使用绝对值运算)
            #通过与之前对方向判别相乘得出具体的delta_x, delta_y
            if x != spirit_position_x and y != spirit_position_y:
                #rx, ry -- r为reverse缩写，判定火球飞行方向，
                # 由于要用到root运算所以下方要用绝对值，所以点击方向在这里计算
                rx = (x - spirit_position_x)/abs(x - spirit_position_x)
                ry = (y - spirit_position_y)/abs(y - spirit_position_y)
                theta = math.atan(1/(abs(x - spirit_position_x)/abs(y - spirit_position_y)))
                dx = (dh*math.cos(theta))*rx
                dy = (dh*math.sin(theta))*ry
            #排除所有undefined的地方
            elif x == spirit_position_x and y > spirit_position_y:
                dx = 0
                dy = dh
            elif x == spirit_position_x and y < spirit_position_y:
                dx = 0
                dy = -dh
            elif x > spirit_position_x and y == spirit_position_y:
                dx = dh
                dy = 0
            elif x < spirit_position_x and y == spirit_position_y:
                dx = -dh
                dy = 0
            #使用得到的数据创造一个对象，并添加到list里面，fire_ball_list 参见line 44
            ball = fire_ball(spirit_position_x, spirit_position_y, dx, dy)
            self.fire_ball_list.append(ball)
            print(dx, dy)

    def on_key_press(self, key, modifiers):
        pass

def main():
    window = Window()
    window.set_up()
    arcade.run()

if __name__ == '__main__':
    main()