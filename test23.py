import math

from wrap import sprite, world, sprite_text, actions
import time, random, wrap

world.create_world(800, 800)
# world.set_back_color(, 255, 10)

turtle = sprite.add("mario-enemies", 100, 100, "turtle_stand")
mario_b = sprite.add("mario-2-big", 100, 100, "walk1")
apple = sprite.add("pacman", 500, 600, "item_apple")


@wrap.on_mouse_down(wrap.BUTTON_WHEELUP, wrap.BUTTON_WHEELDOWN)
def plus(pos_x, pos_y, button):
    fond = find_object(pos_x, pos_y)
    if fond == None:
        return
    if button == wrap.BUTTON_WHEELUP:
        change_size = 2
    else:
        change_size = -2

    w_t = sprite.get_width_percent(fond)
    h_t = sprite.get_height_percent(fond)

    w_t += change_size
    h_t += change_size

    sprite.set_size_percent(fond, w_t, h_t)


@wrap.on_key_always(wrap.K_RIGHT, wrap.K_LEFT)
def flip(pos_x, pos_y, keys):
    fond = find_object(pos_x, pos_y)
    if fond == None:
        return

    if wrap.K_RIGHT in keys :
        change_angle = 5
    else:
        change_angle = -5


    angle_id_object = sprite.get_angle(fond)
    angle_id_object += change_angle
    sprite.set_angle(fond, angle_id_object)

@wrap.on_key_always(wrap.K_UP, wrap.K_DOWN)
def flip(pos_x, pos_y, keys):
    fond=find_object(pos_x,pos_y)
    if fond == None:
        return
    if wrap.K_UP in keys :
        sprite.set_costume_next(fond)
    else:
        sprite.set_costume_prev(fond)


def find_object(pos_x,pos_y):
    if sprite.is_collide_point(turtle, pos_x, pos_y):
        return turtle
    elif sprite.is_collide_point(mario_b, pos_x, pos_y):
        return mario_b
    elif sprite.is_collide_point(apple, pos_x, pos_y):
        return apple
    else:
       return

