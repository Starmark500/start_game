import math

from wrap import sprite, world, sprite_text, actions
import time, random, wrap

world.create_world(800, 800)
world.set_back_color(255, 255, 10)

turtle = sprite.add("mario-enemies", 100, 100, "turtle_stand")
mario_b = sprite.add("mario-2-big", 300, 200, "walk1")
apple = sprite.add("pacman", 500, 600, "item_apple")


@wrap.on_mouse_down(wrap.BUTTON_WHEELUP, wrap.BUTTON_WHEELDOWN)
def plus(pos_x, pos_y, button):
    if sprite.is_collide_point(turtle, pos_x, pos_y):
        id_object = turtle
    elif sprite.is_collide_point(mario_b, pos_x, pos_y):
        id_object = mario_b
    elif sprite.is_collide_point(apple, pos_x, pos_y):
        id_object = apple
    else:
        return
    if button == wrap.BUTTON_WHEELUP:
        change_size = 2
    else:
        change_size = -2

    w_t = sprite.get_width_percent(id_object)
    h_t = sprite.get_height_percent(id_object)

    w_t += change_size
    h_t += change_size

    sprite.set_size_percent(id_object, w_t, h_t)


@wrap.on_key_always(wrap.K_RIGHT, wrap.K_LEFT)
def flip(pos_x, pos_y, keys):
    if sprite.is_collide_point(turtle, pos_x, pos_y):
        id_object = turtle
    elif sprite.is_collide_point(mario_b, pos_x, pos_y):
        id_object = mario_b
    elif sprite.is_collide_point(apple, pos_x, pos_y):
        id_object = apple
    else:
        return

    if wrap.K_RIGHT in keys :
        change_angle = 5
    else:
        change_angle = -5


    angle_id_object = sprite.get_angle(id_object)
    angle_id_object += change_angle
    sprite.set_angle(id_object, angle_id_object)

@wrap.on_key_always(wrap.K_UP, wrap.K_DOWN)
def flip(pos_x, pos_y, keys):
    if sprite.is_collide_point(turtle, pos_x, pos_y):
        id_object = turtle
    elif sprite.is_collide_point(mario_b, pos_x, pos_y):
        id_object = mario_b
    elif sprite.is_collide_point(apple, pos_x, pos_y):
        id_object = apple
    else:
        return
    if wrap.K_UP in keys :
        sprite.set_costume_next(id_object)
    else:
        sprite.set_costume_prev(id_object)