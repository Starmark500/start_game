import math

from wrap import sprite, world, sprite_text, actions
import time, random, wrap

world.create_world(800, 800)
world.set_back_color(255,255,10)


turtle=sprite.add("mario-enemies",100,100,"turtle_stand")
mario_b=sprite.add("mario-2-big",300,200,"walk1")
apple=sprite.add("pacman", 500, 600,"item_apple")

@wrap.on_mouse_down(wrap.BUTTON_WHEELUP,wrap.BUTTON_WHEELDOWN)
def plus(pos_x,pos_y,button):
    if sprite.is_collide_point(turtle,pos_x,pos_y):
        id_object=turtle
    elif sprite.is_collide_point(mario_b,pos_x,pos_y):
        id_object=mario_b

    if button==wrap.BUTTON_WHEELUP:
        change_size=2
    else:
        change_size=-2
    if sprite.is_collide_point(id_object,pos_x,pos_y):

        w_t = sprite.get_width(id_object)
        h_t = sprite.get_height(id_object)

        w_t += change_size
        h_t += change_size

        sprite.set_size(id_object,w_t,h_t)





