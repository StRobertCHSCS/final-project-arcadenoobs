import math

y = -1# y= cy-oy
x = 0# x= cx-ox
quadrant = None
if x > 0 and y > 0:
    quadrant = 1
elif x < 0 and y > 0:
    quadrant = 2
elif x < 0 and y < 0:
    quadrant = 3
elif x > 0 and y < 0:
    quadrant = 4
if x > 0:
    theta = math.atan(y/x)

if x == 0 and y > 0:
    print('upon')
elif x == 0  and y < 0:
    print('down')
elif y == 0 and x > 0:
    print('right')
elif y == 0 and x < 0:
    print('left')

if quadrant == 1:
    if theta < 0.25*math.pi:
        print('right')
    else:
        print('upon')
elif quadrant == 2:
    if theta < -0.25*math.pi:
        print('upon')
    else:
        print('left')
elif quadrant == 3:
    if theta < 0.25*math.pi:
        print('left')
    else:
        print('down')
elif quadrant == 4:
    if theta < -0.25*math.pi:
        print('down')
    else:
        print('right')