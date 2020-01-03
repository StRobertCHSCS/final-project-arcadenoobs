import math
import arcade

def square_collision(key, character, obstacles_list):
    '''character_obstancles_square_display_collisions
    To cheak if the collision happened between the character and obstacles

    Arguments:
        character{Object} -- object of the character(include positions and status)
        obstacles_list{List} -- a list of obstacles, each object of a obstacles include its positions and status

    Returns:
        [NoneType] -- determine if the collision happened and reset the positions if happened

    '''
    for obstacles in obstacles_list:
        odr = obstacles.display_radius
        ox = obstacles.position_x
        oy = obstacles.position_y
        cx = character.position_x
        cy = character.position_y
        if cy + 27.5 + odr > oy > cy - 12.5 - odr:
            if key == arcade.key.A and cx - 27.5 < ox + odr and cx > ox:
                character.position_x = ox + odr + 27.5
                return True#right
            elif key == arcade.key.D and cx + 27.5 > ox - odr and cx < ox:
                character.position_x = ox - odr - 27.5
                return True#left
        if cx + 12.5 + odr > ox > cx - 12.5 - odr:
            if key == arcade.key.S and cy - 12.5 < oy + odr and cy > oy:
                character.position_y = oy + odr + 12.5
                return True#upon
            elif key == arcade.key.W and cy + 37.5 > oy - odr and cy < oy:
                character.position_y = oy - odr - 37.5
                return True#below
        else:
            pass
            
def fire_ball_collision(fire_ball, object):
    '''Fire_ball_object_circle_real_collision
    To cheak if a fireball hit a object

    Arguments:
        fire_ball{list} -- a list of all objects of fire balls
        object{List} -- a list of a kind of objects(can be characters, monsters and obstacles)

    Returns:
        [NoneType] -- determine if the collision happened and reset datas
    '''
    for balls in fire_ball:
        for obj in object:
            if math.sqrt((abs(balls.x - obj.position_x))**2 + (abs(balls.y - obj.position_y))**2) < obj.real_radius:
                fire_ball.remove(balls)
                obj.health -= 1
                obj.color = 1