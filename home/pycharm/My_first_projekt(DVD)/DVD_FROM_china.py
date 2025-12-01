from pynput.mouse import Button, Controller
import keyboard  # using module keyboard
import random
import time
import math

mouse = Controller()

def move_mouse_constant_speed(to_x, to_y, speed=800):
    """Moves mouse smoothly to (to_x, to_y) at constant speed (pixels/second)."""
    from_x, from_y = mouse.position
    dx = to_x - from_x
    dy = to_y - from_y
    distance = math.hypot(dx, dy)

    duration = distance / speed  # in seconds
    steps = int(distance)  # one step per pixel
    if steps == 0:
        steps = 1

    step_dx = dx / steps
    step_dy = dy / steps
    delay = duration / steps

    for i in range(steps):
        x = from_x + step_dx * i
        y = from_y + step_dy * i
        mouse.position = (x, y)
        time.sleep(delay)


def setup():
    move_mouse_constant_speed(960, 540)
    return (960, 540)
    
to_x = 1
to_y = 0
while True:
    n = random.randint(1,50)
    m = random.randint(1,50)


    to_x += n
    to_y += m
    move_mouse_constant_speed(to_x, to_y)
    print(to_x, to_y)
    if to_x == 0 or to_x >= 1919 or to_y == 0 or to_y >= 1079:
        print("toches a screan")
        to_x = 1
        to_y = 0
#    else:
#        to_x += n
#        to_y += m
#        move_mouse_constant_speed(to_x, to_y)
#        print("not yet toches a screan")


while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed
            print('You Pressed A Key!')
            break  # finishing the loop

    except:
        break  # if user pressed a key other than the given key the loop will break

setup()
move_side()