import os
import arcade

arcade.open_window(600, 600, 'title')
arcade.set_background_color(arcade.color.WHITE)

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))
os.chdir(file_path)

arcade.start_render()

texture = arcade.load_texture('Final project/Resource/Mage/Textures/Front1.png')
arcade.draw_line(300, 0, 300, 600, arcade.color.BLACK, 3)
arcade.draw_line(0, 300, 600, 300, arcade.color.BLACK, 3)
arcade.draw_circle_outline(300, 300, 12.5, arcade.color.BLACK)
arcade.draw_texture_rectangle(300, 300+12.5, 0.5*texture.width, 0.5*texture.height, texture, 0)

arcade.finish_render()
arcade.run()