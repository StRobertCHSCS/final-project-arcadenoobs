import os
import arcade

arcade.open_window(600, 600, 'title')
arcade.set_background_color(arcade.color.WHITE)

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))
os.chdir(file_path)

arcade.start_render()

texture = arcade.load_texture('Final project/Resource/Artworks/example.png')
arcade.draw_texture_rectangle(300, 300, texture.width, texture.height, texture, 0)

arcade.finish_render()
arcade.run()