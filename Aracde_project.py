import arcade
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'TITLE'

class MyGame(arcade.Window):
    '''
    这是一个arcade设计好的对象，里面有很多预设好的函数，比如我们之前用到过的on_mouse_press,
    on_update等等。这些预设好的函数会自动运行
    '''
    def __init__(self):
        '''
         关于class（中文：面对对象）的画，简单解释一下：你们可以把class理解成一个完整的程序，
         它可以独立运转，也有自己的‘global varibles’，在class里的global varbles 被成为
         self objects，在定义self objects的时候要加‘self.’
         下面有个例子，除了class哪的变量要加‘self.’以外，其余的完全一样
         比较特殊的公式我已经做完了
         所有self变量必须要定义在__init__下面！！
         这个函数在MyGame这个class被called的时候自动运行，主要是用来定义变量与初始化
        '''
        # 底下这句是设定，不用管
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # 这句同理
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        arcade.set_background_color(arcade.color.WHITE)

        # 这句就是一个object，前面要加‘self.’
        self.radius = None
    
    def setup(self):
        '''
         这个方法不是预设好的！！这个方法是在main()中手动call的
         也代表不会像其他函数一样自动运行，只会运行一次。
         这个函数的作用是初始化数据，因为self变量定义只能写到__init__里
         所以我们需要这个函数初始化数据
        '''
        self.radius = 20

    def on_draw(self):
        '''
         Arcade预设好的方法，用于绘制，所有绘制命令写在这
        '''
        arcade.start_render()

        # 当要使用属于这个class的object的时候，也要加‘self.’，否则会报错
        arcade.draw_circle_filled(400, 300, self.radius, (1, 1, 1))

    def on_update(self, delta_time):
        '''
         Arcade预设方法，用于更新数据，所有自动的数据更新写在这
         更新频率每秒60次
        '''
        pass

    def on_key_press(self, symbol, modifiers):
        '''
         Arcade预设方法，用于检测键盘按压
        '''
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        '''
         Aracde预设方法，用于检测鼠标按压
        '''
        pass

def main():
    '''
    这是运行，主函数
    '''
    window = MyGame()
    window.setup()
    arcade.run()

# 底下代表这个程序必须作为主程序时才可以运行，不用管，
# 以后我们要多在外面套程序可能会用到，但现在用不到
if __name__ == '__main__':
    main()