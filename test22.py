from wrap import sprite, world, sprite_text, actions
import time, random, wrap

world.create_world(800, 600)

v = False
width = 20
height = 20
aim = sprite.add("pacman", 100, 100, "player2", v)
sprite.set_angle(aim, 0)
size = sprite.set_size(aim, width, height)
green_tank = sprite.add("battle_city_tanks", 100, 100, "tank_enemy_size1_green1")


@wrap.always(500)
def tp_tank():
    y_r = random.randint(100, 500)
    x_r = random.randint(100, 700)
    sprite.move_to(green_tank, x_r, y_r)
    height1=sprite.get_height(aim)
    width1=sprite.get_width(aim)
    print(width,height,height1,width1)

@wrap.on_key_down(wrap.K_UP)
def aims():
    global height,width
    sprite.set_size(aim,width, height)
    sprite.show(aim)

    if width == 20 and height == 20:
        width = width + 20
        height = height + 20
    elif width == 40 and height == 40:
        width = width + 20
        height = height + 20
    elif width == 60 and height == 60:
        width = width + 20
        height = height + 20

    elif width==80 and height == 80:
        sprite.hide(aim)
        width=20
        height=20


@wrap.on_mouse_move
def dv_aim(pos_x,pos_y):
    sprite.move_to(aim,pos_x,pos_y)
