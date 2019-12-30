import math
import arcade

def square_collision(key, character, obstacles_list):
    '''character_obstancles_square_display_collisions计算角色与物体之间是否视觉上碰撞

    Arguments:
        character{Object} -- 角色的object
        obstacles_list{List} -- 包含一类obstacles的objects的list

    Returns:
        [Jugement] -- 判断是否视觉碰撞

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
    for balls in fire_ball:
        for obj in object:
            if math.sqrt((abs(balls.x - obj.position_x))**2 + (abs(balls.y - obj.position_y))**2) < obj.real_radius:
                fire_ball.remove(balls)
                obj.health -= 1
                obj.color = 1